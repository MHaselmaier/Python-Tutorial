import threading


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


class IncrementerThread(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        for i in range(1000000):
            self.counter.increment()


counter = Counter()
threads = []
for i in range(10):
    thread = IncrementerThread(counter)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(counter.count)