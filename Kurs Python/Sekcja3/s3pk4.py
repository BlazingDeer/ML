import os
files_to_process=["./skrypt1.py","./skrypt2.py"]

for file in files_to_process:
    print(os.path.basename(file))
    with open(file,"r") as f:
        source=f.read()
    exec(source)