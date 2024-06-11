def main():
    try:
        divisor = 0
        if divisor != 0:
            x = 1 / divisor
            print("Result : ", x)
        else:
            print("Cannot divide by zero")
    except Exception as e:
        print("Error", e)

    try:
        my_dict = {'name': 'Alice'}
        name = my_dict.get('name')
        if name is not None:
            print("name: ", name)
        else:
            print("name not found")
    except KeyError as e:
        print("Error: key not found", e)

    try:
        result = int('123')  # No ValueError
        print("result: ", result)
    except ValueError as e:
        print("Error: Invalid value - ", e)

if __name__ == "__main__":
    main()
