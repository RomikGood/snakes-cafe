from textwrap import dedent
import sys
import csv
from collections import defaultdict
import uuid

WIDTH = 80


def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to the Snake Cafe!'
    ln_two = 'Please see menu options below.'
    ln_tree = 'You can load your own menu file in this direcory'
    print(dedent(f'''
        {'*' * WIDTH}
        {'**   '  + ln_one + '  **'}
        {'**   '  + ln_two + '  **'}
        {'**   '  + ln_tree + '  **'}
        {'**'}
        {'*' * WIDTH}
        '''))


def print_menu():
    print(dedent(f'''
        {'*' * WIDTH}
        {'**   Snake Cafe Menu  **'}
        {'*' * WIDTH}
        
        {'Appetizers'}
        {'-----------------'}
        {'Wings ----------- $7'}
        {'Cookies --------- $1'}
        {'Rolls ----------- $2'}
        {'Sliders --------- $6'}
        {'Taco ------------ $2'}
        {'Nachos ---------- $10'}
        {' '}

        {'Entrees'}
        {'-----------------'}
        {'Salmon ---------- $10'}
        {'Steak------------ $10'}
        {'Meat Tornado ---- $10'}
        {'Cod ------------- $20'}
        {'Rolls ----------- $3'}
        {'Pizza ----------- $9'}
        {' '}

        {'Sides'}
        {'-----------------'}
        {'Green Salad ----- $9'}
        {'Potato Salad ---- $7'}
        {'Roast Potatoes -- $11'}
        {'Mashed Potatoes - $10'}
        {'Coleslaw -------- $5'}
        {'Sausage --------- $6'}
        {' '}

        {'Desserts'}
        {'-----------------'}
        {'Ice Cream ------- $3'}
        {'Cake ------------ $4'}
        {'Pie ------------- $5'}
        {'Banana Bread ---- $4'}
        {'Sorbet ---------- $9'}
        {'Chocolate ------- $4'}
        {' '}

        {'Drinks'}
        {'-----------------'}
        {'Coffee ---------- $3'}
        {'Tea ------------- $1'}
        {'Blood Mary ------ $10'}
        {'Beer ------------ $9'}
        {'Wine ------------ $12'}
        {'Juice ----------- $2'}

        {' '}
        {'*' * WIDTH}
        {'**  What would you like to order?  **'}
      
        {'*' * WIDTH}

    '''))


menu = {
    'wings': [7, 10], 'cookies': [1, 10], 'taco': [2, 10], 'nachos': [2, 10],
    'sliders': [6, 10], 'rolls': [3, 10], 'salmon': [10, 10],
    'steak': [15, 10], 'meat tornado': [11, 10], 'cod': [20, 10],
    'pizza': [9, 10], 'green salad': [8, 10], 'potato salad': [7, 10],
    'Roasted Potatoes': [11, 10], 'mashed potatoes': [8, 10],
    'coleslaw': [5, 10], 'sausage': [6, 10], 'ice cream': [5, 10],
    'cake': [2, 10], 'pie':  [5, 10], 'banana bread': [4, 10],
    'sorbet': [7, 10], 'chocolate': [3, 10], 'coffee': [2, 10],
    'tea':  [1, 10], 'bloody mary': [10, 10], 'Beer': [5, 10],
    'wine': [12, 10], 'juice': [2, 10]}


def display_csv_menu():
    '''opens custom menu as csv file. throws an error if its not csv '''
    try:
        with open('menu.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(
                    f'\t{row[0]} ** {row[1]} ** Qt({row[2]}) --------- ${row[3]}')
 
    except (FileNotFoundError, TypeError)as e:
            print(e)


