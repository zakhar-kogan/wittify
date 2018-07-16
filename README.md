# wittify

## Description  
Transcribes a folder full o' audiofiles and finds occurencies of words from a text file. Useful for analysing sentiment, for example.

## Requirements
**speech_recognition** and **tqdm** need to be installed.

## Usage  
files_args.py [-h] [-w WORDS] [-o OUTPUT_FILE] [-t THREADS] [-k WIT_KEY] folder  

### Positional arguments:  
  **folder**                folder to scan/use  

### Optional arguments:   
  -**w WORDS**, --**words WORDS** - word text file location  
  -**o OUTPUT_FILE**, --**output_file OUTPUT_FILE** - text file to output things  
  -**t THREADS**, --**threads THREADS** - number of threads to use; default is 8  
  -**k WIT_KEY**, --**wit_key WIT_KEY** - your wit.ai key (a default sure is added, but huh)