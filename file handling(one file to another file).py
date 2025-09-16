f1=open("fileone.txt",'r')
f2=open("filetwo.txt",'a')
l=f1.readline()
while(l!=""):
    f2.write(l)
    l=f1.readline()

f1.close()
f2.close()
