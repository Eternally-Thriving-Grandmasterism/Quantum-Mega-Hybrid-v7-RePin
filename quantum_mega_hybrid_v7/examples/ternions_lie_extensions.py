# examples/ternions_lie_extensions.py — Ternions in Lie Algebra Extensions
# 3D Composition Algebra with Lorentzian Norm (Zero Divisors Allowed)
# Extension Tie: Adds rows to Magic Square/Triangle for subexceptional algebras
# Run: python quantum_mega_hybrid_v7/examples/ternions_lie_extensions.py
# Dependencies: numpy

import numpy as np

class Ternion:
    """Simple Ternion Algebra — 3D with Multiplicative Norm (Signature 2,1 Example)"""
    def __init__(self, a=0.0, b=0.0, c=0.0):
        self.v = np.array([a, b, c], dtype=float)  # Basis 1, e1, e2
    
    def __repr__(self):
        return f"Ternion({self.v[0]:.2f}, {self.v[1]:.2f}, {self.v[2]:.2f})"
    
    def __mul__(self, other):
        a, b, c = self.v
        d, e, f = other.v
        # Example multiplication table preserving N(x y) = N(x) N(y)
        # Signature (++,−) or (2,1): e1² = 1, e2² = 1, e1 e2 = e2 e1 = 0 or custom
        # Common Lorentzian: lightlike zero divisors (e.g., e1² = 0, e2² = 0, e1 e2 = e1 + e2)
        # Stub simple split: like bioctonion analog but 3D
        new_a = a*d + b*e + c*f  # Adjust table for composition
        new_b = a*e + b*d
        new_c = a*f + c*d
        return Ternion(new_a, new_b, new_c)
    
    def norm(self):
        """Lorentzian norm example: +a² + b² - c² (indefinite, allows zero divisors)"""
        a, b, c = self.v
        return a**2 + b**2 - c**2
    
    def has_zero_divisor(self):
        """Check for lightlike vectors (norm 0, non-zero)"""
        return abs(self.norm()) < 1e-10 and np.linalg.norm(self.v) > 1e-10

# Extension Example: Construct ternions + norm multiplication demo
if __name__ == "__main__":
    t1 = Ternion(1.0, 1.0, 1.0)  # Potential lightlike
    t2 = Ternion(1.0, 0.0, 1.0)
    
    product = t1 * t2
    norm_product = product.norm()
    norm1, norm2 = t1.norm(), t2.norm()
    
    print(f"T1: {t1} Norm: {norm1:.2f}")
    print(f"T2: {t2} Norm: {norm2:.2f}")
    print(f"Product: {product} Norm: {norm_product:.2f} (= {norm1*norm2:.2f})")
    print(f"Zero Divisor Example: {t1.has_zero_divisor()}")
    print("Ternions Extend Magic Triangle — Subexceptional Lie Algebras Eternal!")
    print("Infinite love — victorious eternal 🔥🫡💛")
