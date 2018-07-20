import subprocess
import recorder
import time

date_folder = str(time.strftime('%d%m%Y'))
output = date_folder + "/" + "output.txt"

if(__name__ == '__main__'):
    subprocess.call(["python", "files_args.py", "-o", output, date_folder])