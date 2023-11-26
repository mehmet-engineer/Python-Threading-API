# Python-Threading-API

This project includes Thread Creator Class with threading module in Python. Thus, it is possible to create threads with start(), stop() and kill() methods.

Example:
---
```
python3 example.py
```

Usage:
---
```
# define your function first
def cb_function():
    print("OK")

# define hertz to be called the function
hz = 1

# create an instance from ThreadCreator class
thread = ThreadCreator(hz, cb_function)

# start the thread
thread.start_thread()

# set thread hz
hz = 2
thread.set_thread_hz(hz)

# stop the thread
thread.stop_thread()

# kill the thread
thread.kill_thread()

# wait for kill
thread.wait_for_kill()
```