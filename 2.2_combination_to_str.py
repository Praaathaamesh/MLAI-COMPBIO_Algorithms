seq = ""
reads = seq.split()
String = []
String1 = []
for i in reads:
    String.append(reads[0])
    break
for j in range(len(reads)):
    if j>0:
        String1.append(reads[j])

def liststr(s):
    str1 = ""
    return str1.join(s)

mod_string1 = [read[-1] for read in String1]
final_string = liststr(String)
final_string1 = liststr(mod_string1)

Res = final_string + final_string1
print(Res)