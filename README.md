# 🏎️ Assetto Corsa Evo — Vehicle Physics Reference Documentation

Welcome to the central community repository dedicated to the structural data and vehicle physics architecture of **Assetto Corsa Evo (v0.7.1)**. 

This project serves as an open, standardized, and highly technical knowledge base designed to help modders, vehicle dynamics engineers, and simulation enthusiasts understand, build, and adapt core vehicle files within the simulation engine.

---

## 📖 Documentation Structure

To ensure maximum clarity and professionalism for the developer community, every analyzed physics asset follows a strict, uniform blueprint:
1. **General Description:** The fundamental role of the asset within the core physics engine architecture.
2. **Areas of Influence:** The concrete physical consequences of the asset and how it dictates track behavior.
3. **Key Architecture & Fields:** In-depth technical breakdowns of data parameters, formatting variables, and units.
4. **Configuration Strategies:** Real-world engineering profiles mapping numbers to recognizable vehicle archetypes (e.g., Stock Road, GT3, Prototypes).

### 🗂️ Mapped Vehicle Physics Assets

| Asset Module | File Extension | Core Operational Domain & Dynamic Impact |
| :--- | :---: | :--- |
| **Brake System** | `.brakesystem` | Governs vehicle-wide peak deceleration balance, static brake bias, electronic cockpit adjusters, and complex controller logic loops (EBB, Steer-Brake systems). |
| **Brakes Hardware** | `.brakes` | Manages localized wheel physics, including thermal capacities, ambient/airflow/wet cooling rates, pad/disc wear ratios, and temperature-to-friction look-up curves. |
| **Car Data** | `.cardata` | Defines the baseline chassis carcass, center of gravity height, global dry weight, polar inertia tensors (Pitch/Roll/Yaw), and volumetric fuel tank tracking coordinates. |
| **Car Engine** | `.carengine` | Maps powertrain performance via internal combustion torque curves, rotating assembly flywheel inertia mass, lift-throttle engine drag parameters, and turbocharger boost matrix curves. |
| **Car Setup** | `.setup` / `.ini` | Exposes pit-garage engineering variables such as cold tyre inflation pressures, alignment geometry (camber/toe), structural coil spring rates, and 4-way damper valving steps. |
| **Car Setup Limits** | `.carsetuplimits` | Enforces regulatory, technical, and administrative boundaries, including min/max sliders, incremental steps, UI visibility flags, and Balance of Performance (BOP) constraints. |
| **Car Setup Units** | `.carsetupunits` | Handles physics localization mappings, translating raw SI variables (e.g., Newtons, Kelvins) into visual UI values like bars, PSI, degrees, or clicks. |
| **Car Tuning Parts** | `.tuningpart` | Serves as a modular asset router, managing performance packages, component overrides (e.g., engine/LSD swaps), and system toggles like disabling ABS/TC. |

---

## 💾 Download the Complete Technical PDF

For a seamless dual-monitor reading experience or mobile browsing in your modding workspace, the complete structured reference guide is compiled as a print-ready PDF document:

👉 **[Download / View the Complete Vehicle Physics Guide (PDF)](./ACE%20-%20Cars%20Physics%20Assets.pdf)**

*(Note: GitHub's native interface includes an integrated PDF viewer allowing full text searches via `Ctrl + F` or `Cmd + F` directly inside the file).*

---

## 🤝 Contributing to the Repository

Collaborative reverse engineering keeps this documentation robust and up to date. If you discover undocumented physics fields, verify a look-up table translation, or map telemetry outputs to newly uncovered strings:
1. **Fork** this repository.
2. Create or adjust descriptions while strictly maintaining the project's layout formatting.
3. Submit a clean **Pull Request** explaining your physical testing methods, source files, or verified data parameters.

---

## 📄 License

This documentation suite is released and made available to the public under the terms of the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. 
You are entirely free to copy, share, redistribute, adapt, or build upon this content for any purpose (including third-party modding frameworks), provided you give **appropriate credit to the original authors and the community project**.

---
*Disclaimer: This repository is a community-driven, non-commercial research initiative. Assetto Corsa Evo is a registered trademark of Kunos Simulazioni. All technical descriptions are provided transparently for educational, data-mapping, and modification reference purposes.*
