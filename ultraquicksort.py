import sys

def ultraquicksort():
    input = sys.stdin.read().strip()
    input_nums = list(map(int, input.splitlines()))
    n, arr = input_nums[0], input_nums[1:]
    count = 0
    swaps = 0
    def countswaps(arr, larr, rarr):
        pass
    
    def merge(arr, l, mid, r):
        n1 = mid - l + 1
        n2 = r - mid
        L = [0] * n1
        R = [0] * n2
        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]
        i = j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                # print(L[i], R[j])
                j += 1
                nonlocal swaps
                # swaps = r + j
                swaps += (n1 - i)
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    def mergesort(arr, l, r):
        if l < r:
            mid = (l+r)//2
            mergesort(arr, l, mid)
            mergesort(arr, mid+1, r)
            merge(arr, l, mid, r)
    
    mergesort(arr, 0, n-1)
    # print(arr)
    # def swap(arr,i,j):
    #     temp = arr[j]
    #     arr[j] = arr[i]
    #     arr[i] = temp
    
    # for i in range(1, n):
    #     for i in range(i, 0, -1):
    #         prev = arr[i-1]
    #         curr = arr[i]
    #         if curr < prev:
    #             count += 1
    #             swap(arr, i-1, i)
    #         else:
    #             break
    # print(arr, count)
    return swaps

swaps = ultraquicksort()

sys.stdout.write(str(swaps))