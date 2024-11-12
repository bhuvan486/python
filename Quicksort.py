import time
import matplotlib.pyplot as plt
import math start=time.time()
import time
import matplotlib.pyplot as plt
import math
def quicksort(alist,start,end):
    if end–start > 1:
        p=partition(alist,start,end)
        quicksort(alist,start,p)
        quicksort(alist,p+1,end)
def partition(alist,start,end):
    pivot = alist[start]
    i = start +1
    j = end – 1
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
            while (i <= j and alist[i] >= pivot):
                j = j – 1
                if i <= j:
                    alist[i],alist[j] = alist[j],alist[i]
                    else:
                        alist[start],alist[j] = alist[j],alist[start]
                        return j
alist = input(“enter the list of number: “).split()
alist= [int(x) for x in alist]
quicksort(alist,0,len(alist))
print(“sorted list: “, end=' ')
print(alist)
end=time.time() x=list(range(1,1000)) 
print("runtime of the program is{end - start}") 
plt.plot("mergsort=o(n)") plt.plot(x,[y*math.log(y,2)for y in x]) 
plt.xlabel("input")
plt.ylabel("time") 
plt.show()