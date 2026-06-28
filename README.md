# SageWire Location Service (LOC)

A lightweight REST API providing standardized GPS location stamping.

## Endpoints

GET /health

Returns service health.

POST /stamp

Accepts:

```json
{
  "latitude":40.12345,
  "longitude":-80.12345,
  "accuracy_m":5,
  "altitude_m":312,
  "heading":180,
  "speed_mps":0.5,
  "device_id":"headset001"
}
```

Returns a normalized location record with a UTC timestamp and Google Maps URL.

Runs on port 5003.
