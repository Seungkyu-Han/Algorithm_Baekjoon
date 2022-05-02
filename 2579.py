num = int(input())

score = [0] * 300

for i in range(num):
    score[i] = int(input())

step = [0] * 300
step[0] = score[0]
step[1] = score[0] + score[1]
step[2] = max(score[0], score[1]) + score[2]
for i in range(3, num):
    step[i] = max(step[i-2], step[i-3] + score[i-1]) + score[i]

print(step[num - 1])
