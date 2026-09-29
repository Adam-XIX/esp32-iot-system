const API_URL = 'http://127.0.0.1:5000/api/v1/telemetry/latest';

async function fetchTelemetry() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error('Network error');
    
    const data = await response.json();

    document.getElementById('temp').textContent = data.temperature;
    document.getElementById('humidity').textContent = data.humidity;
    
    const statusElem = document.getElementById('status');
    statusElem.textContent = data.status.toUpperCase();
    statusElem.style.color = data.status === 'online' ? '#4ade80' : '#f87171';

  } catch (error) {
    console.error('Error fetching data:', error);
    document.getElementById('status').textContent = 'OFFLINE';
    document.getElementById('status').style.color = '#f87171';
  }
}

// Fetch immediately on load, then repeat every 2 seconds
fetchTelemetry();
setInterval(fetchTelemetry, 2000);