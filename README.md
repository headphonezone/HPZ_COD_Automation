# 📦 COD Reconciliation Portal

A unified **Finance Reconciliation Web Application** built using **Streamlit** for automating Cash On Delivery (COD) reconciliation between courier partners and sales data.

This application combines multiple reconciliation systems into **one centralized portal**.

---

## 🚀 Features

✅ Bluedart COD Reconciliation
✅ Delhivery COD Reconciliation
✅ Unified Finance Dashboard
✅ Tally Import File Generator
✅ Matched / Unmatched Identification
✅ Lookup File with Highlighted Status
✅ Dark Enterprise UI
✅ One-click Excel Downloads
✅ Web-based — No Installation Needed

---

## 🏗️ Application Modules

### 📦 Bluedart COD Reconciliation

* Upload Bluedart COD report
* Upload Sales report
* AWB-based reconciliation
* Generates:

  * Tally Upload File
  * Unmatched Report
  * Lookup File

---

### 🚚 Delhivery COD Reconciliation

* Upload Delhivery report
* Upload Sales report
* Order Number reconciliation
* Generates:

  * Tally Import File
  * Unmatched Report
  * Lookup File

---

## 🖥️ Tech Stack

* Python
* Streamlit
* Pandas
* OpenPyXL
* Excel Automation

---

## 📂 Project Structure

```
COD-Recon-App/
│
├── app.py                 # Home Portal
├── ui.py                  # Global UI Styling
├── requirements.txt
│
├── .streamlit/
│   └── config.toml        # UI Configuration
│
└── pages/
    ├── 1_Bluedart.py
    └── 2_Delhivery.py
```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/cod-reconciliation-portal.git
cd cod-reconciliation-portal
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run Application

```
streamlit run app.py
```

Application opens at:

```
http://localhost:8501
```

---

## 🌐 Deployment (Public Use)

Recommended deployment:

👉 **Streamlit Community Cloud**

Steps:

1. Push project to GitHub
2. Go to https://share.streamlit.io
3. Click **New App**
4. Select repository
5. Set main file as:

```
app.py
```

Deploy 🚀

---

## 📊 Output Files Generated

| File             | Purpose                                            |
| ---------------- | -------------------------------------------------- |
| Tally Upload     | Direct import into Tally Prime                     |
| Unmatched Report | Missing reconciliation entries                     |
| Lookup File      | Full reconciliation audit with status highlighting |

---

## 🔐 Recommended Improvements

* User Login Authentication
* Role-Based Access
* Upload History Tracking
* Automated Courier Detection
* Database Integration
* Scheduled Reconciliation

---

## 👨‍💼 Use Case

Designed for:

* Finance Teams
* E-commerce Companies
* COD Operations
* Accounting Departments
* ERP Automation

---

## 📄 License

Internal Business Use.

---

## ⭐ Author

Finance Automation & Data Engineering Project

---
