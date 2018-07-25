import subprocess
import recorder
import time
import sys
import os.path
import argparse

# date_folder = str(time.strftime('%d%m%Y'))
if len(sys.argv) > 1:
    date_folder = sys.argv[1]
    output = date_folder + "/" + "output.txt"
else:
    output = "output.txt"
    date_folder = "/"

if not os.path.isfile(output):
    f = open(output,"w+")

if(__name__ == '__main__'):
    subprocess.call(["python", "files_args.py", "-o", output, date_folder])