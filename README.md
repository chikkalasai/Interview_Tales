# 🐦 Interview Tales - Twitter-like Full-Stack App (React + Django)

This is a full-stack Twitter-like social media application where users can sign up, log in, create and update profiles, post tweets (text or images), like and comment on posts, and view other users' profiles.

Built with **Django** for the backend and **React.js** for the frontend.

---

## 🚀 Features

- ✅ User registration, login, and logout
- 🧑‍💼 Profile creation and update (bio + profile pic)
- 📝 Create posts with text and image upload
- ❤️ Like and comment on posts
- 🧭 View other users’ profiles
- 🔐 Authentication using Token-based login

---

## 🛠 Tech Stack

| Frontend         | Backend      | Database | Others            |
|------------------|--------------|----------|-------------------|
| React.js         | Django       | SQLite   | Axios, REST API   |
| HTML/CSS/JS      | Django REST  |          | Django Auth Token |

---

## 🗂 Project Structure

Interview_Tales/
├── frontend/ # React frontend
│ ├── src/
│ └── package.json
├── backend/ # Django backend
│ ├── manage.py
│ ├── resume_analyzer/
│ └── media/ # profile pics, post images






---

## 🧪 Setup Instructions (Local)

### 🔧 Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver




💻 Frontend (React)

cd frontend
npm install
npm start
Runs at: http://localhost:3000/
