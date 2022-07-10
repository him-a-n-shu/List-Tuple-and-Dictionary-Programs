num = int(input("Enter a number to generate its pattern = "))

for i in range(1,num+1):
    for j in range(1,i+1):
        for k in range(1,j+1):
            for l in range(1,k+1):
                print("*",end='')
    print()    
