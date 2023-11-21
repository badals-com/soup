
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    # URL of the product page
    url = 'https://www.macys.com/shop/product/michael-michael-kors-womens-single-breasted-wool-blend-coat-created-for-macys?ID=16050718&swatchColor=Crew%20Blue%20Blue'
    url = request.args.get('url')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    #print(response.content)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract image URL
    og_image = soup.find('meta', property='og:image')
    og_title = soup.find('meta', property='og:title')
    return {"title": og_title, "image": og_image}

