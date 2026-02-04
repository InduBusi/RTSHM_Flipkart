
# 📡 Real-Time Sensor Data Stream Processor & Device Health Monitoring System

## 📌 Project Overview
This project is a Python-based real-time monitoring system that simulates live sensor data streams from multiple devices, processes them concurrently, detects anomalies, tracks device health, generates alerts, and produces daily reports.

It mimics real-world monitoring systems used in factories, warehouses, robotics, automation units, and logistics platforms.

---

## 🎯 Objectives
- Simulate real-time sensor data streams using multithreading
- Process incoming data continuously
- Detect abnormal sensor readings using thresholds
- Maintain device health statistics
- Generate alerts and logs automatically
- Store all sensor data persistently
- Produce daily summary reports

---

## 🧩 System Features

### 🔁 Sensor Stream Simulation
- Simulates 5 devices using multithreading
- Each device sends data every 1–2 seconds
- Data includes:
  - Temperature
  - Vibration
  - Voltage
  - Timestamp
  - Message ID

### ⚙️ Real-Time Data Processing
Threshold rules applied:
- Temperature > 85°C → Critical
- Vibration > 10.0 → Warning
- Voltage < 180 → Warning

### ❤️ Device Health Monitoring
Tracks:
- Device status
- Packets received
- Error count
- Uptime
- Last active timestamp

### 🚨 Alerts & Notifications
- Console alerts
- alerts.log for warnings
- critical_alerts.log for critical failures
- Email alert simulation via console output

### 💾 Data Storage
- SQLite database
- Stores raw data, status, alerts, and timestamps

### 📊 Reporting Module
- Auto-generated daily reports
- Output format:
  - report_<date>.txt

---

## 📁 Folder Structure
sensor_monitor/
│── sensors/
│   └── sensor_simulator.py
│── processor/
│   └── data_processor.py
│── storage/
│   └── database.py
│── reports/
│── logs/
│   ├── alerts.log
│   └── critical_alerts.log
│── main.py
│── README.md

---

## 🛠 Technologies Used
- Python 3.x
- threading
- queue
- sqlite3
- logging
- json
- datetime
- random

---

## ▶️ How to Run
python main.py

Press CTRL+C to stop execution safely.

---

## 🚀 Future Enhancements
- PDF report generation
- Web dashboard
- Email integration
- REST API support

---

## 👨‍💻 Author
Busi Indu
