from fastapi.responses import HTMLResponse
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import random
from utils import Message, Sequential


mock_db = [
    {
        "image_name": "prayut หล่อเท่",
        "image_url": "https://quotepark.com/media/authors/prayut-chan-o-cha.jpeg"
    },    
    {
        "image_name": "prayut2",
        "image_url": "https://www.thephuketnews.com/photo/listing/2019/1559752046_1-org.jpg"
    },    
    {
        "image_name": "prayut3",
        "image_url": "https://static.bangkokpost.com/media/content/dcx/2019/08/03/3278931.jpg"
    },    
    {
        "image_name": "prayut4",
        "image_url": "https://pbs.twimg.com/media/D1Hb6g_V4AAvf64?format=jpg&name=900x900"
    }
]


app = FastAPI() 


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def serve_home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Song Flex API</title>
    <style>
    
        .main {
            text-align: center;
            padding: 1em;
            max-width: none;
            margin: 0 auto;
        }

    </style>
</head>
<body>
    <div class="main">
        <h1>Hello, Welcome to Song Flex API Services</h1>
        <p>Visit the <a href="/docs">Song Flex API Docs</a> to learn how to use this API services</p>
    </div>
</body>
</html>
"""

@app.get("/images/random", status_code=status.HTTP_200_OK)
async def send_random_image():
    random_image: dict = random.choice(mock_db)
    return Sequential(
        Message.text_message(f"This is {random_image['image_name']} image"),
        Message.image_message(random_image['image_url'], random_image['image_url'])
    ).to_dict()



