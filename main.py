import threading

lock = threading.RLock()


def worker():
    lock.acquire()
    try:
        thread_name = threading.current_thread().name
        print(f"Выполняется поток {thread_name}")

    finally:
        lock.release()


def main():
    threads = []

    for i in range(5):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()