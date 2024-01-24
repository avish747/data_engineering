import time
from datetime import datetime

def greet(function):
    def wrapper():
        print("******************")
        function()
        print("******************")

    return wrapper

def timer(function):
    def wrapper():
        start_time = datetime.now()
        function()
        time.sleep(5)
        print("Function Execution time : " + str(datetime.now() - start_time))
    return wrapper()

def Epam():
    print("EPAM Systems")


def Deloitte():
    print("Deloitte Consulting")


#@greet
@timer
def Cognizant():
    print("Cognizant Technology Solutions")
#a = greet(Epam)
#b = greet(Deloitte)
#a()
#b()

Cognizant()