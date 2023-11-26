import time
from ThreadCreator import ThreadCreator

def cb_function1():
    print("1 --> OK")

def cb_function2():
    print("2 --> OK")

hz = 1
thread1 = ThreadCreator(hz, cb_function1)
thread2 = ThreadCreator(hz, cb_function2)

print("\n Starting threads... \n")
thread1.start_thread()
thread2.start_thread()

time.sleep(3)

print("\n Stopping threads... \n")
thread1.stop_thread()
thread2.stop_thread()

time.sleep(3)

print("\n Starting threads... \n")
thread1.start_thread()
thread2.start_thread()

time.sleep(3)

print("\n Killing threads... \n")
thread1.kill_thread()
thread2.kill_thread()

print("\n Waiting threads to be killed... \n")
thread1.wait_for_kill()
thread2.wait_for_kill()