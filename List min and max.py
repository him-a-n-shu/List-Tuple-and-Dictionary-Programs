'''l_int = eval(input("Enter a List: "))
l = list(l_int)

print(l(min))
print(l(max))

#Searching element in list
list1 = [ 1, 6, 3, 5, 3, 4 ]
print(list1)
n = input("Enter element to be searched: ")

for x in list1:
    if (x==4):
        print("yes")
        pass
    else:
        print("no")
'''

l1 = eval(input("Enter a List: "))
n_max = 0
n_min = l1[0]
for i in l1:
    if i > n_max:
        n_max=i

for j in l1:
    if j< n_min:
        n_min=j
print("Largest Number: ", n_max)
print("Smallest Number: ", n_min)
