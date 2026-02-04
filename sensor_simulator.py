import threading
import time
import random
import json
from datetime import datetime

class SensorDevice(threading.Thread):#SensorDevice class
    def __init__(self, device_id, data_queue):
        threading.Thread.__init__(self)
        self.device_id = device_id
        self.queue = data_queue
        self.running = True
        self.msg_id = 0

    def generate_data(self):#Generate data
        data = {
            "device_id": self.device_id,
            "temperature": round(random.uniform(60, 100), 2),#Random Temperature
            "vibration": round(random.uniform(2, 15), 2),#Random Vibration
            "voltage": round(random.uniform(150, 240), 2),#Random Voltage
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),#Timestamp
            "message_id": self.msg_id#Message ID
        }
        self.msg_id += 1
        return json.dumps(data)

    def run(self):
        while self.running:#Running
            data = self.generate_data()
            self.queue.put(data)
            time.sleep(random.randint(1, 2))

    def stop(self):
        self.running = False