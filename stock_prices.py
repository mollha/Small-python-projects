def get_max_profit(stock_prices: list) -> int:
    """
    Get the best profit from buying and selling ONE share
    :param stock_prices: a list of integers representing the best stock price at each consecutive minute
    :return: an int representing the best profit to be made from buying and selling one shar
    Note: We cannot buy and sell within the same minute, and we must buy before we sell
    """
    higher_price = None
    lower_price = None
    best_profit = 0

    for index, price in enumerate(stock_prices):
        if not lower_price:
            lower_price = price
            continue
        if not higher_price:
            higher_price = price
            best_profit = higher_price - lower_price

        if price < lower_price:
            lower_price = price
        elif price - lower_price > best_profit:
            best_profit = price - lower_price
    return best_profit


print(get_max_profit([10, 5, 7, 8, 11, 9]))

# Example where the stock price decreases ALL day (negative best profit)
print(get_max_profit([10, 9, 8, 7, 6, 5]))
