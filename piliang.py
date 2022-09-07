import os
import secrets
import string

initpass = "YAoissS@00"
setpass = input("setPASS(No use set pass enter):")
if setpass == "":
    setpass=initpass
alphabet = string.ascii_letters + string.digits
print(os.getcwd())
ps = os.getcwd()
setdir = input("setDirPath:")
os.chdir(setdir)
a = os.listdir()

listdirnamepas={}
for i in a:
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    passwd = setpass+password
    print(passwd)
    os.system(ps+r"\bz.exe c -p:"+passwd+" "+i+".zip "+i)
    listdirnamepas[i]=passwd

fd = open("namepass.txt","a+")
for ii in listdirnamepas:
    writea = ii+"\n"+listdirnamepas[ii]+"\n"
    fd.write(writea)
    fd.write("\n")

fd.close()