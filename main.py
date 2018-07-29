import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():

    fact = get_fact()

    # Send a request to https://hidden-journey-62459.herokuapp.com/piglatinize/
    # it should be a POST request, and it should ahve form data with 'input_text' 
    # of the fact that we scraped. And use the keyword argument 'follow_redirects=False'
    # when making your request so that you can capture and analyze the redirect response
    # Looks like:

    response = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/',
        data = {'input_text': fact},
        allow_redirects = False,)

    # Then, get the 'Location' header from the response

    location_header = response.headers['Location']

    return "<a href='{}'>{}</a>".format(location_header, location_header)
    # return location_header

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

