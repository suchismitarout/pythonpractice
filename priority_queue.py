class PriorityQueue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert_into_queue(self, data):
        self.queue.append(data)

    def delete_from_queue(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print("pr-queue")
            exit()

    def print_queue(self):
        return self.queue


p = PriorityQueue()
p.insert_into_queue(12)
p.insert_into_queue(10)
p.insert_into_queue(5)
p.insert_into_queue(3)
p.insert_into_queue(18)
print(p.print_queue())
p.delete_from_queue()
print(p.print_queue())
p.delete_from_queue()
print(p.print_queue())

