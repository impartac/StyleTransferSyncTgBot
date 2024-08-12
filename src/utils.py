import telebot
import io
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from src.model import device
from PIL import Image
from src.config import EPOCHS, MAX_SIZE


# Class, that contains a lot of utils for model.
class Utils:
    @staticmethod
    def style_transfer(model, user_id, images_path, bot: telebot.TeleBot):
        image = bot.download_file(images_path[0])
        style = bot.download_file(images_path[1])

        image_stream = io.BytesIO(image)
        style_stream = io.BytesIO(style)

        content_img = Utils.load_image(image_stream)
        style_img = Utils.load_image(style_stream)

        content_features = Utils.get_features(content_img, model)
        style_features = Utils.get_features(style_img, model)

        style_grams = [Utils.gram_matrix(feature) for feature in style_features]

        target = content_img.clone().requires_grad_(True)

        style_weights = [1e4] * len(style_grams)
        content_weights = [1]
        optimizer = torch.optim.Adam([target], lr=0.001)

        num_steps = EPOCHS
        for step in range(num_steps):
            target_features = Utils.get_features(target, model)

            content_loss = content_weights[0] * nn.MSELoss()(target_features[4], content_features[4])
            style_loss = 0

            for target_gram, style_gram, weight in zip([Utils.gram_matrix(feature) for feature in target_features],
                                                       style_grams, style_weights):
                style_loss += weight * nn.MSELoss()(target_gram, style_gram)

            total_loss = content_loss + style_loss

            optimizer.zero_grad()
            total_loss.backward(retain_graph=True)
            optimizer.step()

            if step % 50 == 0:
                print(user_id, f'Step {step}, Total Loss: {total_loss.item()}')
        answer = Utils.tensor_to_image(target[0])
        bot.send_photo(user_id, answer)

    @staticmethod
    def load_image(image_path, max_size=MAX_SIZE):
        image = Image.open(image_path).convert("RGB")
        size = min(max_size, max(image.size))
        transform = transforms.Compose([
            transforms.Resize(size),
            transforms.ToTensor(),
            transforms.Lambda(lambda x: x[None, :])
        ])
        return transform(image).to(device)

    @staticmethod
    def get_features(image, model):
        layers = {
            '0': 'conv1_1',
            '5': 'conv2_1',
            '10': 'conv3_1',
            '19': 'conv4_1',
            '21': 'conv4_2',
            '28': 'conv5_1',
        }
        features = []
        x = image

        for name, layer in model._modules.items():
            x = layer(x)
            if name in layers:
                features.append(x)

        return features

    @staticmethod
    def gram_matrix(tensor):
        _, d, h, w = tensor.size()
        tensor = tensor.view(d, h * w)
        gram = torch.mm(tensor, tensor.t())
        return gram

    @staticmethod
    def tensor_to_image(tensor):
        if tensor.size(0) == 1:
            tensor = tensor.repeat(3, 1, 1)

        tensor = tensor.detach().clamp(0, 1)

        image = transforms.ToPILImage()(tensor.squeeze(0))

        img_byte_array = io.BytesIO()
        image.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)
        return img_byte_array
