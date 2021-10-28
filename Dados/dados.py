import random
import matplotlib.pyplot as plt
import numpy as np
x=0
y=0
def generateDictionay(maxNum):
    Dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    for i in range(0,maxNum):
        value=0
        x=int(random.randrange(1,6))
        y=int(random.randrange(1,6))  
        value=x+y
        z=Dict[value]
        Dict[value]=z+1
    return Dict


Dict=generateDictionay(100)
Dict2=generateDictionay(1000)
Dict3=generateDictionay(10000)

fig,ax= plt.subplots(figsize=(10,7))

#plt.subplot(3,2,1)
for val in Dict.keys():
    ax.annotate(Dict[val],xy=(val,Dict[val]))
plt.bar(Dict.keys(), Dict.values(), width=.5, color='g')
plt.xlabel("Total Lanzamientos: 100 ")
plt.ylabel("Frecuencia suma")
plt.title("HISTOGRAMA")

fig,ax= plt.subplots(figsize=(10,7))
#plt.subplot(3,2,2)
plt.bar(Dict2.keys(), Dict2.values(), width=.5, color='b')
for val in Dict2.keys():
    ax.annotate(Dict2[val],xy=(val,Dict2[val]))

plt.xlabel("Total Lanzamientos: 1000 ")
plt.ylabel("Frecuencia suma")

#plt.subplot(3,2,3)
fig,ax= plt.subplots(figsize=(10,7))
plt.bar(Dict3.keys(), Dict3.values(), width=.5, color='y')
for val in Dict3.keys():
    ax.annotate(Dict3[val],xy=(val,Dict3[val]))


plt.xlabel("Total Lanzamientos: 10000 ")
plt.ylabel("Frecuencia suma")
plt.show()

