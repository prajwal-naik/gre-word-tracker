from getopt import GetoptError, getopt
import sys
import operator

import apicall

def main(argv):

  filename = "trial-wordslearnt.txt"
  url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
  words = set()
  existingWords = set()
  checkWordsFlag = False

  try:
    opts, args = getopt(argv, "hcf", ["help","check-words", "file"])
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
      if(len(deleteWord)):
        try:
          words.remove(deleteWord)
          print("Deleted word: ", deleteWord)
        except KeyError as e:
          print("Word not found in current sprint - ", deleteWord)
      else: 
        print("Specify word to remove")
    else: 
      word = word.lower().strip()
      if (checkWordsFlag == True):
        try: 
          dictionaryResult = apicall.makeGetRequest(url, word)
          if(apicall.checkResult(dictionaryResult)):
            words.add(word)
            print("Totals words learnt in this sprint: {}".format(len(words)))
          else:
            print("Possible typo or word doesn't exist\n")
        except: 
          print("Unable to check word. Skipping word...")
      else: 
        words.add(word)
        print("Totals words learnt in this sprint: {}".format(len(words)))

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
  with open(filename, "w") as f:
    for i in existingWords:
      f.write(i+"\n")
    f.close()

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
