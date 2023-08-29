import importlib

fr_num_str = input("Please enter a front number: ")
fr = importlib.import_module("forwardpropagation"+fr_num_str)
back_num_str = input("Please enter a back number: ")
back = importlib.import_module("backpropagation"+back_num_str)

f = fr.get_fr_res()
#print(f)


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

print(len(titii))
