import numpy as np

ls = [1.,10.,0.1]
n  = 10
SAMPLES = 500000

for l in ls:
    a = np.random.exponential(1/(10*l),SAMPLES)
    b = np.random.exponential(1/l,(n,SAMPLES))
    b = np.sort(b,axis=0)
    res = np.logical_and(b[2]<a,a<b[3])
    print( np.sum(res)/SAMPLES , "(l = %f)"%l)

print("20/323 =",20/323)
