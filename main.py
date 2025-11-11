"""
FLAM R&D / AI Assignment
Author: Raghavendra
Objective: Estimate θ, M, X in a parametric curve equation using L1 distance minimization.
"""

import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# ------------------------------
# Step 1: Load Data
# ------------------------------
data = pd.read_csv("xy_data.csv")
x_data = data['x'].values
y_data = data['y'].values
t_data = np.linspace(6, 60, len(data))

# ------------------------------
# Step 2: Define Model
# ------------------------------
def curve_model(t, theta, M, X):
    x = t*np.cos(theta) - np.exp(M*np.abs(t))*np.sin(0.3*t)*np.sin(theta) + X
    y = 42 + t*np.sin(theta) + np.exp(M*np.abs(t))*np.sin(0.3*t)*np.cos(theta)
    return x, y

# ------------------------------
# Step 3: Define L1 Loss
# ------------------------------
def loss(params, t, x_data, y_data):
    theta, M, X = params
    x_pred, y_pred = curve_model(t, theta, M, X)
    return np.sum(np.abs(x_data - x_pred) + np.abs(y_data - y_pred))

# ------------------------------
# Step 4: Optimization
# ------------------------------
bounds = [(0, np.deg2rad(50)), (-0.05, 0.05), (0, 100)]
initial_guess = [np.deg2rad(25), 0, 50]

result = minimize(
    loss,
    initial_guess,
    args=(t_data, x_data, y_data),
    bounds=bounds,
    method='L-BFGS-B'
)

theta_opt, M_opt, X_opt = result.x
L1_score = result.fun

# ------------------------------
# Step 5: Display Results
# ------------------------------
print("\n✅ Optimization Results")
print(f"Theta (deg): {np.rad2deg(theta_opt):.4f}")
print(f"M: {M_opt:.6f}")
print(f"X: {X_opt:.4f}")
print(f"L1 Distance: {L1_score:.4f}\n")

# ------------------------------
# Step 6: Plot Comparison
# ------------------------------
x_pred, y_pred = curve_model(t_data, theta_opt, M_opt, X_opt)

plt.figure(figsize=(8,6))
plt.plot(x_data, y_data, 'b.', label='Actual Data', alpha=0.6)
plt.plot(x_pred, y_pred, 'r-', linewidth=2, label='Predicted Curve')
plt.title('Observed vs Predicted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig("fitted_curve.png", dpi=300)
plt.show()

# ------------------------------
# Step 7: Print Desmos Equation
# ------------------------------
theta_radians = theta_opt
print("Copy-paste into Desmos:")
print(f"(t*cos({theta_radians:.4f}) - e^({M_opt:.4f}*|t|)*sin(0.3*t)*sin({theta_radians:.4f}) + {X_opt:.3f}, "
      f"42 + t*sin({theta_radians:.4f}) + e^({M_opt:.4f}*|t|)*sin(0.3*t)*cos({theta_radians:.4f}))")
