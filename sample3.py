import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access variables
USER = os.getenv("USER")
TOKEN = os.getenv("TOKEN")
print(USER)
with requests.Session() as gh_session:
    gh_session.auth = (USER, TOKEN)
