# Flask URL Shortener

Flask URL Shortener is a simple web application that allows users to shorten long URLs and track the number of visits to the shortened links.

## Features

- **Shorten URLs:** Convert long URLs into short, easy-to-share links.
- **Track Clicks:** Monitor the number of times each shortened link is accessed.
- **View All Shortened URLs:** Access a list of all shortened URLs and their original counterparts.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/flask_shortner.git
cd flask_shortner
```
2. **Create a virtual environment:**

```bash
python3 -m venv venv
```

3. **Activate the virtual environment:**
- On macOS/Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
venv\Scripts\activate
```

4. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

## Usage

1. **Run the Flask application:**

```bash
flask run
```

2. **Access the application:**
Open your web browser and go to http://127.0.0.1:5000/.

3. **Shorten a URL:**

- On the homepage, enter the long URL you want to shorten and click the button to generate a short link.
- You will be redirected to the /urls page, where you can view your newly created short link and all previously created links.

4. **Redirect using a short URL:**

- Use the short URL in your browser, and it will redirect you to the original long URL.
- The number of visits will be incremented each time the short URL is accessed.

## Dependencies

- Flask
- Flask-WTF
- Flask-SQLAlchemy
- WTForms

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. We welcome improvements, bug fixes, and new features.

## Author
Developed by [iwannafly69](https://github.com/1sten)

- **Email:** iwannafly666@yandex.ru
- **GitHub:** [iwannafly69](https://github.com/iwannafly69)
