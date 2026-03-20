# Load your transcript from a local file
with open("arthur_eyes.txt", "r", encoding="utf8") as f:
    br = f.read()

print(type(br))
print(len(br))