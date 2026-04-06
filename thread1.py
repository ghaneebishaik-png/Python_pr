## Used to create multiple threads and run parallelly  and acheive multi threading.
import threading
import time

def task1():
    for i in range(1,3):
        print(f"Task 1 -iteration{i}")
        time.sleep(1)

def task2():
    for i in range(1,3):
        print(f"Task 2 -iteration{i}")
        time.sleep(1)

#task1()
#task2()

#Creating threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

#starting threads
thread1.start()
thread2.start()

#joining threads
thread1.join()
thread2.join()