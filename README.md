# Adv-Django-Final-Project


# **SkillSphere Platform Documentation**

## **Overview**

**SkillSphere** is a collaborative learning platform where users can create and join mini-courses, articles, and challenges, interact with AI mentors, and receive certifications.



## **User Roles**

1. **Learner**

   * Takes courses and challenges
   * Participates in forums
   * Earns certificates and achievements

2. **Mentor**

   * Creates mini-courses and quizzes
   * Provides help and feedback to other users
   * Participates in mutual mentoring

3. **Admin**

   * Manages users and content
   * Moderates forums and reports
   * Oversees platform integrity

---

## **Core Features**

### **1. Learning System**

* **Course Creation**

  * Add text, video, quizzes, and assignments
  * Drag & Drop editor for structuring content
  * Progress bars and checkpoints
  * AI-generated quizzes based on content

* **Challenges**

  * 7-day / 30-day structured activities
  * Examples: “30 Days of Python”, “7-Day Design Sprint”


* **Progress Tracking**

  * Monitor completion of lessons and quizzes
  * Automatic grading and feedback

---

### **2. AI Features**

* **AI Mentor (OpenAI-based)**

  * Answers questions in natural language
  * Explains course concepts
  * Provides personalized suggestions

* **Quiz and Test Generation**

  * Automatically generate questions from uploaded content

* **Error Analysis**

  * Reviews user code or submissions and provides corrections or hints

---

### **3. Community**

* **User Profiles**

  * Skills, badges, completed courses
  * Downloadable, shareable resume
  * LinkedIn integration


### **4. Certification System**

* **Smart Certificates**

  * Auto-generated PDF upon course completion
  * Stored in profile, downloadable
  * Includes course title, user name, completion date

* **LinkedIn Integration**

  * One-click sharing of certifications

---

## **Tech Stack**

### **Backend (Django + DRF)**

* **PostgreSQL** – relational data (users, courses, certifications)
* **MongoDB** – forums, AI chat history
* **Celery + Redis** – background tasks (e.g., certificate generation, reminders)
* **OpenAI / HuggingFace APIs** – AI mentor, quiz generation, feedback

Frontend (React + Tailwind CSS)
Drag & drop course builder (e.g., with dnd-kit or react-beautiful-dnd)
Responsive UI built with Tailwind CSS
Real-time progress tracking with interactive components
Forum threads, markdown rendering, voting
Mobile-first design and dark mode support




## **APIs Overview**

### **Auth and User Management**

* `POST /api/register/`
* `POST /api/login/`
* `GET /api/profile/`

### **Courses and Lessons**

* `GET /api/courses/`
* `POST /api/courses/`
* `GET /api/courses/<id>/lessons/`


### **Certifications**

* `GET /api/certificates/`
* `POST /api/certificates/generate/`



## **Future Enhancements**

* Gamification: XP, badges, ranking
* AI-based skill gap analysis
* Marketplace for premium courses
* Live sessions & chat rooms
* Multilingual support

