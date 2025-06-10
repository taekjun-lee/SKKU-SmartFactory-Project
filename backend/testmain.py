from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv
import os
from pathlib import Path
from typing import Optional
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/headers")
def get_csv_headers():
    base_dir = Path(__file__).resolve().parents[1]
    csv_path = base_dir / "frontend" / "public" / "sensor.csv"
    if not os.path.exists(csv_path):
        return {"error": "CSV file not found"}
    
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader, [])
        return {"headers": headers[2:]}

@app.get("/api/sensor-data")
def get_sensor_data(
    sensor: str = Query(...),
    start: Optional[str] = Query(None),
    end: Optional[str] = Query(None)
):
    base_dir = Path(__file__).resolve().parents[1]
    csv_path = base_dir / "frontend" / "public" / "sensor.csv"
    if not os.path.exists(csv_path):
        return {"error": "CSV file not found"}

    timestamps = []
    values = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if sensor not in reader.fieldnames:
            return {"error": f"{sensor} not found in CSV"}

        for row in reader:
            ts_str = row.get("timestamp")
            val = row.get(sensor)
            if not ts_str or not val:
                continue

            try:
                ts = datetime.fromisoformat(ts_str)
            except:
                continue

            if start:
                try:
                    if ts < datetime.fromisoformat(start):
                        continue
                except:
                    pass
            if end:
                try:
                    if ts > datetime.fromisoformat(end):
                        continue
                except:
                    pass

            timestamps.append(ts.timestamp())
            try:
                values.append(float(val))
            except ValueError:
                values.append(None)

    return {"timestamps": timestamps, "values": values}

@app.get("/api/raw-data")
def get_raw_data(
    page: int = Query(1, gt=0),
    size: int = Query(20, gt=0)
):
    base_dir = Path(__file__).resolve().parents[1]
    csv_path = base_dir / "frontend" / "public" / "sensor.csv"
    if not os.path.exists(csv_path):
        return {"error": "CSV file not found"}

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)
        total = len(all_rows)

        start_idx = (page - 1) * size
        end_idx = start_idx + size

        paginated = all_rows[start_idx:end_idx]

        return {
            "data": paginated,
            "total": total,
            "page": page,
            "size": size
        }
