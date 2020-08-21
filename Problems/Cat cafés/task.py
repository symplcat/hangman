cafe = ['', 0]

while True:
    temp_cafe = input()
    temp_cafe = temp_cafe.split()

    if len(temp_cafe) < 2:
        break
    elif int(temp_cafe[-1]) > int(cafe[-1]):
        cafe = temp_cafe

print(cafe[0])