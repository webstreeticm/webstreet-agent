
import pandas as pd
import random

def fetch_price_data(symbol='BTC', days=100):
    dates = pd.date_range(end=pd.Timestamp.today(), periods=days)
    prices = [random.uniform(20000, 30000) for _ in range(days)]
    return pd.DataFrame({'date': dates, 'close': prices})
