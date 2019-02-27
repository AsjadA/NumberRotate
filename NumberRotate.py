k = 10
n = str(726354)

nlist = list(n)
nlength = nlist.__len__()
start = nlength - k
end = start + k
temp = ""
remainder = n[0:2]
for i in range(start, end):
  temp = temp + nlist[i]

print (temp + remainder)
