"""Slide 18 — Threading & GIL practice."""
import threading
from concurrent.futures import ThreadPoolExecutor


def run_with_lock() -> int:
    counter = 0
    lock = threading.Lock()

    def safe_increment():
        nonlocal counter
        with lock:
            counter += 1

    threads = [threading.Thread(target=safe_increment) for _ in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter


def io_task(n: int) -> str:
    return f"done-{n}"


if __name__ == "__main__":
    print("counter with lock:", run_with_lock())
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(io_task, range(4)))
    print("thread pool:", results)
