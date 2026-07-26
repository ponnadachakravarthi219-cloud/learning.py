#input PyThOn , output  NoHtYp
# s = "PyThOn"
# mirror = s[::-1].swapcase()
# print(mirror)

s = input("Emter a input: ")
vowels = "aeiou"
positions = []
for i in range(len(s)):
    if s[i] in vowels:
        positions.append(i)
if len(positions)<2:
    print("Balanced")
else:
    gap = positions[1] - positions[0]
    balanced = True
for i in range(1,len(positions)-1):
    if positions[i+1]-positions[i]!=gap:
        balanced = False
        break
if balanced:
        print("Balanced")
else: 
        print("Not Balanced")                       

