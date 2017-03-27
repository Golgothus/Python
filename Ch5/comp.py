n = ["Michael", "Lieberman"]

# Add your function here
def join_strings(words):
    result = ""
    for w in words:
        result += w
        print(type(w))
    return result

print(join_strings(n))

n = [22, 23, 24]

# Add your function here
def join_nums(numbers):
    result = 0
    for num in numbers:
        result += num
#    for nums in range(len(numbers)):
#        result += numbers[nums]
    return result

print(join_nums(n))

