from getopt import GetoptError, getopt
import signal
import sys
import apicall


filename = "trial-wordslearnt.txt"
url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
words = set()
existingWords = set()
checkWordsFlag = False

def confirmWord(checkWord):
  return (checkWord in words)

def removeWord(deleteWord):
  if(len(deleteWord)):
    try:
      words.remove(deleteWord)
      print("Deleted word: ", deleteWord)
    except KeyError as e:
      print("Word not found in current sprint - ", deleteWord)
  else: 
    print("Specify word to remove")
  print("Totals words learnt in this sprint: {}".format(len(words)))

def addWord(newWord):
  if (checkWordsFlag == True):
    try: 
      dictionaryResult = apicall.makeGetRequest(url, newWord)
      if(apicall.checkResult(dictionaryResult)):
        words.add(newWord)
        print("Totals words learnt in this sprint: {}".format(len(words)))
      else:
        print("Possible typo or word doesn't exist\n")
    except: 
      print("Unable to check word. Skipping word...")
  else: 
    words.add(newWord)
    print("Totals words learnt in this sprint: {}".format(len(words)))


def main(argv):

  global filename
  global checkWordsFlag

  try:
    opts, args = getopt(argv, "hcf:", ["help","check-words", "file"])
  except GetoptError as e:
    print("Invalid command line arguments")
    print("trial.py [-c | --check-words]")
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
        print("trial.py [-c | --check-words]")
        sys.exit()
    elif opt in ("-c", "--check-words"):
        checkWordsFlag = True
    elif opt in ("-f", "--file"):
        filename = arg
    else: 
      print("Invalid argument -", opt)
      print("trial.py [-c | --check-words]")
      sys.exit()

  print("Check words is set as - ", checkWordsFlag)
  print("Output file is set as - ", filename)

  while(True):
    word = input("Enter word: ")

    if(word in ("exit", "EXIT", "stop", "STOP")):
      break
    elif("remove" in word.lower()):
      deleteWord = word.split(" ")[-1].lower().strip()
      removeWord(deleteWord)
    elif("check" in word.lower()):
      checkWord = word.split(" ")[-1].lower().strip()
      if (confirmWord(checkWord)):
        print("{} has already been entered".format(checkWord))
      else:
        print("{} not found".format(checkWord))
    else: 
      word = word.lower().strip()
      addWord(word)

  print(words)

  try:
    with open(filename, "r") as f:
      lines = f.readlines()
      lines = [line.rstrip() for line in lines]
      existingWords.update(set(lines))
      f.close()
  except FileNotFoundError as e:
    print("This is probably your first sprint: {} - {}".format(e.strerror, filename))

  existingWords.update(words)

  try:
    with open(filename, "w") as f:
      for i in existingWords:
        f.write(i+"\n")
      f.close()
  except:
    print("Specified file not found. Printing words on console...")
    for i in existingWords:
      print(i + "\n")
    print("Total words learnt this sprint: ", len(existingWords))

def sigint_handler(signal, frame):
    print("\nForcefully exiting. Printing current sprint words on console...")
    for i in words:
      print(i)
    sys.exit(0)

if __name__ == "__main__":
  signal.signal(signal.SIGINT, sigint_handler)
  sys.exit(main(sys.argv[1:]))
