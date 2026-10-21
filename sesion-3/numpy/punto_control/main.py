import numpy as np

data = np.array([10, 20, 30, 40, 50])

sub = data[1:4]
print(sub)

sub[0] = 999
print(sub)

print(data)