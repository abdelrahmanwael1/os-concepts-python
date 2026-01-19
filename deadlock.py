import threading
import time

resource_1 = threading.Lock()
resource_2 = threading.Lock()


def process_1():
    with resource_1:
        print("process 1 acquire for resource 1 ")
        time.sleep(1)
        print("waiting for resource 2")
    with resource_2:
        print("acquire for resource 2 complete.")


def process_2():
    with resource_2:
        print("process 2 acquire for resource 2 ")
        time.sleep(1)
        print("waiting for resource 1")
        with resource_1:
            print("acquire for resource 1 complete.")


a = threading.Thread(target=process_1,)
b = threading.Thread(target=process_2)
a.start()
b.start()
