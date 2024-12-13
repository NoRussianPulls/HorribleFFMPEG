import sys
import subprocess
import time
import os
os.system("")  # enables ansi escape characters in terminal

#title
print("LLLLLLL                          FFFFFFFFFFFFFFFFFFFFFF")
print("L:::::L                          F::::::::::::::::::::F")
print("L:::::L                          F::::::::::::::::::::F")
print("L:::::L                          FF::::::FFFFFFFFF::::F")
print("L:::::L                           F:::::F       FFFFFF")
print("L:::::L                           F:::::F             ")
print("L:::::L                           F::::::FFFFFFFFFF   ")
print("L:::::L                           F:::::::::::::::F   ")
print("L:::::L                           F:::::::::::::::F   ")
print("L:::::L                           F::::::FFFFFFFFFF   ")
print("L:::::L                           F:::::F  ")
print("L:::::L      LLLLLL   PPPPPPPP    F:::::F  ")
print("L::::::LLLLLL::::::L  pp::::PP  FF:::::::FF")
print("L::::::::::::::::::L  p:::::PP  F::::::::FF")
print("L::::::::::::::::::L  p:::::PP  F::::::::FF")
print("LLLLLLLLLLLLLLLLLLLL  pppppppp  FFFFFFFFFFF")
print()
print("+---------------------------------------------+")
print("| Batch Processing Streamurls with FFmpeg     |")
print("+---------------------------------------------+")
print("| Extracting URLs...                          |")
print("| Generating Batch File Commands...           |")
print("| Sequential Execution with Error Handling... |")
print("+---------------------------------------------+")
print("| Powered by Python, FFmpeg and Seppo         |")
print("+---------------------------------------------+")

time.sleep(3)
# Input and output files and settings
if len(sys.argv) < 2:
    input_file = input('Path to the file')
else:
     input_file = sys.argv[1]
output_file = input_file + "_Output.bat"
link = input('A specific set of Url leading to streams?(leave Empty to use every Url )')
if link == '':
    link = 'https://'
distinctcharacter = input('Any special character to distinct between url part and outputname?(leave empty for default: "_")')
if distinctcharacter == '':
    distinctcharacter = '_'

# Open files
with open(input_file, "r", encoding="utf8") as i, open(output_file, "w", encoding="utf8") as o:
    a = 0  # Count of valid lines
    o.write("@echo off\n")
    
    lines = [line.strip() for line in i if line.strip() and link in line and distinctcharacter in line]

    count = len(lines)
    
    for index, line in enumerate(lines, start=1):
        a += 1
        url_part = line[line.rindex('_') + 1:].strip()  # Extract URL
        output_name = line[:line.rindex('_')].strip()  # Extract output name
        
        print(f"{output_name} : {url_part}")
        
        # Write the command to the batch file
        if index < count:
            o.write(f'ffmpeg -i {url_part} -c copy "{output_name}.mp4" && ^\n')
        else:
            o.write(f'ffmpeg -i {url_part} -c copy "{output_name}.mp4"\n')
    
    # Add error handling and completion messages
    o.write("if %errorlevel% neq 0 (\n")
    o.write("  echo An error occurred. Exiting...\n")
    o.write("  pause\n")
    o.write("  exit /b\n")
    o.write(")\n")
    o.write("echo+---------------------------------------------+\n")
    o.write("echo| All commands executed successfully          |\n")
    o.write("echo+---------------------------------------------+\n")
    o.write("pause\n")

print(f"{a} files found in this text file.")
print("+---------------------------------------------+")
print("| Executing batch file...                     |")
print("+---------------------------------------------+")
time.sleep(3)

# Run the batch file
subprocess.run(output_file, shell=True)
