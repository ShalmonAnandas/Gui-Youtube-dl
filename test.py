test = open('multi_clip.txt', 'r')
counter = 0

content = test.read()
content_list = content.split("\n")

for i in content_list:
    if i:
        counter += 1

print(counter)