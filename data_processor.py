import json #JSON module
import logging #Logging module
from datetime import datetime #Datetime module
import os #OS module

class DataProcessor:#DataProcessor class
    def __init__(self, db):
        self.db = db
        self.device_stats = {}

        # Get the path to the project root folder
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logs_dir = os.path.join(project_root, "logs")
        
        # Create logs directory if it doesn't exist
        os.makedirs(logs_dir, exist_ok=True)

        alerts_log_path = os.path.join(logs_dir, "alerts.log")
        critical_log_path = os.path.join(logs_dir, "critical_alerts.log")

        logging.basicConfig(
            filename=alerts_log_path,#Logging file
            level=logging.WARNING,
            format="%(asctime)s - %(message)s"
        )

        self.critical_logger = logging.getLogger("critical")#Critical logger
        handler = logging.FileHandler(critical_log_path)
        self.critical_logger.addHandler(handler)

    def process(self, raw_data):
        data = json.loads(raw_data)

        device = data["device_id"]#Device ID

        if device not in self.device_stats:
            self.device_stats[device] = {
                "packets": 0,
                "errors": 0,
                "start_time": datetime.now(),
                "last_active": None
            }

        self.device_stats[device]["packets"] += 1
        self.device_stats[device]["last_active"] = datetime.now()

        status = "Good"#Status
        alert_type = "None"#Alert type

        if data["temperature"] > 85:#Temperature
            status = "Critical"#Status
            alert_type = "High Temperature"#Alert type

        elif data["vibration"] > 10:#Vibration
            status = "Warning"#Status
            alert_type = "High Vibration"#Alert type

        elif data["voltage"] < 180:#Voltage
            status = "Warning"#Status
            alert_type = "Low Voltage"#Alert type

        if status == "Warning":#Warning
            logging.warning(f"{device} - {alert_type}")
            print(f"[WARNING] {device}: {alert_type}")
            print("EMAIL: Warning alert sent to admin")

        if status == "Critical":#Critical
            self.critical_logger.critical(f"{device} - {alert_type}")
            print(f"[CRITICAL] {device}: {alert_type}")
            print("EMAIL: CRITICAL alert sent to admin")
            self.device_stats[device]["errors"] += 1

        data["status"] = status#Status
        data["alert_type"] = alert_type#Alert type

        self.db.insert(data)
        return data