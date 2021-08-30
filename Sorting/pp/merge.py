intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
l = [intervals[0]]
for i in range(1,len(intervals)):
    if l[-1][1]>=intervals[i][0]:
        l[-1] = [l[-1][0], max(l[-1][1],intervals[i][1])]
    else:
        l.append(intervals[i])
    print(l)