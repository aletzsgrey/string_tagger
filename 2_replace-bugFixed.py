def findAndHash(textInput, keyWord, replaceHash):
    '''hash sha256 string patherns'''
    return textInput.replace(keyWord,replaceHash)
def deHashAndReplace(textInput, keyHash, newPattern):
    '''tags the sha256 and replace the patterns'''
    newPattern = '<tag=\''+keyHash+'\'>'+newPattern+'</tag>'
    return textInput.replace(keyHash,newPattern)

def main():
    '''
    here we can find an error with the order, if a key is included into a bigger hash first,
    it cannot be found a second longer key
    '''
    tagsDict ={
            "abc": {"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad": "this is abc"},
            "abcd":{ "88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589": "this is abcd"},
            "ab": {"fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603":  "this is ab"},
            "aaaaa": {"ed968e840d10d2d313a870bc131a4e2c311d7ad09bdf32b3418147221f51a6e2": "this is 5 times a"},
            "aaaaaa": {"ed02457b5c41d964dbd2f2a609d63fe1bb7528dbe55e1abf5b52c249cd735797" :"this is 6 times a"},
            "aaa": {"9834876dcfb05cb167a5c24953eba58c4ac89b1adf57f28f2f9d09af107ee8f0": "this is 3 times a"}}
    textInput = '''
      a
      abc
      abcd
      ab
      aaaaa
      aaaaaa
      aaa
      something else
      else
      apple
      abecedary 
    '''

    print('this is the text input:\n {}'.format(textInput))
    #Run the Tagger
    for key, value in tagsDict.items():
        for hashed, replacer in value.items():
            textInput = findAndHash(textInput,key,hashed)

    print('this is the text hashed:\n {}'.format(textInput))

    for key, value in tagsDict.items():
        for hashed, replacer in value.items():
            textInput = deHashAndReplace(textInput,hashed,replacer)

    print('this is the text deHashed and Replaced:\n {}'.format(textInput))


if __name__ == "__main__":
   main() 
