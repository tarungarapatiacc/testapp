# Human vs AI Thinking Assessment Platform

A web application designed to assess out-of-the-box thinking and evaluate how human reasoning differs from algorithmic thinking through dynamic question generation and nuanced evaluation.

## 🎯 Objective

This platform judges analytical and creative thinking capabilities by:
- Generating context-specific questions
- Analyzing responses for nuance, real-time knowledge, and business acumen
- Comparing human thinking patterns against AI/algorithmic approaches
- Providing insights into divergent thinking abilities

## 🏗️ Architecture

```
├── backend/              # Python FastAPI server
│   ├── app/
│   ├── models/           # Database models & schemas
│   ├── routes/           # API endpoints
│   ├── services/         # Business logic & NLP services
│   ├── tests/
│   ├── requirements.txt
│   └── main.py
├── frontend/             # React TypeScript UI
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── .env
├── docker-compose.yml    # Local development setup
└── docs/                 # Documentation
```

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: React, TypeScript, Axios, TailwindCSS
- **ML/NLP**: spaCy, NLTK, scikit-learn for response analysis
- **Deployment**: Docker, Docker Compose

## 📋 Features

1. **Dynamic Question Generation**
   - Context-aware questions across multiple domains
   - Difficulty levels (beginner, intermediate, advanced)
   - Randomized question sequences

2. **Response Analysis Engine**
   - NLP-based sentiment and complexity analysis
   - Nuance detection in human responses
   - Real-time knowledge assessment
   - Business logic evaluation

3. **Scoring & Comparison**
   - Human vs AI thinking score
   - Creativity index
   - Out-of-box thinking metrics
   - Detailed feedback and insights

4. **User Dashboard**
   - Progress tracking
   - Historical assessments
   - Comparative analytics
   - Downloadable reports

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 16+
- Docker & Docker Compose (optional)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

## 📚 API Documentation

Once backend is running, visit: `http://localhost:8000/docs`

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 📖 Documentation

See `/docs` folder for detailed documentation on:
- Question generation strategy
- Response analysis algorithms
- Scoring methodology
- API specifications

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details
