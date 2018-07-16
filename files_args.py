import os, sys, json, math, argparse
import speech_recognition as sr
from tqdm import tqdm
from multiprocessing.dummy import Pool
from operator import itemgetter

parser = argparse.ArgumentParser()


parser.add_argument( "-w", "--words", help="word text file location", default="words.txt")
parser.add_argument("folder", help="folder to scan/use", default="")
parser.add_argument( "-o", "--output_file", help="text file to output things", default="output.txt")
parser.add_argument( "-t", "--threads", help="number of threads to use; default is 8", default=8)
parser.add_argument( "-k", "--wit_key", help="your wit.ai key", default="KRNOPGHS5M2HXO3ETBTHGTUFABB62V3H")

args = parser.parse_args()

# Initiating threads
pool = Pool(8) # Number of concurrent threads

# Loading the terms' text file
drugs = [line.rstrip('\n') for line in open(args.words)]

r = sr.Recognizer()
files = sorted(os.listdir(args.folder + '/'))
all_text = []

def transcribe(data):
    idx, file = data
    name = args.folder + '/' + file
    print(name + " started")
    # Load audio file
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    # Transcribe audio file
    text = r.recognize_wit(audio, key=args.wit_key).lower()
    print(name + " done")
    return {
        "idx": idx,
        "text": text,
        "length": len(text.split(" "))
    }

# Multi-threaded synchronization
all_text = pool.map(transcribe, enumerate(files))
pool.close()
pool.join()

# total_seconds = 0
transcript = ""

for t in sorted(all_text, key=lambda x: x['idx']):
    # total_seconds += int(durations[t['idx']])
    # Cool shortcut from:
    # https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
    # to get hours, minutes and seconds
    # m, s = divmod(total_seconds, 60)
    # h, m = divmod(m, 60)
 
    # Format time as h:m:s - 30 seconds of text
    transcript += "[{0}]: {1}\n".format(t['idx'], t['text']) + " "

# # Non-threaded
# for i, t in enumerate(all_text):
#     transcript += t.lower() + " "  

split_transcript = transcript.split(" ")

# Initializing the occurencies dictionary
occurencies = {}

# Counting occurencies of X in Y and writing them to a dictionary, naive
def count(what, where):
    for term in what:
        occur = where.count(term)
        if occur > 0 and term != '':
            occurencies[term] = str(occur) + ', ' + str(round(occur/len(split_transcript)*100, 2)) + "%"
    return occurencies

# Writing everything to a file
with open(args.output_file, "w", encoding="utf-8") as f:
    f.write(transcript)
    f.write("\n")
    final = count(drugs, split_transcript)
    prettyprinted = dict(sorted(final.items(), key=itemgetter(1), reverse=True))
    f.write (json.dumps(prettyprinted, ensure_ascii=False, indent=4))



