class Queue:
    def __init__(self, limit=None):
        self.limit = limit
        self.que = []
        self.front = None
        self.end = None
        self.size = 0

    def is_empty(self):
        return len(self.que) <= 0

    def enque(self, new_data):
        if len(self.que) >= self.limit:
            print("Queue is already reached to its limit")
            return
        else:
            self.que.append(new_data)
            if self.front is None:
                self.front = self.end = 0
            else:
                self.size = self.end
        self.size += 1

    def dequeue(self):
        if len(self.que) <= 0:
            print("No more nodes to be deleted")
            return

        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.end = None
            else:
                self.end = self.size - 1

    def get_front(self):
        if self.front is None:
            print("no front node")
        return self.que[self.front]

    def get_end(self):
        if self.end is None:
            print("no nodes present")
        return self.que[self.end]


queue = Queue(4)
queue.enque(12)
queue.enque(23)
queue.enque(11)
queue.enque(15)
queue.enque(26)
print(queue.que)
queue.dequeue()
print(queue.que)
print(queue.get_front)