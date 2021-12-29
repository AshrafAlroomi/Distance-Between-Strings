from distance import Levenshtein

with open("data.txt", "r") as f:
    for line in f.readlines():
        a, b, v = line.split(" ")
        value = int(v.replace("\n", ""))
        dis = Levenshtein(a, b).distance()
        print(True if value == dis else False)
