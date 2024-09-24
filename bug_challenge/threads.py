import threading

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

counter = Counter()

def worker():
    for _ in range(100000):
        counter.increment()

threads = []
for _ in range(10):
    thread = threading.Thread(target=worker)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(counter.count)


