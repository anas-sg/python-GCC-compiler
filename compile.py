import os, subprocess
from platform import system
files_c, file, cls = [], "", 0 #set to 1 for clear screen
if system() == "Windows":
    cls_cmd = "cls"
else:
    cls_cmd = "clear"  #  for Linux/MacOS

def get_files():
    global files_c
    cwd = os.getcwd()
    files = os.listdir(cwd)
    files_c = [i for i in files if i.lower().endswith('.c')]

def show_files():
    print("Identified following .c file(s):")
    for i in range(len(files_c)):
        print(i, files_c[i])

def clear_screen():
    os.system(cls_cmd)
    
def compile():
    if cls:
        clear_screen()
    try:
        subprocess.run(["gcc", "-std=c17", "-Wall", "-o", file[:-2], file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    except subprocess.CalledProcessError as suberror:
        print(suberror.stdout.decode("utf-8"))
    else:
        print(f"Successfully compiled! Running {file[:-2]}.exe...\n")
        exit_code = subprocess.run(file[:-2]).returncode
        print(f"\n-----------------------------------\nProcess terminated with exit code {exit_code}") 

while True:
    get_files()
    if files_c:
        show_files()
        if len(files_c) == 1:
        	file = files_c[0]
        while True:
            if file:
                cmd = input(f"\nENTER to compile {file} or input index of .c file: ")
            else:
                cmd = input("\nEnter index of .c file: ")
            if not cmd:
            	compile()
            elif cmd.isnumeric() and int(cmd) in range(len(files_c)):
                file = files_c[int(cmd)]
                compile()
            elif cmd == "f": #refresh list of files
            	get_files()
            	show_files()
            elif cmd == "c":
                clear_screen()
            elif cmd == "q":
            	exit()
            else:
                print("Invalid input")	
    else:
        input("No .c files found. Press ENTER to try again...")
