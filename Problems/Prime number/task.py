number = int(input())
prime = bool
if number == 1:
    prime = False
for a in range(2, number):
    if prime == False:
        break
    for b in range(2, number):
        if a * b == number:
            prime = False
            break
if prime == False:
    print("This number is not prime")
else:
    print("This number is prime")