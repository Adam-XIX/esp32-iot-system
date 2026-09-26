from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows your HTML frontend to communicate with this API

# In-memory database for latest sensor values
latest_telemetry = {
    "temperature": 24.0,
    "humidity": 50.0,
    "status": "online",
    "device_id": "esp32-sim-01"
}

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "running", "system": "ESP32 IoT API"}), 200

@app.route('/api/v1/telemetry/latest', methods=['GET'])
def get_telemetry():
    """Frontend calls this endpoint to get live measurements"""
    return jsonify(latest_telemetry), 200

@app.route('/api/v1/telemetry', methods=['POST'])
def receive_telemetry():
    """ESP32 / Wokwi calls this endpoint to post new sensor data"""
    global latest_telemetry
    data = request.get_json()
    
    if not data or 'temperature' not in data or 'humidity' not in data:
        return jsonify({"error": "Invalid payload format"}), 400
    
    latest_telemetry['temperature'] = float(data['temperature'])
    latest_telemetry['humidity'] = float(data['humidity'])
    
    print(f"NEW TELEMETRY RECEVIED -> Temp: {latest_telemetry['temperature']}°C | Humidity: {latest_telemetry['humidity']}%")
    return jsonify({"message": "Data updated successfully", "current": latest_telemetry}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)