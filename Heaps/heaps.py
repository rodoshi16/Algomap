class Heap:
    def __init__(self, capacity: int):
        self.heap = [0] * capacity
        self.size = 0

    def parent(self, i):
        return (i-1) // 2

    def left_child(self, i):
        return (2*i) + 1

    def right_child(self, i):
        return (2*i) + 2

    def peek(self):
        """

        Return the root element without removing it.
        """

        if not self.heap:
            raise IndexError("Heap is empty")

        return self.heap[0]

    def insert(self, val):
        """

        Insert the element val in the heap. For a max heap:

        - insert the val at the very end
        - if the parent < val: swap
        - keeping doing this until the parent is greater

        :param val:
        :return:
        """

        self.heap.append(val)
        index = len(self.heap) - 1

        while index > 0:
            parent = (index-1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

        self.size += 1

    def extract(self):
        """
        Remove the top element and return it.

        - replace the last ele with the root
        - swap ele with largest of the 2 children every time
        - keep going until the children are no longer larger
        """

        root = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        n = len(self.heap)

        i = 0

        while i < len(self.heap):
            m = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self.heap[left] > self.heap[m]:
                m = left
            if right < n and self.heap[right] > self.heap[m]:
                m = right

            if m == i:
                break

            self.heap[m], self.heap[i] = self.heap[i], self.heap[m]
            i = m

        self.size += 1
        return root














