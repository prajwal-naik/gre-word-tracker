words = set()
while(True):
    word = input("Enter word: ").lower().strip()
    if(word == "exit"): 
        break
    words.add(word)
    print("Totals words learnt in this sprint: {}".format(len(words)))
print(words)
existingWords = set()
try:
    with open("wordslearnt.txt", "r") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        existingWords.update(set(lines))
        f.close()
except FileNotFoundError as e:
    print("This is probably your first sprint: ", e.strerror)
    
existingWords.update(words)
with open("wordslearnt.txt", "w") as f: 
    for i in existingWords: 
        f.write(i+"\n")
    f.close()
    
