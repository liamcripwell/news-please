import os
import time
import json
import subprocess
from itertools import product
from multiprocessing import Pool

import numpy as np
import fire

from discourse.connectives import PATTERNS, INNERS, FORWARDS

ADVS = [adv for sense in PATTERNS.values() for adv in sense.keys()]
CONNS = list(set(list(INNERS.keys()) + list(FORWARDS.keys())))

ADV_IDX = {ADVS[i]: i for i in range(len(ADVS))}
CONN_IDX = {CONNS[i]: i for i in range(len(CONNS))}


def get_connective_counts(args):
    filename, conn_type = args

    if conn_type == "adverbial":
        options = ADV_IDX
    else:
        options = CONN_IDX

    con_counts = np.zeros(len(options))

    doc = json.load(open(filename, "r"))
    for sample in doc:
        con_counts[options[sample["connective"]]] += 1

    return con_counts

def summarize(in_dir, conn_type="adverbial", num_procs=4):
    docs = []
    samples = {}
    mod_times = []

    for root, dirs, files in os.walk(in_dir):
        for name in files:
            doc_name = os.path.join(root, name)
            docs.append((doc_name, conn_type))
            mod_times.append(os.path.getmtime(doc_name))

    with Pool(num_procs) as status_pool:
        connective_counts = np.stack(status_pool.map(get_connective_counts, docs)).sum(axis=0)
    
    for i, c in enumerate(CONNECTIVES):
        print(f"{c}{' '*(25-len(c))}{connective_counts[i]}")
    print(f"Total samples mined: {connective_counts.sum()}")

    disk_usage = subprocess.check_output(['du','-sh', in_dir]).split()[0].decode('utf-8')
    print(f"Disk space used: {disk_usage}")

    # first_write = time.ctime(min(mod_times))
    # print(f"\nMine started: {first_write}")


if __name__ == '__main__':
  fire.Fire(summarize)