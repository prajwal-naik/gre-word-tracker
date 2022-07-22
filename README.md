# GRE Word Tracker #

This can be used to track the number of words you have learnt everyday.

How to run - <br/>
  &emsp;`python3 wordlist.py -c -f filename`
  
  &emsp;-c - OPTIONAL - Used to check if every word entered is present in the english dictionary<br/>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;False by default.<br/><br/>
  &emsp;-f filename - REQUIRED - Used to enter the words into a file at the end of every sprint for future use.<br/>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;If not provided, enters into file named trial-wordslearnt.txt

  First Header  | Second Header | Description                                                                   | Default
  | :---: | :---: | :---: | :---:
  c             | OPTIONAL      | Used to check if every word entered<br/> is present in the english dictionary |  False
  f             | OPTIONAL      | Used to enter the words into a file<br/> at the end of every sprint for future use |  trial-wordslearnt.txt