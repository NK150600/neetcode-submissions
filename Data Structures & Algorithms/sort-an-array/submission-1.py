class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapsort(nums)


    def heapify(self,arr,n,i):

        largest = i
        left_child = (2*i)+1
        right_child = (2*i)+2

        if left_child < n and arr[left_child]>=arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child]>=arr[largest]:
            largest = right_child

        if largest!=i:
            arr[i],arr[largest]=  arr[largest], arr[i] 

            self.heapify(arr,n,largest)

    def heapsort(self,arr):
        n = len(arr)

        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)

        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(arr,i,0)
        
        return arr

