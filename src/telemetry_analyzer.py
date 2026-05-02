import csv
from collections import Counter
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "telemetry.csv"


def read_telemetry(file_path):
    telemetry_data = []

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            telemetry_data.append({
                "time": int(row["time"]),
                "battery": int(row["battery"]),
                "depth": float(row["depth"]),
                "speed": float(row["speed"]),
                "temperature": float(row["temperature"]),
                "status": row["status"]
            })

    return telemetry_data


def analyze_telemetry(data):
    max_depth = max(row["depth"] for row in data)
    max_speed = max(row["speed"] for row in data)
    min_battery = min(row["battery"] for row in data)
    average_speed = sum(row["speed"] for row in data) / len(data)
    status_counts = Counter(row["status"] for row in data)

    return {
        "max_depth": max_depth,
        "max_speed": max_speed,
        "min_battery": min_battery,
        "average_speed": average_speed,
        "status_counts": status_counts
    }


def print_report(results):
    print("Vehicle Telemetry Report")
    print("------------------------")
    print(f"Maximum depth: {results['max_depth']} m")
    print(f"Maximum speed: {results['max_speed']} m/s")
    print(f"Minimum battery level: {results['min_battery']}%")
    print(f"Average speed: {results['average_speed']:.2f} m/s")
    print()
    print("Status counts:")

    for status, count in results["status_counts"].items():
        print(f"- {status}: {count}")


def main():
    data = read_telemetry(DATA_FILE)
    results = analyze_telemetry(data)
    print_report(results)


if __name__ == "__main__":
    main()
