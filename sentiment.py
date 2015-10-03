# Twitter Sentiment Analysis using Python

import sys  
import json  
   
def main():  
      sent_file = open(sys.argv[1])  
      tweet_file = open(sys.argv[2])  
   
      scores = {} # initialize an empty dictionary  
      for line in sent_file:  
       term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"  
       scores[term] = int(score) # Convert the score to an integer.  
   
      for line in tweet_file:  
           #convert the line from file into a json object  
           mystr = json.loads(line)  
           #check the language is english, if "lang" is among the keys  
           if 'lang' in mystr.keys() and mystr["lang"]=='en':  
                #if "text" is not among the keys, there's no tweet to read, skip it  
                if 'text' in mystr.keys():  
                     resscore=0  
                     #split the tweet into a list of words  
                     words = mystr["text"].split()  
                     for word in words:  
                          #if the current word exists in our dictionary, add its value to the total  
                          if word in scores:  
                               resscore+=scores[word]  
                     #convert to float  
                     resscore+=0.0  
                     print str(resscore)  
           else:  
                print 0.0  
   
if __name__ == '__main__':  
      main()  