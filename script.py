from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]

ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

#Calculate rate of return
def get_returns(prices):
  for i in range(0, prices + 1):
    returns.append(calculate_log_return(i))
  return returns

amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

#Print returns as percentage
print(display_as_percentage(amazon_returns))
print(display_as_percentage(ebay_returns))
