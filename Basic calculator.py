choice_of_operation = input('Enter 1 for addition and 2 for subtraction, enter 3 for multiplication and 4 for division. ')
if choice_of_operation == '1':
    value_1 = input('What is the value of the first number? ')
    value_2 = input('What is the value of the second number? ')
    print(float(value_1) + float(value_2))
if choice_of_operation == '2':
     value_1_sub = input('What is the value of the first number? ')
     value_2_sub = input('What is the value of the second number? ')
     print(float(value_1_sub) - float(value_2_sub))
if choice_of_operation == '3':
     value_1_multi = input('What is the value of the first number? ')
     value_2_multi = input('What is the value of the second number? ')
     print(float(value_1_multi) * float(value_2_multi))
if choice_of_operation == '4':
     value_1_div = input('What is the value of the first number? ')
     value_2_div = input('What is the value of the second number? ')
     print(float(value_1_div) / float(value_2_div))
