class MinHeap:
    def __init__(self):
        self.heap = []
    def parent(self,i):
        return (i-1)//2
    def leftchild(self,i):
        return 2*i+1
    def rightchild(self,i):
        return 2*i+2
    def insertion(self,x):
        self.heap.append(x) 
        self.heapifyup(len(self.heap)-1)
    def heapifyup(self,i):
        while i>0:
            p=self.parent(i)
            if self.heap[i]>=self.heap[p]:
                break
            self.heap[i],self.heap[p]=self.heap[p],self.heap[i]
                