#Sentiment analysis on Twitter live stream
This python code is used in conjunction with established 
Sentiment scores (eg. AFINN) to analyze sentiment based on twitter feed.
Twitter stream was initially collected using Twitter API. 



==================AFINN==============================


AFINN is a list of English words rated for valence with an integer
between minus five (negative) and plus five (positive). The words have
been manually labeled by Finn Nielsen in 2009-2011. The file
is tab-separated. There are two versions:

AFINN-111: Newest version with 2477 words and phrases. One can see the list here:
https://github.com/fnielsen/afinn/blob/master/afinn/data/AFINN-111.txt

AFINN-96: 1468 unique words and phrases on 1480 lines. Note that there
are 1480 lines, as some words are listed twice. The word list in not
entirely in alphabetic ordering.  

An evaluation of the word list is available in:
Finn Årup Nielsen
"A new ANEW: Evaluation of a word list for sentiment analysis in microblogs",
Proceedings of the ESWC2011 Workshop on 'Making Sense of Microposts':
Big things come in small packages 718 in CEUR Workshop Proceedings : 93-98. 2011 May.
http://arxiv.org/abs/1103.2903

The list was used in: 
Lars Kai Hansen, Adam Arvidsson, Finn Ã…rup Nielsen, Elanor Colleoni,
Michael Etter, "Good Friends, Bad News - Affect and Virality in
Twitter", The 2011 International Workshop on Social Computing,
Network, and Services (SocialComNet 2011).


This database of words is copyright protected and distributed under
"Open Database License (ODbL) v1.0"
http://www.opendatacommons.org/licenses/odbl/1.0/ or a similar
copyleft license.

Source: http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010

Reference:
https://finnaarupnielsen.wordpress.com/2011/03/16/afinn-a-new-word-list-for-sentiment-analysis/
