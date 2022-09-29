import collections
def maxSlideWindow(nums, k):
    output = []
    q = collections.deque()
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()
        
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output
print(maxSlideWindow([1,2,3,4,5], 5))