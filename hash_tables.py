import hash_functions
import argparse


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
