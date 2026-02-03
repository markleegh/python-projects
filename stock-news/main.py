import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "46Q43YS0UUHBQW68"
NEWS_API_KEY = "5730e06def02486890f075f7ae8ac84f"
THRESHOLD_PERCENT = 2
url = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}
response = requests.get(url, params=params)
data = response.json()

time_series = data.get("Time Series (Daily)", {})
print(time_series)
if not time_series:
    raise ValueError("No time series data found. Check API key, symbol, or API limit.")

dates = sorted(time_series.keys(), reverse=True)

yesterday = dates[0]
day_before = dates[1]

yesterday_close = float(time_series[yesterday]["4. close"])
day_before_close = float(time_series[day_before]["4. close"])

percent_change = ((yesterday_close - day_before_close) / day_before_close) * 100

print(f"{STOCK} change: {percent_change:.2f}%")
if abs(percent_change) >= THRESHOLD_PERCENT:
    print("Fetching news...")
    news_params = {
        "function": "NEWS_SENTIMENT",
        "qInTitle": STOCK,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_URL, params=news_params)
    news_data = news_response.json()
    feed = news_data.get("articles", [])
    print(feed)
    for article in feed[:3]:
        print("\nHeadline:", article.get("title", "No title"))
        print("URL:", article.get("url", "No URL"))

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

