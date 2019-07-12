# python-GCC-compiler
Python script to automate compilation (with GCC) and running of .c files

When compile.py is run, it scans the working directory for all .c files and lists them, allowing the user to choose the file to be compiled. Python then invokes GCC with the -std=c17 and -Wall flags to compile the c file and then run it. Compilation errors, if any, would be shown. The script uses an infinite while loop to continuously stay open and allow the user to press Enter to re-compile and re-run the C program. 
