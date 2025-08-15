from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow any site to call your API (so your friend can open it in Chrome)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict this later
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

@app.get("/")
def root():
    return {"ok": True, "try": "/random-quote", "docs": "/docs"}

@app.get("/random-quote")
def get_random_quote():
    return {"quote": random.choice(quotes)}
