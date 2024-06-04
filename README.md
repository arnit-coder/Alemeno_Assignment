# Urine Strip Color Detector

This project provides a web interface to upload an image of a urine strip and identifies the colors on the strip.

## Features
- Upload urine strip images through a web interface.
- Extract colors from the image and return them as JSON.

## Technologies
- Django for the backend API.
- OpenCV for image processing.
- Vanilla JS for the frontend.

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/urine-strip-color-detector.git
    cd urine-strip-color-detector
    ```

2. Set up the backend:
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

3. Open `frontend/index.html` in a web browser.

## Usage
1. Open the web interface.
2. Select an image of a urine strip.
3. Click "Upload" to process the image and view the results.

