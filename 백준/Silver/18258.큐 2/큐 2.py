import sys

class Queue:

    def __init__(self):
        self.queue = []
        self.index = 0

    def empty(self):
        if self.index == len(self.queue):
            return 1

        else: return 0

    def push(self, x):
        self.queue.append(x)
        return

    def pop(self):
        if self.empty() == 1:
            return -1

        else:
            res = self.queue[self.index]
            self.index += 1
            return res

    def size(self):
        return len(self.queue) - self.index

    def front(self):
        if self.empty() == 1:
            return -1

        else:
            return self.queue[self.index]

    def back(self):
        if self.empty() == 1:
            return -1

        else:
            return self.queue[-1]


n = int(sys.stdin.readline())

queue = Queue()

for _ in range(n):
    func = sys.stdin.readline().strip() # 개행문자 삭제 필요

    if "push" in func:
        func, num = func.split()
        queue.push(int(num))

    elif func == 'pop':
        print(queue.pop())

    elif func == 'size':
        print(queue.size())

    elif func == 'empty':
        print(queue.empty())

    elif func == 'front':
        print(queue.front())

    elif func == 'back':
        print(queue.back())
