def main():
    #write your code below this line
    numbers = []

    while True:
        number = int(input())

        if number == -1:
            break

        numbers.append(number)

    result = 0
    for number in numbers:
        result += number

    print("Sum:", result)

if __name__ == '__main__':
    main()
