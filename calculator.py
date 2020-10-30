class Calculator:
    past_result = []
    def calculator(rea, past_result):
        result = 0
        num1, op, num2 = rea.split('')
        n1, n2 = int(num1), int(num2)
        if op == '+':
            result = n1+n2
        elif op == '*':
            result = n1*n2
        elif op == '/':
            result = n1/n2
        past_result.append(result)
        return result


        pass
