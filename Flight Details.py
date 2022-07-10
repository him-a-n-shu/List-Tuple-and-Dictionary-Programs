'''n = int(input("Enter the number of Students: "))
d = {}
for x in range(n):
    name = input("Enter the Student name: ")
    d[name]= input("Enter Subject Name: ")
print(d)'''

n = int(input("Enter the number of Students: "))
d = {}
for x in range(n):
    print("\n")
    roll_no = int(input("Enter roll number:"))
    name = input("Enter the Student name: ")
    pert = float(input("Enter percentage:"))
    tup_st = (name, pert)
    d[roll_no] = tup_st
print(d)



'''d = {}
d['fname'] = eval(input(("Enter the Flight name: ")))
d['fare'] = eval(input("Enter Fare: "))
print(d)

'''
'''
d = {'Indigo' : 7000, 'SpiceJet' : 8000, 'Air India' : 5000}
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(max(print(d.values())))
print(min(print(d.values())))'''
