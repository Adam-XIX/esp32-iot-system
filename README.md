# ESP32 IoT Monitoring System

Real-time IoT telemetry system built with an ESP32 (Wokwi / MicroPython), a Flask REST API backend, and a vanilla JavaScript live dashboard.

## Project Architecture
- **ESP32 (MicroPython / Wokwi):** Reads DHT22 sensor data (Temperature & Humidity) and POSTs JSON payloads to the Flask API.
- **Backend (Flask):** Exposes REST API endpoints for receiving telemetry and serving the latest device state.
- **Frontend (HTML/CSS/JS):** Polls the Flask API and updates UI elements in real time.

## Quick Start

### 1. Run the Flask Backend
```bash
pip install -r requirements.txt
python app.py
