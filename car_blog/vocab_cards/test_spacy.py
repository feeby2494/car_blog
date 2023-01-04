# This is a space to test out Spacy without 
# affecting rest of app

# test Chinese
import spacy
from spacy.lang.zh.examples import sentences 

nlp = spacy.load("zh_core_web_sm")
doc = nlp(sentences[0])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)

