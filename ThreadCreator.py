import time
import threading

"""
  @author: Mehmet Kahraman
  @date: 21.11.2023
  @about: useful threading methods and single thread termination
"""

class ThreadCreator():
    def __init__(self, hz, callback_function):
        self.hz = hz
        self.sleep_value = 1 / self.hz
        self.daemon = True
        self.run_flag = False
        self.kill_flag = False
        self.callback_function = callback_function
        
        self.init_thread()
    
    def init_thread(self):
        self.thread = threading.Thread(target=self.thread_function, daemon=self.daemon)
        self.thread.start()
    
    def start_thread(self):
        self.run_flag = True
    
    def stop_thread(self):
        self.run_flag = False
        
    def kill_thread(self):
        self.kill_flag = True
    
    def wait_for_kill(self):
        self.thread.join()

    def thread_function(self):
        
        # wait for first start
        while True:
            if self.run_flag == True:
                break
        
        # execute main loop
        while True:
            if self.run_flag == True:
                while True:
                    if self.run_flag == False:
                        break
                    self.callback_function()
                    time.sleep(self.sleep_value)
            if self.kill_flag == True:
                break


if __name__ == "__main__":

    def my_callback_function():
        print("OK.")
    
    hz = 1
    
    process = ThreadCreator(hz, my_callback_function)
    process.start_thread()
    time.sleep(2)
    process.stop_thread()
    time.sleep(2)
    process.kill_thread()
    time.sleep(2)
    process.wait_for_kill()
