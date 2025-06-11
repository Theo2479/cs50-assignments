# def playback():
#     typing=input("write a sentance ")
#     print(typing.split(   ).join(   ))

# playback()

def playback():
    typing = input("write a sentence ")
    print('...'.join(typing.split()))

playback()
#here we say '...' joins the words in the sentence, 
# we wrote, but that input 'typing' was spilt into indivdual list of words. 