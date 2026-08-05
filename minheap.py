# class MinHeap:
#     def __init__(self):
#         self.heap = []
#     def parent(self,i):
#         return (i-1)//2
#     def leftchild(self,i):
#         return 2*i+1
#     def rightchild(self,i):
#         return 2*i+2
#     def insertion(self,x):
#         self.heap.append(x) 
#         self.heapifyup(len(self.heap)-1)
#     def heapifyup(self,i):
#         while i>0:
#             p=self.parent(i)
#             if self.heap[i]>=self.heap[p]:
#                 break
#             self.heap[i],self.heap[p]=(self.heap[p],self.heap[i])
#             i=p
#     def disp(self):
#         print(self.heap)
# h1=MinHeap()
# h1.disp
# h1.insertion(10)
# h1.insertion(40)
# h1.insertion(45)
# h1.insertion(80)
# h1.insertion(110)
# h1.disp
# h1.insertion(60)
# h1.disp()
# h1.insertion(5)
# h1.disp()
                