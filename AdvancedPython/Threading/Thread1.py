import time
  
def countdown(n):
    while n > 0:
        print('T-minus\n', n)
        n -= 1
        time.sleep(2)
def add():
    c = 44+66
    print("\n Addition Result: {}".format(c))

    
# Create and launch a thread
from threading import Thread
t = Thread(target = countdown, args =(10, ))
t1 = Thread(target = add, args =())

t.start()
t1.start()
#t.join()
#t1.join()
print("*******************")
