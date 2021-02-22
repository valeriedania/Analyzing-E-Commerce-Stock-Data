from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]

ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

#Calculate rate of return
def get_returns(prices):
  returns = [calculate_log_return(i, i+1) for i in prices]

amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

#Print returns as percentage
amazon_percentages = [display_as_percentage(i) for i in amazon_returns]
ebay_percentages = [display_as_percentage(j) for j in ebay_returns]
print(amazon_percentages)  
print(ebay_percentages) 
                    
#Calculate the annual rate of return
amazon_annual = display_as_percentage(sum(amazon_returns))
ebay_annual = display_as_percentage(sum(ebay_returns))

#Calculate variance
amazon_variance = calculate_variance(amazon_returns)
ebay_variance = calculate_variance(ebay_returns)

#Calculate standard deviance
amazon_stddev = display_as_percentage(calculate_stddev(amazon_returns))
ebay_stddev = display_as_percentage(calculate_stddev(ebay_returns))

#Calculate correlation coefficient
correlation = calculate_correlation(amazon_returns, ebay_returns)
     
