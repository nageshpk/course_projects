import time

def is_palindrome(val):
    val = str(val)
    if val == val[::-1]:
        return True
    else:
        return False

def palindrome():
    start_time = time.time()
    palindrome_list = []
    debug_list= []
    low_val = 900
    high_val = 999
    iterations = 0

    for num1 in range(low_val, high_val):
        for num2 in range(low_val, high_val):
            iterations += 1
            if is_palindrome(num1*num2):
                palindrome_list.append(num1*num2)
                debug_list.append([num1, num2, num1*num2])
            if num1 == num2:
                break
    print(f'print of palindromes: {palindrome_list}, {num1}, {num2}')
    print(f'debug_list: {debug_list}')
    print(f'iterations: {iterations}')
    print(f'Largest palindrome: {max(palindrome_list)}')
    print(f'Runtime: {time.time() - start_time}')
    print('-----------END RUN--------------')



def palindrome_back():
    start_time = time.time()
    palindrome_list = []
    debug_list= []
    low_val = 100
    high_val = 999
    iterations = 0
    low_num2_val = 100

    for num1 in range(high_val, low_val, -1):
        if num1 < low_val:
            break
        for num2 in range(high_val, low_num2_val, -1):
            iterations += 1
            if is_palindrome(num1*num2):
                palindrome_list.append(num1*num2)
                low_val = max((num1*num2)/high_val, low_val)
                low_num2_val = num2
                debug_list.append([num1, num2, (num1*num2)/high_val, low_val])
            if num1 == num2:
                break
    print(f'print of palindromes: {palindrome_list}, {num1}, {num2}')
    print(f'debug_list: {debug_list}')
    print(f'iterations: {iterations}')
    print(f'Largest palindrome: {max(palindrome_list)}')
    print(f'Runtime: {time.time() - start_time}')
    print('-----------END RUN--------------')


palindrome()
palindrome_back()