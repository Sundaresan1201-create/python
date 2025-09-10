d={"Eno":5821,"Ename":"zoro"}
print(d)
print(d["Eno"])
print(d["Ename"])
d["Ename"]="sanji"
print(d)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,":",value)
