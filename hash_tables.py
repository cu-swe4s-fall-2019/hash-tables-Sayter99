import hash_functions
import argparse
import sys
import time
import random


def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


class LinearProbe:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        if (start_hash is None):
            return None

        for i in range(self.N):
            next_hash = (start_hash + i) % self.N
            if (self.T[next_hash] is None):
                self.T[next_hash] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        if (start_hash is None):
            return None

        for i in range(self.N):
            next_hash = (start_hash + i) % self.N
            if (self.T[next_hash] is None):
                return None
            if (self.T[next_hash][0] == key):
                return self.T[next_hash][1]
        return None


class ChainedHash:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        if (start_hash is None):
            return False

        self.T[start_hash].append((key, value))
        self.M += 1
        return True

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        if (start_hash is None):
            return None

        for k, v in self.T[start_hash]:
            if (key == k):
                return v
        return None


if __name__ == '__main__':
    # adding arguments
    parser = argparse.ArgumentParser(
        description='Implementation of hash tables',
        prog='hash_tables')

    parser.add_argument('--size', type=int,
                        help='Size of hash table', required=True)
    parser.add_argument('--hash_method', type=str,
                        help='ascii/rolling', required=True)
    parser.add_argument('--collision_strategy', type=str,
                        help='Collision strategy', required=True)
    parser.add_argument('--input', type=str,
                        help='Name of the input file', required=True)
    parser.add_argument('--key_nums', type=int,
                        help='Keys to be added', required=True)
    parser.add_argument('--search_nums', type=int,
                        help='Times of searching', required=True)

    args = parser.parse_args()

    N = args.size
    hash_alg = args.hash_method
    collision_strategy = args.collision_strategy
    data_file_name = args.input
    keys_to_add = args.key_nums
    keys_to_search = args.search_nums

    ht = None

    if hash_alg == 'ascii':
        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_ascii)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_ascii)

    elif hash_alg == 'rolling':
        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_rolling)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_rolling)

    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('add', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)

    sys.exit(0)
