from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_profit, min_price_seen = 0.0, float('inf')
    first_buy_sell_profits = [0.0] * len(prices)
    for i, price in enumerate(prices):
        min_price_seen = min(min_price_seen, price)
        max_profit = max(max_profit, price - min_price_seen)
        first_buy_sell_profits[i] = max_profit

    max_price_seen = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_seen = max(max_price_seen, price)
        max_profit = max(max_profit, max_price_seen - price + first_buy_sell_profits[i])

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
