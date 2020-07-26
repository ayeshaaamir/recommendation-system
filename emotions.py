# sentiment analysis
# Importing library for web 
# scrapping 
from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP 

# Main Function for scraping 
def main(emotion): 
  
    # imdb for genre against emotion Sad 
    if(emotion == "Sad"): 
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
  
    # for disguisting
    elif(emotion == "Disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
  
    # for angry
    elif(emotion == "Anger"): 
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
    # for anticipation
    elif(emotion == "Anticipation"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # for fear
    elif(emotion == "Fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    # for enjoyment
    elif(emotion == "Enjoyment"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # for trust
    elif(emotion == "Trust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
  
    # for surprise
    elif(emotion == "Surprise"): 
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
  
    # http request to get data
    response = HTTP.get(urlhere) 
    data = response.text 
  
    # data parsing
    soup = SOUP(data, "lxml") 
  
    # extracting movie titles from regex
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    return title 
   
if __name__ == '__main__': 
  
    emotion = input("Please tell me genre: ") 
    a = main(emotion) 
    count = 0
  
    if(emotion == "Disgust" or emotion == "Anger"
                           or emotion=="Surprise"): 
  
        for i in a: 
  
            # Splitting each line of imdb to scrape movies 
            tmp = str(i).split('>;') 
  
            if(len(tmp) == 3): 
                print(tmp[1][:-3]) 
  
            if(count > 13): 
                break
            count += 1
    else: 
        for i in a: 
            tmp = str(i).split('>') 
  
            if(len(tmp) == 3): 
                print(tmp[1][:-3]) 
  
            if(count > 11): 
                break
            count+=1
