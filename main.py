import telebot
from src.config import BOT_TOKEN
from src.state import State
from src.utils import Utils
from src.model import model, device
from src.bot_messages import BotMessages

# Run a bot.
bot = telebot.TeleBot(BOT_TOKEN)

# Set local variables, will be replaced by sql database.
state_dictionary = dict()
images_path = dict()
bot_messages = BotMessages()

# Checking device. It can help to set .env variables .
print(device)


# Registration
@bot.message_handler(commands=['start'])
def start(message):
    state_dictionary[message.from_user.id] = State.first_image_waiting
    bot.send_message(message.from_user.id, bot_messages.intro)
    print(message.from_user.id,message.text)
    images_path[message.from_user.id] = [None, None]


# Text reaction :)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.from_user.id,message.text)
    if message.from_user.id not in state_dictionary:
        bot.send_message(message.from_user.id, bot_messages.question)
        return
    match state_dictionary[message.from_user.id]:
        case State.stop:
            bot.send_message(message.from_user.id, bot_messages.request_start)
        case _:
            bot.send_message(message.from_user.id, bot_messages.request_image)


# Photo logic.
@bot.message_handler(content_types=['photo'])
def get_image_messages(message):
    if message.from_user.id not in state_dictionary:
        bot.send_message(message.from_user.id, bot_messages.request_start)
        return
    file_info = bot.get_file(message.photo[-1].file_id)
    match state_dictionary[message.from_user.id]:
        case State.first_image_waiting:
            images_path[message.from_user.id][0] = file_info.file_path
            state_dictionary[message.from_user.id] = State.second_image_waiting
            bot.send_message(message.from_user.id, bot_messages.request_another_image)
        case State.second_image_waiting:
            images_path[message.from_user.id][1] = file_info.file_path
            state_dictionary[message.from_user.id] = State.sending_image
            bot.send_message(message.from_user.id, bot_messages.waiting_result)
        case _:
            bot.send_message(message.from_user.id, bot_messages.no_image)
    if state_dictionary[message.from_user.id] == State.sending_image:
        Utils.style_transfer(model=model,
                             user_id=message.from_user.id,
                             images_path=images_path[message.from_user.id],
                             bot=bot)
        state_dictionary[message.from_user.id] = State.stop
    return 0


@bot.message_handler(commands=['stop'])
def stop(message):
    state_dictionary.pop(message.from_user.id)
    images_path.pop(message.from_user.id)


# Update chats
bot.polling(none_stop=True, interval=0)
