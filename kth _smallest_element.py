import heapq
def smallest_kth(k,list):
    h = []
    for e in list:
        heapq.heappush(h,e)
    for i in range(k):
       e = heapq.heappop(h)
    return e
def largest_kth(k,list):
    h = []
    for e in list:
        heapq.heappush(h, (-e,e))
    for i in range(k):
       w,e = heapq.heappop(h)

    return e

list=[3,7,6,1,2,9,8]
print(smallest_kth(3,list))
print(largest_kth(4,list))