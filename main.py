from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
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
        "You must be a magician — whenever you're around, everyone else disappears.",
        "Is your name Google? Because you have everything I've been searching for.",
        "Do you believe in love at first sight, or should I walk by again?",
        "Are you a camera? Every time I look at you, I smile.",
        "Do you have a sunburn, or are you always this hot?",
        "If you were a vegetable, you'd be a cute-cumber.",
        "Are you a parking ticket? Because you've got 'fine' written all over you.",
        "I must be a snowflake, because I've fallen for you.",
        "Do you have a Band-Aid? I just scraped my knee falling for you.",
        "Are you a magnet? Because I feel an undeniable pull toward you.",
        "I'd say God bless you, but it looks like he already did.",
        "Is it hot in here, or is it just you?",
        "You must be tired — you've been running through my mind all day.",
        "If looks could kill, you'd definitely be a weapon of mass destruction.",
        "I was going to play it cool, but then you smiled at me.",
        "Excuse me, I think you dropped something — my jaw.",
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
        "Loving you is the easiest thing I've ever done.",
        "You make my heart feel like it's seeing sunshine for the first time.",
        "I don't need the stars — I have you, and you're brighter.",
        "The world is a better place simply because you're in it.",
        "I fall in love with you a little more every single day.",
        "You're not just my person — you're my favorite person.",
        "Even on my worst days, you are still my best thing.",
        "Thank you for being the kind of love I didn't know I deserved.",
        "You are soft and strong and the most beautiful thing I know.",
        "I'd choose you in a hundred lifetimes, in any universe, always you.",
    ],
    "poetic": [
        "You are the poetry I never knew how to write.",
        "In the arithmetic of love, one plus one equals everything.",
        "I carry your heart with me — I carry it in my heart.",
        "You are the last thought I want to have before I dream.",
        "Like stars need the night, I need you to feel alive.",
        "If I know what love is, it is because of you.",
        "You are the music while the song lasts.",
        "You are the calm in the storm and the warmth in the cold.",
        "To love you is to breathe — unconscious, necessary, endless.",
        "You are the space between heartbeats where everything is still.",
        "Love is not a feeling — it is you, simply existing near me.",
        "I looked for beauty in ordinary things and found you.",
        "You are every unfinished sentence I have ever wanted to say.",
        "In the quiet hours, you are the thought that stays.",
        "You are not where I am going — you are why I go.",
        "Some loves are a chapter. You are the whole book.",
        "I have loved you in every language I know, and in some I invented.",
        "You are the kind of rare thing the universe makes only once.",
        "Even silence sounds different when you're in the room.",
        "You are the story I will tell when someone asks what changed me.",
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