# palindrome
s = input("")
count = 0
if s==s[::-1]:
    print("palindrome")
else:
    print("notpalindrome")

# conut vowels 
s = input("Enter a:")
count = 0
for ch in s.lower():
    if ch in "a,e,i,o,u":
        count+=1
print(count)
#----------------------------------------------#
# count upper cases 
s = "ChaKri"
count = 0
for ch in s:
    if ch in s.upper():
     count += 1
    print(count)
#-----------------------------------------
# find a3 
s = "banana"
max_chr = s[0]
max_count = s.count(s[0])
for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_chr = ch
print(max_chr,max_count)        
#--------------------------------------
# s = "nanana"
max_ch = s[0]
max_count = s.count(s[0])
for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_ch = ch
print(max_ch,max_count)
#------------------------------------
s = input("enter a input ")
result = ""
count = 1
for i in range (len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1 
result += s[-1] + str(count)
print(result)   
#-----------------------------------
# reverse words
s = "Fan of Prabhas"
words =s.split()
result = " "
for i in range(len(words)-1,-1,-1):
    result += words[i] + " "
print(result.strip())