import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access variables
USER = "ttran375"
TOKEN = os.getenv("TOKEN")

# GitHub API URL
api_url = "https://api.github.com/user"

# Create a session
with requests.Session() as gh_session:
    # Authenticate the session
    gh_session.auth = (USER, TOKEN)

    # Fetch user profile data multiple times
    for i in range(3):
        response = gh_session.get(api_url)

        # Print response header and content
        print(f"Request {i + 1}:")
        print("Response Headers:", response.headers)
        print("Response Content:", response.json(), "\n")
