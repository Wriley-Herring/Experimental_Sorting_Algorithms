"""
File: testquicksort.py

Tests the quicksort algorithm
"""
from algorithms import insertionSort
from profiler import Profiler

def quicksort(lyst, profiler):
    quicksortHelper(lyst, 0, len(lyst) - 1, profiler)

def quicksortHelper(lyst, left, right,profiler):
    if left < right:
        
        mod = profiler.mod()
        if mod:
            
            subLyst = lyst[left:right+1]
            if len(subLyst) < 12:
                insertionSort(subLyst, profiler)
                lyst[left:right+1] = subLyst
        
            else:
                pivotLocation = partition(lyst, left, right, profiler)
                quicksortHelper(lyst, left, pivotLocation - 1, profiler)
                quicksortHelper(lyst, pivotLocation + 1, right, profiler)
        else:
            pivotLocation = partition(lyst, left, right, profiler)
            quicksortHelper(lyst, left, pivotLocation - 1, profiler)
            quicksortHelper(lyst, pivotLocation + 1, right, profiler)

def partition(lyst, left, right, profiler):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            profiler.comparison()
            swap(lyst, index, boundary, profiler)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary, profiler)
    return boundary

def swap(lyst, i, j, profiler):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    profiler.exchange()
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp



def main(size = 1000, sort = quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main() 
