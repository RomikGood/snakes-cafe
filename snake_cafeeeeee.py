from textwrap import dedent
import sys
import re
import csv
from collections import defaultdict
import uuid




class Order:
    def __init__(self, order_num):
        self.order_limit = order_num
        pass



    def __repr__(self):
        pass

    def add_item(self):
        pass

    def remove_item(self):
        pass
    
    def display_order(self):
        pass

    def print_receipt(self):
        pass
