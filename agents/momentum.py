
import pandas as pd

def momentum_strategy(df, lookback=10):
    df['momentum'] = df['close'].pct_change(periods=lookback)
    df['signal'] = 0
    df.loc[df['momentum'] > 0.05, 'signal'] = 1  # buy
    df.loc[df['momentum'] < -0.05, 'signal'] = -1  # sell
    return df[['close', 'momentum', 'signal']]
