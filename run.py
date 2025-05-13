
from agents.momentum import momentum_strategy
from utils.price_feed import fetch_price_data

df = fetch_price_data()
signals = momentum_strategy(df)
print(signals.tail())
