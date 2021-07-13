def heapify(num_list, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and num_list[l] < num_list[smallest]:
        smallest = l

    if r < n and num_list[r] < num_list[smallest]:
        smallest = r

    if smallest != i:
        num_list[i], num_list[smallest] = num_list[smallest], num_list[i]
        heapify(num_list, n, smallest)


def heapsort(num_list):
    n = len(num_list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(num_list, n, i)

    for i in range(n - 1, -1, -1):
        num_list[0], num_list[i] = num_list[i], num_list[0]
        heapify(num_list, i, 0)


num_list = [1, 12, 9, 5, 6, 10]
heapsort(num_list)
n = len(num_list)
print("Sorted array is")
for i in range(n):
    print("%d " % num_list[i], end='')
