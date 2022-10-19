import time
import requests
from bs4 import BeautifulSoup
from sendmail import sendmail

target_class = "movie-item-title"
keyword = 'Black Panther: Wakanda Forever'
track_interval = 300 # seconds as unit
cont_loop = True

def toMillisecond(epoch):
    return int(round(epoch) * 1000)

def handle_content(ctx):
    global cont_loop 

    soup = BeautifulSoup(ctx, 'html.parser')
    results = soup.find_all("div", {"class": target_class})
    # print(results)
    if any(keyword in result for result in results):
        print(f"'{keyword}' found.")
        sendmail()
        global cont_loop 
        cont_loop = False
    else:
        print(f"'{keyword}' not found.")

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