'''n= int (input("Enter a Number: "))

if n%2==0:
    print(n, "Its a even")
else:
    print(n, "Its odd")    '''


''''n = int(input("Enter a Number: "))

print("Even Numbers are:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

print("Odd Numbers are:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)'''

n= int(input("Enter a Number: "))

count = 0

print("Even numbers are")
for i in range(1,n+1):
    if i %2 == 0:
        count += 1
        print(i)

print("Odd Numbers in range are:",count)        

count = 0
print("Odd numbers are")
for i in range(1,n+1):
    if i %2 != 0:
        count += 1
        print(i)        

print("Odd Numbers in range are:",count)        

