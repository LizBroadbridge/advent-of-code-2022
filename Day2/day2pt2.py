input_data = open('input.txt', 'r').read().split('\n')[:-1]

total_score = 0

array_input_data = []

for item in input_data:
    array_input_data.append(list(item))

for item in array_input_data:
    opponent = item[0]
    desired_result = item[2]

    if desired_result == 'X': # Lose
        if opponent == 'A': # Rock
            item[2] = 'Z' # Scissors
        elif opponent == 'B': # Paper
            item[2] = 'X' # Rock
        else: # Scissors
            item[2] = 'Y' # Rock
    elif desired_result == 'Y': # Draw
        if opponent == 'A': # Rock
            item[2] = 'X' # Rock
        elif opponent == 'B': # Paper
            item[2] = 'Y' # Paper
        else: # Scissors
            item[2] = 'Z' # Scissors
    else: # Win
        if opponent == 'A': # Rock
            item[2] = 'Y' # Paper
        elif opponent == 'B': # Paper
            item[2] = 'Z' # Scissors
        else: # Scissors
            item[2] = 'X' # Rock
print(array_input_data)

for item in array_input_data:
    if (item[0] == 'A' and item[2] == 'X'):
        score = 4 
        total_score += 4
        #print('Draw')
        #print(score)
    elif (item[0] == 'B' and item[2] == 'Y'):
        score = 5
        total_score += 5 
        #print('Draw')
        #print(score)
    elif (item[0] == 'C' and item[2] == 'Z'):
        score = 6
        total_score += 6
        #print('Draw')
        #print(score)
    elif (item[0] == 'C' and item[2] == 'X'):
        score = 9
        total_score += 7
        #print('Win')
        #print(score)
    elif (item[0] == 'A' and item[2] == 'Y'):
        score = 8
        total_score += 8
        #print('Win')
        #print(score)
    elif (item[0] == 'B' and item[2] == 'Z'):
        score = 9
        total_score += 9
        #print('Win')
        #print(score)
    elif (item[0] == 'B' and item[2] == 'X'):
        score = 1
        total_score += 1 
        #print('Loss')
        #print(score)
    elif (item[0] == 'C' and item[2] == 'Y'):
        score = 2
        total_score += 2
        #print('Loss')
        #print(score)
    elif (item[0] == 'A' and item[2] == 'Z'):
        score = 3
        total_score += 3
        #print('Loss')
        #print(score)
    else:
        print('Not calculated yet')


print('--------')
print(total_score)
#print('--------')
#print(input_data)
