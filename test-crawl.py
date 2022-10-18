import requests
from bs4 import BeautifulSoup
from sendmail import sendmail

target_class = "movie-item-title"
keyword = 'Black Panther: Wakanda Forever'

def handle_content(ctx):
    soup = BeautifulSoup(ctx, 'html.parser')
    results = soup.find_all("div", {"class": target_class})
    print(results)
    if any(keyword in result for result in results):
        print(f"'{keyword}' found.")
        sendmail()
    else:
        print(f"'{keyword}' not found.")


response = requests.get(f'https://www.emperorcinemas.com/en/ticketing/by_movie')
# response = requests.get(f'https://www.emperorcinemas.com/en/ticketing/upcoming')

if response.ok:
    handle_content(response.content)
else:
 print(response.status_code + " " + response.text)