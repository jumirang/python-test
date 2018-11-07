# Set
mySet = {10,20,30,100,20,30} # 중복 제거..
# print (mySet[0])
# print (mySet[0:3])

# mySet.add(1000)
# mySet.remove(30)

# print (mySet)
# print (type(mySet))

mySet1 = {10,20,30}
mySet2 = {20,30,40,50}

print (mySet1.intersection(mySet2))
print (mySet1 & mySet2) # 교집합

print (mySet1.union(mySet2))
print (mySet1 | mySet2) # 합집합

print (mySet1.difference(mySet2))
print (mySet1 - mySet2) # 차집합

print (mySet1.symmetric_difference(mySet2))
print (mySet1 ^ mySet2) # 대상 차집합 (합집합 - 차집합)
