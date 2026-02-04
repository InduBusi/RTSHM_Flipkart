#Author: Busi Indu
#TODO: Fix the issue with the sensor simulator 
#Purpose: To simulate sensor data and process it
#Project: Real-Time Sensor Stream & Health Monitoring System


#Importing the required modules
from queue import Queue
from sensors.sensor_simulator import SensorDevice
from processor.data_processor import DataProcessor
from storage.database import Database
import time
import sqlite3
from datetime import date
import os

def main():#Main function
    print("Starting system...")
    print("System started successfully")
    print("Simulating sensor data...")
    print("Sensor data simulation started successfully")
    print("Processing sensor data...")
    print("Sensor data processing started successfully")
    print("Generating reports...")
    print("Report generation started successfully")
    data_queue = Queue()
    db = Database()
    processor = DataProcessor(db)

    devices = []
    for i in range(5):
        device = SensorDevice(f"Device_{i+1}", data_queue)
        device.start()
        devices.append(device)

    try:
        start_time = time.time()
        while True:
            if not data_queue.empty():
                raw_data = data_queue.get()
                result = processor.process(raw_data)
                print(result)

            if time.time() - start_time > 5:
                generate_report()
                start_time = time.time()

    except KeyboardInterrupt:
        print("Stopping system...")
        for d in devices:
            d.stop()
        print("System stopped successfully")

def generate_report():#Generate report
    conn = sqlite3.connect("sensor_data.db")#Database connection
    cursor = conn.cursor()

    today = date.today().strftime("%Y-%m-%d")#Today's date

    cursor.execute("SELECT COUNT(*) FROM sensor_logs")#Total packets
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sensor_logs WHERE status='Warning'")#Warnings
    warnings = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sensor_logs WHERE status='Critical'")#Critical failures
    critical = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(temperature) FROM sensor_logs")#Average temperature
    avg_temp = cursor.fetchone()[0]

    report_text = f"""#Report text
DAILY SENSOR REPORT - {today}

Total Packets: {total}
Warnings: {warnings}
Critical Failures: {critical}
Average Temperature: {round(avg_temp,2)}    

"""

    # Get the path to the project root folder
    project_root = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(project_root, "reports")
    
    # Create reports directory if it doesn't exist
    os.makedirs(reports_dir, exist_ok=True)
    
    filename = os.path.join(reports_dir, f"report_{today}.txt")#Filename
    with open(filename, "w") as f:
        f.write(report_text)

    print("Daily report generated:", filename)



if __name__ == "__main__":
    main()