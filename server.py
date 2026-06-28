from flask import Flask, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "service": "sagewire-loc-service",
        "status": "ok",
        "version": "1.0"
    })

@app.route("/stamp", methods=["POST"])
def stamp():

    data = request.get_json(force=True)

    return jsonify({
        "status": "ok",
        "service": "sagewire-loc-service",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),

        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),

        "accuracy_m": data.get("accuracy_m"),
        "altitude_m": data.get("altitude_m"),

        "heading": data.get("heading"),
        "speed_mps": data.get("speed_mps"),

        "device_id": data.get("device_id"),

        "google_maps":
            f"https://maps.google.com/?q={data.get('latitude')},{data.get('longitude')}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
