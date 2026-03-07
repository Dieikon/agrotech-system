🚜 AgroTech Monitor - Agricultural Fleet Management
A robust web-based solution designed for real-time monitoring and Business Intelligence (BI) of high-tech agricultural machinery. This system streamlines fleet maintenance and operational availability, specifically tailored for John Deere equipment.

📺 Live Demo

🚀 Key Features

Inventory & Data Persistence: Complete CRUD (Create, Read, Update, Delete) functionality for fleet management, powered by a local SQLite database to ensure data integrity.

Maintenance Intelligence: Automated status logic that triggers "Maintenance Required" alerts once a machine surpasses 600 operational hours.

BI Dashboard: A dedicated reporting page that calculates real-time metrics, including Total Assets, Critical Alerts, and Fleet Availability Percentage.

Smart Search: Optimized JavaScript-based filtering system allowing users to find specific equipment by Model or Fleet Number instantly.

🛠️ Tech Stack
Backend: Python 3.11 & Flask

Database: SQLite3 (Relational Database)

Frontend: HTML5, CSS3 (Responsive Design), and Vanilla JavaScript

Version Control: Git & GitHub

📂 Project Structure
Plaintext
agrotech-system/
├── app.py # Main Flask application & Database logic
├── database.db # SQLite database file (Persistent Storage)
├── static/
│ ├── style.css # Custom UI/UX styling
│ └── script.js # Real-time search filter logic
├── templates/
│ ├── index.html # Main Dashboard
│ ├── relatorio.html # BI & Metrics page
│ └── editar.html # Asset modification interface
└── img/
└── demo.gif # System demonstration

⚙️ Installation & Usage:

1 Clone the repository:

Bash
git clone https://github.com/YourUser/agrotech-system.git

2 Setup Environment:
Ensure you are using Python 3.9. Create and activate your virtual environment.

3 Run the application:

Bash
python app.py

4 Access the system:
Open your browser and go to http://127.0.0.1:5000
