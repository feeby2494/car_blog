# This is a space to test out Spacy without 
# affecting rest of app
import spacy


# with open("./vocab_test_data/단독_피싱_불법_도박하다_전세사기_바지사장_됐다.txt", "r") as f:
#     print(f.read())

# test Korean 
nlp_ko = spacy.load("ko_core_news_sm")
ko_doc_objects = []
with open("./vocab_test_data/단독_피싱_불법_도박하다_전세사기_바지사장_됐다.txt", "r") as f:
    for line in f.readlines():
        ko_doc_objects.append(line)

def print_text(token):
    print(token.text)

doc_ko = list(nlp_ko.pipe(ko_doc_objects, batch_size=5))

print(dir(doc_ko[0].doc))

#for token in doc_ko:
#    print(token.doc.vocab.strings)    


#for token in doc_ko:
#    print(token.text, token.pos_, token.dep_)


# test Chinese

# from spacy.lang.zh.examples import sentences 

# nlp = spacy.load("zh_core_web_sm")
# doc = nlp(sentences[0])
# print(doc.text)
# for token in doc:
#     print(token.text, token.pos_, token.dep_)

