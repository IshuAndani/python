import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def brew(lock1, lock2):
    print(f"{threading.current_thread().name} waiting for {lock1}")
    with lock1:
        print(f"{threading.current_thread().name} acquired {lock1}")
        time.sleep(3)
        print(f"{threading.current_thread().name} waiting for {lock2}")
        with lock2:
            print(f"{threading.current_thread().name} acquired {lock2}")
        print(f"{threading.current_thread().name} released {lock2}")
    print(f"{threading.current_thread().name} released {lock1}")


t1 = threading.Thread(
    target=brew,
    args=(
        lock1,
        lock2,
    ),
    name="t1",
)
t2 = threading.Thread(
    target=brew,
    args=(
        lock2,
        lock1,
    ),
    name="t2",
)
start = time.time()
t1.start()
t2.start()
t2.join()
t1.join()
end = time.time()
print(f"end of main thread in {end - start:.2f} seconds")
