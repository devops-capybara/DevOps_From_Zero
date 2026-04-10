import threading
def function():
    print ("Wating 3 seconds ... ")

timer = threading.Timer(3.0, function)
timer.start()

# print ("Starting test ...")