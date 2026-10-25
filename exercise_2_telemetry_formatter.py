"""
Exercise 2: Telemetry Formatter
--------------------------------
Practice parsing and formatting simulated sensor values into readable log lines.

Practice task for teammates:
1. Create a function that calculates average battery voltage.
2. Commit your change and submit a Pull Request.
"""

def format_telemetry_line(timestamp, position, roll_deg, pitch_deg, yaw_deg):
    x, y, z = position
    return (
        f"[{timestamp:07.2f}s] "
        f"Pos: ({x:+06.2f}, {y:+06.2f}, {z:+06.2f}) m | "
        f"Attitude: R={roll_deg:+05.1f} deg, P={pitch_deg:+05.1f} deg, Y={yaw_deg:+05.1f} deg"
    )

def main():
    print("=== Telemetry Log Formatter Practice ===")
    
    # Mock practice telemetry data (generic dummy readings)
    sample_records = [
        (0.00,  (0.0, 0.0, 0.0),   0.0, 0.0, 0.0),
        (2.50,  (0.1, 0.2, 0.05),  1.2, -0.5, 3.1),
        (5.00,  (0.3, 0.5, 0.12), -0.4, 0.8, 5.0),
        (7.50,  (0.6, 0.8, 0.15),  0.0, 0.2, 5.2),
        (10.00, (1.0, 1.0, 0.20),  0.1, -0.1, 5.0),
    ]
    
    for t, pos, r, p, y in sample_records:
        print(format_telemetry_line(t, pos, r, p, y))

if __name__ == "__main__":
    main()
