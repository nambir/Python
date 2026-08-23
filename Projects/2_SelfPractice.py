import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# ── GIL: only one thread runs Python bytecode at a time ──
# Good for I/O-bound (network, disk) | Bad for CPU-bound (math)

counter = 0
lock = threading.Lock()

def unsafe_increment():
    global counter
    counter += 1              # race condition without lock

def safe_increment():
    global counter
    with lock:                # only one thread at a time
        counter += 1

# ── THREADS: lightweight, shared memory ──
threads = [threading.Thread(target=unsafe_increment) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()                  # wait for all to finish
print("Counter:", counter)    # 100

# ── ThreadPoolExecutor: pool for I/O tasks ──
def fetch(url_id):
  time.sleep(0.1)               # simulate network I/O
  return f"data-{url_id}"

# with ThreadPoolExecutor(max_workers=4) as pool:
#     results = list(pool.map(fetch, range(8)))
# print(results)

# CPU-bound heavy math → use ProcessPoolExecutor instead



from concurrent.futures import (ProcessPoolExecutor,
                                ThreadPoolExecutor)
from PIL import Image
import io
import urllib.request

def download(url):
    with urllib.request.urlopen(url, timeout=10) as r:
        return r.read()          # wait on network

urls = [
    "http://a/img1.jpg",
    "http://b/img2.jpg",
]

def heavy_resize(data):        # data = one item from images
    img = Image.open(io.BytesIO(data))
    img = img.resize((200, 200))   # CPU pixel work
    out = io.BytesIO()
    img.save(out, format="JPEG")
    return out.getvalue()

if __name__ == "__main__":
    # 1) I/O first — threads. images = [bytes1, bytes2]
    with ThreadPoolExecutor(max_workers=4) as pool:
        images = list(pool.map(download, urls))

    # 2) then CPU — processes. Feed those bytes in.
    with ProcessPoolExecutor(max_workers=4) as pool:
        out = list(pool.map(heavy_resize, images))

    # OUTPUT
    # out → [resized1, resized2]  (CPU on multiple cores)