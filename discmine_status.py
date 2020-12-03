import os
import time
import json
import subprocess
from multiprocessing import Pool

import numpy as np
import fire

CONNECTIVES = [
    "afterward(s)",
    "after that",
    "eventually",
    "in turn",
    "later",
    "next",
    "thereafter",
    "before that",
    "earlier",
    "previously",
    "in the meantime",
    "meanwhile",
    "simultaneously",
    "accordingly",
    "as a result",
    "consequently",
    "therefore",
    "thus",
    "additionally",
    "also",
    "besides",
    "further(more)",
    "in addition",
    "likewise",
    "moreover",
    "similarly",
    "by/in comparison",
    "by/in contrast",
    "conversely",
    "nevertheless",
    "on the other hand",
    "for example",
    "for instance",
    "in particular",
    "instead",
    "rather",
]
CDICT = {CONNECTIVES[i]: i for i in range(len(CONNECTIVES))}


def get_connective_counts(filename):
    con_counts = np.zeros(len(CONNECTIVES))

    doc = json.load(open(filename, "r"))
    for sample in doc:
        con_counts[CDICT[sample["connective"]]] += 1

    return con_counts

def summarize(in_dir, num_procs=4):
    docs = []
    samples = {}
    mod_times = []

    for root, dirs, files in os.walk(in_dir):
        for name in files:
            doc_name = os.path.join(root, name)
            docs.append(doc_name)
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