def load_csv_menu():
    '''funtion loads csv menu'''
    with open('menu.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        cust_menu = {}
        for row in readCSV:
            cust_menu[row[0]] = [int(row[3]), int(row[2])]
        return cust_menu


class Order:
    """Order class for managing orders"""
    def __init__(self):
        self.order = defaultdict(int)
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return 'Order {} | Items: {} | Total: {}'.format(self.id, self.order, len(self.order))

    def __len__(self):
        return len(self.order)

    def add_item(self, order):
        
        while True:
            item = input('Enter item (enter \'order\' to see you order): ').lower()
            if item in menu:
                try:
                    item_qt = int(input('Enter quantity: '))
                except ValueError:
                    item_qt = 1
                if item_qt < menu[item][1]:
                    self.order[item] += item_qt  # adds to order
                    menu[item][1] -= item_qt  # removes from inventory
                else:
                    print('Not sufficient inventory. Please order smaller amount')
                    try:
                        item_qt = int(input('Enter quantity: '))
                    except ValueError:
                        item_qt = 1

                    self.order[item] += item_qt  # adds to order
                    menu[item][1] -= item_qt  # removes from inventory

                if  self.order[item] == 1:
                    print('-' * 30)
                    print('**  ' + str(self.order[item]) + ' order of ' + item + ' has been added to your order   **\n')
                else:
                    print('-' * 30)
                    print('**  ' + str(self.order[item]) + ' orders of ' + item + ' have been added to your order   **\n')
            print_subtotal(self.order)        
    
            if item == 'order':
                print(print_order(self.order))
                # item =  input('Would you like save you order?: ').lower()
                # if item == 'yes':
                #     with open("my_output_file.txt", "w") as out:
                #         out.write(print(print_order(order)))
                    # fh=open("output.txt",'w')
                    # print(print_order(order),file=fh)
                    # fh.close()
                    # fh=open("output.txt",'r')
                    # print(fh.read())
            elif item == 'menu':
                print(print_menu())

            # remove item from the order 
            elif item.split(' ')[0] == 'remove':
                self.order.remove_item(item.split(' ')[1])

            elif item == 'quit':
                exit()
        
            # elif item not in menu and item not in ('order', 'menu', 'quit', 'delete'):
            #     print('Item is not in menu. Please see our menu')
    def remove_item(self, item):
        if item in self.order:
            self.order[item] -= 1
            print('**  You removed one ' + item + ' from your order  **')
            print('-' * 30)
            print_subtotal(self.order)


current = Order()


def print_order(order):
        '''this function culculates tax and prints subtotal and total of the order
        '''
        order_sub_total = 0
        print(dedent(f'''
            {'*' * WIDTH}
            {'**  Snake Cafe! **'}
            {'*' * WIDTH}
            {'**   Order # ' + str(uuid.uuid4()) + '  **'}
            '''))
        
        print('-' * 30)
        for key, value in order.items():
            print('{} x {} {:>16}$'.format(key, value, value*menu[key][0]))

            order_sub_total += value*menu[key][0]
        print('-' * 30)
        print('Subtotal:    {:>15}$ '.format(str(order_sub_total)))
        print('Taxes:       {:>15}$ '.format(str(tax(order_sub_total))))
        print('-' * 30)
        print('Order Total: {:>15}$ ' .format(str(order_total(order_sub_total))))
        print(dedent('''
                **  Thank you! Please come again!  **\n
            '''))   


def print_subtotal(order):
    '''prints subtotal of eash item  '''
    order_sub_total = 0
    for key, value in order.items():
        order_sub_total += value*menu[key][0]
    print('-' * 30)
    print('Your order subtotal:  $' + str(order_sub_total))
    print('-' * 30)


def tax(amount):
    '''culc taxes'''
    return round(amount * .101, 2)


def order_total(order):
    return order + tax(order)


def exit():
    print(dedent('''
        Thanks for visiting Snake Cafe!
    '''))
    sys.exit()


def start_order():
    greeting()
    item = input('Would you like custom menu(yes/no): ').lower()
    if item == 'yes':
        display_csv_menu()
        menu = load_csv_menu()
        current.add_item(current)
        return menu
    else:
        print_menu()
        current.add_item(current)
                

if __name__ == '__main__':
    try:
        start_order()
    except KeyboardInterrupt:
        exit()