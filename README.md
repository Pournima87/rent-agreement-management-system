# 🏠 More Enterprises - Rent Agreement Management System

A complete cloud-based Rent Agreement Management System built for **More Enterprises** to automate the creation, management, and renewal of rent agreements.

The application generates professional Marathi Rent Agreement PDFs, Police NOC documents, manages customer records, tracks agreement expiry, and sends WhatsApp reminders.

---

# 🚀 Features

## 📄 Document Generation

- Automatic Rent Agreement PDF
- Automatic Police NOC PDF
- Marathi Unicode Support
- Professional PDF Formatting

---

## 👥 Customer Management

- Add New Customer
- Customer Search
- Customer Renewal
- Auto-fill Existing Customer Details
- Unique Customer ID

---

## ☁️ Cloud Database

- Supabase PostgreSQL
- Fast Customer Search
- Secure Cloud Storage
- Excel Backup

---

## 📊 Dashboard

- Total Customers
- Active Agreements
- Expiring Agreements
- Business Summary
- Greeting Dashboard

---

## 🔔 Reminder Center

- Agreements Expiring Soon
- WhatsApp Reminder
- Reminder Status Tracking
- Renewal Shortcut

---

## 📱 WhatsApp Integration

- One Click Reminder
- Marathi Reminder Message
- Opens WhatsApp Automatically

---

# 🛠 Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## Database

- Supabase PostgreSQL

## Backup

- Excel (OpenPyXL)

## PDF Generation

- PyMuPDF

## Voice Input

- SpeechRecognition
- streamlit-mic-recorder

---

# 📁 Project Structure

```
rent-agreement-system/

├── app.py

├── components/

├── database/

├── notifications/

├── pdf/

├── services/

├── templates/

├── utils/

├── views/

├── records/

├── fonts/

├── requirements.txt

└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rent-agreement-system.git
```

Move into the project

```bash
cd rent-agreement-system
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# 🔑 Environment Variables

Create

```
.streamlit/secrets.toml
```

Add

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"

SUPABASE_KEY="YOUR_SUPABASE_KEY"
```

---

# 📸 Screenshots

(Add dashboard, agreement page, reminder page and search page screenshots after deployment.)

---

# 🔮 Future Roadmap

- OCR Aadhaar Reader
- PAN Reader
- AI Auto Fill
- Marathi Voice Assistant
- Mobile App
- SMS Notifications
- Multi User Login
- Analytics Dashboard
- Digital Signature Support

---

# 👨‍💻 Developed By

**Pournima More**

Developed as a real-world business automation solution for **More Enterprises**.

---

# 📄 License

This project is licensed under the MIT License.