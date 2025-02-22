# Quran Semantic Search Web App

This web application allows users to perform semantic search for verses in the Quran using sentence embeddings. The app uses the `sentence-transformers/all-MiniLM-L6-v2` model to embed text and perform the search efficiently.

## Features
- Semantic search for Quranic verses
- Fast and accurate search results based on sentence embeddings

## Requirements
- Python 3.x
- Flask
- Gunicorn (for production)
- `sentence-transformers` library
- Other dependencies (listed in `requirements.txt`)

## Installation

1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Building the Database

To build the database of Quranic verses, run the following command:

```bash
python build_db.py
```

This script will preprocess the Quranic verses, create sentence embeddings, and store them in the database for efficient search.

## Running the Web App

### On Linux/MacOS

To run the app in production using Gunicorn, use the following command:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

### On Windows

If you're using Windows, run the app with the `wsgi_win.py` script:

```bash
python wsgi_win.py
```

This will start the web server and you can access the app at `http://localhost:8000`.

## Usage

Once the web app is running, navigate to `http://localhost:8000` in your browser. You can enter a search query, and the app will return the most relevant verses from the Quran based on semantic similarity.
