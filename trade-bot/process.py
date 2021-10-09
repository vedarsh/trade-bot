from api_init import *

import numpy as np


def inpt(*args, **kwargs):
    #inputting required arguments
    return args

def init():
    #taking multiple inputs
    input_arr = input("give your ipla ticker:")
    stonk_arr = inpt(list(map(str,input_arr.split(' '))))
    #converting inputs into arrays
    for i in range(len(stonk_arr)):
        #secondary array
        x = stonk_arr[i]
        for j in range(len(x)):
            #primary array
            y = x[j]
            stock = TradeInit(y)
            print(stock.max_volume)
            print(stock.information)
    else:
        return "loop_error"

if __name__ == "__main__":
    init()
