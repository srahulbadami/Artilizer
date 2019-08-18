from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
from google_images_download import google_images_download  
import re

with open('data.txt', 'r') as file:
    text = file.read().replace('\n', '')

for k in text.split("\n"):
    text2 = re.sub(r"[^a-zA-Z0-9&]+", ' ', k)
text = text2
tokens = [t for t in text.split()]
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))

response = google_images_download.googleimagesdownload()  
search_queries = [sorted(freq.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[0][0] +"  "+ sorted(freq.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[1][0]+"  "+ sorted(freq.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[2][0]+"  "+ sorted(freq.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[3][0]+"  "+ sorted(freq.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[4][0]]

def downloadimages(query): 
	arguments = {"keywords": query, "format": "jpg", "limit":1,"print_urls":True, "size": "large", "aspect_ratio": "panoramic"} 
	try: 
		response.download(arguments) 
	except FileNotFoundError:
		arguments = {"keywords": query,"format": "jpg", "limit":1,  "print_urls":True,   "size": "large"} 
		try: 
			response.download(arguments) 
		except: 
			pass
  
# Driver Code 
for query in search_queries: 
    downloadimages(query)  
    print()  


freq.plot(20, cumulative=False)