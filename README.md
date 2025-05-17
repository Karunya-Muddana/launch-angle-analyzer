# 🚀 Projectile Motion Simulator

A simple Python script that figures out how fast and at what angle you need to launch something to reach different distances. It prints the results and plots two graphs using `matplotlib`.

## 📌 What It Does

- Calculates the required launch **velocity** and **angle** to hit distances from 0 to 100 meters (in 2 seconds)
- Plots:
  - Velocity vs Distance
  - Angle vs Distance

## ✏️ Equations Used

- Horizontal velocity: `ux = distance / time`
- Vertical velocity: `uy = (g * time) / 2`
- Total velocity: `u = √(ux² + uy²)`
- Launch angle: `θ = arctan(uy / ux)`

(*Assumes g = 9.8 m/s² and no air resistance.*)

## 🛠️ Requirements

- Python 3
- `matplotlib` → install with:
  ```bash
  pip install matplotlib
