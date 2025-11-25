"""Create a simple calculator implemented as lambdas"""

calc_dict = {"a" : lambda x,y : x + y,
             "s" : lambda x,y : x - y,
             "m" : lambda x,y : x * y,
             "d" : lambda x,y : x / y,}
while True:
    op = input("What operation do you want to perform?\n" \
    "[(a) add, (s) subtract, (m) multiply, (d) divide, (q) quit]")
    if op == 'q':
        break
    elif op in calc_dict.keys():
        num1 = input("What is the first operand?")
        num2 = input("What is the second operand?")
        # if op == 'd' and num2 == '0':
        #     print("can't divide by zero")
        #     continue
        # result = calc_dict[op](float(num1), float(num2))
        math_func = calc_dict[op] # gets us the calc function
        try:
            result = math_func(float(num1), float(num2))
        except ZeroDivisionError as zde:
            print(f'divide by zero error {zde.args}')
        except ValueError as ve:
            print(f'value error {ve.args}')
        else:
            print(f'result is {result}')
        finally:
            print('all done')
    else:
        print('invalid operations')
