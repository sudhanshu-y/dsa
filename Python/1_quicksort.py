
# T: O(n*log n), S: O(n)
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    # last element as pivot
    pivot = arr[-1]

    # all elements which are smaller than pivot except last/pivot element
    left_subarr = [ x for x in arr[:-1] if x < pivot]

    # all elements which are greater than pivot except last/pivot element
    right_subarr = [ x for x in arr[:-1] if x >= pivot]

    return quick_sort(left_subarr) + [pivot] + quick_sort(right_subarr)

# T: O(n*log n), S: O(1)
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]

    # i is the partition index which seperates left and right subarray
    # initially there is no left subarray
    i = low -1

    for j in range(low, high):
        # if smaller element found in array, then swap small - jth element with bigger ith element 
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # i represents the left subarray so swap pivot element with (i+1)th pivot element
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1 # pivot element index

if __name__=='__main__':
    arr = [1, 7, 4, 1, 10, 9, -2]
    print('Array:', arr)

    arr = quick_sort(arr)
    print('After Quicksort:', arr)
    
    arr = [0, -2, 80, 80, 3, 3]
    print('Array:', arr)
    
    quicksort(arr, 0, len(arr)-1)
    print('After Quicksort:', arr)
    
