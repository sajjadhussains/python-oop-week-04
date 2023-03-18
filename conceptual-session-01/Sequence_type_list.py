# Ordered collect of similar or different data types
# Sequence->strings(immutable),list(mutable),Tupple(immutable)
"""Creating a list"""
# list = []
# print(list)
"""creating a list using list() method/function"""
# list1="hello"
# print(list(list1))
"""Creating a list with the use of a string"""
# str1="hello"
# list2=[str1]
# print(list2)
"""Creating a list with the use of multiple values"""
# list3=["working","with","list"]
# print(list3)
"""Multi-Dimensional list(By Nesting a list inside a list)"""
# list4=[["working","with"],["person"]]
# print(list4)
"""append method"""
list5=[1,2,3,4,5,6,8,0.5]
# list6=[7,8,9]
# list5.append(6)-->output:[1,2,3,4,5,6]
# list5.clear()--->output:[]
# list6=list5.copy()--->output:[1,2,3,4,5,6]
# output=list5.count(4)--->output:1
# list5.extend(list6)
# output=list5.index(5)
# print(output)
# list5.insert(0,100)
# output=list5.pop()
# print(output)
# list5.remove(5)->remove the first item with the specified value
# list5.reverse()
list5.sort()
print(list5)