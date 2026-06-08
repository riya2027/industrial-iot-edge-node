# Industrial IoT Edge Node

## Overview
Industrial edge monitoring system that simulates sensor data, performs local health diagnostics, detects faults, and logs telemetry data.

## Features

- Temperature monitoring
- Vibration monitoring
- Pressure monitoring
- Humidity monitoring
- Edge-based diagnostics
- Fault injection
- Telemetry logging
- Device uptime tracking
- Automated testing

## Architecture

Sensors
↓
Device Controller
↓
Health Monitor
↓
Alert Manager
↓
CSV Logger

## Run

python main.py

## Test

pytest