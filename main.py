def benjamin(kevin_steinacker):
    print(f'benjamin {kevin_steinacker}')
    # print('OH BROTHER THIS GUY STINKS!!')

def fizzbuzz(nums):
    for x in nums:
        s = ''
        if x % 3 == 0:
            s += 'Fizz'
        if x % 5 == 0:
            s += 'Buzz'
        print(s)

if __name__ == '__main__':
    x = (3 + 2 - 10) / 15
    var = 'hello'
    print((3**2+4**2)**0.5)
    fun_list = list(range(1,10))
    print(fun_list[4])
    print(fun_list[4:6])
    fun_list[-1] = 10
    fun_string = '123456789'
    print(fun_string[4])
    print(fun_string[4:6])
    fun_string = fun_string[:-1] + '10'
    fizzbuzz(list(range(30)))