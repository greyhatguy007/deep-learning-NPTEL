import math
def softmax(arr):
    den = 0
    for i in arr:
        den += math.exp(i)
    ans = []
    for i in arr:
        ans.append(math.exp(i)/den)
    return ans

print(softmax([2.5,3.6,4.2,5]))

## output : [0.04616675712845395, 0.13869260320108814, 0.25271439976780363, 0.5624262399026543]
    