#for i in range(2,16):
#    print(i)

y_0 = ["0",3,4,6,8,9,13,14]
y_1 = ["1",2,5,7,8,9,12,15]
y_2 = ["2",1,4,6,10,11,12,15]
y_3 = ["3",0,5,7,10,11,13,14]
y_4 = ["4",0,2,5,8,11,14,15]
y_5 = ["5",1,3,4,9,10,14,15]
y_6 = ["6",0,2,7,9,10,12,13]
y_7 = ["7",1,3,6,8,11,12,13]
y_8 = ["8",0,1,4,7,10,13,15]
y_9 = ["9",0,1,5,6,11,12,14]
y_10 = ["10",2,3,5,6,8,13,15]
y_11 = ["11",2,3,4,7,9,12,14]
y_12 = ["12",1,2,6,7,9,11,12]
y_13 = ["13",0,3,6,7,8,10,13]
y_14 = ["14",0,3,4,5,9,11,14]
y_15 = ["15",1,2,4,5,8,10,15]
Y=[y_0,y_1,y_2,y_3,y_4,y_5,y_6,y_7,y_8,y_9,y_10,y_11,y_12,y_13,y_14,y_15]


res_m2SL = []
for i in range(0,16):
   for j in range(i+1,16):
        name = str(str(i)+"_"+str(j))
        resi_m2SL = []
        resi_m2SL.append(name)
        for yi in Y:
            if (i in yi) or (j in yi):
                resi_m2SL.append(yi[0])      
                ##The format of the answer is: start difference 1_ start difference 2: the position where m_2^{SL} is not 0 (it is a list)
        res_m2SL.append(resi_m2SL)

named = []
drs = []

for ri in res_m2SL:
    dri = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    named.append(ri[0])
    for yi in Y:
        for j in range(1,len(ri)):
            if int(ri[j]) in yi:
                dri_index = int(yi[0])
                dri[dri_index].append(int(ri[j]))
    drs.append(dri)

fr_res = []
for di in range(len(drs)):
    for i in range(16):
        for j in range(i+1,16):
            if drs[di][i] == drs[di][j] and i != j:
                fr_res.append(named[di])
                fr_res.append((i,j))

#print(fr_res)
# re: fr_res
def get_fr_res():
    return fr_res
    






