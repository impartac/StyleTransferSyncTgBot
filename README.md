# StyleTransferSyncTgBot
This is telegram-bot, which works with images. It transfers style from second image to first and get a result. It really works good, but spend a lot of time and resourses, if you deploy it localy.
# Realisation
I use model VGG19 to get features from images.
# How to install
1. Copy repository
```git clone https://github.com/impartac/StyleTransferSyncTgBot```

2. Open project directory StyleTransferSyncTgBot

```cd StyleTransferSyncTgBot```

3. Create virtual enviroment

```python3 -m venv venv```

4. Activate virtual enviroment

```source venv/bin/activate```

5. Install requiremets

```pip3 install -r requirements.txt```

6. Set in .env variables of token, epochs and image size. 
I think the best values is 
```MAX_SIZE=480```
```EPOCHS=300``` 
(Values depend from your pc)

If you want to use gpu for your model, you need to set conda interpretator(other 3rd step) and install requirements.txt.
# Examples
<p>
  <img src="https://github.com/user-attachments/assets/6b575d5b-fa8e-46af-9e6c-1d05a805867b" height = "200">
  <img src="https://github.com/user-attachments/assets/8a691ac0-2b1b-4ed4-8c34-acc488d6c898" height = "200">
  ------------>
  <img src="https://github.com/user-attachments/assets/a6416b48-670d-4cc8-b02c-5429133862ad" height = "200">
</p>
<p>
  <img src="https://github.com/user-attachments/assets/dcd53b9b-988f-4dd7-a8cc-e30256bf5e1e" height = "150">
  <img src="https://github.com/user-attachments/assets/d3e999b9-164c-46d9-b0f4-4c89088c8acd" height = "150">
  ------------>
  <img src="https://github.com/user-attachments/assets/ce683203-1a36-4fcb-99a4-5dff08bda038" height = "150">
</p>


