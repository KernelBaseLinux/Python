import logging
'''
evel	Numeric value
CRITICAL    50
ERROR	    40
WARNING	    30
INFO	    20
DEBUG	    10
NOTSET	     0
'''
logging.basicConfig(level=logging.DEBUG)

def Add(a,b):
    c = a+b
    return c

def Sub(a,b):
    c = a-b
    return c

def Mul(a,b):
    c = a*b
    return c


num_1 = 10
num_2 = 5

add_result = Add(num_1,num_2)
logging.debug("Add: {} + {} = {}".format(num_1,num_2,add_result))

add_result = Sub(num_1,num_2)
logging.debug("Sub: {} - {} = {}".format(num_1,num_2,add_result))

add_result = Mul(num_1,num_2)
logging.debug("Mul: {} * {} = {}".format(num_1,num_2,add_result))
