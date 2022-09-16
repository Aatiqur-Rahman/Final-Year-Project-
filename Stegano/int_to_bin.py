def method(a_int):
    quo=list()
    for i in range(0,8):
        quo.append(a_int%2)
        a_int=int(a_int/2)
    quo1=[0,0,0,0,0,0,0,0]
    j=7
    for i in quo :
        quo1[j]=i
        j-=1
    return quo1
method(10)