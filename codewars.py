def sum_array(a):
    if len(a) == 0:
        return 0
    else:
        sum=0
        for i in a:
            sum = sum + i
        return sum
    


print(sum_array([1, 2, 3]))

