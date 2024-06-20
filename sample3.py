import requests
from dotenv import load_dotenv
import os

load_dotenv()

USER = "ttran375"
TOKEN = os.getenv("TOKEN")

with requests.Session() as gh_session:
    gh_session.auth = (USER, TOKEN)

    first_response = gh_session.get("https://api.github.com/user")
    second_response = gh_session.get("https://api.github.com/user")

    print(first_response.json())
    print(first_response.json())
