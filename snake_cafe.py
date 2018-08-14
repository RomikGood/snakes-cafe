from textwrap import dedent
from collections import defaultdict

WIDTH = 96

def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to the Snake Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit"'
    ln_four = 'Please, limit yourself to 20 items!"'

    print(dedent(f'''
        {'*' * WIDTH}
        {'**   '  + ln_one + '  **'}
        {'**   '  + ln_two + '  **'}
        {'**   '  + ln_three + '  **'}
        {'**'}
        {'*' * WIDTH}

        {'Appetizers'}
        {'----------------'}
        {'Wings'}
        {'Cookies'}
        {'Rolls'}
        {' '}

        {'Entrees'}
        {'----------------'}
        {'Salmon'}
        {'Steak'}
        {'Meat Tornado'}
        {' '}

        {'Desserts'}
        {'----------------'}
        {'Ice Cream'}
        {'Cake'}
        {'Pie'}
        {' '}

        {'Drinks'}
        {'----------------'}
        {'Coffee'}
        {'Tea'}
        {'Blood Mary'}

        {' '}
        {'*' * WIDTH}
        {'**  What would you like to order?  **'}
      
        {'*' * WIDTH}

    '''))

question = dedent('''
            **  Place another order or type quit to finish:  **\n
        ''')

menu = ['wings', 'cookies', 'rolls','salmon','steak', 'meat tornado',
'ice cream', 'cake','pie', 'coffee', 'tea', 'bloody mary' ]
order = defaultdict(int)

def place_order():
    order_limit = 0
    greeting()
    while order_limit < 20:
        item =  input()
        if item in menu:
            order[item] += 1
            order_limit += 1
            if order[item] == 1:
                print ('**  ' + str(order[item]) + ' order of ' + item + ' has been added to your order   **\n')
            else:
                print ('**  ' + str(order[item]) + ' orders of ' + item + ' have been added to your order   **\n')
            print(question)
        if item not in menu and item != 'quit':
            print (dedent('''
            **  Item you entered is not in menu.  **\n
        '''))
            
        if item == 'quit':
            return print_order(order)
 

def print_order(order):
    print(dedent('''
            **  Your order:  **\n
        '''))
    for key, value in order.items() :
        print (value, key)    

    print(dedent('''
            **  Thank you! Please come again!  **\n
        '''))   


if __name__ == '__main__':
    place_order()
