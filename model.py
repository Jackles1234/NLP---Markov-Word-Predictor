import markov
import nltk
from nltk.corpus import brown

nltk.download('brown')



#print(brown.categories())

model = markov.MarkovModel()
text1 = brown.words(categories='news')
text2 = brown.words(categories='editorial')
text3 = brown.words(categories='government')
text4 = brown.words(categories='hobbies')
text5 = brown.words(categories='belles_lettres')
text6 = brown.words(categories='reviews')
text7 = brown.words(categories='humor')

model.train(text1)
model.train(text2)
model.train(text3)
model.train(text4)
model.train(text5)
model.train(text6)
model.train(text7)




def generate_next(text):
    btn1 = ( model.generate_text(1,text1[-1]))
    btn2 = ( model.generate_text(1,text1[-1]))
    btn3 = ( model.generate_text(1,text1[-1]))
    return btn1, btn2, btn3




    
