# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 12:35:09 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

lst = []
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)  # Output: [1, 2, 3]
lst.extend([5, 6, 7])
print(lst)  # Output: [1, 2, 3, 5, 6, 7]
lst.insert(3, 4)
print(lst)  # Output: [1, 2, 3, 4, 5, 6, 7]
lst.pop()
print(lst)  # Output: [1, 2, 3, 4, 5, 6]
lst.remove(6)
print(lst)  # Output: [1, 2, 3, 4, 5]
index = lst.index(3)
print(index)  # Output: 2
lst.reverse()
print(lst)  # Output: [5, 4, 3, 2, 1]
new_lst = lst[:3]
print(new_lst)  # Output: [5, 4, 3]

lst = [2, 4, 1, 5, -1]

# sorted() returns a new sorted list without modifying the original list

sorted_lst = sorted(lst)
print(sorted_lst)  # Output: [-1, 1, 2, 4, 5]

# list.sort() sorts the list in place (modifies the original list)
lst.sort()
print(lst)  # Output: [-1, 1, 2, 4, 5]

#Fix:
#To create three independent lists, you need to append copies of lst2 to lst1:


#lst1 = []
#lst2 = [1, 2, 3]

#lst1.append(lst2.copy())  # Append a copy of lst2
#lst1.append(lst2.copy())  # Append another copy of lst2
#lst1.append(lst2.copy())  # Append another copy of lst2

#lst1[0][0] = 10

#print(lst1)  # Output: [[10, 2, 3], [1, 2, 3], [1, 2, 3]] 
