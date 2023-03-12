# GRE Word Tracker #

This can be used to track the number of words you have learnt everyday.

## How to run - ```python wordlist.py -c -f filename``` ##
  

  Argument  | Requirement | Description | Default Value
   :---: | :---: | :---: | :---:
  -c \| --check-words | OPTIONAL | Used to check if every word entered<br/> is present in the english dictionary | False
  -f \| --file | OPTIONAL | Used to enter the words into a file<br/> at the end of every sprint for future use | trial-wordslearnt.txt


## Commands ##

1. `<word>` - Enters word into present sprint<br/>`hello` - Enters the word hello into the present sprint<br/><br/>
2. `remove <word>` - Removes word from the present sprint if present<br/>`remove hello` - Removes word "hello" from the present sprint<br/><br/>
3. `check <word>` - Checks if word has been entered in the present sprint<br/>`check hello` - Checks if word "hello" is present in the current sprint<br/><br/>
4. `check length` - Checks how many words have been learnt in this sprint. 
5. `list <prefix>` - List all words starting with <prefix>
6. `exit | EXIT | STOP | stop` - Stops current sprint<br/>`stop` - Stops the sprint

