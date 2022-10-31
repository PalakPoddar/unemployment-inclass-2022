
# this is the "app/unemployment_report.py" file...

import os
import json
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)



parsed_response = json.loads(response.text)

data = parsed_response["data"]
print(type(parsed_response))
pprint(parsed_response)

#breakpoint()
#Challenge A

#latest = parsed_response ["data"][0]
#print(latest)

#breakpoint()

# Challenge B
# 
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

from statistics import mean

data = parsed_response["data"]
this_year = [d for d in data if "2022-" in d["date"]]

rates_this_year = [float(d["value"]) for d in this_year]
#print(rates_this_year)

print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("NO MONTHS:", len(this_year))

breakpoint()
# Challenge C
# 
# Plot a line chart of unemployment rates over time.

from plotly.express import line

dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]

fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
fig.show()

