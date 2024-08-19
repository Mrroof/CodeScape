name = 'kate'
age = 45
Height = 2.5
def handy(anythings):
    return f"Hello,{anythings}!"
print(handy(name))

numbers = [2,3,4,5,6,7]
for num in numbers:
    print(num)

dickson = {'name': name, 'age': age, 'Height': Height }
print(dickson)

unique = {1,2,3,4,5,6}
print(unique)

point = (2,3)
x,y = point 
print(f'Coordinate is ({x},{y})')

def calculate_area(radius):
    pi = 3.142
    Area = pi * radius ** 2
    return Area
print(f'printing the area of a circle {calculate_area(0)}') 


print ("Hi")