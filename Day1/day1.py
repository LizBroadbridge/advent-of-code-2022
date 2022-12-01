input_data = open('input.txt', 'r').read().split('\n')

def elf_calories(input_data):
    calorie_count = 0
    elf_calories = []
    for item in input_data:
        if item != '':
            calorie_count += int(item)
        else:
            elf_calories.append(calorie_count)
            calorie_count = 0
    elf_calories.sort(reverse=True)
    print(elf_calories)
    print(sum(elf_calories[:3]))
elf_calories(input_data)
