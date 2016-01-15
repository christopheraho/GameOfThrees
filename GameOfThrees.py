import prompt, predicate

StartingNumber = prompt.for_int("Enter starting number", is_legal = predicate.is_positive)

while StartingNumber > 0:
    if StartingNumber % 3 == 0:
        print(StartingNumber, 0)
        StartingNumber = StartingNumber // 3
    elif (StartingNumber+1) % 3 == 0:
        print(StartingNumber, 1)
        StartingNumber = (StartingNumber+1)//3
    elif (StartingNumber-1) % 3 == 0 and (StartingNumber-1) != 0:
        print(StartingNumber, -1)
        StartingNumber = (StartingNumber-1)//3
    elif StartingNumber == 1:
        print(StartingNumber)
        break
