# Sentiment Analysis Application

A web-based application for analyzing sentiment in text using natural language processing.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Frontend](#frontend)
- [Backend](#backend)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Overview

This application provides sentiment analysis capabilities for text input. Users can either paste text directly or upload text files for analysis. The system processes the input and returns sentiment scores along with other text statistics.

## Features

- Text input for sentiment analysis
- File upload support (TXT, PDF)
- Sentiment classification (Positive, Negative, Neutral)
- Detailed sentiment scores (Positive, Negative, Neutral, Compound)
- Word count and character count
- Visualization of sentiment distribution
- Results history and comparison

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 14+
- Flask
- Streamlit
- NLTK

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Saswatsusmoy/fiXit
   cd sentiment-analysis-app
   ```

2. Set up the backend:
   ```sh
   cd backend
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```sh
   cd ../frontend
   npm install
   ```

## Usage

1. Start the backend server:
   ```sh
   cd backend
   python run.py
   ```

2. Start the frontend application:
   ```sh
   cd frontend
   streamlit run app.py
   ```

3. Open your browser and navigate to `http://localhost:8501` to use the application.

## API Reference

### POST /upload

Upload a file for analysis.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (File)

**Response:**
```json
{
  "file_id": "filename.txt"
}
```

### POST /analyze

Analyze text or a previously uploaded file.

**Request:**
- Method: POST
- Content-Type: application/json
- Body:
  ```json
  {
    "text": "Sample text to analyze"
  }
  ```
  or
  ```json
  {
    "file_id": "filename.txt"
  }
  ```

**Response:**
```json
{
  "filename": "filename.txt",
  "file_size": 1024,
  "text": "Sample text to analyze",
  "word_count": 4,
  "char_count": 24,
  "sentiment": "Positive",
  "pos_score": 0.75,
  "neg_score": 0.0,
  "neu_score": 0.25,
  "compound_score": 0.8
}
```

### GET /results

Retrieve all analysis results.

**Response:**
```json
[
  {
    "filename": "file1.txt",
    "file_size": 1024,
    "text": "Sample text 1",
    "word_count": 3,
    "char_count": 13,
    "sentiment": "Neutral",
    "pos_score": 0.0,
    "neg_score": 0.0,
    "neu_score": 1.0,
    "compound_score": 0.0
  },
  {
    "filename": "file2.txt",
    "file_size": 2048,
    "text": "Sample text 2",
    "word_count": 3,
    "char_count": 13,
    "sentiment": "Positive",
    "pos_score": 0.5,
    "neg_score": 0.0,
    "neu_score": 0.5,
    "compound_score": 0.6
  }
]
```

## Frontend

The frontend is built using Streamlit and consists of the following main components:

- `app.py`: Main application entry point
- `pages/home.py`: Home page with text input and file upload
- `pages/results.py`: Results page with visualizations
- `utils/api.py`: API client for communicating with the backend

### Key Functions

- `upload_file(file)`: Uploads a file to the backend
- `analyze_sentiment(input_data)`: Sends text or file_id for sentiment analysis
- `get_all_results()`: Retrieves all analysis results
- `display_result(result)`: Renders the analysis result

## Backend

The backend is built with Flask and uses NLTK for sentiment analysis:

- `app/__init__.py`: Flask application initialization
- `app/routes.py`: API route definitions
- `app/services/file_service.py`: File handling operations
- `app/services/sentiment_service.py`: Sentiment analysis logic
- `config.py`: Configuration settings
- `run.py`: Application entry point

### Key Functions

- `save_file(file)`: Saves uploaded files
- `read_file(file_id)`: Reads file contents
- `analyze_sentiment(text)`: Performs sentiment analysis on text

## Deployment

The application is deployed using the following services:

- Backend: Render (https://fixit-zvso.onrender.com)
- Frontend: Streamlit Cloud (https://sentiment-analyser-fixit.streamlit.app/)

### Deployment Steps

1. Push your code to GitHub.
2. Set up a new web service on Render, connecting to your GitHub repository.
3. Configure the start command: `gunicorn wsgi:app`
4. Set environment variables in the Render dashboard.
5. Deploy the Streamlit frontend by connecting your GitHub repository to Streamlit Cloud.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request
