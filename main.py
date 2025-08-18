from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import random
import os

app = FastAPI()

# Allow any site to call your API (useful if you ever host the page elsewhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = [
    "Are you a time traveler? Because every moment with you feels like my favorite future",
    "Do you know what’s on the menu? Me-n-you",
    "I’m not a photographer, but I can picture us forever",
    "Are you French? Because Eiffel for you",
    "Do you have a name, or can I call you mine?",
    "Are you made of sugar? Because you’re making my life so sweet",
    "If kisses were snowflakes, I’d send you a blizzard",
    "Do you have a map? I keep getting lost in your eyes",
    "You must be a magician, because whenever you’re around, everyone else disappears",
]

@app.get("/random-quote")
def get_random_quote():
    return {"quote": random.choice(quotes)}

# Serve index.html at the root
@app.get("/")
def serve_index():
    here = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(here, "static", "index.html")
    return FileResponse(index_path)
