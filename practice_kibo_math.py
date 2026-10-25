#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Team Apsara - 7th Kibo-RPC Practice Script
Demonstrates basic 3D distance and coordinate checks for Int-Ball 2 navigation.
"""

import math

def calculate_distance(pos1, pos2):
    """Calculate Euclidean distance between two 3D points in meters."""
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)

def check_level_3_position(target, actual):
    """Verify if drone arrival is within Level 3 position threshold (<= 10.0 cm)."""
    dist_m = calculate_distance(target, actual)
    dist_cm = dist_m * 100.0
    passed = dist_cm <= 10.0
    return passed, dist_cm

if __name__ == "__main__":
    dock = [0.21, 0.00, -0.02]
    checkpoint_1 = [1.41, -0.50, 0.69]
    actual_arrival = [1.415, -0.498, 0.692]

    hop_distance = calculate_distance(dock, checkpoint_1)
    is_l3, error_cm = check_level_3_position(checkpoint_1, actual_arrival)

    print("==================================================")
    print(" Team Apsara - Kibo-RPC Navigation Practice")
    print("==================================================")
    print(f"Dock to CP1 Distance : {hop_distance:.3f} meters")
    print(f"Arrival Error        : {error_cm:.2f} cm")
    print(f"Level 3 Qualified    : {'PASS [OK]' if is_l3 else 'FAIL'}")
    print("==================================================")
