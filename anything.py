import sys
print("My python version is: ")
print(sys.version)

print("Hello, world!")

input_first = input("Type your first name: ")
input_last = input("Type your last name: ")
print("Hello, " + input_first + " " + input_last)


input_num=int(input("Type a whole positive number: "))
print (input_num)

num_sq=input_num * input_num
print(num_sq)

if(input_num > 10): 
    print("Your number was bigger than 10")
else:
    print("Your number was less than or equal to 10")

i = 1
while(i <= input_num):
    print(i)
    i = i + 1

def goodbye():
    print("Goodbye, " + input_first + " " + input_last)
goodbye()

def goodbyeMulti(times):
    for value in range(times):
        goodbye()

goodbyeMulti(3)