#name = {"toyto", "benz",  "volve"}
#name.dd('ford')
#print(name)

#GIVING TWO SETS 
set1 ={'banana','apple','guava','grape','orange'}
set2 ={'cashew', 'guava','pineapple','avocado'}
# finding the union while union is everything they have 
#finding interception.means their similiarties
# in a set it has only removing and adding
set3 = set1|set2 
print(set3)
 #looking for intersection
fruits  = set1& set2
print(fruits)
set1.add('mango')
set2.add('mango')
print("adding mango to set1 and set2")
#  removingFROM THE SETS
set1.remove('apple')
print(set1)
