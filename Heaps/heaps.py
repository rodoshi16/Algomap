class Heap:

    def __init__(self, l: list):
        self.heap = l

    def FindMax(self):
        return self.heap[0]

    def extractMax(self):
        """


        >>> h = Heap([17, 9, 15, 7, 7, 9, 5, 3, 4])
        >>> h.extractMax()
        >>> h.heap
        [15, 9, 9, 7, 7, 4, 5, 3]
        >>> t = Heap()

        """
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()

        i = 0
        if 2*i+1 > len(self.heap) and 2*i+2 > len(self.heap):
            return
        elif 2*i+2 > len(self.heap):
            self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
        elif 2*i+1 > len(self.heap):
            self.heap[i], self.heap[2*i+2] = self.heap[2*i+2], self.heap[i]

        while (2*i+1) <= len(self.heap) and 2*i+2 <= len(self.heap):
            if self.heap[2*i+2] > self.heap[2*i+1]:
                max_l = 2*i+2
            else:
                max_l = 2*i+1

            self.heap[i], self.heap[max_l] = self.heap[max_l], self.heap[i]
            i = max_l























