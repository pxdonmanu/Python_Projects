# BeutifulSoup4 is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup
import requests as rqs
import openpyxl as oxl

excel=oxl.Workbook()
sheet=excel.active
sheet.title='Top Rated Movies'

# Columns excel
sheet.append(['Movie Rank','Movie Name','Year of Release','IMDB Rating'])

try:
  # Get the HTML source code
  source=rqs.get('https://www.imdb.com/chart/top/')
  # Raise an exception if the request fails
  source.raise_for_status()

  # Create a BeautifulSoup object, which represents the document as a nested data structure
  soup=BeautifulSoup(source.text, 'html.parser')
  
  # Get the table with the top 250 movies
  movies=soup.find('tbody', class_='lister-list').find_all('tr')
  ### print(len(movies)) 250
  
  for movie in movies:
    movie_name=movie.find('td', class_='titleColumn').a.text

    rank=movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0] # strip=True removes the leading and trailing whitespace

    year=movie.find('td', class_='titleColumn').span.text.strip('()') # stip('()') removes the parentheses

    rating=movie.find('td', class_='ratingColumn imdbRating').strong.text

    # print(rank, movie_name, year, rating)

    sheet.append([rank, movie_name, year, rating])
  

except Exception as e:
  print(e)

excel.save('IMDB Movie Rating.xlsx')