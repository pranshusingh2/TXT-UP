import os

API_ID = os.environ.get("API_ID", "25038096")

API_HASH = os.environ.get("API_HASH", "098112aae38be62db58363267a061b59")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8123485632:AAHTvq38wj0-8426bsE0TDqsYvGIYU_9JMA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("5201266500", ))

LOG = 

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5201266500").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


