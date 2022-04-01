
ar_time=[900,915,930,945,1030,1045,1105]
dp_time=[1000,1100,940,1011,1145,1115,1130]
dp_time.sort()

def platform():
    track = 0
    max_track = 0
    i = 0
    j = 0
    while i<len(ar_time) and j<len(dp_time):
        if ar_time[i]<dp_time[j]:
            track+=1
            i+=1
        else:
            track-=1
            j+=1
        if max_track<track:
            max_track=track

    return max_track
p1=platform()
print(p1)