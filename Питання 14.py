P= int(input())
S = str(2**P)
print(S)
if len(S) < 2:
    Sr = (str(int(int(S[::-1])/(10**(len(S)-1))))[::-1])
    print(Sr)
elif len(S) > 1:
    Sr = (str(int(int(S[::-1])/(10**(len(S)-2))))[::-1])
    print(Sr)
