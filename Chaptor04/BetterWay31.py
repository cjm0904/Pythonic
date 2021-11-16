def normalize(numbers):
    total = sum(numbers)
    result = []
    print("Numbers")
    print(type(numbers), total)
    for value in numbers: # numbers에 아무것도 없음
        print("value")
        print(value)
        percent = 100 * value / total
        print(percent)
        result.append(percent)
    print("result")
    print(result)
    return result


# visits = [15, 35, 80]
# percentages = normalize(numbers=visits)
# print(percentages)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            print(int(line))
            yield int(line)


it = read_visits(data_path="my_numbers.txt")
print("it")
print(list(it))
percentages = normalize(it)

print(it)  # <generator object read_visits at 0x000001D79270AE58>
print(percentages)  # []

testGenerator = (i for i in range(0,5) )
print(testGenerator)
