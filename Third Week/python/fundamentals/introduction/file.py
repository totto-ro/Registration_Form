num1 = 42 #- variable declaration
num2 = 2.3 #- variable declaration
boolean = True #- Data Types - Primitive - Boolean
string = 'Hello World' #- Data Types - Primitive - Boolean -Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #- Data Types - Composite - List 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #- Data Types - Composite  - Dictionary
fruit = ('blueberry', 'strawberry', 'banana')  #- Data Types - Composite  - Dictionary - Tuples
print(type(fruit)) # - log statement
print(pizza_toppings[1]) # - access value - List  - log statement
pizza_toppings.append('Mushrooms') # - access value - add value - List  - log statement
print(person['name']) # - access value - Dictionary - log statement
person['name'] = 'George' # - access value - change value - Dictionary - log statement
person['eye_color'] = 'blue'  # - access value  - add value - Dictionary - log statement 
print(fruit[2]) # - access value - Tuples - log statement

if num1 > 45: # - conditional - if
    print("It's greater")
else: # - conditional - else
    print("It's lower")

if len(string) < 5: # - conditional - if
    print("It's a short word!") 
elif len(string) > 15: # - conditional - else if
    print("It's a long word!")
else: # - conditional - else
    print("Just right!")

for x in range(5): #- for loop - start
    print(x)
for x in range(2,5): # - for loop - increment
    print(x)
for x in range(2,10,3): # - for loop - sequence
    print(x)
x = 0
while(x < 5): #- while loop - start - stop
    print(x)
    x += 1

pizza_toppings.pop() # - Data Types - Composite - List - delete value
pizza_toppings.pop(1)  # - Data Types - Composite - List - access value - delete value

print(person) # - accese value - Dictionary - log statement
person.pop('eye_color') # - accese value - Dictionary - delete value
print(person) # - accese value - Dictionary - log statement

for topping in pizza_toppings: # - for loop - conditional - if
    if topping == 'Pepperoni': # - Boolean
        continue # - continue
    print('After 1st if statement') # - log statement
    if topping == 'Olives': # - Boolean
        break # - break

def print_hello_ten_times(): # - function
    for num in range(10): # - for loop
        print('Hello') # - log statement

print_hello_ten_times() # - log statement

def print_hello_x_times(x): # - function
    for num in range(x): # - for loop
        print('Hello') # - log statement

print_hello_x_times(4) # - accese value - change value - log statement

def print_hello_x_or_ten_times(x = 10): # - function
    for num in range(x): # - for loop
        print('Hello') # - log statement

print_hello_x_or_ten_times() # - log statement
print_hello_x_or_ten_times(4)  # - accese value - change value - log statement


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)