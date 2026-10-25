"""
Exercise 1: Hello Drone
-----------------------
A simple beginner Python script for practicing basic syntax,
dictionaries, and loops for robotics telemetry.

Practice task for teammates:
1. Add a new sensor to the 'subsystems' dictionary.
2. Commit your change and push to your branch.
"""

def main():
    print("=== Space Robotics Practice: System Init ===")
    
    drone_info = {
        "robot_id": "PRACTICE-DRONE-01",
        "mode": "SIMULATION_PRACTICE",
        "battery_pct": 98.5,
        "is_docked": True,
        "subsystems": {
            "imu": "ONLINE",
            "optical_camera": "ONLINE",
            "thruster_actuators": "READY",
            "telemetry_link": "CONNECTED"
        }
    }
    
    print(f"Robot ID: {drone_info['robot_id']}")
    print(f"Battery:  {drone_info['battery_pct']}%")
    print(f"Status:   {'Docked' if drone_info['is_docked'] else 'In Flight'}")
    print("\nSubsystem Health Check:")
    for sub, status in drone_info["subsystems"].items():
        print(f"  - {sub.ljust(20)}: [{status}]")
        
    print("\nAll practice subsystems initialized successfully.")

if __name__ == "__main__":
    main()
