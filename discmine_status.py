import os
import time
import json
import subprocess

import fire


def summarize(in_dir):
    samples = {}
    mod_times = []
    for root, dirs, files in os.walk(in_dir):
        for name in files:
            mod_times.append(os.path.getmtime(os.path.join(root, name)))
            doc = json.load(open(os.path.join(root, name), "r"))

            for sample in doc:
                if sample["connective"] in samples:
                    samples[sample["connective"]] += 1
                else:
                    samples[sample["connective"]] = 1

    disk_usage = subprocess.check_output(['du','-sh', in_dir]).split()[0].decode('utf-8')

    samples = {k: v for k, v in sorted(samples.items(), key=lambda item: item[1])}
    for k, v in samples.items():
        print(f"{k}{' '*(25-len(k))}{v}")

    print(f"Total samples mined: {sum([x for x in samples.values()])}")

    first_write = time.ctime(min(mod_times))
    print(f"\nMine started: {first_write}")
    print(f"Disk space used: {disk_usage}")


if __name__ == '__main__':
  fire.Fire(summarize)