import threading
import time
count = 0
def brew():
    global count
    print(f"starting {threading.current_thread().name}")
    for i in range(100_000):
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
print(f'total time : {end-start:.2f} seconds')