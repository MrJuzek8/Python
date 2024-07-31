# sum_even = 0
# x = 0
# for i in range(1,100):
#   x =+ i
#   if x % 2 == 0:
#     sum_even += x
# print(sum_even)
  
# for i in range(1,50):
#     x =+ i
#     if x % 3 == 0:
#       print(x)


numbers = [3, 7, 2, 10, 15, 1, 9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)