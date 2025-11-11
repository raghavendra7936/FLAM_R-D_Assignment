# Assignment for  FLAM Research and Development / AI

## Problem Statement

Find the values of unknown variables in the given parametric equation of a curve:

x = ( t*cos(θ) - e^(M|t|)*sin(0.3t)*sin(θ) + X )  
y = ( 42 + t*sin(θ) + e^(M|t|)*sin(0.3t)*cos(θ) )

Unknowns are:  
θ, M, X

Given range for unknown parameters is:

0° < θ < 50°  
-0.05 < M < 0.05  
0 < X < 100  

Parameter ‘t’ has range:  
6 < t < 60  

Given is the list of points that lie on the curve for 6 < t < 60:  
xy_data.csv

---

## Approach

1. Imported the dataset and generated a uniform t sequence between 6 and 60.  
2. Defined the mathematical model for x(t) and y(t).  
3. Created a loss function using L1 distance between predicted and actual data points.  
4. Used the L-BFGS-B optimization algorithm (scipy.optimize.minimize) under the given parameter bounds.  
5. Computed the best-fit values of θ, M, and X that minimize the L1 loss.  
6. Visualized the actual vs predicted curve for validation.

---

## Results

θ = 28.12°  
M = 0.0214  
X = 54.901  
L1 Distance = 37865.09

---

## Final Parametric Equation

(t*cos(0.4908) - e^(0.0214*|t|)*sin(0.3*t)*sin(0.4908) + 54.901,  
42 + t*sin(0.4908) + e^(0.0214*|t|)*sin(0.3*t)*cos(0.4908))

This equation can be copied directly into Desmos for verification:  
https://www.desmos.com/calculator/tyjfpmbpeg

---

## Visualization

Blue points - actual dataset  
Red line - predicted curve

![Fitted Curve](FLAM_R&D_CurveFit_Comparision.png)

---



## Conclusion

The unknown parameters were successfully estimated within their specified ranges.  
The predicted curve closely follows the given data, achieving an L1 distance of 37865.09.

Final parameter values:  
θ = 28.12°, M = 0.0214, X = 54.901
