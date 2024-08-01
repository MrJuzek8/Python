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


# numbers = [3, 7, 2, 10, 15, 1, 9]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# x = int(input("Podaj libczę:"))
# for i in range(1,x+1):
#   if i % 2 == 0:
#     print(f"Parzysta {i}")
#   else:
#     print(f"Nieparzysta {i}")

# n = int(input("podaj Libcze:"))
# sum = 0
# for i in range(1,n):
#   sum += i
# print(sum)

# inputs = []
# num_inputs = int(input("How many inputs do you want to enter? "))
# for i in range(num_inputs):
#     user_input = input("Enter a value: ")
#     inputs.append(user_input)
# inputs.reverse()
# print(inputs)



n = int(input("Podaj zakres:"))
for i in range(2,n):
    if n <= 1:
        return False
    else:
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
        return False
    else:
    return True