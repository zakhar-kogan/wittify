import os, sys, json, math, argparse
import speech_recognition as sr
from tqdm import tqdm
from multiprocessing.dummy import Pool
from operator import itemgetter
import re, glob

parser = argparse.ArgumentParser()

parser.add_argument( "-w", "--words", help="word text file location", default="words.txt")
parser.add_argument("folder", help="folder to scan/use", default="")
parser.add_argument( "-o", "--output_file", help="text file to output things", default="output.txt")
parser.add_argument( "-t", "--threads", help="number of threads to use; default is 4", default=8)
parser.add_argument( "-k", "--wit_key", help="your wit.ai key", default="KRNOPGHS5M2HXO3ETBTHGTUFABB62V3H")

args = parser.parse_args()

# Initiating threads
pool = Pool(args.threads) # Number of concurrent threads

# Loading the terms' text file
terms = [line.rstrip('\n') for line in open(args.words)]

def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

r = sr.Recognizer()
files = sorted_aphanumeric(glob.glob(args.folder + '/*.wav'))

indexes = []
all_text = []
split_transcript = []
json_dict = {}
string = ""

def transcribe(data):
    global json_dict
    idx, file = data
    name = file
    filename = re.search(r"\\(\d+)_", name).group(1)
    if os.path.getsize(args.output_file) > 10:
        with open(args.output_file, "r+", encoding="utf-8") as o:
            json_dict = json.load(o)
        # x = re.findall(r"\[(\w+)\]", lines)
    try:
        if filename not in json_dict:
            print("  " + name + " started")
            with sr.AudioFile(name) as source:
                audio = r.record(source)
            # Transcribe audio file
            text = r.recognize_wit(audio, key=args.wit_key).lower()
            print ("  " + name + " finished recognizing")
            json_dict[filename] = text
            with open(args.output_file, "w+", encoding="utf-8") as f:
                json.dump(json_dict, f, sort_keys=True, indent=4, ensure_ascii=False)
            split_transcript.extend(text.split(" "))
            print("  " + name + " done")
    except KeyboardInterrupt:
        pass

# Multi-threaded synchronization
all_text = pool.map(transcribe, enumerate(files))
pool.close()
pool.join()

# total_seconds = 0
transcript = ""

# Initializing the occurencies dictionary
occurencies = {}

# Counting occurencies of X in Y and writing them to a dictionary, naive
def count(what, where):
    for term in what:
        occur = where.count(term)
        if occur > 0 and term != '':
            occurencies[term] = str(occur) + ', ' + str(round(occur/len(where)*100, 2)) + "%"
    return occurencies

# Writing everything to a file
# with open(args.output_file, "a", encoding="utf-8") as f:
#     final = count(terms, split_transcript)
#     prettyprinted = dict(sorted(final.items(), key=itemgetter(1), reverse=True))
#     f.write ("\n" + json.dumps(prettyprinted, ensure_ascii=False, indent=4))



