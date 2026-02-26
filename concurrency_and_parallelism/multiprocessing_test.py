from multiprocessing import Process
import time

def brew():
    count = 0
    print("starting")
    for i in range(100_000_000):
        count+=1
    print(count)
    print("ending")

if __name__ == "__main__":
    p1 = Process(target=brew)
    p2 = Process(target=brew)
    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print(f'total time : {end-start:.2f} seconds')
