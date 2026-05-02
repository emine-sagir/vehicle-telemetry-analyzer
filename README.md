# Vehicle Telemetry Analyzer

A small Python project that analyzes simulated vehicle telemetry data and generates a basic status report.

This project is designed as an academic/portfolio exercise to practice Python, CSV file handling, basic data analysis, and software organization in a vehicle-oriented context.

## Project Overview

The program reads simulated telemetry data from a CSV file and calculates:

- maximum depth
- maximum speed
- minimum battery level
- average speed
- system status counts

The sample dataset represents basic telemetry values from a vehicle system, such as battery level, depth, speed, temperature, and status messages.

## Repository Structure

```text
vehicle-telemetry-analyzer/
├── data/
│   └── telemetry.csv
├── src/
│   └── telemetry_analyzer.py
└── README.md
```

## Sample Data

The input CSV file contains the following columns:

- time
- battery
- depth
- speed
- temperature
- status

Example status values:

- OK
- LOW_BATTERY
- CRITICAL_BATTERY
