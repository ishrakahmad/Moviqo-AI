# 🎬 Moviqo AI

An AI-powered Movie Recommendation System built with Machine Learning, Streamlit and the TMDB API.  
Search movies in **English, Hindi, Tamil, Telugu, Korean, Japanese** and many other languages to receive intelligent movie recommendations with posters.

---

## 🚀 Live Demo

https://moviqo.streamlit.app/

---

## ✨ Features

- 🎥 AI-powered movie recommendation engine
- 🌍 Multilingual movie search
- 🇺🇸 Hollywood Movies
- 🇮🇳 Bollywood Movies
- 🇮🇳 South Indian Movies
- 🇰🇷 Korean Movies
- 🇯🇵 Japanese Movies
- 🖼 Movie posters from TMDB API
- ⚡ Fast recommendations using Cosine Similarity
- 🎨 Clean Streamlit UI
- 🔍 Smart movie search

---

## 🧠 Machine Learning

Moviqo AI uses a **Content-Based Recommendation System**.

The recommendation model is built using:

- CountVectorizer
- Cosine Similarity
- NLP Text Processing
- Feature Engineering
- Movie Metadata

Movie similarity is calculated using:

- Overview
- Genres
- Keywords
- Top Cast
- Director

---

## 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy

### Web

- Streamlit

### API

- TMDB API

### Others

- Pickle
- Requests
- python-dotenv

---

## 📂 Project Structure

```
Moviqo-AI/
│
├── app.py
├── model.py
├── requirements.txt
├── README.md
│
├── assets/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── utils/
│   └── tmdb.py
│
└── .env
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/ishrakahmad/Moviqo-AI.git
```

Move into the project

```bash
cd Moviqo-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```
TMDB_API_KEY=YOUR_API_KEY
```

Get your API Key from:

https://developer.themoviedb.org/

---

## ▶ Run

```bash
streamlit run app.py
```

---

## 📸 Preview

### Home

> Add your project screenshot here.

---

## 📊 Dataset

TMDB 5000 Movies Dataset

Contains

- 4800+ Movies
- Genres
- Overview
- Cast
- Director
- Keywords

---

## 🎯 Future Improvements

- Movie trailers
- Genre filters
- IMDb ratings
- Trending movies
- Watchlist
- User authentication
- Hybrid recommendation system
- Deep Learning recommendation model

---

## 🤝 Contributing

Contributions are welcome.

Fork the repository and create a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developer

**Ishrak Ahmad**

Computer Science & Engineering

American International University-Bangladesh (AIUB)

GitHub

https://github.com/ishrakahmad

LinkedIn

https://linkedin.com/in/ishrakahmad

Portfolio

https://www.ishrakahmad.me
