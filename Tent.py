def cyl(h,r):
    area_cyl = 2*3.14*r*h #Area of cylindrical part
    return(area_cyl)
#function definition
def con(l,r):
    area_con = 3.14*r*l #Area of conical part
    return(area_con)
#function definition
def post_tax_price(cost): #compute payable amount for the tent
    tax = 0.18 * cost;
    net_price = cost + tax
    return(net_price)

print("Enter values of cylindrical part of the tent in meters:")
h = float(input("Height: "))
r = float(input("Radius: "))
csa_cyl = cyl(h,r) #function call
l = float(input("Enter slant height of the conical area in meters: "))
csa_con = con(l,r) #function call
#Calculate area of the canvas used for making the tent
canvas_area = csa_cyl + csa_con
print("Area of canvas = ",canvas_area," m^2")
#Calculate cost of canvas
unit_price = float(input("Enter cost of 1 m^2 canvas in rupees: "))
total_cost = unit_price * canvas_area
print("Total cost of canvas before tax = ",total_cost)
print("Net amount payable (including tax) = ",post_tax_price(total_cost))
