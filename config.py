import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_URL = "http://20.244.56.144/evaluation-service/auth"
COMPANY_URL = "http://20.244.56.144/test/company"
