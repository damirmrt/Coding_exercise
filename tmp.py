import heapq     

class MedianFinder:

    def __init__(self):
        self.arr = []
        heapq.heapify(self.arr)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr, num)
        

    def findMedian(self) -> float:
        lenght = len(self.arr)
        if lenght % 2 != 0:
            return self.arr[int(lenght / 2)]
        else:
            res = (self.arr[int(lenght / 2) - 1] + self.arr[int(lenght / 2)]) / 2
        return res


l = MedianFinder()
print(l.addNum(1))
print(l.findMedian())
print(l.addNum(3))
print(l.findMedian())
print(l.addNum(2))
print(l.findMedian())

