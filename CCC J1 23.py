packages_delivered = int(input())
collisions = int(input())


score = packages_delivered * 50 - collisions * 10
if packages_delivered > collisions:
    score += 500


print(score)