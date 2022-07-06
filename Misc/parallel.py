import math
import sys
import multiprocessing
#Merge Sort
def merge(*args):
        
        left, right = args[0] if len(args)==1 else args
        length_left, length_right = len(left), len(right)
        left_index, right_index = 0, 0
        
        merged = []
        
        while left_index < length_left and right_index < length_right:
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
                
        if left_index == length_left:
            merged.extend(right[right_index:])
        else:
            merged.extend(left[left_index:])
        return merged
def mergeSort(array):
    
    length = len(array)
    
    if length<=1:
        return array
    else:
        middle = length//2
        left = mergeSort(array[:middle])
        right = mergeSort(array[middle:])
        
        return merge(left, right)
        
def sortParallel(data):
    
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    
    size = int( math.ceil( float(len(data)) / processes) )
    data = [ data[ i*size : (i+1)*size ] for i in range(processes) ]
    
    data = pool.map(mergeSort, data)
    
    while len(data)>1:
        extra = data.pop() if len(data)%2==1 else None
        data = [ (data[i], data[i + 1]) for i in range(0, len(data), 2) ]
        data = pool.map(merge, data) + ([extra] if extra else [])
    
    return data[0]
a = list(range(1000000))
a = a[::-1]
import time
start = time.time()

b = mergeSort(a)

end = time.time()-start

print(end)

start = time.time()

b = sortParallel(a)

end = time.time()-start

print(end)


#Quick Sort

def partition(array, left, right):

    pivot_index = left
    pivot = array[pivot_index]

    while left < right:

        while left < len(array) and array[left] <= pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if(start < right):
            array[left], array[right] = array[right], array[left]

    array[right], array[pivot_index] = array[pivot_index], array[right]

    return right
def quickUtil(array, start, end):

    if start<end:

        p = int(partition(array, start, end))

        quickUtil(array, start, p - 1)
        quickUtil(array, p + 1, end)
        
def quickSort(array):
    quickUtil(array, 0, len(array)-1)
    return array

def merge(*args):
        
        left, right = args[0] if len(args)==1 else args
        length_left, length_right = len(left), len(right)
        left_index, right_index = 0, 0
        
        merged = []
        
        while left_index < length_left and right_index < length_right:
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
                
        if left_index == length_left:
            merged.extend(right[right_index:])
        else:
            merged.extend(left[left_index:])
        return merged
def sortParallel(data):
    
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    
    size = int( math.ceil( float(len(data)) / processes) )
    data = [ data[ i*size : (i+1)*size ] for i in range(processes) ]
    
    data = pool.map(quickSort, data)
    
    #return data
    
    while len(data)>1:
        extra = data.pop() if len(data)%2==1 else None
        data = [ (data[i], data[i + 1]) for i in range(0, len(data), 2) ]
        data = pool.map(merge, data) + ([extra] if extra else [])
    
    return data[0]

array = list(range(5000))
array = array[::-1]
import time
start = time.time()

a = array[:]
a = quickSort(a)

end = time.time()-start

print(end)

start = time.time()

b = array[:]
b = sortParallel(b)

end = time.time()-start

print(end)
