
# 🎵 Pacify — Adaptive Music Recommender for Athletes

Pacify is an AI-powered application that dynamically syncs your workout music to your real-time heart rate, helping you maximize endurance, stamina, and motivation. This MVP version uses the **YouTube Data API** instead of Spotify — so you don’t need a premium subscription to get in the zone.

---

## ⚡️ Why Pacify?

🚀 **Boost Endurance:** Adaptive playlists that match your body’s tempo.  
🎯 **Personalized AI:** ML-powered BPM prediction based on your heart rate.  
📈 **Performance Data:** Proven to increase workout duration and satisfaction.  
🎵 **Free Playback:** Find songs directly on YouTube Music, no premium required.

---

## 📸 Demo

> **🚧 Coming Soon!**  
> A short video will show how Pacify predicts your BPM and recommends tracks via YouTube. Stay tuned!

---

## 🧠 How It Works

1. **Real-time Heart Rate:** Stream live data from a fitness device or simulate with sample data.
2. **ML Inference:** A KNN regression model predicts the optimal song BPM range for your activity level.
3. **YouTube Search:** The app queries the YouTube Data API for tracks that match your target BPM.
4. **Playback:** Play the recommended tracks via embedded YouTube videos or direct links.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask or FastAPI, Scikit-Learn (KNN regression)
- **Frontend:** React.js (web) or React Native (mobile)
- **APIs:** YouTube Data API v3, BLE SDK for heart rate sensors (optional)
- **ML:** Signal processing (NumPy, SciPy), BPM prediction

---

## 📂 Project Structure

\`\`\`
Pacify/
├── backend/           # Flask/FastAPI server + ML model
│   ├── app.py
│   ├── model/         # Saved KNN model .pkl
│   ├── requirements.txt
│   └── utils/         # Signal processing scripts
│
├── frontend/          # React.js or React Native client
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   ├── api.js     # Handles backend API calls
│   ├── package.json
│
├── data/              # Sample heart rate data, BPM lookups
│   ├── heart_rate_samples.csv
│   ├── bpm_lookup.csv
│
├── tests/             # Unit tests for backend + ML
│   ├── test_model.py
│   ├── test_routes.py
│
├── .gitignore
├── README.md
└── LICENSE
\`\`\`

---

## 🚀 Getting Started

### 🔑 1. Clone the Repo

\`\`\`bash
git clone https://github.com/yourusername/pacify.git
cd pacify
\`\`\`

### ⚙️ 2. Setup Backend

\`\`\`bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
\`\`\`

- Be sure to add your **YouTube Data API key** to your backend config or `.env` file.

### 💻 3. Setup Frontend

\`\`\`bash
cd frontend
npm install
npm start
\`\`\`

- The frontend will run on `localhost:3000` and connect to your backend server.

---

## 🧪 Testing

\`\`\`bash
pytest tests/
\`\`\`

Unit tests cover:
- ML model inference
- API routes
- Heart rate data processing

---

## 📜 License

**MIT License** — Free to use, fork, and adapt for your own projects.

---

## 🤝 Contributing

Got an idea to make Pacify smarter? Found a bug?  
Open an issue or submit a pull request — contributions are always welcome!

---

## 🙌 Connect

Built with ❤️ by [Warren Dmello](https://www.linkedin.com/in/warrenlukedmello)  
[📧 warrenlukedmello@gmail.com](mailto:warrenlukedmello@gmail.com) • [GitHub](https://github.com/Warren2005)

---

**Ready to sync your heartbeat to your hustle? Let’s Pacify!** 🎵🔥
