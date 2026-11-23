# 🧠 EmotionAI – Emotion Detection using NLP & Machine Learning

An AI-powered Emotion Detection application that analyzes user-provided text and predicts the underlying emotion using Natural Language Processing and Machine Learning.

## 🚀 Live Demo

**[Click Here to Try EmotionAI](https://emotionai-j9qzxfzv6lewu2trsqjgey.streamlit.app/)**

## ✨ Features

- Emotion detection from text input
- NLP-based text preprocessing and vectorization
- Machine Learning-based emotion classification
- Prediction probability visualization
- Interactive Streamlit web interface
- Real-time text predictions

## 🛠️ Tech Stack

- **Language:** Python
- **Machine Learning:** Scikit-learn
- **NLP:** Natural Language Processing
- **Vectorization:** Bag of Words
- **Algorithm:** Multinomial Naive Bayes
- **Libraries:** NumPy, Pandas
- **Frontend:** Streamlit

## 📂 Project Structure

```text
EmotionAI/
│
├── app.py
├── model/
│   ├── emotion_model.pkl
│   ├── vectorizer.pkl
│   └── label_mapping.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project**

```bash
cd EmotionAI
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

## 🧠 How It Works

1. User enters a text sentence.
2. Text is transformed into numerical features using the trained Bag of Words vectorizer.
3. The trained Multinomial Naive Bayes model predicts the emotion.
4. The application displays the predicted emotion and probability scores.

## 👨‍💻 Author

**Vansh Malhotra**

B.Tech Computer Science Engineering

## ⭐ Support

If you find this project useful, consider giving this repository a star!
