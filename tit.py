import importlib

fr_num_str = input("Please enter a front number: ")
fr = importlib.import_module("fr_"+fr_num_str)
back_num_str = input("Please enter a back number: ")
back = importlib.import_module("back_"+back_num_str)

#使用测试集:2 8，2 4

f = fr.get_fr_res()
#print(f)

#假定取到'1_11', (6, 12)  
#f[i],f[i+1][0],f[i+1][1] 对应 '1_11', 6 12 

for i in range(0, len(f), 2):
    print(f[i],f[i+1][0],f[i+1][1])

b = back.get_back_res()
titii = []
for i in range(0, len(f), 2):
    for bi in b:
        medium0 = f[i+1][0] + 1
        medium1 = f[i+1][1] + 1
        if bi[medium0] != bi[medium1] and (bi[medium0] == '' or bi[medium1] == ''):
            aroad = f[i]+"," + bi[0] + ","
            mediumindex = "("+ str(f[i+1][0]) + "," + str(f[i+1][1]) + ")"
            aroad = aroad + mediumindex
            titii.append(aroad)

for i in titii:
    print(i)

"""
2 8
if "1_11,0_1_2_4_6_9_10_14,(6,12)" in titii:
    print(len(titii))
if "4_10,0_4_6_7_9_11_14_15,(1,15)" in titii:
    print(len(titii))
10080
"""

"""
2 4
if "4_9,4_6_13_14,(3,14)" in titii:
    print(len(titii))
if "0_5,0_1_6_14,(11,14)" in titii:
    print(len(titii))
if "7_13,0_4_13_15,(0,10)" in titii:
    print(len(titii))
1440
"""

print(len(titii))