from graphics import rectangle,circle
from graphics.graphics_3d import cuboid,sphere
# using rectangle module
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
print("Area of rectangle = ", rectangle.area(length, width))
print("Perimeter of rectangle = ", rectangle.perimeter(length, width))
# using circle module
radius = int(input("Enter the radius of the circle: "))
print("Area of circle = ", circle.area(radius))
print("Perimeter of circle = ", circle.perimeter(radius))
# using cuboid module
clength = int(input("Enter the length of the cuboid: "))
cwidth = int(input("Enter the width of the cuboid: "))
cheight = int(input("Enter the height of the cuboid: "))
print("Surface Area of cuboid = ", cuboid.surface_area(clength, cwidth, cheight))
print("Volume of cuboid = ", cuboid.volume(clength, cwidth, cheight))
# using sphere module
sradius = int(input("Enter the radius of the sphere: "))
print("Surface Area of sphere = ", sphere.surface_area(sradius))
print("Volume of sphere = ", sphere.volume(sradius))



mits@mits-HP-280-Pro-G6-Microtower-PC:~$ python3 main.py
Enter the length of the rectangle: 4
Enter the width of the rectangle: 5
Area of rectangle =  20
Perimeter of rectangle =  18
Enter the radius of the circle: 6
Area of circle =  113.09733552923255
Perimeter of circle =  37.69911184307752
Enter the length of the cuboid: 5
Enter the width of the cuboid: 6
Enter the height of the cuboid: 2
Surface Area of cuboid =  104
Volume of cuboid =  60
Enter the radius of the sphere: 8
Surface Area of sphere =  804.247719318987
Volume of sphere =  2144.660584850632
mits@mits-HP-280-Pro-G6-Microtower-PC:~$ 
