import sys


class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [0] * (self.max_size+1)
        self.heap[0] = -1 * sys.maxsize
        self.front = 1
        self.size = 0

    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2 * pos) + 1

    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def is_leaf_present(self, pos):
        if pos >= self.size // 2 and pos <= self.size:
            return True
        return False

    ###-- , 4,9,5,8,6,
    ### -  4,6,5,8,9
    def min_heapify(self, pos):
        if not self.is_leaf_present(pos):
            if self.heap[pos] > self.heap[self.left_child(pos)] or self.heap[pos] > self.heap[self.right_child(pos)]:
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element
        current = self.size
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.min_heapify(self.front)
        return popped

    def print(self):
        r = []
        for i in range(1, self.size // 2 + 1):
            print(self.heap[i], self.heap[2 * i], self.heap[(2 * i) + 1])

    def print_heap(self):
        r = []
        for i in range(1, self.size+1):
            print(self.heap[i],end=" ")
        print("\n")


    def min_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.min_heapify(i)


heap = MinHeap(7)
h = [2, 6, 1, 8, 4, 9, 5]
for i in h:
    heap.insert(i)
heap.print()
heap.min_heap()
# print(heap.heap)
# for i in range(2):
#     heap.remove()
# print(heap.heap)
# print(heap.front)
#
print("++++++++++++++++++++++++++++")
heap.remove()
heap.print()
print("...")
heap.print_heap()
print("=====")

heap.remove()
heap.print_heap()
heap.remove()
heap.print_heap()
print("----")
heap.remove()
heap.print_heap()
print("...")
heap.remove()
heap.print_heap()