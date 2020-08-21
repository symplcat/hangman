# put your python code here
sum_squares = 0
sum_numbers = 0
while True:
    number = int(input())
    sum_squares += number ** 2
    sum_numbers += number
    if sum_numbers == 0:
        break

print(sum_squares)