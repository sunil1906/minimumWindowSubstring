from collections import Counter
s = "abbaacdbcab"
t=  "abc"

window = dict()
for i in t:
    if i in window:
        window[i] +=1
    else:
        window[i] = 1        

required = len(window)
res = [-1, 0, 0]
l = 0
r = 0
expected = 0
minimumWindow = dict()

while r < len(s):
    c = s[r]
    if c in minimumWindow:
        minimumWindow[c] += 1
    else:
        minimumWindow[c] = 1
    if (c in window) and (window[c] == minimumWindow[c]):
        expected += 1    
    while (l <= r) and (expected == required):
        if res[0] == -1 or (res[0] > (r-l)+1):
            res[0] = (r-l) + 1
            res[1] = l
            res[2] = r
        c = s[l]
        minimumWindow[c] -= 1
        if(c in window) and (minimumWindow[c] < window[c]):
            expected -= 1
        l += 1
    r += 1
if res[0] == -1:
    print("No match found")
else:
    print(s[res[1]:res[2]+1])

    
