#!/usr/bin/python3

from pwn import *
filename="37366.zip"
io = process('sh')

while 1:    
    print("filename="+filename)
    if(filename == "6969.zip"):
        break
    io.sendline("7z l "+filename)
    result = io.recvrepeat(1).decode().strip().split("\n")
    #print("\n \n \n")
    #print(result)
    password=(result[-3].split(" ")[-1]).split(".")[0]
    #break
    print("password="+password)
    io.sendline("7z e " + filename+ " -p"+password)
    io.recvrepeat(1)
    #io.recvline()
    io.sendline("rm "+filename)
    io.sendline("ls | grep zip")
    ls =io.recvrepeat(1).decode().strip()
    if ls == "":
        break
    filename=ls
    print("newfile="+filename)

