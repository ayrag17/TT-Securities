#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the max price and its day')
    print('(5) Find the min single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

# Option 3
def avg_price(prices):
    """the inputs are a list of 1 or more prices and the function calculates 
    and returns the average price
    """
    avg = 0
    p_len = len(prices)
    for x in prices:
        avg += x
    
    return avg/p_len

# Option 4
def max_day(prices):
    """takes in a list of prices and returns the day in which the prices were
    at its maximum.
    """
    price_x = prices[0]
    day = 0
    for x in range(len(prices)):
        if prices[x] > price_x:
            price_x = prices[x]
            day = x
    return day

# Option 5
def min_change_day(prices):
    """takes in a list of 2 or more prices and return the minimum single day 
    absolute change in price.
    """
    mindiff = abs(prices[0]-prices[1])
    day = 0
    for x in range(1, len(prices)):
        d = abs(prices[x]-prices[x-1])
        if d < mindiff:
            mindiff = d
            day = x
    return day

# Option 6
def any_above(prices, n):
    """takes in a list of 1 or more prices and using a loop it determines 
    whether or not there are prices above the threshold. Returning True if 
    there are and False if there are not"""
    for x in prices:
        if x > n:
            return True
        
    return False

# Option 7
def find_tts(prices):
    """takes in a list of two or more prices and loops to find the best day to
    buy and sell the stock"""
    mindiff = prices[1] - prices[0]
    buy = 0
    sell = 1
    for x in range(len(prices)):
        for y in range(x+1, len(prices)):
            d = prices[y] - prices[x]
            if d > mindiff:
                mindiff = d
                buy = x
                sell = y
    return [buy, sell, mindiff]

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            avg_p = avg_price(prices)
            print('The average price is', avg_p)
        elif choice == 4:
            max_p = max_day(prices)
            print('The max price is', prices[max_p],'on day', max_p)
        elif choice == 5:
            minday = min_change_day(prices)
            print('The min single-day change occurs on day', minday) 
            print('when the price goes from', prices[minday-1], 'to', prices[minday])
        elif choice == 6:
            n = int(input('Enter the threshold: '))
            if any_above(prices, n) == False:
                print('There are no prices above', n)
            else:
                print('There is at least one price above', n)
        elif choice == 7:
            plan = find_tts(prices)
            print(' Buy on day', plan[0],'at price', prices[plan[0]])
            print('Sell on day', plan[1],'at price', prices[plan[1]])
            print('Total profit:', plan[2])
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
