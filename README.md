# 💬 DevConnect

**DevConnect** is a multi-user group chat platform built using **Django**. It allows users to sign up, log in, create or join chat rooms, and send messages with other participants. It’s designed for collaborative discussions, team coordination, or just casual chat.

---

## 🚀 Features

- 👤 User Registration and Login
- 🏠 Create and Join Chat Rooms
- 🗨️ Messaging Within Rooms
- 👥 View All Rooms You’ve Joined
- ⏱️ Message Timestamping
- 🔒 Secure Session Handling

---

## 🛠️ Tech Stack

| Layer        | Technology       |
|--------------|------------------|
| Backend      | Django (Python)  |
| Frontend     | HTML, CSS        |
| Database     | SQLite           |
| Auth System  | Django Sessions  |

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/devconnect.git
cd devconnect
2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Migrations
bash
Copy
Edit
python manage.py migrate
5. Start the Server
bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

🧩 Folder Structure
bash
Copy
Edit
devconnect/
├── chat/              # Chat logic: rooms, messages, participants
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── ...
├── users/             # User registration and login
├── templates/
├── static/            # CSS and assets
├── db.sqlite3
└── manage.py
💡 How It Works
User Auth: Users sign up and log in using Django’s auth system.

Rooms: Users can create new chat rooms or join existing ones.

Messaging: Inside each room, users can send and read messages. Page reloads handle updates.

Participants: Each room keeps track of users who’ve joined.
