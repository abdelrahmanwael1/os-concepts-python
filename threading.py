import threading
import time


def print_1():
    print("Starting of a thread: ", threading.current_thread().name)
    time.sleep(2)
    print("finishing of a thread: ", threading.current_thread().name)


def print_2():
    print("Starting of a thread: ", threading.current_thread().name)
    print("finishing of a thread: ", threading.current_thread().name)


a = threading.Thread(target=print_1, name="Thread_1")
b = threading.Thread(target=print_2, name="Thread_2")
a.start()
b.start()
