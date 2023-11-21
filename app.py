
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    # URL of the product page
    # url = 'https://www.macys.com/shop/product/michael-michael-kors-womens-single-breasted-wool-blend-coat-created-for-macys?ID=16050718&swatchColor=Crew%20Blue%20Blue'
    url = request.args.get('url')
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "en-US,en;q=0.9", 
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"", 
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Platform": "\"Windows\"", 
        "Sec-Fetch-Dest": "document", 
        "Sec-Fetch-Mode": "navigate", 
        "Sec-Fetch-Site": "cross-site", 
        "Sec-Fetch-User": "?1", 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
        "X-Amzn-Trace-Id": "Root=1-655c25ce-251a8d2f2039fe1505dc4aef"
    }
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    #print(response.content)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    image = ""
    title = ""

    # Extract image URL
    og_image = soup.find('meta', property='og:image')

    if(og_image is None):
        image = ""
    else:
        image = og_image.get('content')

    og_title = soup.find('meta', property='og:title')
    if(og_title is not None):
        title = og_title.get('content')

    if(title == ""):
        og_title = soup.find('meta', attrs={'name': 'title'})
        if(og_title is not None):
            title = og_title.get('content')

    print(og_image)
    print(og_title)
    return {"title": title, "image": image}

