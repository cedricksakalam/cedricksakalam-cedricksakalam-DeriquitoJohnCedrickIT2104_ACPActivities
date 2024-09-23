#sets
set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

#Set Differrence
difference_set1 = set1 - set2
difference_set2 = set2 - set1
print ("Set Difference")
print (difference_set1)
print (difference_set2)

#Union of Sets
union_set = set1 | set2
print ("Union Set")
print (union_set)

#Symmetric Difference
symmetric_difference1 = set2 ^ set1
symmetric_difference2 = set1 ^ set2
print ("Symmetric Difference")
print (symmetric_difference1)
print (symmetric_difference2)

#Set Intersection
set_interesection1 = set1 & set2
set_interesection2 = set2 & set1
print ("Set Intersection")
print (set_interesection1)
print (set_interesection2)