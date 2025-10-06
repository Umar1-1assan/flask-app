# backend/app/predictor.py
def moving_average_predict(prices, window=3):
    """
    prices: list [older ... newer] ; window: last n days used for average
    """
    last = prices[-window:]
    return sum(last) / len(last)

