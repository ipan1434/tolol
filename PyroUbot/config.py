import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "7289533914").split()))

API_ID = int(os.getenv("API_ID", "27299185"))

API_HASH = os.getenv("API_HASH", "5664aaf969ce1fadf09cdffbf39c73b1")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7188015488:AAH2Hw-YHOm_ThqxdPqv1BrEBYAae-rXapE")

OWNER_ID = int(os.getenv("OWNER_ID", "7289533914"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002186564307 -1002182272135 ").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://buyervalls:buyervalls@cluster0.ixfnxed.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))
