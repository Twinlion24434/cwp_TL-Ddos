import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt-get install python")
    os.system("apt-get install python3")
    os.system("pip install colorama")
    os.system("pip install tqdm")
    os.system("git pull")
   

elif c == "1":
    os.system("apt-get install python")
    os.system("apt-get install python3")
    os.system("pip3 install colorama")
    os.system("pip3 install tqdm")
    os.system("git pull")
   
print("Done.")
