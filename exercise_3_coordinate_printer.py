"""
Exercise 3: Coordinate Printer and Bounding Box
----------------------------------------------
Practice analyzing a set of 3D waypoints and computing their bounding box.

Practice task for teammates:
1. Add a function to find the waypoint farthest from the origin (0, 0, 0).
2. Commit your change with a clear commit message.
"""

def compute_bounding_box(waypoints):
    if not waypoints:
        return None
    xs = [p[0] for p in waypoints]
    ys = [p[1] for p in waypoints]
    zs = [p[2] for p in waypoints]
    return {
        "x_range": (min(xs), max(xs)),
        "y_range": (min(ys), max(ys)),
        "z_range": (min(zs), max(zs)),
    }

def main():
    print("=== Waypoint Bounding Box Calculator ===")
    
    # Sample practice waypoints (dummy values for practice only)
    dummy_waypoints = [
        (1.0, 2.0, 0.5),
        (2.5, 1.5, 0.8),
        (0.5, 3.0, 1.2),
        (3.0, 2.2, 0.4),
        (1.8, 0.8, 1.5)
    ]
    
    print(f"Total waypoints: {len(dummy_waypoints)}")
    for i, pt in enumerate(dummy_waypoints, start=1):
        print(f"  WP {i}: x={pt[0]:.2f}, y={pt[1]:.2f}, z={pt[2]:.2f}")
        
    bbox = compute_bounding_box(dummy_waypoints)
    print("\nBounding Box:")
    print(f"  X: [{bbox['x_range'][0]:.2f} to {bbox['x_range'][1]:.2f}]")
    print(f"  Y: [{bbox['y_range'][0]:.2f} to {bbox['y_range'][1]:.2f}]")
    print(f"  Z: [{bbox['z_range'][0]:.2f} to {bbox['z_range'][1]:.2f}]")

if __name__ == "__main__":
    main()
