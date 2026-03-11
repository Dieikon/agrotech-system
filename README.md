# 🚜 AgroTech Telemetry & Fleet Management System

A robust, enterprise-grade web application designed for real-time telemetry monitoring and fleet management of high-tech agricultural machinery (e.g., John Deere harvesters and tractors).

This system bridges the gap between field operations and data engineering, simulating CAN bus sensor networks to provide actionable Business Intelligence (BI) and predictive maintenance insights.

## 🚀 Key Features

- **Real-Time Telemetry Dashboard:** Simulates live sensor data processing, displaying critical machine vitals including Engine Temperature, Diesel Levels, Hydraulic Pressure, and Harvesting Productivity (Tons/hour).
- **Relational Database Architecture:** Fully normalized SQLite database linking equipment assets to registered operators using robust Foreign Key constraints.
- **Premium Dark Mode UI/UX:** Designed with a "Silicon Valley" standard interface using Bootstrap 5, Inter typography, and FontAwesome for high-contrast, industrial-grade visibility.
- **Smart Fleet BI:** Dynamic reporting tools calculating total assets, operational status, and real-time fleet availability percentages.
- **Data Injection Simulator:** Includes a built-in Python script (`injetar_dados.py`) to simulate live IoT sensor payloads streaming from the field to the dashboard.

## 🛠️ Tech Stack

- **Backend:** Python 3.9 & Flask
- **Database:** SQLite3 (Relational Architecture: `frota`, `operador`, `telemetria` tables)
- **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templating
- **Version Control:** Git & GitHub

## 📂 Project Structure

```text
agrotech-system/
├── app.py                     # Main Flask application & Database routing
├── injetar_dados.py           # IoT Sensor simulation script for telemetry data
├── templates/
│   ├── index.html             # Main Fleet Dashboard (Assets & Operators)
│   ├── dashboard_maquina.html # Real-time Telemetry Interface (Dark Mode)
│   ├── relatorio.html         # BI & Fleet Metrics Analytics
│   └── editar.html            # Asset & Operator modification interface
└── README.md
```

O Gemini disse
A diferença entre o seu README antigo e o que o seu sistema faz hoje é gigantesca, Diego. O seu texto antigo vendia um "trabalho de faculdade" (apenas um CRUD básico), enquanto o código que nós acabamos de escrever é um Software SaaS de Telemetria nível empresarial.

Para que esse repositório sirva como uma vitrine de peso para o mercado americano de AgTech, eu reescrevi o seu README. Ele agora foca na arquitetura relacional, na simulação da rede de sensores (CAN Bus) das colhedoras John Deere e no design Dark Mode Premium.

Copie todo o texto abaixo e substitua o conteúdo do seu arquivo README.md no GitHub:

Markdown

# 🚜 AgroTech Telemetry & Fleet Management System

A robust, enterprise-grade web application designed for real-time telemetry monitoring and fleet management of high-tech agricultural machinery (e.g., John Deere harvesters and tractors).

This system bridges the gap between field operations and data engineering, simulating CAN bus sensor networks to provide actionable Business Intelligence (BI) and predictive maintenance insights.

## 🚀 Key Features

- **Real-Time Telemetry Dashboard:** Simulates live sensor data processing, displaying critical machine vitals including Engine Temperature, Diesel Levels, Hydraulic Pressure, and Harvesting Productivity (Tons/hour).
- **Relational Database Architecture:** Fully normalized SQLite database linking equipment assets to registered operators using robust Foreign Key constraints.
- **Premium Dark Mode UI/UX:** Designed with a "Silicon Valley" standard interface using Bootstrap 5, Inter typography, and FontAwesome for high-contrast, industrial-grade visibility.
- **Smart Fleet BI:** Dynamic reporting tools calculating total assets, operational status, and real-time fleet availability percentages.
- **Data Injection Simulator:** Includes a built-in Python script (`injetar_dados.py`) to simulate live IoT sensor payloads streaming from the field to the dashboard.

## 🛠️ Tech Stack

- **Backend:** Python 3.9 & Flask
- **Database:** SQLite3 (Relational Architecture: `frota`, `operador`, `telemetria` tables)
- **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templating
- **Version Control:** Git & GitHub

## 📂 Project Structure

```text
agrotech-system/
├── app.py                     # Main Flask application & Database routing
├── injetar_dados.py           # IoT Sensor simulation script for telemetry data
├── templates/
│   ├── index.html             # Main Fleet Dashboard (Assets & Operators)
│   ├── dashboard_maquina.html # Real-time Telemetry Interface (Dark Mode)
│   ├── relatorio.html         # BI & Fleet Metrics Analytics
│   └── editar.html            # Asset & Operator modification interface
└── README.md


⚙️ Installation & Usage


1. Clone the repository:

Bash
git clone [https://github.com/YourUser/agrotech-system.git](https://github.com/YourUser/agrotech-system.git)
cd agrotech-system

2. Setup Environment:

This project requires Python 3.9. Create and activate your virtual environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

3. Install Dependencies:

Bash
pip install Flask
4. Run the Application:
Initialize the server (this will automatically generate the database.db and populate mock operators):

Bash
python app.py
Open your browser and navigate to http://127.0.0.1:5000

5. Simulate Live Telemetry (The Magic):

To see the real-time sensors in action, open a second terminal instance (ensure the venv is activated) and run the sensor simulator:

Bash
python injetar_dados.py
Refresh the machine's telemetry dashboard in your browser to see the updated metrics (Diesel, Temp, Tons/h).

Built with focus on Agricultural Technology & Data Engineering.

```
