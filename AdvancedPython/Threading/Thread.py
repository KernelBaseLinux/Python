import threading

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))

def print_Add(num, n1):
    """
    function to print square of given num
    """
    print("add: {}".format(num + n1))
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    t3 = threading.Thread(target=print_Add, args=(44,55))
    print("t1 ---------> ",t1)
    print("t2 ---------> ",t2)
    print("t3 ---------> ",t3)
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # wait until thread 3 is completely executed
    t3.join()
    # both threads completely executed
    print("Done!")
