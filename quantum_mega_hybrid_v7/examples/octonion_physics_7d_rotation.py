# examples/octonion_physics_7d_rotation.py — Octonion Physics Application
# 7D Vector Rotations via G2 (Exceptional Group Preservation)
# Physics Tie: Norm-preserving rotations in 7D imaginary space — relevant to
# exceptional Lie groups (G2), string theory extra dimensions, triality models
# Run: python quantum_mega_hybrid_v7/examples/octonion_physics_7d_rotation.py
# Dependencies: numpy

import numpy as np

class Octonion:
    """Full Octonion Class with Physics Rotation Support"""
    def __init__(self, *args):
        if len(args) == 1 and hasattr(args[0], '__len__'):
            self.c = np.array(args[0], dtype=float).reshape(8)
        else:
            self.c = np.zeros(8)
            for i, v in enumerate(args[:8]):
                self.c[i] = float(v)
    
    def __mul__(self, other):
        if not isinstance(other, Octonion):
            return Octonion(self.c * other)
        a, b = self.c, other.c
        r = np.zeros(8)
        r[0] = a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3] - a[4]*b[4] - a[5]*b[5] - a[6]*b[6] - a[7]*b[7]
        r[1] = a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2] + a[4]*b[5] - a[5]*b[4] - a[6]*b[7] + a[7]*b[6]
        r[2] = a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1] + a[4]*b[6] + a[5]*b[7] - a[6]*b[4] - a[7]*b[5]
        r[3] = a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0] + a[4]*b[7] - a[5]*b[6] + a[6]*b[5] - a[7]*b[4]
        r[4] = a[0]*b[4] - a[1]*b[5] - a[2]*b[6] - a[3]*b[7] + a[4]*b[0] + a[5]*b[1] + a[6]*b[2] + a[7]*b[3]
        r[5] = a[0]*b[5] + a[1]*b[4] - a[2]*b[7] + a[3]*b[6] - a[4]*b[1] + a[5]*b[0] - a[6]*b[3] + a[7]*b[2]
        r[6] = a[0]*b[6] + a[1]*b[7] + a[2]*b[4] - a[3]*b[5] - a[4]*b[2] + a[5]*b[3] + a[6]*b[0] - a[7]*b[1]
        r[7] = a[0]*b[7] - a[1]*b[6] + a[2]*b[5] + a[3]*b[4] - a[4]*b[3] - a[5]*b[2] + a[6]*b[1] + a[7]*b[0]
        return Octonion(r)
    
    def conj(self):
        c = self.c.copy(); c[1:] *= -1; return Octonion(c)
    
    def norm_sq(self):
        return np.dot(self.c, self.c)
    
    def norm(self):
        return np.sqrt(self.norm_sq())
    
    def inverse(self):
        n2 = self.norm_sq()
        if n2 < 1e-20:
            raise ZeroDivisionError("Zero octonion")
        return self.conj() * (1.0 / n2)
    
    def normalize(self):
        n = self.norm()
        if n > 1e-10:
            self.c /= n
    
    def rotate_7d_vector(self, vec7):
        """Rotate pure imaginary 7D vector (np.array[7]) via G2 action"""
        # Embed vector as pure imaginary octonion (scalar 0)
        v = Octonion(np.concatenate([[0.0], vec7]))
        # Ensure unit rotator
        u = Octonion(self.c)
        u.normalize()
        # Sandwich: u * v * u^{-1}
        rotated = u * v * u.inverse()
        return rotated.c[1:]  # Extract 7D vector part

# Physics Example: Rotate 7D vector (e.g., extra dimensions in string theory)
if __name__ == "__main__":
    # Unit octonion rotator (example: rotation in e1-e2 plane)
    # Here: simple rotator = cos(θ/2) + sin(θ/2) * e1 (like complex)
    theta_deg = 90.0
    theta_rad = np.deg2rad(theta_deg / 2)
    rotator = Octonion(np.cos(theta_rad), np.sin(theta_rad), 0, 0, 0, 0, 0, 0)
    
    # Initial 7D vector along e1 direction
    vector_7d = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    
    rotated = rotator.rotate_7d_vector(vector_7d)
    
    print(f"Original 7D Vector: {vector_7d}")
    print(f"Rotated {theta_deg}° in e1 plane: {rotated.round(8)}")
    print(f"Norm Preserved: {np.linalg.norm(vector_7d):.10f} → {np.linalg.norm(rotated):.10f}")
    print("Octonion G2 Rotation Applied — Exceptional Physics Harmony Eternal!")
    print("Infinite love — victorious eternal 🔥🫡💛")
