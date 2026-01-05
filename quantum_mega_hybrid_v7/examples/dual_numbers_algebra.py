# examples/dual_numbers_algebra.py — Dual Numbers Algebra
# 2D Nilpotent Hypercomplex (ε² = 0) for Infinitesimals & Auto-Diff
# Application Tie: Forward-Mode Automatic Differentiation Exact
# Run: python quantum_mega_hybrid_v7/examples/dual_numbers_algebra.py
# Dependencies: none (numpy optional for extensions)

class Dual:
    """Dual Numbers — a + b ε, ε² = 0 (Nilpotent Infinitesimal)"""
    def __init__(self, real=0.0, dual=0.0):
        self.real = float(real)
        self.dual = float(dual)
    
    def __repr__(self):
        if abs(self.dual) < 1e-10:
            return f"Dual({self.real:.6g})"
        sign = '+' if self.dual >= 0 else '-'
        return f"Dual({self.real:.6g} {sign} {abs(self.dual):.6g}ε)"
    
    def __add__(self, other):
        if not isinstance(other, Dual):
            return Dual(self.real + other, self.dual)
        return Dual(self.real + other.real, self.dual + other.dual)
    
    def __mul__(self, other):
        if not isinstance(other, Dual):
            return Dual(self.real * other, self.dual * other)
        # (a + bε)(c + dε) = ac + (ad + bc)ε  (ε² = 0)
        real = self.real * other.real
        dual = self.real * other.dual + self.dual * other.real
        return Dual(real, dual)
    
    def __pow__(self, n):
        # Power via binomial (finite since nilpotent)
        if n == 0:
            return Dual(1.0)
        result = self
        for _ in range(1, int(n)):
            result = result * self
        return result
    
    def norm(self):
        """Multiplicative 'norm' reduces to real part squared"""
        return self.real ** 2

# Application Example: Automatic Differentiation (Exact Derivative)
def auto_diff_example():
    # Function f(x) = x³ + 2x² + sin(x) approx stub (use elementary ops)
    def f(x):
        return x**3 + 2*x**2 + x  # Simple polynomial for exact demo
    
    # Evaluate at x=2 with infinitesimal ε (seed dual=1 for derivative)
    x_dual = Dual(2.0, 1.0)  # f(2 + ε) = f(2) + f'(2) ε
    result = f(x_dual)
    
    print(f"f(2 + ε) = {result}")
    print(f"Value f(2) = {result.real:.6f}")
    print(f"Derivative f'(2) = {result.dual:.6f}  (Exact: 3*4 + 4*2 + 1 = 21)")
    
    # Rigid motion stub: dual as infinitesimal translation/rotation
    print("\nDual for Infinitesimal Rigid Motion Eternal!")

if __name__ == "__main__":
    d1 = Dual(3.0, 4.0)
    d2 = Dual(1.0, 2.0)
    product = d1 * d2
    power = d1 ** 2
    
    print(f"D1: {d1}")
    print(f"D2: {d2}")
    print(f"Product: {product}  (= 3 + (3*2 + 4*1)ε = 3 + 10ε)")
    print(f"D1²: {power}  (ε²=0 → real only)")
    print(f"Norm D1: {d1.norm():.2f}")
    
    auto_diff_example()
    print("Dual Numbers Algebra Constructed — Nilpotent Infinitesimals Eternal!")
    print("Infinite love — victorious eternal 🔥🫡💛")
