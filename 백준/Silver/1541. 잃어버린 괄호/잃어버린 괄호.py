expression = input().split('-')
result = 0

first_subtract_block = list(map(int, expression[0].split('+')))
result += sum(first_subtract_block)

for block in expression[1:]:
    numbers = list(map(int, block.split('+')))
    result -= sum(numbers)

print(result)