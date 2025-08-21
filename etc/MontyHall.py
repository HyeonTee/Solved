import random

def monty_hall(change, trial):
    win_count = 0
    for _ in range(trial):
        doors = [0, 0, 0]
        car = random.randrange(3)
        doors[car] = 1

        choice = random.randrange(3)
        result = doors[choice]
        
        for i in range(3):
            if i != choice and doors[i] == 0:
                doors.pop(i)
                break
        
        if change:
            result = 1 - result
        
        if result == 1:
            win_count += 1
    
    return (win_count / trial) * 100

print(monty_hall(True, 100000))
print(monty_hall(False, 100000))