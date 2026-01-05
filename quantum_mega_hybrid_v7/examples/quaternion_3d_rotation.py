# examples/quaternion_3d_rotation.py — Practical Quaternion Application
# 4D Hypercomplex for Gimbal-Lock-Free 3D Rotations (Space Habitats/Drones/Robotics)
# Run: python quantum_mega_hybrid_v7/examples/quaternion_3d_rotation.py
# Dependencies: numpy
# Use: Orient geodesic domes/orbital modules in Venus/Mars transfers mercy-seeded

import numpy as np

class Quaternion:
    """Simple Quaternion Class for Rotation Applications"""
    def __init__(self, w=1.0, x=0.0, y=0.0, z=0.0):
        self.q = np.array([w, x, y, z], dtype=float)
    
    @staticmethod
    def from_axis_angle(axis, angle_deg):
        """Create rotation quaternion from axis (np.array 3D) and angle (degrees)"""
        angle_rad = np.deg2rad(angle_deg / 2)
        axis = axis / np.linalg.norm(axis)
        w = np.cos(angle_rad)
        xyz = np.sin(angle_rad) * axis
        return Quaternion(w, *xyz)
    
    def multiply(self, other):
        w1, x1, y1, z1 = self.q
        w2, x2, y2, z2 = other.q
        w = w1*w2 - x1*x2 - y1*y2 - z1*z2
        x = w1*x2 + x1*w2 + y1*z2 - z1*y2
        y = w1*y2 - x1*z2 + y1*w2 + z1*x2
        z = w1*z2 + x1*y2 - y1*x2 + z1*w2
        return Quaternion(w, x, y, z)
    
    def rotate_vector(self, v):
        """Rotate 3D vector v (np.array) using this quaternion"""
        v_q = Quaternion(0, *v)
        result = self.multiply(v_q).multiply(self.conjugate())
        return result.q[1:]
    
    def conjugate(self):
        return Quaternion(self.q[0], *-self.q[1:])
    
    def norm(self):
        return np.linalg.norm(self.q)
    
    def normalize(self):
        n = self.norm()
        if n > 0:
            self.q /= n

# Practical Example: Rotate habitat module 90° around Z-axis (Mars surface orientation)
if __name__ == "__main__":
    # Initial vector: pointing along X-axis (e.g., solar panel direction)
    vector = np.array([1.0, 0.0, 0.0])
    
    # Rotation: 90 degrees around upward Z-axis
    rot_q = Quaternion.from_axis_angle(np.array([0, 0, 1]), 90)
    rot_q.normalize()
    
    rotated = rot_q.rotate_vector(vector)
    
    print(f"Original Vector: {vector}")
    print(f"Rotated 90° around Z: {rotated.round(6)}  # Should be [0, 1, 0]")
    print("Quaternion Rotation Applied — Symbiotic Space Habitat Oriented Eternal!")
    print("Infinite love — victorious eternal 🔥🫡💛")
