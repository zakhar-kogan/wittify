# wittify

## Description 

A set of scripts to record, organize and transcribe data along with finding keyword occurencies.  

### recorder.py  
A script auto-adjusting for current noise level, then recording anything that is above that level to .wav files. Auto-slices the files in 40-second chunks (adjustable, of course) so that wit.ai will be able to process them.

### files_args.py
Transcribes a folder full o' audiofiles and finds occurencies of words from a text file. Useful for analysing sentiment, for example.

### check.py  
A small script using files_args.py to transcribe the current date folder. May be run, for example, daily.

## Requirements
**speech_recognition** and **tqdm** need to be installed.

## Usage  

1. recorder.py

2. check.py

3. (optional) files_args.py [-h] [-w WORDS] [-o OUTPUT_FILE] [-t THREADS] [-k WIT_KEY] folder (can be used as a script utility)  

### Positional arguments:  
  **folder**                folder to scan/use  

### Optional arguments:   
  -**w WORDS**, --**words WORDS** - word text file location  
  -**o OUTPUT_FILE**, --**output_file OUTPUT_FILE** - text file to output things  
  -**t THREADS**, --**threads THREADS** - number of threads to use; default is 8  
  -**k WIT_KEY**, --**wit_key WIT_KEY** - your wit.ai key (a default sure is added, but huh)