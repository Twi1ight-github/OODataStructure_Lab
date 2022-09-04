print("*** Converting hh.mm.ss to seconds ***")
h,m,s = input("Enter hh mm ss : ").split()
if int(m)>=60 or int(m)<0:
    print("mm("+m+") is invalid!")
    exit()

sec = int(h)*3600 + int(m)*60 + int(s)
sec = "{:,}" .format(sec)
if int(h)<10 :
    h=str(h)
    h=h.zfill(2)
if int(m)<10 :
    m=str(m)
    m=m.zfill(2)

if int(s)<10 :
    s=str(s)
    s=s.zfill(2)

print(h+":"+m+":"+s+" = "+str(sec)+" seconds")
