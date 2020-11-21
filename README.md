# string_tagger

This project intends to analyze Text patterns in a string, then tag these unique strings matching a dictionary.

In order to accomplish, I made multiple proof of concepts until reaching an acceptable soultion.

  1. the first test has a problem, that even in the tagged strings it keeps processing
  inside the tags, so we propose a hash based solution.

  2. In this code we can find an error with the order, if a key is included in a bigger hash first, 
  it cannot be found a second longer key.

  3. In this version we use a method for sorting and getting a dictionary with a decremental key order.
  This Fix the issue with processing shorter patterns included in bigger patterns. 

