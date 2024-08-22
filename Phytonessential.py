# 1. an integer as input and checks whether the number is even or odd.

num = int(input("Enter a number: ")) 

if num % 2 == 0:
    print("The number",num, "is even")
else:
    print("The number",num, "is odd")

#2. generates the multiplication table of a number provided by the user.

num = int(input("Enter a number: "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

#3. takes three numbers as input from the user and prints the largest one.

a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
c = int(input("Enter third number: "))

print("The largest number is", max(a, b, c))

#4. counts the number of vowels (a, e, i, o, u) in a given string.Input: Hello World Output: 3

string = input("Enter a string: ")
vowels = "a,e,i,o,u,A,E,I,O,U"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("The number of vowels in", string, "is", count)