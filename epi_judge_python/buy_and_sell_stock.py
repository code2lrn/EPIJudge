from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price_seen, max_profit = float('inf'), 0.0
    for price in prices:
        profit = price - min_price_seen
        max_profit = max(max_profit, profit)
        min_price_seen = min(min_price_seen, price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
