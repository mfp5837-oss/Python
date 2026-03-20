from urllib import request


bookurl= "https://www.gutenberg.org/cache/epub/2081/pg2081.txt"
bookurl="https://www.gutenberg.org/cache/epub/2081/pg2081.txt"
response = request.urlopen(bookurl)
br = response.read().decode('utf8')
type(br)
print(len(br))
# make a variable
howLong = len(br)
# picture string version! 
print(f"howLong = {howLong}")
novelSlice = br[:500]
print(f"novelSlice = {novelSlice}")

splitEmUp = br.split()
print(f"splitEmUp = {splitEmUp[-100:]}")

for token in splitEmUp:
    if token.endswith('ed'):
        print(token)

