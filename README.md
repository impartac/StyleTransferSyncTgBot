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
![image](https://github.com/user-attachments/assets/5e324196-7c75-43f1-a6fd-3ec45eea75ab) ![image](https://github.com/user-attachments/assets/daa64006-4a29-4c11-b454-1588f8a7ac62) ![image](https://github.com/user-attachments/assets/11a67faf-2deb-4208-8474-2c560d19276b)
![image](https://github.com/user-attachments/assets/805118e1-74b0-4896-a22e-209131d1a746) ![image](https://github.com/user-attachments/assets/0ef08603-ed31-4323-84a9-e5bba8aeb243) ![image](https://github.com/user-attachments/assets/1a2e7866-b1bd-46dd-a857-15b9019945ab)




