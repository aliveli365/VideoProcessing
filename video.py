import speech_recognition as sr
import nltk
from textblob import TextBlob

filename = "16-122828-0002.wav"
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
	audio_data = r.record(source)
    
       
pos_count = 0
pos_correct = 0

text = r.recognize_sphinx(audio_data)
blob = TextBlob(text)
 
#positive
if blob.sentiment.subjectivity > 0.9:
	if blob.sentiment.polarity > 0:
		pos_correct += 1
		pos_count +=1    
		

neg_count = 0
neg_correct = 0		
#negative
if analysis.sentiment.subjectivity > 0.9:
	if analysis.sentiment.polarity <= 0:
		neg_correct += 1
        neg_count +=1
		

positive = pos_correct/pos_count*100.0, pos_count
negative = neg_correct/neg_count*100.0, neg_count

print(postive)
print(negative)
 
		 
		 
