trig=[2,3,4,5]
echo=[6,7,8,9]
def pinMode():
    d={}
    para=[]
    for i in range(0,len(trig)):
        para.append(trig[i])
        para.append(echo[i])
        d[i]=para
        para=[]
    return d
print(pinMode())