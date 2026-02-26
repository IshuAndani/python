import threading
import time
count = 0
sync=0
lock = threading.Lock()
def brew_sync():
    global sync
    print(f"starting {threading.current_thread().name}")
    for i in range(100_000_00):
        sync+=1
    print("sync" , sync)
    print(f"ending {threading.current_thread().name}")

def brew():
    global count
    print(f"starting {threading.current_thread().name}")
    for i in range(100_000_00):
        with lock:
            count+=1
    print(count)
    print(f"ending {threading.current_thread().name}")

thread1 = threading.Thread(target=brew,name='thread1')
thread2 = threading.Thread(target=brew,name='thread2')
start = time.time()
# brew()
# brew()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print(f'total time for threading brew: {end-start:.2f} seconds')

thread1 = threading.Thread(target=brew_sync,name='thread1')
thread2 = threading.Thread(target=brew_sync,name='thread2')
start = time.time()
brew_sync()
brew_sync()
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
end = time.time()
print(f'total time for sync brew: {end-start:.2f} seconds')