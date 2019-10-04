def recognition():
  # import libraries
  import spacy

  #the input needed to process
  sentence = input("Enter the sentence you want to be processed ")

  # loading the language that would be recognized
  spacy_nlp = spacy.load('en')
  document = spacy_nlp(sentence)

  #prints the original statement 
  print('Original Sentence: %s' % (sentence))

  for element in document.ents:
      #prints the recognized words and their types
      print('Type: %s, Value: %s' % (element.label_, element))
      #prints the type of the word recognized and the meaning
      print(element.label_ + " means " + spacy.explain(element.label_))

if __name__=='__main__':
  recognition()