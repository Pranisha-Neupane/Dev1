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

Got it — the issue you're seeing in your `README.md` preview (from the screenshot) is that **GitHub or your Markdown editor is misinterpreting block types**, possibly because of extra "bash" labels or incorrect formatting under the code blocks.

Let me give you a cleaner and correctly-rendered version without unnecessary "Copy", "Edit", or duplicate `bash` tags.

---

### ✅ Cleaned `README.md` Markdown Snippet (especially for Folder Structure & Commands):

````markdown
## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/devconnect.git
cd devconnect
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Folder Structure

```
devconnect/
├── chat/              # Chat logic: rooms, messages, participants
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── users/             # User registration and login
├── templates/         # Global templates
├── static/            # CSS and static assets
├── db.sqlite3
└── manage.py
```

````

---

### ✅ Notes:
- Remove the "Copy" and "Edit" annotations — those are GitHub UI elements, **not part of the markdown**.
- Use triple backticks (```) before and after code blocks (not inside).

Let me know if you want the final `.md` file exported for direct use!
````
