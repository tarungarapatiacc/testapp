# Setup Instructions - Human vs AI Thinking Assessment Platform

## 📋 Prerequisites

Make sure you have installed:
- **Python 3.10+** - Download from [python.org](https://www.python.org/downloads/)
- **Node.js 16+** - Download from [nodejs.org](https://nodejs.org/)
- **Git** - Download from [git-scm.com](https://git-scm.com/)

## 🚀 Quick Start (Development Mode)

### Step 1: Clone the Repository

```bash
git clone https://github.com/tarungarapatiacc/testapp.git
cd testapp
git checkout dev/init-humanai-app
```

### Step 2: Backend Setup

#### On macOS/Linux:

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download NLP model
python -m spacy download en_core_web_sm

# Run the backend
python main.py
```

#### On Windows:

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLP model
python -m spacy download en_core_web_sm

# Run the backend
python main.py
```

**Expected Output:**
```
🚀 Starting Human vs AI Assessment Platform
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Backend is now running on: **http://localhost:8000**

### Step 3: Frontend Setup (New Terminal)

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

**Expected Output:**
```
On Your Network: http://192.168.x.x:3000

  Local: http://localhost:3000
```

Frontend is now running on: **http://localhost:3000**

## 🌐 Access the Application

1. Open your browser
2. Navigate to: **http://localhost:3000**
3. Click "Start Assessment" to begin

## 📚 API Documentation

Once the backend is running, access the interactive API docs:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Running Tests

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## 🐳 Docker Setup (Alternative)

If you prefer using Docker:

```bash
# Build and run with Docker Compose
docker-compose up
```

This will:
- Build and start the backend on port 8000
- Build and start the frontend on port 3000

## 📝 Environment Variables

### Backend (.env)

```
PORT=8000
DEBUG=True
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
SPACY_MODEL=en_core_web_sm
```

### Frontend (.env)

```
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_TIMEOUT=30000
```

## ✅ Troubleshooting

### Python Dependencies Issue

```bash
# Upgrade pip
pip install --upgrade pip

# Clear cache and reinstall
pip cache purge
pip install -r requirements.txt
```

### spaCy Model Not Found

```bash
python -m spacy download en_core_web_sm
```

### Port Already in Use

**For Backend (Port 8000):**
```bash
# macOS/Linux
lsof -i :8000
kill -9 <PID>

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**For Frontend (Port 3000):**
```bash
# macOS/Linux
lsof -i :3000
kill -9 <PID>

# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### CORS Errors

Make sure the backend is running on `http://localhost:8000` and the frontend is accessing it correctly. Check the `.env` file in the frontend directory.

## 📁 Project Structure

```
testapp/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── config.py
│   ├── tests/
│   ├── requirements.txt
│   ├── main.py
│   ├── Dockerfile
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── styles/
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── public/
│   ├── package.json
│   ├── Dockerfile
│   ├── tailwind.config.js
│   └── .env
├── docs/
│   ├── ARCHITECTURE.md
│   └── API.md
└── docker-compose.yml
```

## 🎯 Next Steps

1. Access the app at http://localhost:3000
2. Click "Start Assessment"
3. Answer the questions thoughtfully
4. View your detailed analysis and scores
5. Compare your human thinking with AI approaches

## 📖 Documentation

- Architecture Overview: `/docs/ARCHITECTURE.md`
- API Documentation: `/docs/API.md`

## 🤝 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Ensure all prerequisites are installed
3. Verify both servers are running
4. Check the browser console for errors

## 🎉 You're All Set!

Your Human vs AI Thinking Assessment Platform is ready to use!
