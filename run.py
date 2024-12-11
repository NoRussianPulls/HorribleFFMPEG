import sys
import subprocess

# Input and output files
input_file = sys.argv[1]
output_file = input_file + "_Output.bat"

# Open files
with open(input_file, "r", encoding="utf8") as i, open(output_file, "w", encoding="utf8") as o:
    a = 0  # Count of valid lines
    o.write("@echo off\n")
    
    lines = [line.strip() for line in i if line.strip() and 'https://' in line]  # Filter valid lines
    count = len(lines)
    
    for index, line in enumerate(lines, start=1):
        a += 1
        url_part = line[line.rindex(' ') + 1:].strip()  # Extract URL
        output_name = line[:line.rindex(' ')].strip()  # Extract output name
        
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
    o.write("echo All commands executed successfully.\n")
    o.write("pause\n")

print(f"{a} files found in this text file.")
print("Executing batch file...")

# Run the batch file
subprocess.run(output_file, shell=True)
