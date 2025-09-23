word = input()

# divide
word1 = list(word[:len(word)//2])
word2 = list(word[len(word)//2:])
rotate = 0

for ch in word1:
    rotate += ord(ch) - 65

for i in range(len(word1)):
    x = ord(word1[i]) - 65   
    x = (x + rotate) % 26    
    word1[i] = chr(x + 65)

rotate = 0
for ch in word2:
    rotate += ord(ch) - 65

for i in range(len(word2)):
    x = ord(word2[i]) - 65   
    x = (x + rotate) % 26    
    word2[i] = chr(x + 65)

ans = []
for i in range(len(word1)):
    x = ord(word1[i]) - 65
    y = ord(word2[i]) - 65
    x = (x+y) % 26
    ans.append(chr(x+65))
ans = "".join(ans)
print(ans)
