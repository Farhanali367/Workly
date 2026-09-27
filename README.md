# 🚀 Workly — Modern Job Search & Career Platform

<p align="center">
  <b>A full-stack Django-based career platform connecting Job Seekers and Companies.</b>
</p>

<p align="center">
  🔎 Find Jobs • 👤 Build Profiles • 📄 Create Resumes • 💼 Apply • 🤝 Connect • 💬 Message
</p>

<p align="center">

[🌐 Live Demo](https://workly-w2py.onrender.com/)

&nbsp;&nbsp;|&nbsp;&nbsp;

[💻 GitHub Repository](https://github.com/Farhanali367/Workly)

</p>

---

## 🌐 Live Demo

🚀 **Try Workly Online:**

👉 **https://workly-w2py.onrender.com/**

The application is deployed using **Render**.

> ⏳ If the application has been inactive for some time, the first request may take a little longer while the service starts.

---

# 🌟 About Workly

**Workly** is a full-stack job search and career networking platform built using **Python and Django**.

The platform brings **job seekers, recruiters, and companies** together in one place.

Job seekers can discover opportunities, create professional profiles, build resumes, apply for jobs, save interesting positions, manage applications, connect with other users, and communicate through messages.

Companies can manage their profiles, publish job opportunities, review applications, and interact with potential candidates.

---

# ✨ Key Features

## 👨‍💻 Job Seeker Features

- 🔐 User Registration & Login
- 👤 Professional Profile Management
- ✏️ Edit Profile
- 📄 Resume Builder
- 🔎 Job Search
- 💼 Apply for Jobs
- 🔖 Save Jobs
- 📊 Application Tracking
- 👀 Profile View Statistics
- 🤝 Professional Connections
- 💬 User Messaging
- 📱 Social Feed
- 🔔 Recent Activity
- 📈 Dashboard Analytics
- 🔑 Forgot Password
- 🔢 OTP Verification
- 🔄 Password Reset

---

## 🏢 Company Features

- 🏢 Company Profile
- 📢 Job Posting
- 👥 Candidate Management
- 📋 Application Management
- 🔎 Candidate Discovery
- 📊 Recruitment Activity
- 👤 Candidate Profiles
- 💬 Communication

---

# 📊 Dashboard

Workly provides a centralized dashboard for monitoring career activity.

### Dashboard includes:

- 💼 Jobs Applied
- 📅 Interviews
- 👀 Profile Views
- 🔖 Saved Jobs
- 📊 Application Activity
- 🔔 Recent Activity
- 📈 Profile Completion
- 🎯 Career Statistics

---

# 🔎 Job Search

Users can discover available job opportunities and explore positions according to their career interests.

### Job Search Features

- Search Jobs
- View Job Details
- Explore Company Information
- Apply for Jobs
- Save Jobs
- Track Applications

---

# 📄 Resume Builder

Workly includes a built-in **Resume Builder** that allows users to create and manage professional resume information.

Users can manage:

- Personal Information
- Education
- Skills
- Experience
- Projects
- Career Information

---

# 🤝 Professional Networking

Workly also provides professional networking functionality.

Users can:

- Send Connection Requests
- Accept Connections
- Manage Connections
- Discover Professionals
- Communicate with Connections
- Share Content

---

# 💬 Messaging System

Workly includes a user-to-user messaging system for professional communication.

Users can communicate with:

- Job Seekers
- Recruiters
- Professionals
- Connections

---

# 🔐 Authentication

The authentication system includes:

- User Registration
- Login
- Logout
- Forgot Password
- OTP Verification
- Password Reset
- Authenticated User Areas

---

# 🏗️ Project Architecture

```text
Workly/
│
├── account/
│   ├── Authentication
│   ├── Registration
│   ├── Login
│   ├── OTP Verification
│   └── Password Reset
│
├── company/
│   ├── Company Profiles
│   ├── Job Posting
│   └── Application Management
│
├── jobseeker/
│   ├── Job Seeker Profiles
│   ├── Job Search
│   ├── Applications
│   ├── Saved Jobs
│   ├── Connections
│   └── Resume Builder
│
├── workly/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── Project Configuration
│
├── media/
│   └── Uploaded Files
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Backend Programming |
| 🌐 Django | Web Framework |
| 🎨 HTML5 | Page Structure |
| 🎨 CSS3 | Styling |
| ⚡ JavaScript | Frontend Interactivity |
| 🗄️ SQLite | Database |
| 📦 Bootstrap | UI Components |
| 🔧 Git | Version Control |
| 🐙 GitHub | Source Code Management |
| ☁️ Render | Deployment |

---

# 🔄 How Workly Works

```text
                    ┌─────────────────┐
                    │      USER       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  AUTHENTICATION │
                    └────────┬────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │   JOB SEEKER    │     │     COMPANY     │
        └────────┬────────┘     └────────┬────────┘
                 │                       │
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │   SEARCH JOBS   │     │    POST JOBS    │
        └────────┬────────┘     └────────┬────────┘
                 │                       │
                 └───────────┬───────────┘
                             ▼
                    ┌─────────────────┐
                    │   APPLICATION   │
                    │   MANAGEMENT    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   NETWORKING    │
                    │  & MESSAGING    │
                    └─────────────────┘
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Farhanali367/Workly.git
```

## 2️⃣ Navigate to Project

```bash
cd Workly
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 6️⃣ Apply Migrations

```bash
python manage.py migrate
```

## 7️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

## 8️⃣ Collect Static Files

```bash
python manage.py collectstatic --noinput
```

## 9️⃣ Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# ☁️ Deployment

Workly is deployed using **Render**.

### Production URL

👉 https://workly-w2py.onrender.com/

### Static Files

```bash
python manage.py collectstatic --noinput
```

---

# 📈 Future Improvements

The project can be extended with:

- 🤖 AI-Powered Job Recommendations
- 🧠 AI Resume Analysis
- 🎯 Skill-Based Job Matching
- 📧 Email Notifications
- 🔔 Real-Time Notifications
- 💬 Real-Time Chat
- 📊 Advanced Analytics
- 🌍 Location-Based Job Search
- 🔍 Advanced Candidate Search
- ☁️ Cloud Database
- 🔐 Two-Factor Authentication
- 🧠 AI Career Assistant
- 📈 Personalized Career Recommendations

---

# 🎯 Project Goals

The main goals of Workly are:

- Simplify the job search process
- Help candidates build professional profiles
- Provide companies with an efficient recruitment platform
- Centralize job applications
- Enable professional networking
- Improve communication between candidates and recruiters
- Provide a unified career management experience

---

# 💡 Why Workly?

Traditional job searching often requires users to switch between multiple platforms:

```text
Jobs
  ↓
Applications
  ↓
Resume
  ↓
Networking
  ↓
Messaging
```

**Workly** aims to bring these career activities together into a single platform.

---

# 📸 Project Screenshots

Add screenshots of the application here.

Recommended screenshots:

- 🏠 Dashboard
- 🔐 Login
- 👤 User Profile
- 🔎 Job Search
- 💼 Job Details
- 📄 Resume Builder
- 📋 Applications
- 🤝 Connections
- 💬 Messaging
- 🏢 Company Dashboard

---

# 👨‍💻 Developer

## Farhan Ali

**B.Tech Computer Science Engineering Student**

### Interests

- 💻 Software Engineering
- 🧩 Data Structures & Algorithms
- 🐍 Python
- ⚡ C++
- 🌐 Web Development
- 🤖 Artificial Intelligence & Machine Learning
- 🐙 Git & GitHub

### GitHub

👉 https://github.com/Farhanali367

---

# 📌 Project Information

| Category | Details |
|----------|---------|
| Project Name | Workly |
| Project Type | Full-Stack Web Application |
| Backend | Django / Python |
| Frontend | HTML / CSS / JavaScript |
| Database | SQLite |
| Version Control | Git & GitHub |
| Deployment | Render |

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐

---

<p align="center">

## 🚀 Workly

### Build Your Career • Find Opportunities • Connect • Grow

</p>
