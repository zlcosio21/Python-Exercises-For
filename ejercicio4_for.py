# Find the smallest value of a list of integers.

import random

def lower_value(range_list):
    list_ = [random.randint(1, 1000) for i in range(0, range_list)]

    return list_, min(list_)
  
