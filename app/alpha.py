#this is the "app/alpha.py" file 

import os
from dotenv import load_dotenv

load_dotenv() #look in the ".env" file for en

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

