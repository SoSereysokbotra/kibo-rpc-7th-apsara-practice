# kibo-rpc-7th-apsara-practice
## Team Apsara - 7th Kibo-RPC Practice Repository

Welcome to the **Team Apsara** practice repository for the **7th Kibo Robot Programming Challenge (7th Kibo-RPC)**.

## Purpose of this Repository
This repository is set up for team members to practice Git collaboration workflows, including:
- Cloning and pulling repository updates
- Creating feature branches (`git checkout -b feature/<name>`)
- Making clean, documented commits
- Pushing commits to GitHub (`git push origin <branch>`)
- Opening and reviewing Pull Requests (PRs)

---

## Practice Files Index

| File Name | Description |
| :--- | :--- |
| `practice_kibo_math.py` | 3D coordinate distance demo |
| `exercise_1_hello_drone.py` | Beginner robot health check script |
| `exercise_2_telemetry_formatter.py` | Log formatting exercise for mock sensor data |
| `exercise_3_coordinate_printer.py` | Waypoint inspector and 3D bounding box calculator |
| `test_practice.py` | Automated unit tests (`py -m unittest test_practice.py`) |
| `sample_config.json` | Sample JSON configuration for Git conflict practice |
| `mock_sensor_data.csv` | Mock telemetry data (voltage, temperature, status) |
| `CONTRIBUTING.md` | Team guide for branching, commits, and PRs |
| `git_cheatsheet.md` | Common Git commands quick reference card |

---

## Quick Kibo-RPC Reference

### Coordinate System (JAXA Int-Ball 2)
The Japanese Experiment Module (Kibo) on the International Space Station uses the following 3D coordinate system:
- **X-axis:** Along the length of the module (approx. 0.0m at Dock to 7.0m at aft end).
- **Y-axis:** Starboard (negative) to Port (positive).
- **Z-axis:** Deck / Nadir (negative) to Overhead / Zenith (positive).

### Key Flight Metrics
- **Max Translation Velocity:** 0.20 m/s (20 cm/s)
- **Max Angular Velocity:** 25.0 degrees/s
- **Accuracy Level 3 Thresholds:**
  - Position error: <= 10.0 cm (0.10 m)
  - Centering angle: <= 10.0 degrees
  - Attitude roll angle: <= 10.0 degrees
  - Stationary settle hold: >= 1.0 second

---

## Getting Started Practice Workflow
```bash
# 1. Check git status
git status

# 2. Create your own practice branch
git checkout -b practice/your-name

# 3. Add your changes
git add .

# 4. Commit with a clear message
git commit -m "docs: add practice notes for team onboarding"

# 5. Push to GitHub
git push -u origin practice/your-name
```
