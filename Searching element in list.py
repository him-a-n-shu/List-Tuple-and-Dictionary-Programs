lst1 = eval(input("Enter a list: "))

ele = int(input("Enter element to be searched: "))
print(type(lst1))
if ele in lst1:
    print("Yes, The element is present in List.")
    print("Index:", lst1.index(ele))
    print("It occurs", lst1.count(ele), "times.")
else:
    print("Error")

'''
l = eval(input("e"))
ele = input("d")
if ele in l:
    print("y")

lst1 = eval(input("Enter a list: "))
ele = input("Enter element to be searched: ")
for i in range(len(lst1)):
    if ele==lst1[i]:
        print("y")'''
'''
mylist = []
print("Enter 5 elements for the list: ")
for i in range(5):
    val = int(input())
    mylist.append(val)

print("Enter an element to be search: ")
elem = int(input())

for i in range(5):
    if elem == mylist[i]:
        print("\nElement found at Index:", i)
        print("Element found at Position:", i+1)
'''
