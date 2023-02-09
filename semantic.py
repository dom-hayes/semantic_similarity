import spacy
nlp = spacy.load("en_core_web_md")

# nlp = spacy.load("en_core_web_sm")

# Comparing the output values between en_core_web_md and en_core_web_sm the 
# similarity values changes quite significantly. For example Tree and iPhone
# returned a value of  0.07 in md but 0.68 in sm. The differences seem almost
# random with some results being higher, some lower and some almost the same.
# Based om my expected result I would say that the md model is much closer to 
# my expectation than the sm model which one might expect as it is larger in
# size it is able to provide a more accurate output.

print("\nSimilarity\n")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Cat and monkey are the most similar at 0.59 which is appropriate given these
# are both animals. Monkey and banana have a small amount of similarity at 0.40
# which makes sense as monkeys are well known to eat bananas. Cat and banana
# have the lowest similarity at 0.22, there is no real tie to these words other
# than the fact they are both nouns.

print("______________________")
# Based on the above findings I would expect that car and bike would have a 
# high simlarity value as they are both modes of personal transport with wheels.

word4 = nlp("car")
word5 = nlp("bike")

print(word4.similarity(word5))

# This returns 0.66 which is a good degree of similarity

print("______________________")

# Equally based on the above I would expect tree and iphone to have a very low
# similarity as there is very little that could be related between the two.

word6 = nlp("tree")
word7 = nlp("iphone")

print(word6.similarity(word7))

# This returns 0.07 which is a very low degree of similarity

print("______________________")

print("\nSimilarity Using Vectors\n")

tokens = nlp("cat apple monkey banana ") 
for token1 in tokens:
  for token2 in tokens:
    print(token1.text, token2.text, token1.similarity(token2))
    
print("______________________")

print("\nSimilarity of Sentences\n")

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I\'d like my boat back","I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
  similarity = nlp(sentence).similarity(model_sentence)
  print(sentence + " - ", similarity)

print("______________________")

