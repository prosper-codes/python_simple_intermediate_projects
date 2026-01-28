import apod_object_parser
import streamlit as sl
import requests
from PIL import Image
from io import BytesIO

api_key="your_api_key"


# Get APOD data
response = apod_object_parser.get_data(api_key)
date = apod_object_parser.get_date(response)
url = apod_object_parser.get_url(response)
title = apod_object_parser.get_title(response)
explanation = apod_object_parser.get_explaination(response)

# Fetch the image from URL
res = requests.get(url)
img = Image.open(BytesIO(res.content))

# Display in Streamlit
sl.title(title)
sl.image(img)
sl.write(explanation)
