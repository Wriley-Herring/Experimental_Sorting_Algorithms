'''

@author: wrileyherring

Is performance of this modified quicksort dependent upon the threshold? 
 - Yes, as the threshold is increased the performance of quicksort drops off.
 
Does the size of the list affect the modification?
 - Yes, as the size of the list increases the difference drops off.
 
When should the insertion sort be used?
 - Insertion sort should be used when the sublist is smaller than 15 elements.
 
 Are the number of comparisons and exchanges affected by the modification?
 - From the tests I ran they were roughly the same.

'''
from profiler import Profiler
from algorithms import insertionSort
from testquicksort import quicksort

import random 

def main(size =50000, sort = quicksort):
    
    lyst = []
    p = Profiler()
    for count in range(size):
        lyst.append(random.randint(1,size+1))
    print(lyst)
    p.test(sort,lyst, size, unique= True, comp = True, exch = True, trace = False, mod = False)
    
    
    
    
if __name__ == '__main__':
    main()
