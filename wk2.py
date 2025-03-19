my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)    
my_list.extend([50, 60, 70])
my_list.remove(70)  #my_list.pop()  Removes the value 70 instead of popping the last item    
my_list.sort()
index_30 = my_list.index(30)
print(index_30)

# Just to see the output
print(my_list)
