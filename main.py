from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import random
import os

app = FastAPI(title="LoveNote API", description="Romantic quote generator 💌")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = {
    "flirty": [
        "Are you a time traveler? Because every moment with you feels like my favorite future.",
        "Do you have a name, or can I call you mine?",
        "Are you French? Because Eiffel for you.",
        "Do you have a map? I keep getting lost in your eyes.",
        "You must be a magician, because whenever you're around, everyone else disappears.",
        "Is your name Google? Because you have everything I've been searching for.",
        "Do you believe in love at first sight, or should I walk by again?",
        "Are you a camera? Every time I look at you, I smile.",
        "If you were a vegetable, you'd be a cute-cumber.",
        "Do you have a sunburn, or are you always this hot?",
    ],
    "sweet": [
        "If kisses were snowflakes, I'd send you a blizzard.",
        "You are my today and all of my tomorrows.",
        "In a sea of people, my eyes will always search for you.",
        "Every love story is beautiful, but ours is my favorite.",
        "You make ordinary moments feel extraordinary.",
        "Home is wherever I'm with you.",
        "You are the reason I look forward to every new day.",
        "With you, every moment is a memory I want to keep forever.",
        "You are the best thing that has ever been mine.",
        "I never knew what love felt like until I met you.",
    ],
    "poetic": [
        "You are the poetry I never knew how to write.",
        "In the arithmetic of love, one plus one equals everything.",
        "I carry your heart with me — I carry it in my heart.",
        "You are the last thought I want to have before I dream.",
        "Like stars need the night, I need you to feel alive.",
        "If I know what love is, it is because of you.",
        "You are the music while the song lasts.",
        "Love is not looking at each other — it is looking together in the same direction.",
        "You are the calm in the storm and the warmth in the cold.",
        "To love you is to breathe — unconscious, necessary, endless.",
    ],
}

all_quotes = [q for category in quotes.values() for q in category]


@app.get("/random-quote")
def get_random_quote(mood: str = Query(default="all", enum=["all", "flirty", "sweet", "poetic"])):
    pool = quotes.get(mood, all_quotes) if mood != "all" else all_quotes
    return {"quote": random.choice(pool), "mood": mood}


@app.get("/moods")
def get_moods():
    return {"moods": list(quotes.keys())}


@app.get("/")
def serve_index():
    here = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(here, "static", "index.html")
    return FileResponse(index_path)
