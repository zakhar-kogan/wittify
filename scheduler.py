import schedule, subprocess, time, sys, os

date_automatic = time.strftime("%d%m%Y")

if len(sys.argv) > 1:
    date_folder = sys.argv[1]
    output = date_folder + "/" + "output.txt"
else:
    output = "output.txt"
    date_folder = "/"

if not os.path.isfile(output):
    f = open(output,"w+")

schedule.every().day.at("23:45").do(subprocess.call(["python", "files_args.py", "-o", output, date_automatic]))