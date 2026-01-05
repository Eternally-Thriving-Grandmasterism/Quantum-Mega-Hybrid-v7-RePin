# examples/quaternion_linear_layer.py — Emerging Hypercomplex ML Application
# Quaternion-Valued Linear Layer (Reduced Parameters for Image/Signal Processing)
# Run: python quantum_mega_hybrid_v7/examples/quaternion_linear_layer.py
# Dependencies: torch
# Use: Efficient hypercomplex neural nets (e.g., color image processing with 4 channels)

import torch
import torch.nn as nn

class QuaternionLinear(nn.Module):
    """Simple Quaternion Linear Layer — Hamilton Product for Parameter Efficiency"""
    def __init__(self, in_features, out_features):
        super().__init__()
        # Weights as 4 real components (r, i, j, k)
        self.weight = nn.Parameter(torch.randn(out_features, in_features, 4) * 0.01)
        self.bias = nn.Parameter(torch.zeros(out_features, 4))
    
    def hamilton_product(self, a, b):
        """Hamilton product for two quaternion tensors (batch, features, 4)"""
        ar, ai, aj, ak = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
        br, bi, bj, bk = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
        out_r = ar*br - ai*bi - aj*bj - ak*bk
        out_i = ar*bi + ai*br + aj*bk - ak*bj
        out_j = ar*bj - ai*bk + aj*br + ak*bi
        out_k = ar*bk + ai*bj - aj*bi + ak*br
        return torch.stack([out_r, out_i, out_j, out_k], dim=-1)
    
    def forward(self, x):
        # x: (batch, in_features, 4) quaternion input
        # Weight: (out_features, in_features, 4) — broadcast over batch
        weight_expanded = self.weight.unsqueeze(0)  # (1, out, in, 4)
        output = self.hamilton_product(x.unsqueeze(1), weight_expanded).sum(dim=2)  # (batch, out, 4)
        return output + self.bias

# Practical Example: Tiny quaternion forward pass
if __name__ == "__main__":
    layer = QuaternionLinear(4, 2)  # 4 quaternion inputs → 2 outputs (real weights: 2*4*4 = 32 vs 128)
    input_q = torch.randn(1, 4, 4)   # Batch 1, 4 features, quaternion
    output = layer(input_q)
    print(f"Input shape: {input_q.shape}")
    print(f"Output shape: {output.shape}")
    print("Quaternion Linear Applied — Hypercomplex ML Efficiency Eternal!")
    print("Infinite love — victorious eternal 🔥🫡💛")
