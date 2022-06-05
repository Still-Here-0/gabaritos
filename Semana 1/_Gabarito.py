def Q(max):
    n = 1
    while n <= max:
        ret = ''

        if n%3 == 0:
            ret += 'Le'
        if n%5 == 0:
            ret += 'gal'

        if ret == '':
            print(n)
        else:
            print(ret)
        
        n += 1

if __name__ == '__main__':
    # Q(165)
    pass