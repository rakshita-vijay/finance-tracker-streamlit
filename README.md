# 💸 Finance Tracker Streamlit

A privacy-first, AI-powered personal finance tracker - **no terminal needed!**
Just open [the app](https://finance-tracker-analyser.streamlit.app/) and start managing your money, your way.

---

## 🌟 Highlights

- **True user isolation:** Each user gets their own private folder and files - no one else can see or change your data.
- **No installation, no terminal:** Everything runs in the browser.
- **AI-powered reports:** Get actionable insights and strategy recommendations.
- **Instant downloads:** Export your data as CSV, TXT, PDF, Markdown, or ZIP.
- **Modern UI:** Built with Streamlit, with a clean sidebar menu and custom theme.
- **Automatic GitHub backup:** All changes are pushed to the repo for transparency.

---

## ✨ Features

- **🔐 User Authentication**
  - Register/login with username and password.
  - Each user’s data is stored in a private folder with username-prefixed files.
- **🧾 Add Transactions**
  - Log expenses/income with all details.
  - Each transaction is stored in your own CSV file.
- **📊 View Spending**
  - See only your own transaction history.
  - Table view with all relevant columns.
- **💰 Change Budget**
  - Set or update monthly and yearly budgets.
  - App warns if you’re overspending and suggests strategies.
- **📝 Generate AI Reports**
  - One-click, AI-generated financial insights and strategy reports.
  - Download as Markdown or PDF.
- **⬇️ Download Your Data**
  - Export your data in multiple formats - always user-specific.
- **🗑️ Wipe Transactions**
  - Clear your own data (with password confirmation).
- **🧹 Cleanup**
  - Remove temporary files and caches.

---

## 🛠️ How It Works

- **Per-User Data Storage**
  - Each user gets a folder in `saved_files/` named after their username.
  - All files are named like `{username}_csv_transactions.csv`, `{username}_budgets.txt`, etc.
- **Automatic File Management**
  - On registration/login, all required files are created if missing (with sensible defaults).
  - If you delete your files, they’re recreated on your next login.
- **No Data Leaks**
  - Every file read/write uses your own folder and file.
  - No global/shared files - guaranteed by code and repo structure.
- **GitHub Integration**
  - All changes are pushed to the repo for transparency and backup.

---

## 🗂️ Repo Structure

```text
finance-tracker-streamlit/
│
├── .devcontainer/                 # VSCode dev container config
│   └── devcontainer.json
├── .streamlit/                    # Streamlit app config (theme, sidebar)
│   └── config.toml
│
├── crewai_toolkits_gem_3point5_flash/ # AI report generation logic
│   ├── generate_report_from_csv.py
│   ├── transform_csv_to_md_table.py
│   └── __init__.py
│
├── file_methods/                  # All file and data handling logic
│   ├── budget_methods.py          # Budget file logic
│   ├── csv_file_methods.py        # CSV (transactions) logic
│   ├── md_file_methods.py         # Markdown report logic
│   ├── pdf_file_methods.py        # PDF creation logic
│   ├── txt_file_methods.py        # ASCII table logic
│   └── user_file_utils.py         # Per-user file path helpers
│
├── pages/                         # Streamlit multipage app pages
│   ├── m_Main_Menu.py             # Main menu page
│   ├── p0_Authentication.py       # Login/register page
│   ├── p1_Add_Transactions.py     # Add transactions
│   ├── p2_View_Spending.py        # View transactions
│   ├── p3_Generate_Report.py      # AI report page
│   ├── p4_Change_Budget.py        # Change budget
│   ├── p5_Download_Files.py       # Download files
│   ├── p6_Wipe_Transactions.py    # Wipe transactions
│   └── p7_Cleanup.py              # Cleanup temp files
│
├── saved_files/                   # All user data (DO NOT DELETE)
│   ├── user_credentials.txt       # Usernames and passwords
│   └── {username}/                # One folder per user
│       ├── {username}_csv_transactions.csv
│       ├── {username}_ascii_table_of_transactions.txt
│       ├── {username}_pdf_of_transactions.pdf
│       ├── {username}_md_report.md
│       └── {username}_budgets.txt
│
├── utils/                         # GitHub push helpers
│   ├── git_utils.py
│   └── __init__.py
│
├── Main_Menu.py                   # Main entrypoint (redirects to m_Main_Menu)
├── download_to_device.py          # Download logic for files
├── requirements.txt               # Python package requirements
├── runtime.txt                    # Python version for deployment
└── README.md                      # This file!
```

---

## ⚙️ Tech Stack

- Python 3.11+
- Streamlit for UI and app logic
- GitPython for GitHub integration
- FPDF, PrettyTable, CrewAI for reports and table formatting
- No terminal needed for users!

---

## 📝 Known Quirks & Tips

- Do not delete your user folder or files manually!
  - If you do, just log in again - the app will recreate everything for you.
- Passwords are stored in plain text (for demo simplicity).
  - Do not reuse sensitive passwords.
- If you see someone else’s data:
  - Make sure you’re logged in as the right user.
  - If the problem persists, open an issue on GitHub.
- Session state:
  - Each browser tab/session is isolated.
  - If you log out or clear cookies, you’ll need to log in again.

---

## 🤝 Credits & License

- Project by [rakshita-vijay](https://github.com/rakshita-vijay)
- Inspired by the need for simple, private, AI-powered personal finance tools.
- License: MIT

---

## 🚀 Get Started Now

- **Open the app:** [finance-tracker-analyser.streamlit.app](https://finance-tracker-analyser.streamlit.app/)
- **Demo login:**
  - Username: `demo`
  - Password: `demo_password_123_not_secure`
- No installation or terminal required!

---

*Last updated: July 2025*
