import numpy as np
# arr=np.array([[1,2,3,4],[4,5,6,7]])
# print(arr)
# arr1=np.asarray(arr,dtype=float,order="F")
# print(arr1)
# for i in np.nditer(arr1):
#     print(i)

# a=b"i am naruto"
# b=np.frombuffer(a,dtype="S1",offset=2)
# print(b)

# a=[10,20,30,40]
# b=np.fromiter(a,dtype=int,count=2)
# print(b)

# a=np.zeros([2,2],dtype=int)
# print(a)

# a=np.full([3],8)
# print(a)

# a=np.random.rand(2,3)
# print(a)
# b=np.ones([2,3],dtype=int)
# print(b)

# a=np.eye(5,dtype=int)
# print(a)

# a=np.arange(5,105,5)
# print(a)

# a=np.linspace(0,100,10,endpoint=False,retstep=True)
# print(a)

# a=np.logspace(1,10,10,base=2)
# print(a)
# print(np.size(a))
# print(np.shape(a))
# print(a.dtype)

# a=np.array([9,7,4,21,2,455,22,11,1])
# b=np.copy(a)
# a=np.sort(a)
# print(a)     

# a=np.dtype([('name','S1'),('per',float)])
# arr=np.array([("sriram",97.9),("hiari",78.9),("raju",99.9)],dtype=a)
# print(np.sort(arr,order="per"))

# a=np.array([[1,2,3],[1,2,3]])
# b=np.array([1,2,3])
# c=np.append(a,b)
# print(a)
# print(c.reshape(3,3))

# a=np.array([[1,2,3],[8,9,1]])
# a=np.insert(a,0,[4,2,1])
# print(a.reshape(3,3))

# a=np.array([[1,2,3],[8,9,10]])
# b=np.array([[10,11,12],[13,14,15]])
# c0=np.stack((a,b))
# c=np.vstack((a,b))
# c1=np.hstack((a,b))
# c2=np.dstack((a,b))
# print(c0)
# print(c)
# print(c1)
# print(c2)

a=np.arange(10,1000,10)
b=np.arange(10,1000,10)
# print(np.array_equal(a,b))
#print(a==b)
# print(np.where(a%20==0))
# print(np.searchsorted(a,900))