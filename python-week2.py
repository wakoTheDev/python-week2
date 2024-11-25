my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

my_list.insert(2,15)


print(my_list)

new_list = [50,60,70]

my_list = my_list + new_list

print(my_list)
# removing the last name
my_list.remove(70)

print(my_list)

my_list.sort()
print(my_list)


index_of_30 = my_list.index(30)

print(index_of_30)


    