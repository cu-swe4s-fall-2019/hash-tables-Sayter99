
def h_ascii(key, N):
    if (not isinstance(key, str)):
        print('Input key is not a string')
        print('Converting...')
        try:
            key = str(key)
        except ValueError:
            print('Failed to convert')
            return None

    if (not isinstance(N, int)):
        print('Input N is not an integer')
        print('Converting...')
        try:
            N = int(N)
        except ValueError:
            print('Failed to convert')
            return None

    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N


def h_rolling(key, N, p=53, m=2**64):
    if (not isinstance(key, str)):
        print('Input key is not a string')
        print('Converting...')
        try:
            key = str(key)
        except ValueError:
            print('Failed to convert')
            return None

    if (not isinstance(N, int)):
        print('Input N is not an integer')
        print('Converting...')
        try:
            N = int(N)
        except ValueError:
            print('Failed to convert')
            return None

    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N
