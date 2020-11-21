def findAndTag(textInput, keyWord, taggedPattern): 
    '''Find and replace a string patterns adding some tags '''
    tagedPattern = '<tag=\''+taggedPattern+'\'>'+keyWord+'</tag>'
    return textInput.replace(keyWord,taggedPattern)

def main():
    '''
    the problem here is that even in the tagged strings it keeps processing
    inside the tags, so we propose a hash based solution.
    '''
    tagsDict={
            "abc":"this is abc",
            "abcd": "this is abcd",
            "ab": "this is ab",
            "aaaaa":"this is 5 times a",
            "aaaaaa":"this is 6times a",
            "aaa": "this is 3 times a"}
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
        textInput = findAndTag(textInput,key,value)

    print('this is the text output:\n {}'.format(textInput))

if __name__ == "__main__":
   main() 
