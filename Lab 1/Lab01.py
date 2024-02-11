f1=open("input.txt","r")
rd=f1.readlines()
f1.close()
keywords=['auto','double','int','struct','break','else','long','switch','case','enum','register','typedef','char',
          'extern','return','union','continue','for','signed','void','do','if','static','while','default','goto',
          'sizeof','volatile','const','float','short','unsigned']
operators=["+","-","/","*","=","%", "+=", "-=", "*=", "/=", "%=", "++", "--"]
logical=["<",">","<=",">=", "==", "!=" , "&&", "||", "!"]
others_symbol=['(',')','[',']','{','}',',',';']

keyword_list=[]
identifiers_list=[]
math_operators_list=[]
logical_operators=[]
numerical_values=[]
others_list=[]
for line in rd:
    for w in line.split():
        if w in keywords:
            keyword_list.append(w)

out1=f"Keywords:"
for i in keyword_list:
    out1+=f" {i}"
    out1+=","
out1=out1[0:len(out1)-1]

for line in rd:
    for i in line.split():
        w=i.replace(';','')
        w=w.replace(')','')
        w=w.replace(',','')
        if w not in logical and w not in operators and w not in keywords and w not in identifiers_list:
            if (ord(w[0])>=97 and ord(w[0])<=122) or (ord(w[0])>=64 and ord(w[0])<=90) or (ord(w[0])==95):
                identifiers_list.append(w)

out2 = f"Identifiers:"
for i in sorted(identifiers_list):
    out2+=f" {i}"
    out2+=","
out2=out2[0:len(out2)-1]

for line in rd:
    for w in line.split():
        if w in operators and w not in math_operators_list:
            math_operators_list.append(w)

out3=f"Math Operators:"
for i in sorted(math_operators_list):
    out3+=f" {i}" 
    out3+=","
out3=out3[0:len(out3)-1]

for line in rd:
    for w in line.split():
        if w in logical and w not in logical_operators:
            logical_operators.append(w)



out4=f"Logical Operators:"
for i in sorted(logical_operators):
    out4+=f" {i}"
    out4+=","
out4=out4[0:len(out4)-1]

for line in rd:
    for w in line.split():
        if ord(w[0])>=48 and ord(w[0])<=57:
            if ";" in w:
                w=w.replace(";","")
            numerical_values.append(w)

out5=f"Numerical Values:"
for i in numerical_values:
    out5+=f" {i}"
    out5+=","
out5=out5[0:len(out5)-1]


for line in rd:
    for w in line.split():
        if w in others_symbol:
            others_list.append(w)

out6=f"Others:"
others_list=[*set(others_list)]

for i in sorted(others_list):
    out6+=f" {i}"

print(f'{out1}\n{out2}\n{out3}\n{out4}\n{out5}\n{out6}')