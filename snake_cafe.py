from textwrap import dedent
from collections import defaultdict
import uuid

WIDTH = 96

def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to the Snake Cafe!'
    ln_two = 'Please see our menu below.'
    ln_four = 'Please, limit yourself to 20 items!"'

    print(dedent(f'''
        {'*' * WIDTH}
        {'**   '  + ln_one + '  **'}
        {'**   '  + ln_two + '  **'}
        {'**   '  + ln_four + '  **'}
        {'**'}
        {'*' * WIDTH}

        {'Appetizers'}
        {'----------------'}
        {'Wings'}
        {'Cookies'}
        {'Rolls'}
        {'Sliders'}
        {'Taco'}
        {'Nachos'}
        {' '}

        {'Entrees'}
        {'----------------'}
        {'Salmon'}
        {'Steak'}
        {'Meat Tornado'}
        {'Cod'}
        {'Rolls'}
        {'Pizza'}
        {' '}

        {'Sides'}
        {'----------------'}
        {'Green Salad'}
        {'Potato Salad'}
        {'Roasted Potatoes'}
        {'Mashed Potatoes'}
        {'Coleslaw'}
        {'Sausage'}
        {' '}

        {'Desserts'}
        {'----------------'}
        {'Ice Cream'}
        {'Cake'}
        {'Pie'}
        {'Banana Bread'}
        {'Sorbet'}
        {'Chocolate'}
        {' '}

        {'Drinks'}
        {'----------------'}
        {'Coffee'}
        {'Tea'}
        {'Blood Mary'}
        {'Beer'}
        {'Wine'}
        {'Juice'}

        {' '}
        {'*' * WIDTH}
        {'**  What would you like to order?  **'}
      
        {'*' * WIDTH}

    '''))

question = dedent('''
            **  Place order for another item  **\n
            **  Type order to see your current order  **\n
        ''')


menu = {'wings' : 7, 'cookies': 1, 'taco': 2, 'nachos': 2, 'sliders':6, 'rolls': 2,'salmon': 5,'steak': 3, 'meat tornado': 4, 'cod': 20, 'pizza':9, 'green salad':9, 'potato salad': 7, 'Roasted Potatoes': 11,'mashed potatoes': 7,'coleslaw': 5, 'sausage': 6, 'ice cream': 3, 'cake': 2,'pie': 5, 'banana bread':4, 'sorbet':5, 'chocolate':3, 'coffee': 2, 'tea': 2, 'bloody mary': 10, 'Beer': 5, 'wine': 6, 'juice': 2  }

order = defaultdict(int)

def place_order():
    order_limit = 0
    greeting()
    while order_limit < 20:
        item =  input().lower()
        if item in menu:
            order[item] += 1
            order_limit += 1
            if order[item] == 1:
                print ('**  ' + str(order[item]) + ' order of ' + item + ' has been added to your order   **\n')
            else:
                print ('**  ' + str(order[item]) + ' orders of ' + item + ' have been added to your order   **\n')
            print(question)
        if item not in menu and item not in ( 'quit', 'order', 'menu'):
            print (dedent('''
            **  Item you entered is not in menu.  **\n
        '''))
            
        if item == 'order':
            print (print_order(order))
        
        if item == 'menu':
            print(greeting())
        

def print_order(order):
    order_sub_total = 0
    print(dedent(f'''
        {'*' * WIDTH}
        {'**  Snake Cafe! **'}
        {'*' * WIDTH}
        {'**   Order #: ' + str(uuid.uuid4()) + '  **'}
        '''))
    
    print('-' * 30)
    for key, value in order.items() :
        print ('{} x {} {:>16}$'.format(key, value, value*menu[key]))

        order_sub_total += value*menu[key]
    print('-' * 30)
    print('Subtotal:    {:>15}$ '.format(str(order_sub_total)))
    print('Taxes:       {:>15}$ '.format(str(tax(order_sub_total))))
    print('-' * 30)
    print('Order Total: {:>15}$ ' .format(str(order_total(order_sub_total))))
    print(dedent('''
            **  Thank you! Please come again!  **\n
        '''))   

def tax(amount):
    return round(amount * .101, 2)

def order_total(order):
    return order + tax(order)

if __name__ == '__main__':
    place_order()
