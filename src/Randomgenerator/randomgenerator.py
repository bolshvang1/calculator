import random


def genrandnum(start_num, end_num):
    random.seed()
    return random.uniform(start_num, end_num)


def genrandnumseed(start_num, end_num, seed):
    random.seed(seed)
    return random.uniform(start_num, end_num)


def genrandlist(start_num, end_num, seed, size):
    randlist = []
    for idx in range(0, size):
        randlist.append(genrandnumseed(start_num, end_num, seed))
    return randlist







