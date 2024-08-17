import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "6304392781").split()))

API_ID = int(os.getenv("API_ID", "26934385"))

API_HASH = os.getenv("API_HASH", "82d8dbe45c307efbef9667ab6b6b7744")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7373690920:AAGSIo4oYue73L5aDz1LA3Emkx6kFFVbynk")

OWNER_ID = int(os.getenv("OWNER_ID", "6304392781"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002186564307 -1002182272135 ").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://buyervalls:buyervalls@cluster0.ixfnxed.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))
