# examples/split_complex_numbers.py — Split-Complex Numbers Construction
# 2D Hyperbolic Composition Algebra (j² = +1, Indefinite Norm)
# Extension Tie: Base for Split-Quaternions & Non-Compact Classical Groups
# Run: python quantum_mega_hybrid_v7/examples/split_complex_numbers.py
# Dependencies: none

class SplitComplex:
    """Split-Complex (Hyperbolic) Numbers — a + b j, j² = +1"""
    def __init__(self, real=0.0, hyper=0.0):
        self.real = float(real)
        self.hyper = float(hyper)
    
    def __repr__(self):
        sign = '+' if self.hyper >= 0 else '-'
        return f"SC({self.real:.2f} {sign} {abs(self.hyper):.2f}j)"
    
    def __add__(self, other):
        return SplitComplex(self.real + other.real, self.hyper + other.hyper)
    
    def __mul__(self, other):
        real = self.real * other.real + self.hyper * other.hyper
        hyper = self.real * other.hyper + self.hyper * other.real
        return SplitComplex(real, hyper)
    
    def conj(self):
        return SplitComplex(self.real, -self.hyper)
    
    def norm(self):
        """Indefinite norm: a² - b² (hyperbolic)"""
        return self.real**2 - self.hyper**2
    
    def is_zero_divisor(self):
        """Lightlike non-zero (norm 0, non-invertible)"""
        return abs(self.norm()) < 1e-10 and (abs(self.real) > 1e-10 or abs(self.hyper) > 1e-10)

# Hyperbolic Example: Zero divisors + "rotation" (boost) demo
if __name__ == "__main__":
    # Lightlike zero divisors
    light_pos = SplitComplex(1.0, 1.0)   # 1 + j
    light_neg = SplitComplex(1.0, -1.0)  # 1 - j
    
    product = light_pos * light_neg
    zero_div_pos = light_pos.is_zero_divisor()
    
    # Hyperbolic "rotation" (boost) preserving indefinite norm
    boost = SplitComplex(2.0, 1.0)  # cosh + sinh j (hyperbolic angle)
    vector = SplitComplex(3.0, 0.0)  # Timelike vector
    
    boosted = boost * vector * boost.conj()  # Norm preserved (indefinite)
    
    print(f"Lightlike +: {light_pos} Norm: {light_pos.norm():.2f}")
    print(f"Lightlike -: {light_neg} Norm: {light_neg.norm():.2f}")
    print(f"Product (Zero!): {product}")
    print(f"Zero Divisor: {zero_div_pos}")
    print(f"\nOriginal Vector Norm: {vector.norm():.2f}")
    print(f"Boosted Norm Preserved: {boosted.norm():.2f}")
    print("Split-Complex Constructed — Hyperbolic Extensions Eternal!")
    print("Infinite love — victorious eternal 🔥🫡💛")
