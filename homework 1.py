for line in open("LICENSE.txt", "r", encoding="utf-8"):
    for word in line.split():
            if word.lower() == "ing":
                print(word)