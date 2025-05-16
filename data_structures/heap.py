class MinHeap:
    # constructor
    def __init__(self):
        self.heap = []

    # insert
    def insert(self, value):
        self.heap.append(value)
        self.shift_up(len(self.heap)-1)

    def shift_up(self, index):
        parent_index = (index - 1) // 2
        # keep shifting value up to its parent if smaller value
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index -1) // 2

    # extract/delete -- only min value can be deleted
    def delete(self):
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.shift_down(0)
        return min_value

    def shift_down(self, index):
        left = 2*index + 1
        right  = 2*index + 2
        while (left < len(self.heap) and self.heap[index] > self.heap[left]) or (right < len(self.heap) and self.heap[index] > self.heap[right]):
            smallest_child = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            self.heap[index], self.heap[smallest_child] = self.heap[smallest_child], self.heap[index]
            index = smallest_child
            left = 2*index + 1
            right = 2*index + 2
            
    # get_min
    def get_min(self):
        return self.heap[0] if len(self.heap) > 0 else None
    # is_empty
    def is_empty(self):
        return len(self.heap) == 0

    # size
    def size(self):
        return len(self.heap)

    # heapify/build_heap
    def heapify(self, nums):
        res = []
    


if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.insert(1)
    min_heap.insert(4)
    min_heap.insert(2)
    min_heap.insert(3)

    min_heap.delete()


    print(min_heap.heap)