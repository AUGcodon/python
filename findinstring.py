text = "X-DSPAM-Confidence:    0.8475";
colpos = text.find(":")
num = text[colpos+1:]
numstrip = num.lstrip()
numfloat = float(numstrip)
print numfloat