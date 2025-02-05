import re
import time
import requests
from bs4 import BeautifulSoup
from sendmail import sendmail

# Title has to be in English and completely identical, get exact title in https://www.emperorcinemas.com/en/ticketing/upcoming
movie_title = '[IMAX with Laser] Captain America: Brave New World'

track_interval = 300 # seconds as unit
cont_loop = True # Flag control loop or not

mask_class = "movie-item-mask"
title_class = "movie-item-title"
showing_url = "https://www.emperorcinemas.com/en/ticketing/movie_detail/showing"

def toMillisecond(epoch):
    return int(round(epoch) * 1000)

def handle_content(ctx):
    global cont_loop 

    soup = BeautifulSoup(ctx, 'html.parser')

    result_titles_div = soup.find_all("div", {"class": title_class})
    
    for result_title_div in result_titles_div:
       result_title = result_title_div.get_text()
       if (result_title in movie_title):
          movie_url = result_title_div.findParent("div", {"class": mask_class}).find(href=re.compile("^" + showing_url))["href"]
          print(f"'{movie_title}' found.\nMovie URL: {movie_url}")
          sendmail(movie_title, movie_url)
          global cont_loop 
          cont_loop = False
          break
       else: 
          print(f"'{movie_title}' not found.")

current_time = toMillisecond(time.time())
time_end = toMillisecond(time.time() + 60 * 60 * 24)
print(current_time, time_end)

while current_time < time_end and cont_loop:
    response = requests.get(f'https://www.emperorcinemas.com/en/ticketing/by_movie')
    # response = requests.get(f'https://www.emperorcinemas.com/en/ticketing/upcoming')

    if response.ok:
        handle_content(response.content)
    else:
        print(response.status_code + " " + response.text)

    time.sleep(track_interval)
    current_time = toMillisecond(time.time())
    print(current_time, time_end)

print("End of tracking loop.")