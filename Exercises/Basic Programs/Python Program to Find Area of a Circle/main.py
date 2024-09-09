#Area of a circle
#version 0.1.0
#@Iustin Desrobitu

PI = 3.142

def circle_area_calculator(user_radius_in):
    area = PI * user_radius_in ** 2
    return area

print("This program takes the radius of a circle and finds the area")
user_radius = float(input("insert the radius: "))

area = circle_area_calculator(user_radius)
print(f"The area of this circle is {area}")