num = [1,2,3]
number = int("".join(map(str, num)))
number += 1
result = [int(x) for x in str(number)]
print(result)
