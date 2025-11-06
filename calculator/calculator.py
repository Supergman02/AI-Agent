def calculate(expression):
    return eval(expression)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        expression = sys.argv[1]
        result = calculate(expression)
        print(result)
    else:
        print("Please provide an expression to calculate.")