list1 = eval(input("Enter a list: "))
sum_even = 0
sum_odd = 0
for elem in list1:
    if (elem%2 == 0):
        sum_even += elem
        continue
    else:
        sum_odd += elem

print("Sum of even integers in list: ", sum_even)
print("Sum of even integers in list: ", sum_odd)
