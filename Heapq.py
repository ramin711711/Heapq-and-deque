
# The heapq module in Python provides functions to work with heaps, which are binary trees where the parent node is always smaller than or equal to its children (for a min-heap)
import heapq

l = [5, 7, 9, 1, 3]
 
heapq.heapify(l) #convert list into heap.
 
print ("Heap is: ", (list(l)))


heapq.heappush(l, 4) #pushing elements into heap.
print("The heap after push: ", l)

print("The popped and smallest element is : ", end="") #poppint the smallest element.
print(heapq.heappop(l))



list1 = [5, 1, 9, 4, 3]
list2 = [5, 7, 9, 4, 3]

heapq.heapify(list1)
heapq.heapify(list2)
 
print("\nThe 1st popped item is: ", heapq.heappushpop(list1, 2)) #pushes and popps items simultaneously
 
print("\nThe 2nd popped item is:", heapq.heapreplace(list2, 2)) #pushes and popps items simultaneously



list3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
 
heapq.heapify(list3)
 
print("\nThe 3 largest numbers: ", heapq.nlargest(3, list3)) #nlargest prints n largest numbers.
print("The 3 smallest numbers: ", heapq.nsmallest(3, list3)) #nsmallest prints n smallest numbers.



v = [5, 1, 3, 7, 4, 2]

heapq.heapify(v)
print("\nHeap:", v)
 
heapq.heappush(v, 6)
print("Heap after push:", v)

 
smlst = heapq.heappop(v)
print("\nThe smallest element:", smlst)
print("\nHeap after pop:", v)
 

n_smlst = heapq.nsmallest(3, v)
print("Smallest 3 elements:", n_smlst)
 

n_lrgst = heapq.nlargest(2, v)
print("Largest 2 elements:", n_lrgst)
