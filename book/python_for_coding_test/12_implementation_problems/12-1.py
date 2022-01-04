score = list(map(int, input()))

half = int(len(score)/2)
if sum(score[:half]) == sum(score[half:]):
    print("LUCKY")
else:
    print("READY")

# 10분