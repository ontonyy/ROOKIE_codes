def exponention():
    user_num = int(input('Number would you like to exponent: '))
    too_user_name = int(input('Exponention number: '))
    result = 1
    for x in range(too_user_name):
        result = result * user_num
    return result
print('Answer is', exponention())

