from image import file2image,color2gray 
from plotting import plot
# 2.3.2
L = [[2,2],[3,2],[1.75,1],[2,1],[2.25,1],[2.5,1],[2.75,1],[3,1],[3.25,1]]
plot(L,4)


def add2(v,w):
    return [v[0]+w[0],v[1]+w[1]]
    
def addn(v,w):
    return [v[i] + w[i] for i in range(0,len(v))]
    
 # 2.4.3   
plot([add2(x,[1,2]) for x in L])


def scalar_vector_mult2(alpha,v):
    return [alpha*v[x] for x in range(len(v))]
    
def scalar_vector_mult(alpha,v):
    return [x*alpha for x in v]

    
plot([scalar_vector_mult(-0.5,x) for x in L],16)

plot([scalar_vector_mult(i/100,[3,2]) for i in range(101)],5)

plot([add2(scalar_vector_mult(i/100,[3,2]),[0.5,1]) for i in range(101)],5)


def segment(pt1,pt2):
    return [add2([x*(i/100) for x in pt1],[x*((100-i)/100) for x in pt2]) for i in range(101)]
    
pt1 = [3.5,3]
pt2 = [0.5,1]
seg = segment(pt1,pt2)

plot(seg,4)


class Vec(object):
    def __init__(self,labels,function):
        self.D = labels
        self.f = function
    
def setitem(v,d,val):
    v.f[d] = val
    
def getitem(v,d):
    if d in v.f:
        return v.f[d]
    else:
        return 0
        
def scalar_mul(v,alpha):
    return Vec(v.D,{d:alpha*value for d,value in v.f.items()})
    
def zero_vec(D):
    return Vec(labels=0,function={})
    #return Vec(labels=D,function={x:0 for x in D})
    
u = {'A':6,'C':10,'B':2}
v = {'A':5,'C':10}
    
def add(u,v):
    k = u.keys() | v.keys()
    return Vec(v.D,{k:getitem(v,k) + getitem(u,k) for i in k})
    
def neg(v):
    return Vec(v.D,{k:(v.f[k]*-1) for k in v.f.keys()})
    
def list_dot(u,v):
    return sum([a*b for (a,b) in zip(u,v)])
    
    
def triangular_solve_n(rowlist,b):
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))    
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x
    
    
triangular_solve_n([Vec({0,1,2},[2,3,-4]),Vec({0,1,2},[0,1,2]),Vec({0,1,2},[0,0,5])],b=[10,3,15])
    
    
rowlist = [Vec({0,1,2},[2,3,-4]),Vec({0,1,2},[0,1,2]),Vec({0,1,2},[0,0,5])]