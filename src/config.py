import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
EPOCHS = int(os.environ.get('EPOCHS'))
MAX_SIZE = int(os.environ.get('MAX_SIZE'))
