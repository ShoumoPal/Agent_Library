# 📚 Agent Library

An **AI-powered agentic library application** built with **Django**, **LangChain**, and **Gemini Free API**, with a custom **JavaScript + CSS frontend**.  

The project demonstrates how intelligent agents can be integrated into a web application for interactive querying, resource management, and AI-driven responses. All you have to do is pick or search for your own genre, and the backend agent would fetch 6 book recommendations for you! There is also an option to generate a summary for the given book as well.

---

## 🚀 Features

- 🤖 **AI-powered agentic workflows** with LangChain + Gemini  
- 🔎 **Library management system** for storing and retrieving resources  
- 🌐 **Full-stack web app** built with Django + JavaScript + CSS  
- 🗂️ **API endpoints** exposed for integration and testing  
- ☁️ **Deployed on AWS Elastic Beanstalk**  
- 🛡️ Environment variables and `.env` support for API keys and configs  

---

## 🏗️ Tech Stack

- **Backend**: Django (Python 3.11)  
- **AI Integration**: LangChain, Gemini Free API  
- **Frontend**: JavaScript, CSS (custom, minimal framework)  
- **Deployment**: AWS Elastic Beanstalk  
- **Other Tools**: python-dotenv, requests  

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository
```
git clone https://github.com/ShoumoPal/Agent_Library.git
cd Agent_Library
```
### 2️⃣ Create a Virtual Environment
```
python -m venv venv

Activate the environment:
python -m venv venv
```
### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Configure environment variables
```
In the .env file:
GOOGLE_API_KEY=your_gemini_api_key
```
### 5️⃣ Apply migrations and run the server
```
python manage.py migrate
python manage.py runserver
```

### 🎨Preview
<img width=75% height=75% alt="image" src="https://github.com/user-attachments/assets/72f1e319-09c6-4b4d-abe4-4befc71049b5" />
