text = "X-DSPAM-Confidence:    0.8475"
sindex = text.find("    ")
print(sindex)
number = text[(sindex+4):(sindex + 4 + 6)]
inumber = float(number)
print(inumber)