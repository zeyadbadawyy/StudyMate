<p align="center">
  <img src="frontend\src\assets\banner.png" alt="StudyMate Banner" width="60%">
</p>

# 📚 StudyMate

![React](https://img.shields.io/badge/Frontend-React-blue)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![OpenRouter](https://img.shields.io/badge/AI-OpenRouter-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

StudyMate is a modern AI-powered study assistant designed to help students learn faster and more effectively. Upload your study materials and instantly generate summaries, flashcards, quizzes, exams, study guides, revision notes, and AI-powered document conversations.

Built with a modern full-stack architecture using React, FastAPI, SQLite, and OpenRouter AI models.

---

## 🚀 Live Demo

### Frontend
🔗 https://study-mate-inky.vercel.app/

### Backend API
🔗 https://studymate-production-2c5e.up.railway.app/docs

---

## ✨ Features

### 📄 Smart Document Upload
- Upload PDF files
- Upload DOCX files
- Upload TXT files
- Automatic document processing and text extraction

### 🤖 AI Study Tools
- Summary Generation
- Flashcard Generation
- Quiz Generation
- Exam Generation
- Study Guide Generation
- Revision Notes Generation

### 💬 Chat With Your Documents
- Ask questions about uploaded content
- Context-aware AI responses
- Interactive learning experience

### 📦 Export System
- Export generated content as PDF
- Export complete Study Package as ZIP
- Automatically includes the latest generated version of each study tool

### 📊 Analytics Dashboard
Track platform usage with:
- Documents uploaded
- Total generations
- Tool usage statistics
- Most used tool
- Latest activity

### 🕒 History Management
- View generation history
- Track previous outputs
- Delete individual items
- Clear all history

### ⚙️ User Experience
- Dark Mode
- Responsive Design
- Modern UI
- Settings Panel
- Keyboard Shortcuts
- Outside-click modal closing
- Real-time state updates

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- Axios
- CSS3

### Backend
- FastAPI
- SQLAlchemy
- SQLite

### AI Integration
- OpenRouter API
- GPT Models

### Document Processing
- PDFPlumber
- Python DOCX

### Exporting
- ReportLab
- ZIP Packaging

### Deployment
- Railway (Backend)
- Vercel (Frontend)

---

## 🏗️ System Architecture

```text
┌─────────────┐
│    User     │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ React Frontend  │
└──────┬──────────┘
       │ REST API
       ▼
┌─────────────────┐
│ FastAPI Backend │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│ OpenRouter API  │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│ AI Responses    │
└─────────────────┘
```

---

## 📁 Project Structure

```text
StudyMate/
│
├── backend/
│   ├── app/
│   ├── routes/
│   ├── services/
│   ├── database/
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── assets/
│   │
│   └── public/
│
└── README.md
```

---

## ⚙️ Local Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/StudyMate.git
cd StudyMate
```

### 2. Backend Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### 3. Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## 🔒 Security Features

- Environment variable protection
- Secure API key management
- CORS configuration
- Input validation
- Error handling
- Protected backend architecture

---

## 📈 Future Improvements

- User authentication
- User accounts and profiles
- Cloud document storage
- Multi-document chat
- AI study recommendations
- Advanced analytics
- Team collaboration
- Mobile application
- Spaced repetition learning
- Progress tracking dashboard

---

## 👨‍💻 Author

### Zeyad Badawy

**Full-Stack Developer | Software Engineer**

- GitHub: https://github.com/YOUR_USERNAME
- LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---

## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project in accordance with the license terms.

---

**StudyMate — Your Docs, Unlocked. 🚀**
