<div align="center">

# 🚀 AI Lead Discovery System

### 🧠 Intelligent Merchant Discovery Engine

### ⚡ FastAPI + DuckDuckGo + AI Scoring

<p align="center">
  <img src="https://img.shields.io/badge/Python-Backend-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-API-green?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/Uvicorn-ASGI-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Render-Deployment-black?style=for-the-badge&logo=render"/>
</p>

---

✨ **Discover high-intent merchants automatically** using
AI-powered search discovery, intelligent filtering, and priority scoring.

</div>

---

# 🌌 Overview

The **AI Lead Discovery System** is an intelligent backend that automatically finds potential business leads from the web.

It uses:

🔍 **Search intelligence**
🌐 **Website scraping**
🧠 **Signal-based scoring**
📊 **Lead prioritization**

to generate **sales-ready merchant leads**.

---

# ✨ Features

### 🔎 Smart Lead Discovery

Searches the web using DuckDuckGo and finds relevant merchants automatically.

### 🧠 AI Signal Scoring

Each discovered domain is scored based on:

* 🇮🇳 Indian business signals
* 🌍 International commerce indicators
* 🏷 Segment-specific relevance

### 🧹 Intelligent Filtering

Removes:

* blogs
* news sites
* directories
* irrelevant domains

### 📊 Lead Priority Ranking

Leads are automatically categorized as:

| Score | Priority |
| ----- | -------- |
| 80+   | 🔥 HOT   |
| 50-79 | 🌤 WARM  |
| <50   | ❄️ COLD  |

### ⚡ FastAPI Backend

Your discovery engine runs as an **API service**.

Example endpoint:

```
GET /discover/travel
```

---

# 🏗 Architecture

```
        🌐 DuckDuckGo Search
                │
                ▼
        🔍 Lead Discovery Engine
                │
                ▼
        🧠 Signal Scoring System
                │
                ▼
        🧹 Filtering Pipeline
                │
                ▼
        📊 Priority Ranking
                │
                ▼
         ⚡ FastAPI Backend
                │
                ▼
           🌍 API Response
```

---

# 📂 Project Structure

```
ai-lead-system
│
├── ai_lead_system.py   # Lead discovery engine
├── main.py             # FastAPI API server
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-lead-system.git
cd ai-lead-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates documentation.

Open:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will appear.

---

# 🔍 Example API Usage

### Discover Travel Merchants

```
GET /discover/travel
```

Example response:

```json
{
 "segment": "travel",
 "lead_count": 5,
 "leads": [
  {
   "domain": "exampletravel.com",
   "website": "https://exampletravel.com",
   "priority_score": 82
  }
 ]
}
```

---

# 🌍 Supported Segments

The engine can discover merchants across multiple industries.

| Segment      | Description                     |
| ------------ | ------------------------------- |
| ✈️ travel    | tour operators, travel agencies |
| 🎓 edtech    | online learning platforms       |
| 🛍 ecommerce | designer fashion brands         |
| 🎬 ott       | streaming platforms             |

---

# 🚀 Deployment (Render)

This project can be deployed easily to **Render**.

### Start Command

```
uvicorn main:app --host 0.0.0.0 --port 10000
```

Render will automatically install dependencies from `requirements.txt`.

---

# 🧠 Lead Scoring Logic

Each merchant receives a **priority score** calculated from:

```
Total Score =
    Indian Business Signal
  + International Commerce Signal
  + Segment Relevance Signal
```

Example signals:

* `.in` domain
* GST mention
* international shipping
* online course
* travel packages

---

# 🛡 Filters

The system automatically blocks:

* adult domains
* payment gateways
* job boards
* directories
* blogs
* news portals

This ensures **high quality merchant leads**.

---

# 📈 Future Improvements

Possible upgrades:

✨ async crawling for faster discovery
✨ AI merchant classification
✨ Redis caching
✨ company enrichment APIs
✨ automated outreach generation

---

# 👨‍💻 Tech Stack

| Technology    | Purpose          |
| ------------- | ---------------- |
| 🐍 Python     | backend engine   |
| ⚡ FastAPI     | API framework    |
| 🚀 Uvicorn    | ASGI server      |
| 🦆 DuckDuckGo | lead discovery   |
| 🐼 Pandas     | data processing  |
| 🌐 Requests   | website scraping |

---

# 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork repository
2. Create feature branch
3. Submit pull request

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

It helps others discover the project.

---

<div align="center">

### 💡 Built for intelligent lead discovery

🚀 Automating the future of sales intelligence

</div>
