def increment(list2):
    n = int(input("How much the element should be incremented: "))
    for i in range(0, len(list2)):
        list2[i] += n
    print('Reference of list Inside Function',id(list2))

list1 = eval(input("Enter List: "))
print("Reference of list in Main",id(list1))
print("The list before function call: ", list1)
increment(list1)
print("The list after the function call")
print(list1)
