# python-GCC-compiler
Python script to automate compilation (with GCC) and running of .c files

## Description
When compile.py is run, it scans the working directory for all .c files and lists them, allowing the user to choose the file to be compiled. Python then invokes GCC with the -std=c17 and -Wall flags to compile the c file and then run it. Compilation errors, if any, would be shown. The script uses an infinite while loop to continuously stay open and allow the user to press Enter to re-compile and re-run the C program as the user updates his C code in a separate code editor such as Sublime Text.

## Usage
1. Install GCC
  - MinGW-w64 for 64 and 32-bit Windows can be downloaded from [here](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download) and installed using the default options
  - MacOS requires [Xcode](https://www.cs.auckland.ac.nz/~paul/C/Mac/) to be isntalled for GCC
  - Linux users can run ```sudo apt install gcc``` from the terminal. Alternatively, ```sudo apt install build-essential``` will install additional libraries, including g++
  
 2. Add GCC to path (for Windows only)
  - ```Control Panel > System and Security > System > Advanced system settings > Environment variables > System variables > Path``` and add a new entry that points to the bin folder of MinGW, eg. C:\Program Files\mingw-w64\x86_64-8.1.0-posix-seh-rt_v6-rev0\mingw64\bin. 
  
 3. Place compile.py in the same directory as your C files. It is advisable to use split screen to work on your code on one half the window and run the Python script on the other half. Whenever you make any change in your C code and would like to re-compile and run the program, save the code in your code editor and switch over to the program to run compilation and execution
 
## Options
compile.py by default does not clear the terminal for every new compilation and run of the C program. This feature can be disabled at line 3:
```
files_c, file, cls = [], "", 0 #set to 1 for clear screen
```
