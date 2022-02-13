hour, minute = map(int, input().split())
time = hour*60+minute
if(time<45):
    time += 1440
time -= 45
print("%d %d"%(time/60, time%60))
