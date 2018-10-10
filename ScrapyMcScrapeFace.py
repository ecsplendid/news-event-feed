#Horrible quickly written jet-lagged code here. Sorry for all the loops and imperative code

import requests
from bs4 import BeautifulSoup
import codecs

subscription_key = ""
assert subscription_key


search_term = "haiti earthquake 2018"
output_dir = '/dbfs/he/'

count = 10
offset = 0
ii = 0


for k in range(1000):
  
  search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search" + '?count=' + str(count) + '&offset=' + str(offset) + '&mkt=en-us&answerCount=2&responseFilter=webpages,news'

  headers = {"Ocp-Apim-Subscription-Key" : subscription_key, 'Accept-Encoding': 'deflate'}
  params  = {"q": search_term, "textDecorations":False, "textFormat":"HTML"}
  response = requests.get(search_url, headers=headers, params=params)
  response.raise_for_status()
  search_results = response.json()
  #print(search_results["webPages"]['totalEstimatedMatches'])
  offset += 10
  
  #if 'webPages' not in search_results:
  #  continue
  
  #print(search_results)
  
  for v in search_results["webPages"]["value"]:
   

    # Use requests to get the contents
    try:
      r = requests.get(v['url'])
    except Exception:
      print("Skipping ", v["name"])  
      continue
    

    # Get the text of the contents
    try:
      html_content = r.text
    except Exception:
      print("Skipping ", v["name"])  
      continue  

    # Convert the html content into a beautiful soup object
    soup = BeautifulSoup(html_content, 'lxml')
    tags = soup.find_all('p')[:]
    filename = output_dir + str(ii) + '.txt'
    with codecs.open(filename, "w", "utf-8-sig") as transcript:
      jj = 0
      for i in range(len(tags)):
        #print(tags[i].text)
        transcript.write(tags[i].text + "\n")
        jj += 1

    ii += 1
    print("Processed",v["name"], str(ii))
    #print(v['url'])
