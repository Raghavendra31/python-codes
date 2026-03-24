def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
    avg = responseTimes[0]
    count = 0
    for i in range(1,len(responseTimes)):
        
        if (responseTimes[i] is None):
            return count
        if (responseTimes[i] > avg):
            count = count +1
        
        avg = (avg + responseTimes[i]) / 2
        
    return count

print(countResponseTimeRegressions([1,2,1,4,2]))
