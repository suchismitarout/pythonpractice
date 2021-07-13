class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, node):
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            for i in range(len(self.queue)):
                if node.priority < self.queue[i].priority:
                    if i == len(self.queue) - 1:
                        self.queue.insert(i + 1, node)
                    else:
                        continue
                else:
                    self.queue.insert(i, node)
                    return True

    def delete(self):
        return self.queue.pop(0)

    def print(self):
        for i in self.queue:
            print(i.val)

    def size(self):
        return len(self.queue)


#
# node1 = Node(10,3)
# node2 = Node(6, 1)
# node3 = Node(12, 2)
# node4 = Node(9, 4)
# p_queue = PriorityQueue()
# p_queue.insert(node1)
# p_queue.insert(node2)
# p_queue.insert(node3)
# p_queue.insert(node4)
# p_queue.print()
# p_queue.delete()
# p_queue.print()

from functools import reduce

l = [[3, 3], [5, -1], [-2, 4]]
k = []
for i in l:
    k.append(reduce((lambda x, y: x ** 2 + y ** 2), i))

node1 = Node(l[0], k[0])
node2 = Node(l[1], k[1])
node3 = Node(l[2], k[2])
pqueue = PriorityQueue()
pqueue.insert(node1)
pqueue.insert(node2)
pqueue.insert(node3)
# pqueue.print()
for i in range(1):
    pqueue.delete()
pqueue.print()

