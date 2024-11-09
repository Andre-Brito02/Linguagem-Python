nums = [1, 2, 3, 4, 5, 6]

for i in range(0, len(nums)):
    x = 0
    while(x <= i):
        print(nums[x], end=" ")
        x += 1
    print()

# texto = 'Olá mundo'
# print(texto[::-1])# Inverter um texto