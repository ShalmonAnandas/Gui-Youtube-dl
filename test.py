
raw_time = "01:01:00"

hours, minutes, seconds = raw_time.split(":", maxsplit=2)
print(hours, minutes, seconds)
gamer = (int(hours) * 60 * 60) + (int(minutes) * 60) + int(seconds)

print(gamer)