This repository contains two custom-built Odoo modules:

University Management Module — for managing student data with full CRUD functionality.

Helpdesk AI Enhancer — extending the Helpdesk app with AI-powered sentiment analysis and team suggestion.

1️⃣ University Management Module
📚 Purpose
The University Module is designed to manage student records with ease. It handles basic CRUD operations through the Odoo backend interface.

🔧 Features
Create, Read, Update, and Delete student records.

Each student record includes:

Name

Major

Year of Admission

Graduation Year

🧱 Model Fields
Field	Type	Description
name	Char	Student's full name
major	Selection	Chosen academic major
year	Integer	Year of admission
graduate_year	Integer	Expected or actual graduation

🖥 UI
Admins can manage students from a dedicated menu.

All fields are visible and editable in the form and list views.

🏗 Structure
markdown
Copy
Edit
university/
├── __init__.py
├── __manifest__.py
├── models/
│   └── student.py
└── views/
    └── student_views.xml
📦 Installation
Copy the module into your Odoo addons folder.

Update Apps list and install the module.

Access it from the main menu (University → Students).

2️⃣ Helpdesk AI Enhancer
🧠 Purpose
Enhances the default Odoo Helpdesk module by adding:

AI-driven Sentiment Analysis (via TextBlob)

Team Suggestion based on ticket descriptions

✅ Features
Sentiment (positive, neutral, negative) is calculated automatically and logged.

Suggested Team is chosen based on predefined keywords.

🧠 AI Logic
Keyword → Suggested Team Mapping:

Keywords	Suggested Team
buy, quote, pricing, order	Sales Team
bug, error, issue, technical	Technical Support
invoice, payment, refund, billing	Financial Team
customer, service, complaint, support	Customer Care

💬 Sentiment Logging
The sentiment is calculated using TextBlob and logged to the backend (visible in the PyCharm terminal or odoo.log file). It is not displayed in the UI to users.

bash
Copy
Edit
INFO odoo.models: [Sentiment] Analyzed: negative (polarity=-0.45)
INFO odoo.models: [Team Suggestion] Description: I want a refund
INFO odoo.models: [Team Suggestion] Matched keyword 'refund' → Financial Team
🧱 Structure
markdown
Copy
Edit
helpdesk_ai_enhancer/
├── __init__.py
├── __manifest__.py
├── models/
│   └── helpdesk_ticket.py
└── views/
    └── helpdesk_ticket_views.xml
📦 Installation
Install required Python lib:

bash
Copy
Edit
pip install textblob
python -m textblob.download_corpora
Add module to your Odoo addons path.

Restart Odoo and install via Apps.

🖼️ UI Integration
Suggested Team: appears below the Helpdesk Team field.

Sentiment: not shown in the UI; appears only in logs.


🧾 Requirements
Odoo 16+ (tested on Odoo 18)

Python 3.8+

textblob library

🛠 Developer Notes
Both modules are structured following Odoo best practices:

Separate models and views

Auto-processing logic in create() and write()

Logging replaces print() to avoid issues in deployment

📄 License
This project is released under the MIT License.

Would you like me to:

Include the sample __manifest__.py for both modules?

Add screenshots and a docs/ folder setup?

Generate GitHub tags or releases structure?

Let me know — we can make this super polished for your GitHub!

You said:
setup as a format I can copy and paste it
ChatGPT said:
Absolutely! Here's a fully formatted README.md file you can copy and paste directly into your GitHub repo:

markdown
Copy
Edit
# 🎓 Odoo Custom Modules by Ahmed Shousha

This repository includes two custom modules developed for Odoo:

1. **University Management Module** – CRUD management of student records  
2. **Helpdesk AI Enhancer** – Adds AI-powered sentiment analysis and team suggestion to Helpdesk

---

## 📘 1. University Management Module

### 🎯 Purpose

A custom Odoo module to manage student records with standard CRUD operations.

### 🧩 Features

- Manage student data from the backend.
- Fields:
  - `Name`
  - `Major`
  - `Year of Admission`
  - `Graduation Year`

### 🧱 Model Structure

| Field          | Type      | Description                    |
|----------------|-----------|--------------------------------|
| `name`         | Char      | Full name of the student       |
| `major`        | Selection | Chosen academic major          |
| `year`         | Integer   | Year of enrollment             |
| `graduate_year`| Integer   | Year of graduation (expected)  |

### 🖥️ UI

- Appears in Odoo menu under **University → Students**
- Editable list & form views

### 📁 File Structure

university/
├── init.py
├── manifest.py
├── models/
│ └── student.py
└── views/
└── student_views.xml

bash
Copy
Edit

### ⚙️ Installation

```bash
# Place module inside your Odoo custom addons path
# Then upgrade module list and install from Odoo UI
🤖 2. Helpdesk AI Enhancer
🎯 Purpose
This module enhances the Helpdesk app with:

Sentiment analysis (using TextBlob)

Automatic team suggestion based on ticket text

✨ Features
Logs sentiment score (positive, neutral, negative) in the terminal

Suggests a Helpdesk team using keyword detection

📌 AI Logic
Keyword Match (in description)	Suggested Team
buy, quote, pricing, order	Sales Team
bug, error, issue, technical	Technical Support
invoice, payment, refund, billing	Financial Team
customer, service, complaint, support	Customer Care

These keywords can be easily expanded or modified in the Python logic.

📋 Logging Output
Sentiment and suggested team are logged automatically on ticket creation or update:

yaml
Copy
Edit
INFO odoo.models: [Sentiment] Analyzed: negative (polarity=-0.65)
INFO odoo.models: [Team Suggestion] Matched keyword 'refund' → Financial Team
📁 File Structure
markdown
Copy
Edit
helpdesk_ai_enhancer/
├── __init__.py
├── __manifest__.py
├── models/
│   └── helpdesk_ticket.py
└── views/
    └── helpdesk_ticket_views.xml
🖥️ UI Integration
Suggested Team: shown below the Helpdesk Team field

Sentiment: not visible in the form view, only in logs

You can add a debug-only tab if you want to visualize it later.

📦 Setup & Requirements
bash
Copy
Edit
# Make sure these are installed:
pip install textblob
python -m textblob.download_corpora
Python 3.8+

Odoo 16 or 18

Logging output will appear in the terminal (or odoo.log)

🚀 Developer Tips
Sentiment is analyzed with TextBlob, which provides polarity scoring.

Keyword matching is done in plain Python, and can later be replaced by FastText or HuggingFace models.

Avoids UI clutter by only exposing necessary fields.

📄 License
Released under the MIT License.
