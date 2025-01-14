tail = ""
res = ""
s = "0221985324"
multiplicity = len(s) % 3

if multiplicity == 1:
    tailLen = 4
else:
    tailLen = multiplicity

if multiplicity != 0:
    tail = s[-tailLen:]
    s = s[:-tailLen]

for i in range(0, len(s), 3):
    if len(res) !=0:
        res = res + "-"
    res = res + s[i:i + 3]

if len(tail):
    res = res + "-" + tail

print(res)