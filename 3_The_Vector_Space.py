from vec import Vec,scalar_mul

# sample data
D = {'metal','concrete','plastic','water','electricity'}
v_gnome = Vec(D,{'concrete':1.3,'plastic':0.2,'water':0.8,'electricity':0.4})
v_hoop = Vec(D,{'plastic':1.5,'water':0.4,'electricity':0.3})



# Task 3.1.7
def lin_comb(vlist, clist):
    return sum([scalar_mul(v,a) for (v,a) in zip(vlist,clist)])
    
tt = lin_comb([v_gnome,v_hoop],[5,2])
    
