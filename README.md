# 💌 LoveNote API

A romantic quote generator built with FastAPI and vanilla JavaScript.

## Features
- Random love notes across 3 moods: flirty, sweet, poetic
- Save favourites, copy, and share
- Auto-play mode and dark mode support

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000)

## API

```
GET /random-quote           → random quote (any mood)
GET /random-quote?mood=sweet → filtered by mood
```

## Stack
Python · FastAPI · Vanilla JS · Deployed on Render