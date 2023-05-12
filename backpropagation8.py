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


res =[]
"""
for i1 in range(16):
    for i2 in range(i1+1, 16):
        resi = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for yi in Y:
            if i1 in yi:
                resi[ int(yi[0]) ] = resi[ int(yi[0]) ] + 1
            if i2 in yi:
                resi[ int(yi[0]) ] = resi[ int(yi[0]) ] + 1
        res.append(resi)

print(res)
"""

for i1 in range(16):
    for i2 in range(i1+1, 16):
        for i3 in range(i2+1,16):
            for i4 in range(i3+1,16):
                for i5 in range(i4+1, 16):
                    for i6 in range(i5+1,16):
                        for i7 in range(i6+1,16):
                            for i8 in range(i7+1,16):
                                name = str(i1) + "_" + str(i2) + "_" + str(i3) + "_" + str(i4) + "_" + str(i5) + "_" + str(i6) + "_" + str(i7) + "_" + str(i8)
                                resi = [name, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                                for yi in Y:
                                    index = int(yi[0]) + 1
                                    if i1 in yi:
                                        resi[ index ] = resi[ index ] + 1
                                    if i2 in yi:
                                        resi[ index ] = resi[ index ] + 1
                                    if i3 in yi:
                                        resi[ index ] = resi[ index ] + 1
                                    if i4 in yi:
                                        resi[ index ] = resi[ index ] + 1
                                    if i5 in yi:
                                        resi[ index ] = resi[ index ] + 1
                                    if i6 in yi:
                                        resi[ index ] = resi[ index ] + 1
                                    if i7 in yi:
                                        resi[ index ] = resi[ index ] + 1
                                    if i8 in yi:
                                        resi[ index ] = resi[ index ] + 1
                                res.append(resi)

#print(res)
for ri in res:
    for i in range(1,17):
        if ri[i] % 2 != 0:
            ri[i] = i-1
        else:
            ri[i] = "-"
    #ri的答案格式：['0_1_2_4_6_9_10_14', 0, 0, 0, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0] ： [后向差分(str), 各有值的位置]

"""
for ri in res:
    if ri[0] == "0_1_2_4_6_9_10_14":
        print(ri)
"""

back_res = []

for ri in res:
    bri = [ri[0], "","","","","","","","","","","","","","","",""]
    for i in range(1,17):
        for yi in Y:
            if ri[i] in yi:
                index = int(yi[0]) + 1 
                if bri[ index ] == "":
                    bri[ index ] += "e" + str(ri[i])
                else:
                    bri[ index ] += "*"
                    bri[ index ] += "e" + str(ri[i])
    back_res.append(bri)

"""
for res in back_res:
    if res[0] == "0_1_2_4_6_9_10_14":
        print(res)
"""

# re: back_res
def get_back_res():
    return back_res


