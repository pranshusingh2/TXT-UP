import os

API_ID = os.environ.get("API_ID", "14578218")

API_HASH = os.environ.get("API_HASH", "1910055ec43e4b46efeb768a82bdaf68")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7148451805:AAEHoW-PiKT4TvgygmBAzxSBZvmtJQ9_Tuo")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "5003683239"))

LOG = -1002478348920

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5003683239").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


