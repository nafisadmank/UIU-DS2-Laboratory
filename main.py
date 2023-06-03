def RMaxMin(A, left_index, right_index):
    if (left_index==right_index):
        return A[left_index], A[right_index]
    else:
        mid = (left_index+right_index)//2
        gmax, gmin = RMaxMin(A, left_index, mid)
        hmax, hmin = RMaxMin(A,mid+1,right_index)
        fmax = max(gmax, hmax)
        fmin = min(gmin,hmin)
        return fmax,fmin

print('Printing max and min value')
arr = [1,2,3,4]
print(RMaxMin(arr,0,len(arr)-1))