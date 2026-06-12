https://ai-horoscope-prediction.streamlit.app/
https://huggingface.co/iTamojeet

---

# 🔮 AI Horoscope Predictor — Your Daily Cosmic Intelligence

> **An AI-powered horoscope assistant that generates personalised daily predictions for all 12 zodiac signs — powered by Google Gemini 1.5 Pro and deployed live on Streamlit.**

**AI Horoscope Predictor** lets users explore their cosmic outlook using cutting-edge generative AI. Select your zodiac sign, ask a custom query, and receive a rich daily reading covering career, relationships, health, lucky numbers, compatibility, and more — all through a clean, interactive interface.

🌐 Live on Streamlit Cloud  
🤖 Powered by Google Gemini 1.5 Pro  
✨ Personalised predictions with custom queries  
♈ Supports all 12 zodiac signs  

---

# ✨ Features

## 🧠 AI-Powered Horoscope Generation

- Generates detailed daily horoscopes using Gemini 1.5 Pro
- Covers career, relationships, health, and personal guidance
- Lucky numbers and lucky dates included in every reading
- Zodiac compatibility analysis with all other signs
- Highlights any negative aspects in bold for honest insights

## 💬 Custom Query Support

- Users can type any personal question alongside their zodiac selection
- Query is appended directly to the AI prompt for contextual predictions
- Encourages practical, tailored advice beyond generic readings

## ⚡ Smart Caching for Performance

- Uses Streamlit's `@st.cache_data` to cache repeated requests
- Avoids redundant API calls for the same sign + query combination
- Significantly faster response on re-runs within the same session

## 🎨 Clean & Simple Dashboard UI

- Minimal, distraction-free Streamlit interface
- Dropdown selection for all 12 zodiac signs
- Displays today's date dynamically with every prediction
- Success-highlighted output for a polished feel

## 🔐 Secure API Key Handling

- Uses `python-dotenv` to load the Google API key from `.env`
- API key is never hardcoded or exposed in source code
- `find_dotenv()` ensures the key is found regardless of working directory

## 🌍 Live Deployment

- Fully deployed and accessible at [ai-horoscope-prediction.streamlit.app](https://ai-horoscope-prediction.streamlit.app/)
- No local setup required for end users

---

# 🧠 How It Works

## Pipeline Flow

```
User selects Zodiac Sign + enters optional query
              ↓
Prompt is constructed with sign, query & instructions
              ↓
Google Gemini 1.5 Pro generates the horoscope
              ↓
Response displayed in Streamlit UI with today's date
```

### Step-by-Step Process

1. User selects their zodiac sign from a dropdown menu.
2. User optionally types a personal question in the text input.
3. A detailed prompt is built including career, health, relationships, lucky numbers, compatibility, and any negative aspects.
4. The prompt is sent to Google Gemini 1.5 Pro via the `google-generativeai` SDK.
5. The prediction is cached using `@st.cache_data` for performance.
6. The result is displayed with today's date in the Streamlit app.

---

# 🏗️ Architecture

## Cloud-Powered AI Stack

```
Frontend        → Streamlit
AI Model        → Google Gemini 1.5 Pro
AI SDK          → google-generativeai
Config          → python-dotenv
Deployment      → Streamlit Cloud
```

### Why this architecture works:

✅ No local model or hardware required  
✅ Gemini 1.5 Pro delivers rich, nuanced predictions  
✅ Streamlit makes deployment and UI trivially simple  
✅ Caching reduces API cost and latency  
✅ `.env`-based key management keeps secrets safe  

---

# 🏗️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | UI framework & deployment |
| Google Gemini 1.5 Pro | Horoscope generation LLM |
| google-generativeai | Official Gemini Python SDK |
| python-dotenv | Secure API key management |
| datetime | Dynamic date display |

---

# 📂 Project Structure

```
ai-horoscope-prediction/
│
├── app.py
├── requirements.txt
├── .gitignore
├── pyvenv.cfg
└── README.md
```

---

# ⚡ Installation & Setup

## 1️⃣ Clone Repository

```
git clone https://github.com/iTamojeet/ai-horoscope-prediction.git
cd ai-horoscope-prediction
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
```

### Activate Environment

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

Or manually:

```
pip install streamlit google-generativeai python-dotenv
```

---

## 4️⃣ Set Up Your Google Gemini API Key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

Get your free API key at:

👉 https://makersuite.google.com/app/apikey

---

## 5️⃣ Run the Application

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 💬 Example Queries

Try asking alongside your zodiac sign:

- Will I get a promotion this month?
- Should I start a new relationship?
- What should I focus on for my health?
- Is this a good time to invest?
- How are my finances looking this week?

---

# 🎯 Use Cases

- Daily personal horoscope reading
- AI-driven astrology platforms
- Entertainment and lifestyle apps
- Spiritual wellness tools
- Social media content generation
- Personalised advice chatbots

---

# 🔐 Security

- API key loaded via `.env` and `python-dotenv` — never exposed in code
- `.gitignore` ensures `.env` is never committed to version control
- No user data is stored or logged
- All API calls go directly to Google's secure Gemini endpoint

---

# 🚀 Future Improvements

- Weekly and monthly horoscope modes
- Birth chart integration (date + time + place of birth)
- Vedic astrology support
- Multi-language predictions
- Voice output using text-to-speech
- Shareable horoscope cards
- User authentication and saved history
- WhatsApp / Telegram bot integration

---

# 👨‍💻 Developer

**Tamojeet**  
AI & Data Enthusiast • Python Developer  
🔗 HuggingFace: https://huggingface.co/iTamojeet  
🌐 Live App: https://ai-horoscope-prediction.streamlit.app/

---

# ⭐ Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request