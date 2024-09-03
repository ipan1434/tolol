import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "1415374553").split()))

API_ID = int(os.getenv("API_ID", "28856059"))

API_HASH = os.getenv("API_HASH", "9be1503a6ebed409cd0c53c188d04a0b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7528751518:AAF6nwjGW2C20hAVCgOSgudtGAulVBqiRIo")

OWNER_ID = int(os.getenv("OWNER_ID", "1415374553"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002186564307 -1002182272135 ").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://buyervalls:buyervalls@cluster0.ixfnxed.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))
