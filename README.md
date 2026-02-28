<h1 align="center">🎬 Movie Recommendation System</h1>

<p align="center">
  Discover trending movies, search thousands of titles, explore by genre,
  and view detailed movie information — all in a sleek Netflix-style UI.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/TMDB-API-green">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

---

## 🚀 Live Features

- 🔥 Real-Time Trending Movies
- 🔎 Smart Movie Search
- 🎭 Browse by Genre
- 🎬 Movie Detail Page (Overview, Rating, Release Date)
- 🎥 Instant Trailer Access
- 👥 Cast Details Section
- 🎯 Movie Recommendations
- 🎨 Modern Cinematic UI

---

## 🖼️ Demo Screenshots

### 🏠 Home Page
<img src="images/Home_page.png" width="100%">

---

### 🔥 Trending Movies
<img src="images/Trending_movies.png" width="100%">

---

### 🎭 Genre Selection
<img src="images/Genre_selection.png" width="100%">

---

### 🎯 Movie Recommendations
<img src="images/Recommendation.png" width="100%">

---

### 🎬 Movie Detail Page
<img src="images/Movie_detail.png" width="100%">

---

### 🎥 Instant Trailer
<img src="images/Instant_trailer.png" width="100%">

---

### 👥 Cast Detail Section
<img src="images/Cast_detail.png" width="100%">

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **TMDB API**
- **HTML + CSS (Custom Styling)**
- **python-dotenv**

---

## 📂 Project Structure

```
movie-recommendation-app/
│
├── app.py
├── tmdb_api.py
├── config.py
├── requirements.txt
├── .env
│
├── assets/
│   └── style.css
│
├── pages/
│   ├── movie_detail.py
│   └── recommendations.py
│
├── images/
│   ├── Home_page.png
│   ├── Trending_movies.png
│   ├── Genre_selection.png
│   ├── Recommendation.png
│   ├── Movie_detail.png
│   ├── Instant_trailer.png
│   └── Cast_detail.png
│
└── README.md
```

  

---

## 🔑 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/movie-recommendation-app.git
cd movie-recommendation-app
```
###2️⃣ Install Dependencies

```bash
pip install streamlit requests python-dotenv
```
###3️⃣ Get TMDB API Key
Create an account at https://www.themoviedb.org/
Go to Settings → API
Generate your API key

###4️⃣ Create .env File
Create a file named:

```bash
.env
```
Add:

```bash
TMDB_API_KEY=your_api_key_here
```

###5️⃣ Run the Application

```bash
streamlit run app.py
```
---

## 🎨 UI Highlights

- Cinematic hero section
- Floating movie posters
- Large centered headline
- Styled search bar
- Netflix-inspired movie cards
- Smooth hover animations
- Clean responsive grid layout

---

## ⚠️ Troubleshooting

**Network Connection Error?**
- Check your internet connection  
- Verify your TMDB API key inside the `.env` file  
- Make sure the `.env` file is placed in the root directory  
- Restart the Streamlit server  

If the issue persists, regenerate your TMDB API key from your account dashboard.

---

## 📌 Future Improvements

- 🤖 AI-Based Personalized Recommendations  
- ⭐ User Ratings & Reviews  
- 🔐 User Authentication System  
- 📺 Watchlist Feature  
- 🌍 Cloud Deployment (Streamlit Cloud / Render / Railway)  
- 📊 Analytics Dashboard  

---

## 👨‍💻 Author

Developed by **Raj Darlami**

---

## 📄No License

This project is created for educational and portfolio purposes.  



