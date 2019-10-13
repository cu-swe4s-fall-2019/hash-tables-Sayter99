import argparse
import os
import sys


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


if __name__ == '__main__':
    # adding arguments
    parser = argparse.ArgumentParser(
        description='Implementation of hash functions',
        prog='hash_functions')

    parser.add_argument('--input', type=str,
                        help='Name of the intput file', required=True)
    parser.add_argument('--hash_method', type=str,
                        help='ascii/rolling', required=True)

    args = parser.parse_args()

    if (os.path.exists(args.input)):
        for l in open(args.input):
            if (args.hash_method == 'ascii'):
                print(h_ascii(l, 100000))
            elif (args.hash_method == 'rolling'):
                print(h_rolling(l, 100000))
            else:
                print('Invalid hash method')
                sys.exit(1)
        sys.exit(0)
    print('Cannot find input file')
    sys.exit(1)
