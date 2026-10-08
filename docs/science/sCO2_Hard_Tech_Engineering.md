# ⚙️ sCO2 Hard-Tech Engineering
**Project:** E-Nexus
**Domain:** Thermodynamics, Turbomachinery, Materials Science

## 1. Thermodynamic Cycle Modeling
Mathematical resolution of the sCO2 Brayton cycle prior to physical prototyping.

### A. Property Analysis
- **Span and Wagner Equation of State:** Calculating fluid behavior near the Critical Point ($31.1^\circ C$ and $7.38$ MPa).
- **Non-Linearities:** Managing extreme density ($> 400 kg/m^3$) and specific heat capacity spikes within $\pm 2^\circ C$ of the critical point.

### B. System Simulation (0D/1D)
- **Tools:** Flownex, MATLAB/Simulink.
- **Scope:** Modeling pressure drops ($\Delta P$) across every valve, bend, and heat exchanger to optimize gross efficiency.

## 2. Turbomachinery Aerodynamics
Engineering power-dense turbines handling extreme mechanical loads.

### A. Radial Inflow Turbine Design
- **Scale:** Designing "coin-sized" high-solidity impellers for $100$ kW to $1$ MW output.
- **Blade Loading:** Managing the massive kinetic energy transfer from dense $CO_2$.

### B. Rotordynamics & CFD
- **Fluid Flow:** Using Ansys CFX to prevent choked flow and transonic shockwaves within the stator vanes.
- **Vibration:** Engineering shafts for ultra-high speeds ($30,000$ to $100,000$ RPM), ensuring operation far from resonant "critical speeds."

## 3. High-Pressure Heat Exchanger Design (PCHEs)
The Recuperator is the thermal heart of the engine, requiring microscopic precision.

### A. Printed Circuit Heat Exchangers (PCHE)
- **Manufacturing:** Chemical etching of semi-circular micro-channels, followed by diffusion bonding for monolithic strength.
- **Performance:** Achieving $>95\%$ effectiveness in a footprint $1/5th$ the size of a shell-and-tube exchanger.

### B. Thermal Stress Analysis
- **Cold Starts:** Modeling thermal expansion gradients. Warming up faster than $10^\circ C / min$ can cause internal stresses to exceed $1,000$ MPa, leading to catastrophic rupture.

## 4. Advanced Sealing & Bearings
Zero-leakage, frictionless operation for closed-loop integrity.

### A. Dry Gas Seals (DGS)
- **Mechanism:** Utilizing a micron-thin hydrodynamic film of $CO_2$ to prevent fluid escape along the high-speed shaft.

### B. Active Magnetic Bearings (AMB)
- **Levitation:** Electromagnetic suspension of the rotor assembly to eliminate friction.
- **Purity:** Complete removal of lubricating oils, preventing $CO_2$ contamination and carbon fouling in the PCHEs.
