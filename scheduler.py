import schedule, subprocess, time, sys, os, time

date_folder = time.strftime("%d%m%Y")
output = date_folder + "/" + "output.txt"

if not os.path.isdir(date_folder):
    os.mkdir(date_folder)

if not os.path.isfile(output):
    f = open(output,"w+")

def job (output, date):
    print("Running the transcriber script on {0} folder.".format(date_folder))
    subprocess.call(["python", "files_args.py", "-o", output, date])

schedule.every().day.at("23:45").do(job, output, date_folder)

while 1:
    date_folder = time.strftime("%d%m%Y")
    schedule.run_pending()
    time.sleep(1)