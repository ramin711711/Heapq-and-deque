import collections
from collections import deque

de = collections.deque([1, 2, 3])
print("deque: ", de)

de.append(4) # right end

print("\nThe deque is: ")
print(de)


de.appendleft(6)


print("\nThe deque2 is: ")
print(de)


de.extend([4,5,6]) # adds numbers to right end 

print ("Extending deque at end: ")
print (de)

de.extendleft([7,8,9]) # add numbers to left end 


print ("Extending deque at beginning: ")
print (de)


de.rotate(-3) # rotates the deque
print ("rotating deque: ")
print (de)


de.reverse() # reverses the deque
print ("reversing deque: ")
print (de)

de = deque([1, 2, 3, 4, 5, 6])
print("Cur Deque: ", de)

print("Front element:", de[0])

print("Back element:", de[-1])


de = deque([1, 2, 3, 4, 5, 6])
print("Cur Deque: ", de)


de.pop() #deletes element from right end


print("\nAfter deleting from right is: ")
print(de)
