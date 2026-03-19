# Python Port Scanner

This is a simple Python tool that checks which ports are opened on a target machine.

---

## What it does

This tool scans a target IP address or domain and checks which ports are open.

- OPEN port → a service is running on that port
- CLOSED port → no service is listening

---

## Features

- Fast multithreaded scanning
- Custom port range input
- Lightweight (no external libraries)
- Educational cybersecurity tool

---

## Vulnerablities

- Easy to block (Firewall can block repeated connections, blacklist your IP and trigger alerts)
- Not scalable for large networks
- Limited detection capability (It does not detect what service is running)

## How to run

Run the script:

```bash
python scanner.py
