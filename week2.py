my_list=[]
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#insert 15 at the second position
my_list.insert(1,15)
print(my_list)

#Extend with another list [50, 60, 70]
another_list = [50,60,70]
my_list.extend(another_list)
print(my_list)

#remove the last element
my_list.pop()
print(my_list)

#sort my_list in ascending order
my_list.sort()
print(my_list)

#find and print the index of value 30
index_30=my_list.index(30)
print(index_30)
