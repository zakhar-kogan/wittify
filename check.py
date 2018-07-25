import json
from operator import itemgetter
import argparse
import re
import os
import itertools

parser = argparse.ArgumentParser()

parser.add_argument( "-w", "--terms", help="word text file location", default="words.txt")
parser.add_argument("folder", help="folder to scan/use", default="")
parser.add_argument( "-o", "--output_file", help="text file to output things", default="output.txt")

args = parser.parse_args()

occurencies = {}

# Counting occurencies of X in Y and writing them to a dictionary, naive
def count(what, where):
    for term in what:
        occur = where.count(term)
        if occur > 0 and term != '':
            occurencies[term] = str(occur) + ', ' + str(round(occur/len(where)*100, 2)) + "%"
    return occurencies

# Getting our terms intact
with open(args.terms, "r") as file:
    terms_string = file.read()
    terms = re.findall(r"(\w+)\n", terms_string)

# Writing everything to a file
path = args.folder + "\\" + args.output_file
if os.path.getsize(path) > 10:
    with open (path, "r+", encoding="utf-8-sig") as o:
        json_dict = json.load(o)
        values = list(json_dict.values())
        split = list(itertools.chain(*[i.split(" ") for i in values if i != ""]))
        final = count(terms, split)
    with open (path, "a", encoding="utf-8-sig") as o:
        prettyprinted = dict(sorted(final.items(), key=itemgetter(1), reverse=True))
        o.write ("\n" + json.dumps(prettyprinted, ensure_ascii=False, indent=4))