#!/usr/bin/python

import sys
import math
import hashlib


class BloomFilter(object):

    def __init__(self, false_positive_prob, num_keys, num_entries):

        self.false_positive_prob = false_positive_prob
        self.num_keys = num_keys
        self.num_bits = int(math.ceil(self.num_keys*(-math.log(self.false_positive_prob,2)/math.log(2,math.e))))
        self.num_entries = num_entries
        self.num_hashes = int(math.ceil(self.num_bits*math.log(2,math.e)/self.num_entries))
        try:
            from bitarray import bitarray
            self.bit_array = bitarray(self.num_bits)
            self.bit_array.setall(False)
        except ImportError:
            self.bit_array = [False for _ in range(self.num_bits)]

    def _hash_func(self, s, mod, idx):
        m = hashlib.md5(str(idx)+"_"+s)
        return int(long(m.hexdigest(), 16)%mod)

    def _multi_hash(self, s):
        hash_arr = []
        for i in range(self.num_hashes):
            hash_arr.append(self._hash_func(s, self.num_bits, i))
        return hash_arr

    def insert(self, key):
        arr = self._multi_hash(key)
        for p in arr:
            self.bit_array[p] = True

    def query(self, key):
        arr = self._multi_hash(key)
        for p in arr:
            if not self.bit_array[p]:
                return False
        return True


num_lines = int(sys.argv[1])
bf = BloomFilter(0.01, num_lines, num_lines)

for line in sys.stdin:
    line = line.strip()
    if not bf.query(line):
        bf.insert(line)
        print line

