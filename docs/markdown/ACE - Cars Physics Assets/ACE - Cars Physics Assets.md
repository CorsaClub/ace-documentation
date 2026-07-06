![](_page_0_Picture_0.jpeg)

# **Assetto Corsa EVO**

Game Version : **0.7.1**

Assets Type : **Cars**

Subtype : **Car Physics Assets** 

![](_page_0_Picture_5.jpeg)

| 1. | Brake                       |             | System<br>[<br>.brakesystem<br>]                                                | 12 |
|----|-----------------------------|-------------|---------------------------------------------------------------------------------|----|
|    | A.                          | Description |                                                                                 |    |
|    |                             | I.          | General<br>Description                                                          | 12 |
|    |                             | II.         | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics             | 12 |
|    |                             | III.        | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained                         | 12 |
|    |                             |             | 1 - Base Mechanical & Physical Parameters                                       | 12 |
|    |                             |             | 2 - Dynamic Control Units (EBB & Steer Brake)                                   | 13 |
|    |                             |             | 3 - Control Stages & Algorithmic Logic                                          | 13 |
|    |                             |             | 4 - EBB Modes                                                                   | 13 |
|    | B.                          |             | Schema                                                                          | 14 |
|    | C.                          |             | Measurement Units & Descriptions                                                | 15 |
|    | D.                          |             | Example data                                                                    | 16 |
|    |                             | I.          | Chosen<br>Cars<br>for<br>Example                                                | 16 |
|    |                             | II.         | Example                                                                         | 17 |
|    |                             |             | Alfa Romeo Giulia GTAm                                                          | 17 |
|    |                             |             | Lancia Delta HF Integrale EVO II ( slug : ks_lancia_delta_hf_integrale_evo_ii ) | 18 |
|    |                             |             | Ferrari 296 GT3                                                                 | 18 |
|    |                             |             | Ferrari SF25                                                                    | 19 |
| 2. |                             |             | [<br>.brakes<br>]                                                               | 22 |
|    | Brakes<br>A.<br>Description |             | 22                                                                              |    |
|    |                             | I.          | General<br>Description                                                          | 22 |
|    |                             | II.         | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics             | 22 |
|    |                             | III.        | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained                         | 22 |
|    |                             |             | 1 - Thermal Modeling & Heat Dissipation                                         | 22 |
|    |                             |             | 2 - Dimensions, Wear, and Degradation (M M = Per Millimeter)                    | 23 |
|    |                             |             | 3 - Perf Curve (Friction Coeffi<br>cient vs. Temperature)                       | 23 |
|    |                             | IV.         | Interpretation<br>of<br>Asset<br>Implementation<br>&<br>Data<br>Profiles        | 23 |
|    |                             |             | Profile A: Split Front/Rear Axle Configurations (e.g., Vintage/Road Cars)       | 23 |
|    |                             |             | Profile B: Single Shared Compound Profiles & Endurance Pads (e.g., Racing GT3)  | 24 |
|    |                             |             | Reading the Performance Curve Trend                                             | 24 |
|    | B.                          |             | Schema                                                                          | 24 |
|    | C.                          |             | Measurement Units & Descriptions                                                | 25 |
|    | D.                          |             | Example data                                                                    | 27 |
|    |                             | I.          | Chosen<br>Brakes<br>for<br>Example                                              | 27 |

|    |     | II.  | Example                                                             | 27 |
|----|-----|------|---------------------------------------------------------------------|----|
|    |     |      | Vintage Road [ Front ]                                              | 27 |
|    |     |      | Vintage Road [ Rear ]                                               | 28 |
|    |     |      | Racing GT3 [ Pad 2 ]                                                | 29 |
| 3. | Car | Data | [<br>.car<br>]                                                      | 31 |
|    | A.  |      | Description                                                         | 31 |
|    |     | I.   | General<br>Description                                              | 31 |
|    |     | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 31 |
|    |     | III. | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 31 |
|    |     |      | 1 - Global Mass & Inertia Properties                                | 31 |
|    |     |      | 2 - Dimensions, Track and Alignement Coordinates                    | 32 |
|    |     |      | 3 - Fuel Management & Consumables                                   | 32 |
|    |     | IV.  | Short<br>Interpretation<br>of<br>Asset<br>Implementation            | 32 |
|    | B.  |      | Schema                                                              | 33 |
|    | C.  |      | Measurement Units & Descriptions                                    | 42 |
|    | D.  |      | Example data                                                        | 42 |
|    |     | I.   | Chosen<br>Car<br>Data<br>for<br>Example                             | 42 |
|    |     | II.  | Example                                                             | 42 |
|    |     |      | Ferrari 296 GTB                                                     | 42 |
|    |     |      | Audi R8 LMS GT3 Evo II                                              | 52 |
|    |     |      | Renault 5 GT Turbo                                                  | 59 |
| 4. | Car |      | Engine<br>[<br>.carengine<br>]                                      | 63 |
|    | A.  |      | Description                                                         | 63 |
|    |     | I.   | General<br>Description                                              | 63 |
|    |     | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 63 |
|    |     | III. | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 63 |
|    |     |      | 1 - Power Generation & Power Curves                                 | 63 |
|    |     |      | 2 - Rotational Dynamics & Throttle Response                         | 64 |
|    |     |      | 3 - Aspiration, Turbocharging & Thermal Behavior                    | 64 |
|    |     | IV.  | Short<br>Interpretation<br>of<br>Asset<br>Implementation            | 64 |
|    | B.  |      | Schema                                                              | 65 |
|    | C.  |      | Example data                                                        | 66 |
|    |     | I.   | Chosen<br>Car<br>Engine<br>for<br>Example                           | 66 |
|    |     | II.  | Example                                                             | 66 |

|    |     |      | Alpine A290 b                                                       | 66 |
|----|-----|------|---------------------------------------------------------------------|----|
|    |     |      | Ferrari SF 25                                                       | 67 |
|    |     |      | Chevrolet Camaro ZL1                                                | 71 |
|    |     |      | Datsun 240z Fairlady                                                | 72 |
| 5. | Car |      | Setup<br>[<br>.carsetup<br>]                                        | 74 |
|    | A.  |      | Description                                                         | 74 |
|    |     | I.   | General<br>Description                                              | 74 |
|    |     | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 74 |
|    |     | III. | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 74 |
|    |     |      | 1 - Tyres ( The Contact Patch )                                     | 74 |
|    |     |      | 2 - Aerodynamics ( The Airflow Platform )                           | 75 |
|    |     |      | 3 - Suspension Geometry & Rates                                     | 75 |
|    |     |      | 4 - Dampers ( Transient Shock Absorption )                          | 75 |
|    |     |      | 5 - Drivetrain & Differential                                       | 75 |
|    |     | IV.  | Interpretation<br>of<br>Setup<br>Configuration<br>Strategies        | 76 |
|    | B.  |      | Schema                                                              | 76 |
|    | C.  |      | Example data                                                        | 77 |
|    |     | I.   | Chosen<br>Car<br>Engine<br>for<br>Example                           | 77 |
|    |     | II.  | Example                                                             | 77 |
|    |     |      | Audi Sport Quattro                                                  | 77 |
|    |     |      | Alfa Romeo Junior                                                   | 80 |
|    |     |      | Ferrari 488 Challenge Evo [ preset : safe_1 ]                       | 82 |
| 6. | Car |      | Setup<br>Limits<br>[<br>.carsetuplimits<br>]                        | 85 |
|    | A.  |      | Description                                                         | 85 |
|    |     | I.   | General<br>Description                                              | 85 |
|    |     | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 85 |
|    |     | III. | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 85 |
|    |     |      | 1 - The Anatomy of a Parameter Limit Object                         | 85 |
|    |     |      | 2 - Core Categories of Application                                  | 86 |
|    |     | IV.  | Interpretation<br>of<br>Setup<br>Limits<br>Strategies               | 86 |
|    | B.  |      | Schema                                                              | 87 |
|    | C.  |      | Example data                                                        | 96 |
|    |     | I.   | Chosen<br>Car<br>Engine<br>for<br>Example                           | 96 |
|    |     | II.  | Example                                                             | 96 |
|    |     |      | BMW M4 CSL                                                          | 96 |

|    |     |      | Lamborghini Countach                                                | 116 |
|----|-----|------|---------------------------------------------------------------------|-----|
| 7. | Car |      | Setup<br>Units<br>[<br>.carsetupunits<br>]                          | 137 |
|    | A.  |      | Description                                                         | 137 |
|    |     | I.   | General<br>Description                                              | 137 |
|    |     | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 137 |
|    |     | III. | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 137 |
|    |     |      | 1 - Wheel and Tyre Telemetry Alignment                              | 137 |
|    |     |      | 2 - Suspension Components & Kinematics                              | 138 |
|    |     |      | 3 - Aerodynamics & Aerostatic Clearance                             | 138 |
|    |     | IV.  | Interpretation<br>of<br>Setup<br>Units<br>Strategies                | 138 |
|    | B.  |      | Schema                                                              | 138 |
|    | C.  |      | Example data                                                        | 140 |
|    |     | I.   | Chosen<br>Car<br>Engine<br>for<br>Example                           | 140 |
|    |     | II.  | Example                                                             | 140 |
|    |     |      | Setup Units                                                         | 140 |
| 8. | Car |      | Tuning<br>Parts<br>[<br>.tuningpart<br>]                            | 144 |
|    | A.  |      | Description                                                         | 144 |
|    |     | I.   | General<br>Description                                              | 144 |
|    |     | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 144 |
|    |     | III. | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 144 |
|    |     |      | 1 - Tuning Part Core Definitions                                    | 144 |
|    |     |      | 2 - Component Path Overrides                                        | 145 |
|    |     | IV.  | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 145 |
|    | B.  |      | Schema                                                              | 145 |
|    | C.  |      | Example data                                                        | 151 |
|    |     | I.   | Chosen<br>Cars<br>for<br>Example                                    | 151 |
|    |     | II.  | Example                                                             | 151 |
|    |     |      | Toyota Supra MK IV                                                  | 151 |
|    |     |      | Datsun 240z Fairlady                                                | 152 |
|    |     |      | Porsche 992 GT3 Cup                                                 | 154 |
| 9. | Car |      | Electronics<br>[<br>.carelectronics<br>]                            | 155 |
|    | A.  |      | Description                                                         | 155 |
|    |     | I.   | General<br>Description                                              | 155 |
|    |     | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 155 |

|     |    | III.     | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 155 |
|-----|----|----------|---------------------------------------------------------------------|-----|
|     |    |          | 1 - Traction Control (TC) Logic Matrix                              | 155 |
|     |    |          | 2 - Anti-lock Braking System (ABS) Map Settings                     | 156 |
|     |    | IV.      | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 156 |
|     | B. |          | Schema                                                              | 156 |
|     | C. |          | Example data                                                        | 157 |
|     |    | I.       | Chosen<br>Cars<br>for<br>Example                                    | 157 |
|     |    | II.      | Example                                                             | 157 |
|     |    |          | Lamborghini Huracan ST Evo 2                                        | 157 |
|     |    |          | Maserati MC20 GT2                                                   | 161 |
|     |    |          | Porsche 992 GT3 Cup                                                 | 164 |
| 10. |    | Clutch   | [<br>.clutch<br>]                                                   | 167 |
|     | A. |          | Description                                                         | 167 |
|     |    | I.       | General<br>Description                                              | 167 |
|     |    | II.      | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 167 |
|     |    | III.     | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 167 |
|     |    |          | 1 - base mechanical & Intertial Parameters                          | 167 |
|     |    |          | 2 - Autoclutch Profile Parameters                                   | 168 |
|     |    | IV.      | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 168 |
|     | B. |          | Schema                                                              | 168 |
|     | C. |          | Example data                                                        | 169 |
|     |    | I.       | Chosen<br>Cars<br>for<br>Example                                    | 169 |
|     |    | II.      | Example                                                             | 169 |
|     |    |          | Caterham 485 CSR                                                    | 169 |
|     |    |          | Ferrari F2004                                                       | 169 |
|     |    |          | Volkswagen Golf GTI mk8                                             | 169 |
| 11. |    | Coilover | [<br>.coilover<br>]                                                 | 171 |
|     | A. |          | Description                                                         | 171 |
|     |    | I.       | General<br>Description                                              | 171 |
|     |    | II.      | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 171 |
|     |    | III.     | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 171 |
|     |    |          | 1 - Wheel Rate & Spring Parameters                                  | 171 |
|     |    |          | 2 - Damper Profile Parameters                                       | 172 |
|     |    |          | 3 - Alignments & Geometry Fields                                    | 172 |

|               |     | IV.<br>Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 173 |
|---------------|-----|----------------------------------------------------------------------------|-----|
|               | B.  | Schema                                                                     | 173 |
|               | C.  | Example data                                                               | 174 |
|               |     | I.<br>Chosen<br>Cars<br>for<br>Example                                     | 174 |
|               |     | II.<br>Example                                                             | 174 |
|               |     | Caterham 485 CSR                                                           | 174 |
|               |     | Alpine A110s                                                               | 176 |
|               |     | Dallara EXP                                                                | 177 |
| 12.<br>Damper | 180 |                                                                            |     |
|               | A.  | Description                                                                | 180 |
|               |     | I.<br>General<br>Description                                               | 180 |
|               |     | II.<br>Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 180 |
|               |     | III.<br>Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained            | 180 |
|               |     | 1 - Wheel Rate & Spring Parameters                                         | 180 |
|               |     | 2 - Damper Profile Parameters                                              | 180 |
|               |     | 3 - Alignments & Geometry Fields                                           | 180 |
|               |     | IV.<br>Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 180 |
|               | B.  | Schema                                                                     | 180 |
|               | C.  | Example data                                                               | 181 |
|               |     | I.<br>Chosen<br>Cars<br>for<br>Example                                     | 181 |
|               |     | II.<br>Example                                                             | 181 |
|               |     | Ford - GT3 Dampers                                                         | 181 |
|               |     | Penske                                                                     | 181 |
|               |     | Porsche Cayman Dampers                                                     | 184 |
| 13.           |     | Drivetrain<br>[<br>.drivetrain<br>]                                        | 186 |
|               | A.  | Description                                                                | 186 |
|               |     | I.<br>General<br>Description                                               | 186 |
|               |     | II.<br>Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 186 |
|               |     | III.<br>Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained            | 186 |
|               |     | 1 - Wheel Rate & Spring Parameters                                         | 186 |
|               |     | 2 - Damper Profile Parameters                                              | 186 |
|               |     | 3 - Alignments & Geometry Fields                                           | 186 |
|               |     | IV.<br>Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 186 |
|               | B.  | Schema                                                                     | 186 |

|     | C.                 |         | Example data                                                        | 189 |
|-----|--------------------|---------|---------------------------------------------------------------------|-----|
|     |                    | I.      | Chosen<br>Cars<br>for<br>Example                                    | 189 |
|     |                    | II.     | Example                                                             | 189 |
|     |                    |         | Audi RS3 Sportback                                                  | 189 |
|     |                    |         | Ferrari F40 LM                                                      | 193 |
|     |                    |         | Abarth 695 Biposto                                                  | 194 |
| 14. |                    | Gearbox | [<br>.gearbox<br>]                                                  | 197 |
|     | A.                 |         | Description                                                         | 197 |
|     |                    | I.      | General<br>Description                                              | 197 |
|     |                    | II.     | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 197 |
|     |                    | III.    | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 197 |
|     |                    |         | 1 - Wheel Rate & Spring Parameters                                  | 197 |
|     |                    |         | 2 - Damper Profile Parameters                                       | 197 |
|     |                    |         | 3 - Alignments & Geometry Fields                                    | 197 |
|     |                    | IV.     | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 197 |
|     | B.                 |         | Schema                                                              | 197 |
|     | C.<br>Example data |         | 198                                                                 |     |
|     |                    | I.      | Chosen<br>Cars<br>for<br>Example                                    | 198 |
|     |                    | II.     | Example                                                             | 198 |
|     |                    |         | Porsche 718 Cayman GT4 CS MR                                        | 198 |
|     |                    |         | Alpine A290 b                                                       | 199 |
|     |                    |         | Renault 5 GT Turbo                                                  | 200 |
| 15. |                    | General | [<br>.generalcar<br>]                                               | 202 |
|     | A.                 |         | Description                                                         | 202 |
|     |                    | I.      | General<br>Description                                              | 202 |
|     |                    | II.     | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 202 |
|     |                    | III.    | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 202 |
|     |                    |         | 1 - Wheel Rate & Spring Parameters                                  | 202 |
|     |                    |         | 2 - Damper Profile Parameters                                       | 202 |
|     |                    |         | 3 - Alignments & Geometry Fields                                    | 202 |
|     |                    | IV.     | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 202 |
|     | B.                 |         | Schema                                                              | 202 |
|     | C.                 |         | Example data                                                        | 203 |
|     |                    | I.      | Chosen<br>Cars<br>for<br>Example                                    | 203 |

| 16.<br>Surface<br>3D<br>[<br>.surface3d<br>] |              |                                                                     | 204 |
|----------------------------------------------|--------------|---------------------------------------------------------------------|-----|
| A.                                           |              | Description                                                         | 204 |
|                                              | I.           | General<br>Description                                              | 204 |
|                                              | II.          | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 204 |
|                                              | III.         | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 204 |
|                                              |              | 1 - Wheel Rate & Spring Parameters                                  | 204 |
|                                              |              | 2 - Damper Profile Parameters                                       | 204 |
|                                              |              | 3 - Alignments & Geometry Fields                                    | 204 |
|                                              | IV.          | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 204 |
| B.                                           |              | Schema                                                              | 204 |
| C.                                           | Example data |                                                                     | 205 |
|                                              | I.           | Chosen<br>Cars<br>for<br>Example                                    | 205 |
|                                              | II.          | Example                                                             | 205 |
|                                              |              | Mercedes AMG GT2                                                    | 205 |
|                                              |              | Audi R8 LMS GT3 Evo 2                                               | 207 |
|                                              |              | Dallara Stradale Coupe                                              | 209 |
| 17.<br>Suspension<br>[<br>.suspension<br>]   |              |                                                                     | 212 |
| A.                                           |              | Description                                                         | 212 |
|                                              | I.           | General<br>Description                                              | 212 |
|                                              | II.          | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 212 |
|                                              | III.         | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 212 |
|                                              |              | 1 - Wheel Rate & Spring Parameters                                  | 212 |
|                                              |              | 2 - Damper Profile Parameters                                       | 212 |
|                                              |              | 3 - Alignments & Geometry Fields                                    | 212 |
|                                              | IV.          | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 212 |
| B.                                           |              | Schema                                                              | 212 |
| C.                                           |              | Example data                                                        | 214 |
|                                              | I.           | Chosen<br>Cars<br>for<br>Example                                    | 214 |
|                                              | II.          | Example                                                             | 214 |
|                                              |              | Volkswagen Golf GTI Mk1                                             | 214 |
|                                              |              | Honda S2000 AP1                                                     | 215 |
|                                              |              | Porsche 992 GT3 R Rennport                                          | 216 |
| 18.                                          | Turbo<br>[   | .turbo<br>]                                                         | 219 |
| A.                                           |              | Description                                                         | 219 |

|                                |    | I.   | General<br>Description                                              | 219 |
|--------------------------------|----|------|---------------------------------------------------------------------|-----|
|                                |    | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 219 |
|                                |    | III. | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 219 |
|                                |    |      | 1 - Wheel Rate & Spring Parameters                                  | 219 |
|                                |    |      | 2 - Damper Profile Parameters                                       | 219 |
|                                |    |      | 3 - Alignments & Geometry Fields                                    | 219 |
|                                |    | IV.  | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 219 |
|                                | B. |      | Schema                                                              | 219 |
|                                | C. |      | Example data                                                        | 220 |
|                                |    | I.   | Chosen<br>Cars<br>for<br>Example                                    | 220 |
|                                |    | II.  | Example                                                             | 220 |
|                                |    |      | Peugeot 205 T16                                                     | 220 |
|                                |    |      | Chevrolet Camaro ZL1                                                | 220 |
|                                |    |      | Toyota Supra MKIV                                                   | 221 |
| 19.<br>Tyre<br>[<br>.tyre<br>] |    |      | 222                                                                 |     |
|                                | A. |      | Description                                                         | 222 |
|                                |    | I.   | General<br>Description                                              | 222 |
|                                |    | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 222 |
|                                |    | III. | Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained             | 222 |
|                                |    |      | 1 - Wheel Rate & Spring Parameters                                  | 222 |
|                                |    |      | 2 - Damper Profile Parameters                                       | 222 |
|                                |    |      | 3 - Alignments & Geometry Fields                                    | 222 |
|                                |    | IV.  | Interpretation<br>of<br>Tuning<br>Part<br>Strategies                | 222 |
|                                | B. |      | Schema                                                              | 222 |
|                                | C. |      | Example data                                                        | 225 |
|                                |    | I.   | Chosen<br>Tyres<br>for<br>Example                                   | 225 |
|                                |    | II.  | Example                                                             | 225 |
|                                |    |      | Eco   Size : 165 - 60 - 12                                          | 225 |
|                                |    |      | Vintage   Size : 195 - 60 - 15                                      | 227 |
|                                |    |      | F1 2025 [ Wet ]   Size : 305 - 720 - 18                             | 230 |
| 20.<br>Wing<br>[<br>.wing<br>] |    |      | 233                                                                 |     |
|                                | A. |      | Description                                                         | 233 |
|                                |    | I.   | General<br>Description                                              | 233 |
|                                |    | II.  | Area<br>of<br>Influence<br>/<br>Impact<br>on<br>Vehicle<br>Dynamics | 233 |

| III.<br>Key<br>Architecture<br>&<br>Data<br>Fields<br>Explained | 233 |
|-----------------------------------------------------------------|-----|
| 1 - Wheel Rate & Spring Parameters                              | 233 |
| 2 - Damper Profile Parameters                                   | 233 |
| 3 - Alignments & Geometry Fields                                | 233 |
| IV.<br>Interpretation<br>of<br>Tuning<br>Part<br>Strategies     | 233 |
| B.<br>Schema                                                    | 233 |
| C.<br>Example data                                              | 234 |
| I.<br>Chosen<br>Tyres<br>for<br>Example                         | 234 |
| II.<br>Example                                                  | 234 |
| Audi RS6 Avant                                                  | 234 |
| Lotus Emira                                                     | 236 |
| Ferrari SF-25                                                   | 238 |

# <span id="page-11-0"></span>**1. Brake System [ .brakesystem ]**

# <span id="page-11-1"></span>**A. Description**

### <span id="page-11-2"></span>**I. General Description**

The BrakeSystem asset is the core configuration file that defines the entire physical, mechanical, and electronic behavior of a vehicle's braking system within the simulation engine.

Rather than just setting a raw stopping power value, this asset acts as a central hub. It governs how braking force is distributed between the front and rear axles (static and dynamic bias), how secondary systems like the handbrake behave, and how advanced modern electronic driving aids —such as Electronic Brake Balance (EBB) and brake-based torque vectoring systems—alter braking pressure in real time based on telemetry.

### <span id="page-11-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The parameters configured in this asset directly impact how the vehicle handles during one of the most critical phases of driving:

- **• Stopping Distance (Braking Power):** Dictated by the total available torque, defining how quickly the vehicle can decelerate.
- **• Braking Stability (Brake Bias):** Controls the balance of force. Too much front bias leads to understeer or front-wheel lockup; too much rear bias causes instability, potentially throwing the car into a spin when braking heavily into a corner.
- **• Cornering Agility & Trajectory Control:** Through dynamic controllers, the system can modulate brake pressure on individual wheels or axles based on steering angle, lateral Gforces, or wheel slip, acting like a performance Stability Control (ESP) or electronic torque vectoring system.
- **• Energy Recovery Systems (Hybrid/EV Integration):** Variables linked to the ERS (Energy Recovery System) interact with regenerative braking, managing how hydraulic pressure scales alongside electric motor resistance (ErsCoastTorque) and battery state-of-charge.

#### <span id="page-11-4"></span>**III. Key Architecture & Data Fields Explained**

The schema is organized into three main categories: **Mechanical Constants**, **Electronic Subsystems**, and **Algorithmic Logic (Stages)**.

#### <span id="page-11-5"></span>**1 - BASE MECHANICAL & PHYSICAL PARAMETERS**

- **• Total Torque:** The absolute maximum braking torque (usually in *Nm*) applied across the entire vehicle when the brake pedal is depressed 100%.
- **• Front Bias:** The baseline, static percentage of braking force sent to the front axle (*e.g. 0.60 = 60% front, 40% rear*).
- **• Hand Brake Torque:** Dedicated torque value applied exclusively by the handbrake (typically impacting only the rear wheels).

- **• Has Cockpit Bias & Bias Step:** Determines whether the driver can adjust the brake balance on the fly from inside the cockpit, and by what percentage increment each button press alters the bias (*e.g. 0.5%*).
- **• Front/Rear Compound Path:** File paths linking the brakes to external thermal and friction physics models (governing brake wear, fade, and optimal operating temperature windows).

### <span id="page-12-0"></span>**2 - DYNAMIC CONTROL UNITS (EBB & STEER BRAKE)**

Advanced vehicles use automated controllers to alter braking performance based on real-time physics data:

- **1. Controller EBB / Controllers EBB:** Electronic Brake Balance controllers. They continuously shift the brake balance forward or backward depending on live driving conditions.
- **2. Steer Brake Controller:** An agile-handling system that applies micro-braking forces to specific wheels based on steering inputs (SteerDEG) or yaw rates (SteerYawDelta). It mimics modern electronic differentials or stability management.
- **3. Torque Controller EBB:** Dynamically scales total braking torque output to prevent global lockups or optimize regenerative braking efficiency.

#### <span id="page-12-1"></span>**3 - CONTROL STAGES & ALGORITHMIC LOGIC**

Every dynamic controller processes data through one or multiple **Stages**. Each stage functions as an automated logical loop:

- **• Input Var (Input Variable):** The live telemetry channel the game reads (e.g., Brake pedal pressure, wheel SlipRatio, lateral forces LatG, or suspension/weight transfer data like LoadSpreadLF).
- **• LUT (Look-Up Table):** A path to a external .curve file. This data curve acts as an instruction set: *"If the input variable is* X*, apply a modifier value of* Y*."*
- **• Combinator Mode:** Dictates how this specific stage interacts with others in the pipeline (Add to sum the values together, or Mult to multiply them).
- **• Filter Gain:** A smoothing coefficient that dampens rapid telemetry spikes, preventing jittery or unnaturally sudden braking corrections.
- **• Up / Down Limit:** Standard clamping values ensuring the controller output stays within safe, physically realistic boundaries.

# <span id="page-12-2"></span>**4 - EBB MODES**

ebbDisabled: Electronic brake distribution is off. The car relies entirely on its static physical brake bias.

ebbInternal: Uses hardcoded engine-level logic to distribute braking.

ebbDynamicControllerAbsolute / Relative: Fully activates the custom look-up tables and stages defined in the asset to modulate balance absolutely or relative to the base setup.

# <span id="page-13-0"></span>**B. Schema**

```
├ 1. Total Torque : float
├ 2. Front Bias : float
├ 3. Hand Brake Torque : float 
├ 4. Has Cockpit Bias : boolean 
├ 5. Bias Step : float 
├ 6. Front Compound Path [x] : float | can have multiple Front Compound 
Path 
├ 7. Rear Compound path [x] : float | can have multiple Rear Compound 
Path 
├ 8. Controller EBB : object with an array of stages within 
│ ├ 8a. Name : string 
│ ├ 8b. Stages [x] : object | Controller EBB can have multiple stages 
│ │ ├ 8b1. Input Var : enum
│ │ ├ 8b2. Combinator Mode : enum
│ │ ├ 8b3. Lut : string - path 
│ │ ├ 8b4. Filter Gain : float 
│ │ ├ 8b5. Up Limit : float 
│ │ ├ 8b6. Down Limit : float 
│ │ ├ 8b7. Current Value : float
│ └ └ 8b8. Const Value : float 
├ 9. Controllers EBB [x] : object with an array of stages within 
│ ├ 8a. Name : string
│ ├ 8b. Stages [x] : object | Controllers EBB [x] can have multiple 
stages 
│ │ ├ 8b1. Input Var : enum 
│ │ ├ 8b2. Combinator Mode : enum 
│ │ ├ 8b3. Lut : string - path 
│ │ ├ 8b4. Filter Gain : float 
│ │ ├ 8b5. Up Limit : float 
│ │ ├ 8b6. Down Limit : float 
│ │ ├ 8b7. Current Value : float 
│ └ └ 8b8. Const Value : float
├ 10. Steer Brake Controller : object with an array of stages within 
│ ├ 8a. Name : string 
│ ├ 8b. Stages [x] : object | Steer Brake Controller can have multiple 
stages 
│ │ ├ 8b1. Input Var : enum 
│ │ ├ 8b2. Combinator Mode : enum 
│ │ ├ 8b3. Lut : string - path 
│ │ ├ 8b4. Filter Gain : float 
│ │ ├ 8b5. Up Limit : float 
│ │ ├ 8b6. Down Limit : float 
│ │ ├ 8b7. Current Value : float 
│ └ └ 8b8. Const Value : float 
├ 11. Troque Controller EBB : object with an array of stages within 
│ ├ 8a. Name : string
│ ├ 8b. Stages [x] : object | Torque Controller EBB can have multiple 
stages 
│ │ ├ 8b1. Input Var : enum 
│ │ ├ 8b2. Combinator Mode : enum 
│ │ ├ 8b3. Lut : string - path
```

```
│ │ ├ 8b4. Filter Gain : float 
│ │ ├ 8b5. Up Limit : float 
│ │ ├ 8b6. Down Limit : float 
│ │ ├ 8b7. Current Value : float 
│ └ └ 8b8. Const Value : float
├ 12. EBB Mode : enum
```

├ 13. EBB Front Multiplier : float

└ 14. EBB Min Speed : float

### **Enum List - Brake System**

| Enum           | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input Var      | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear,<br>SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX,<br>SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG,<br>SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor,<br>RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG,<br>LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR,<br>SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight,<br>ErsChargeLevel, ErsCoastTorque |
| CombinatorMode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                                               |
| EBB Mode       | ebbDisabled, ebbInternal, ebbDynamicControllerAbsolute,<br>ebbDynamicControllerRelative                                                                                                                                                                                                                                                                                                                                                                |

### <span id="page-14-0"></span>**C. Measurement Units & Descriptions**

| ID | Name                | Unit of Measurement                      | Description                                                                                                       |
|----|---------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 1. | Total Torque        | Nm ( Newton-meters )                     | Defines the maximum total braking<br>torque available for the entire<br>vehicle.                                  |
| 2. | Front Bias          | % ( Percentage / Distribution<br>ratio ) | Sets the percentage of total<br>braking torque allocated to the<br>front axle (e.g., 0.60 = 60%).                 |
| 3. | Hand Brake Torque   | Nm ( Newton-meters )                     | Specifies the maximum braking<br>torque applied by pulling the<br>mechanical handbrake.                           |
| 4. | Has Cockpit Bias    | None ( Boolean : True /<br>False )       | Toggles whether the driver can<br>adjust the brake balance manually<br>from inside the cockpit while<br>driving.  |
| 5. | Bias Step           | % ( Percentage increment )               | The step size by which the brake<br>bias changes per click when<br>adjusted (e.g., 0.005 for 0.5%<br>increments). |
| 6. | Front Compound Path | None ( File path )                       | Points to the physics/lookup file<br>defining the friction and thermal<br>properties of the front brake pads.     |

| ID   | Name                 | Unit of Measurement                         | Description                                                                                                                 |
|------|----------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 7.   | Rear Compound Path   | None ( File path )                          | Points to the physics/lookup file<br>defining the friction and thermal<br>properties of the rear brake pads.                |
| 8a.  | Name                 | None ( String )                             | An internal label or identifier for<br>the specific brake controller or<br>modifier stage.                                  |
| 8b1. | Input Var            | None ( Telemetry enum )                     | The telemetry variable used as the<br>trigger input for this controller<br>(e.g., SteerDEG, Brake, Speed).                  |
| 8b2. | Combinator Mode      | None ( Math enum : Add /<br>Mult )          | Determines how this stage's<br>output combines with the baseline<br>value (Addition or Multiplication).                     |
| 8b3. | Lut                  | None ( .curve file path )                   | References a Look-Up Table curve<br>file that maps the raw input value<br>to a specific output factor.                      |
| 8b4. | Filter Gain          | Coeffi<br>cient ( Smoothing<br>multiplier ) | Controls the input signal<br>smoothing filter; acts as a<br>dampener to prevent sudden<br>spikes in controller application. |
| 8b5. | Up Limit             | Depends on the input<br>variable            | The upper bounding limit for the<br>input signal, clamping values that<br>exceed this threshold.                            |
| 8b6. | Down Limit           | Depends on the input<br>variable            | The lower bounding limit for the<br>input signal, clamping values that<br>fall below this threshold.                        |
| 8b7. | Current Value        | Depends on the input<br>variable            | The current, real-time value<br>processed by the controller during<br>simulation.                                           |
| 8b8. | Const Value          | Depends on the input<br>variable            | A fallback fallback constant value<br>used if no dynamic input curve or<br>telemetry is active.                             |
| 12.  | EBB Mode             | None ( Mode enum )                          | Selects the operational logic<br>profile for the Electronic Brake<br>Balance system.                                        |
| 13.  | EBB Front Multiplier | Coeffi<br>cient ( Scaling factor )          | Scaling factor that dynamically<br>adjusts the front brake bias<br>authority under EBB intervention.                        |
| 14.  | EBB Min Speed        | Km/h or m/s * ( Spped<br>threshold )        | The minimum vehicle speed below<br>which the Electronic Brake<br>Balance system deactivates.                                |

#### <span id="page-15-0"></span>**D. Example data**

#### <span id="page-15-1"></span>**I. Chosen Cars for Example**

- Alfa Romeo Giulia GTAm ( slug : ks\_alfa\_romeo\_giulia\_gtam )
- Lancia Delta HF Integrale EVO II ( slug : ks\_lancia\_delta\_hf\_integrale\_evo\_ii )

- Ferrari 296 GT3 ( slug : ks\_ferrari\_296\_gt3 )
- Ferrari SF25 ( slug : ks\_ferrari\_sf\_25 )

#### <span id="page-16-0"></span>**II. Example**

#### <span id="page-16-1"></span>**Alfa Romeo Giulia GTAm**

```
├ 1. Total Torque : 4100.00000
├ 2. Front Bias : 0.75000 
├ 3. Hand Brake Torque : 200.00000 
├ 4. Has Cockpit Bias : false 
├ 5. Bias Step : 0.50000 
├ 6. Front Compound Path : None 
├ 7. Rear Compound path : None
├ 8. Controller EBB 
│ ├ 8a. Name : None 
│ ├ 8b. Stages 1 
│ │ ├ 8b1. Input Var : LoadSpreadLF 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_alfa_romeo_giulia_gtam\data\ctrl_ebbCONTROLLER_0.curve
│ │ ├ 8b4. Filter Gain : 0.01000 
│ │ ├ 8b5. Up Limit : 1.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
│ ├ 8b. Stages 2 
│ │ ├ 8b1. Input Var : SlipAngleRearMAX 
│ │ ├ 8b2. Combinator Mode : Mult 
│ │ ├ 8b3. Lut : 
content\cars\ks_alfa_romeo_giulia_gtam\data\ctrl_ebbCONTROLLER_1.curve
│ │ ├ 8b4. Filter Gain : 0.95000 
│ │ ├ 8b5. Up Limit : 1.20000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
│ ├ 8b. Stages 3 
│ │ ├ 8b1. Input Var : Brake 
│ │ ├ 8b2. Combinator Mode : Mult 
│ │ ├ 8b3. Lut : 
content\cars\ks_alfa_romeo_giulia_gtam\data\ctrl_ebbCONTROLLER_2.curve
│ │ ├ 8b4. Filter Gain : 0.95000 
│ │ ├ 8b5. Up Limit : 1.20000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ └ └ 8b8. Const Value : 0.00000 
├ 9. Controllers EBB [x] : None 
├ 10. Steer Brake Controller : None 
├ 11. Troque Controller EBB : None 
├ 12. EBB Mode : ebbDisabled 
├ 13. EBB Front Multiplier 1.10000 
└ 14. EBB Min Speed : 0.00000
```

### <span id="page-17-0"></span>**Lancia Delta HF Integrale EVO II ( slug : ks\_lancia\_delta\_hf\_integrale\_evo\_ii )**

```
├ 1. Total Torque : 2800.00000
├ 2. Front Bias : 0.78000 
├ 3. Hand Brake Torque : 1300.00000 
├ 4. Has Cockpit Bias : false 
├ 5. Bias Step : 0.00000 
├ 6. Front Compound Path : None 
├ 7. Rear Compound path : None
├ 8. Controller EBB 
│ ├ 8a. Name : None 
│ ├ 8b. Stages 1 
│ │ ├ 8b1. Input Var : LoadSpreadLF 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_lancia_delta_hf_integrale_evo_ii\data\ctrl_ebbCONTROLLER
_0.curve
│ │ ├ 8b4. Filter Gain : 0.01000 
│ │ ├ 8b5. Up Limit : 1.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
│ ├ 8b. Stages 2 
│ │ ├ 8b1. Input Var : Brake 
│ │ ├ 8b2. Combinator Mode : Mult 
│ │ ├ 8b3. Lut : 
content\cars\ks_lancia_delta_hf_integrale_evo_ii\data\ctrl_ebbCONTROLLER
_1.curve
│ │ ├ 8b4. Filter Gain : 0.95000 
│ │ ├ 8b5. Up Limit : 1.20000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
├ 9. Controllers EBB [x] : None 
├ 10. Steer Brake Controller : None 
├ 11. Troque Controller EBB : None 
├ 12. EBB Mode : ebbDisabled 
├ 13. EBB Front Multiplier 1.20000 
└ 14. EBB Min Speed : 0.00000
```

#### <span id="page-17-1"></span>**Ferrari 296 GT3**

```
├ 1. Total Torque : 4300.00000
├ 2. Front Bias : 65.00000 
├ 3. Hand Brake Torque : 200.00000 
├ 4. Has Cockpit Bias : true 
├ 5. Bias Step : 0.20000 
├ 6. Front Compound Path 1 : 
content\cars\common_phsx\brakes\racing\racing_GT3_pad2.brakes 
├ 7. Rear Compound path 2 : 
content\cars\common_phsx\brakes\racing\racing_GT3_pad2.brakes 
├ 8. Controllers EBB [x] : None 
├ 9. Controller EBB : None
```

```
├ 10. Steer Brake Controller : None 
├ 11. Troque Controller EBB : None 
├ 12. EBB Mode : ebbDisabled 
├ 13. EBB Front Multiplier 0.00000 
└ 14. EBB Min Speed : 0.00000
```

#### <span id="page-18-0"></span>**Ferrari SF25**

```
├ 1. Total Torque : 5500.00000
├ 2. Front Bias : 54.00000 
├ 3. Hand Brake Torque : 0.00000 
├ 4. Has Cockpit Bias : true 
├ 5. Bias Step : 0.10000 
├ 6. Front Compound Path : None 
├ 7. Rear Compound path : None 
├ 8. Controller EBB : None
├ 9. Controllers EBB 1 
│ ├ 8a. Name : Mig0 
│ ├ 8b. Stages 1 
│ │ ├ 8b1. Input Var : Brake 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_migration_0.c
urve
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
│ ├ 8b. Stages 2 
│ │ ├ 8b1. Input Var : ErsCoastTorque 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_KERStorque.cu
rve 
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ └ └ 8b8. Const Value : 0.00000 
├ 8. Controllers EBB 2 
│ ├ 8a. Name : Mig2 
│ ├ 8b. Stages 1 
│ │ ├ 8b1. Input Var : Brake 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_migration_2.c
urve
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
│ ├ 8b. Stages 2
```

```
│ │ ├ 8b1. Input Var : ErsCoastTorque 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_KERStorque.cu
rve 
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ └ └ 8b8. Const Value : 0.00000 
├ 8. Controllers EBB 3 
│ ├ 8a. Name : Mig4 
│ ├ 8b. Stages 1 
│ │ ├ 8b1. Input Var : Brake 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_migration_4.c
urve
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
│ ├ 8b. Stages 2 
│ │ ├ 8b1. Input Var : ErsCoastTorque 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_KERStorque.cu
rve 
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ └ └ 8b8. Const Value : 0.00000 
├ 8. Controllers EBB 4 
│ ├ 8a. Name : Mig6 
│ ├ 8b. Stages 1 
│ │ ├ 8b1. Input Var : Brake 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_migration_6.c
urve
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
│ ├ 8b. Stages 2 
│ │ ├ 8b1. Input Var : ErsCoastTorque 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_KERStorque.cu
rve 
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
```

```
│ │ ├ 8b7. Current Value : 0.00000 
│ └ └ 8b8. Const Value : 0.00000 
├ 8. Controllers EBB 5 
│ ├ 8a. Name : Mig8 
│ ├ 8b. Stages 1 
│ │ ├ 8b1. Input Var : Brake 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_migration_8.c
urve
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ │ └ 8b8. Const Value : 0.00000 
│ ├ 8b. Stages 2 
│ │ ├ 8b1. Input Var : ErsCoastTorque 
│ │ ├ 8b2. Combinator Mode : Add 
│ │ ├ 8b3. Lut : 
content\cars\ks_ferrari_sf_25\data\kers\ebb\ebb_controller_KERStorque.cu
rve 
│ │ ├ 8b4. Filter Gain : 0.90000 
│ │ ├ 8b5. Up Limit : 10.00000 
│ │ ├ 8b6. Down Limit : 0.00000
│ │ ├ 8b7. Current Value : 0.00000 
│ └ └ 8b8. Const Value : 0.00000 
├ 10. Steer Brake Controller : None 
├ 11. Troque Controller EBB : None 
├ 12. EBB Mode : ebbDynamicControllerRelative 
├ 13. EBB Front Multiplier 0.00000 
└ 14. EBB Min Speed : 0.00000
```

# <span id="page-21-0"></span>**2. Brakes [ .brakes ]**

# <span id="page-21-1"></span>**A. Description**

#### <span id="page-21-2"></span>**I. General Description**

The **Brakes** asset defines the microscopic physical properties, thermal dynamics, and wear characteristics of the individual hardware components (disks/rotors and pads) on a specific wheel or axle.

While the previous BrakeSystem asset manages macroscopic commands, bias, and electronics, the Brakes asset handles the actual physics of friction and heat. It simulates how brake pads grab the disks, how heat builds up during intense deceleration, how ambient airflow and rain cool the components down, and how the braking performance degrades due to overheating (fade) or physical wear over time.

# <span id="page-21-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The parameters in this file dictate the endurance, consistency, and tactile feel of the brakes under racing conditions:

- **• Brake Fade & Optimal Temperature Window:** Defines how temperature fluctuations change the friction coefficient. Brakes that are too cold or too hot will lose stopping power, drastically altering stopping distances.
- **• Thermal Management & Cooling Strategy:** Controls how fast the brakes heat up and shed energy. This directly influences how hard a driver can push lap after lap, and dictates if cooling ducts need adjustment.
- **• Brake Wear & Lifespan:** Determines the consumption rate of pads and disks, which is vital for endurance racing strategy where brake swaps might be necessary.
- **• Weather Adaptability:** Governs how environmental factors like rain disrupt both the cooling rate and the friction surface.

#### <span id="page-21-4"></span>**III. Key Architecture & Data Fields Explained**

The data in this schema is structured into three fundamental categories: **Thermal Modeling**, **Wear & Dimensions**, and the **Friction Performance Curve**.

#### <span id="page-21-5"></span>**1 - THERMAL MODELING & HEAT DISSIPATION**

- **• Cool Transfer & Cool Speed Factor:** Base coefficients for convective cooling. Cool Transfer sets the ambient cooling rate, while Cool Speed Factor dictates how much faster the brakes cool as vehicle velocity increases (forcing more air through the brake ducts).
- **• Rain Cool Factor:** Modifies the cooling rate when the track is wet, as water spraying onto the brakes drastically increases heat dissipation.

- **• Emissivity:** The radiant heat efficiency of the brake material, simulating how much heat energy is emitted as infrared radiation (crucial at glowing, hightemperature states).
- **• Surface:** The physical surface area of the brake assembly exposed to airflow.
- **• Thermal Capacity & Core Thermal Capacity:** The amount of heat energy required to raise the temperature of the brake surface and the internal "core" mass. Higher capacity means the brakes heat up more slowly but take longer to cool down.
- **• Thermal Conductivity & Conduction Thickness:** Controls the rate of heat transfer from the friction surface into the core of the brake disk.

# <span id="page-22-0"></span>**2 - DIMENSIONS, WEAR, AND DEGRADATION (M M = PER MILLIMETER)**

- **• Disk / Pad Thickness:** The initial, brand-new thickness of the brake disk and pads (typically in millimeters).
- **• Disk / Pad Consumption Rate:** The speed at which material is worn away relative to friction and heat cycles.
- **• T Reference Wear:** The reference temperature at which normal wear calculations occur. Exceeding this temperature usually spikes the wear exponentially.
- **• Perf Decrease M M:** The percentage drop in braking performance or friction for every millimeter of pad/disk material lost to wear.
- **• Mu Reduction M M:** The literal decrease of the friction coefficient (\$\mu\$) as the pads and disks get thinner.
- **• Area Reduction M M:** The reduction of effective pad contact surface area as the components wear down.
- **• Gamma Correction M M:** A scaling factor that non-linearly adjusts how wear alters the brake feel and performance curves over time.

#### <span id="page-22-1"></span>**3 - PERF CURVE (FRICTION COEFFICIENT VS. TEMPERATURE)**

This is a look-up table mapping Temperature (X-axis in °C) to Performance Efficiency (Y-axis where 1.000 = 100% target friction). It dictates the "sweet spot" of the brake compound.

#### <span id="page-22-2"></span>**IV. Interpretation of Asset Implementation & Data Profiles**

Depending on the vehicle category and simulation depth, the deployment of .brakes files generally follows one of two implementation profiles:

# <span id="page-22-3"></span>**PROFILE A: SPLIT FRONT/REAR AXLE CONFIGURATIONS (E.G., VINTAGE/ ROAD CARS)**

In setups where front and rear hardware are separated into distinct files, the simulation treats the axles as independent thermal entities.

- **• Axle Balancing:** Developers can mirror the properties exactly (as seen in some classic vehicles where front and rear drums or basic disks share structural dimensions) or modify them to reflect different rotor sizes.
- **• Thermal Synchronization:** Separate files allow the front brakes to face realistic, intense thermal loading (due to forward weight transfer) while the rear brakes are modeled with lower heat accumulation or distinct cooling properties.

# <span id="page-23-0"></span>**PROFILE B: SINGLE SHARED COMPOUND PROFILES & ENDURANCE PADS (E.G., RACING GT3)**

For modern racing environments—often denoted by specific naming conventions like \_pad1, \_pad2 (representing alternative endurance, sprint, or wet-weather friction compounds)—the simulation frequently utilizes a single master .brakes asset applied globally across the vehicle.

- **• Compound Swaps:** In this scenario, switching files changes the fundamental chemistry of the pads vehicle-wide. For example, a \_pad2 compound might represent a long-distance endurance pad characterized by lower consumption rates (Pad Consumption Rate) and a wider, flatter thermal efficiency window, albeit at the cost of a slightly lower maximum friction coefficient (µ).
- **• Unified Thermal Performance:** A shared file applies identical material limits (such as T Reference Wear and Thermal Capacity) globally, leaving the volumetric difference in heat handling to be modulated purely by the car's distinct front/rear brake duct settings.

#### <span id="page-23-1"></span>**READING THE PERFORMANCE CURVE TREND**

The performance curve look-up table translates directly to driver feel and pedal consistency on track:

- **• The Bite Threshold (0°C 200°C):** A high efficiency value (*0.90+*) at low temperatures indicates a street-friendly or versatile compound that works instantly without requiring a warm-up phase. Modern carbon-ceramic or pure racing pads will often show a massive dip here (0.40 - 0.60), requiring aggressive warming tactics.
- **• The Sweet Spot (300°C 600°C):** The plateau where the curve hits its absolute maximum (*1.000*). A wider plateau indicates an easy-to-manage brake system that provides a consistent stopping distance over a broad operational window.
- **• Thermal Fade Zone (700°C+):** The rate at which the curve drops at extreme temperatures defines the severity of the brake fade. A gradual taper allows the driver to feel the car losing stopping power safely, while a sharp drop-off causes catastrophic brake failure under heavy racing conditions.

#### <span id="page-23-2"></span>**B. Schema**

├ 1. Cool Transfer : float ├ 2. Torque K : float ├ 3. Cool Speed Factor : float ├ 4. Rain Cool Factor : float

├ 5. Emissivity : float

├ 6. Surface : float ├ 7. Thermal Capacity : float ├ 8. Core Thermal Capacity : float ├ 9. Thermal Conductivity : float ├ 10. Conduction Thickness : float ├ 11. Disk Consumption Rate : float ├ 12. Pad Consumption Rate : float ├ 13. Disk Thickness : float ├ 14. Pad Thickness : float ├ 15. Perf Decrease M M : float ├ 16. Gamma Correction M M : float ├ 17. Mu Reduction M M : float ├ 18. Area Reduction M M : float ├ 19. T Reference Wear : float

#### <span id="page-24-0"></span>**C. Measurement Units & Descriptions**

└ 20. Perf Curve : string - path

| ID | Name                  | Unit of Measurement         | Description                                                                                                                                                                             |
|----|-----------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. | Cool Transfer         | Coeffi<br>cient ( W/K )     | Base ambient cooling rate; defines<br>how fast the brakes shed heat to<br>the surrounding air when the<br>vehicle is completely stationary.                                             |
| 2. | Torque Conversion / K | Dimensionless Factor        | Mechanical torque conversion<br>multiplier; scales how effi<br>ciently<br>hydraulic line pressure translates<br>into raw stopping torque.                                               |
| 3. | Cool Speed Factor     | Coeffi<br>cient             | Airflow cooling multiplier; dictates<br>the linear or non-linear scaling of<br>heat dissipation as the vehicle<br>speed increases.                                                      |
| 4. | Rain Cool Factor      | Dimensionless Ratio         | Wet-weather cooling modifier;<br>amplifies the global heat<br>dissipation rate to simulate rain<br>and track water spray striking the<br>brake assembly.                                |
| 5. | Emissivity            | Dimensionless ( 0.0 - 1.0 ) | Thermal radiation effi<br>ciency ( );<br>ε<br>defines how effectively the brake<br>material radiates infrared heat,<br>becoming highly critical at<br>glowing, high-temperature states. |
| 6. | Surface               | 2<br>m ( Square meters )    | Total physical exposed surface<br>area of the brake disc/assembly;<br>larger surfaces naturally facilitate<br>faster convective cooling.                                                |
| 7. | Thermal Capacity      | J/K or J/°C                 | Heat storage capacity of the thin<br>outer friction surface layer;<br>determines how quickly the<br>contact zone heats up under<br>friction.                                            |

| ID  | Name                    | Unit of Measurement        | Description                                                                                                                                                      |
|-----|-------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 8.  | Core Thermal Capacity   | J/K or J/°C                | Heat storage capacity of the<br>internal "core" mass of the brake<br>disc; serves as the main thermal<br>reservoir absorbing energy from<br>the surface.         |
| 9.  | Thermal Conductivity    | W/(m-K) or Coeffi<br>cient | Internal heat transfer rate; controls<br>how fast heat energy moves from<br>the hot outer friction surface into<br>the cooler internal core.                     |
| 10. | Conduction Thickness    | m (Meters) or mm           | Physical distance/depth<br>representing the boundary layer<br>for internal heat transfer between<br>the surface friction node and the<br>core mass.              |
| 11. | Disk Consumption Rate   | Wear Coeffi<br>cient       | Material wear rate of the brake<br>disc/rotor, tracking physical<br>thickness reduction relative to<br>temperature and kinetic energy<br>absorption cycles.      |
| 12. | Pad Consumption Rate    | Wear Coeffi<br>cient       | Material wear rate of the brake<br>pads, tracking friction compound<br>depletion relative to temperature<br>and kinetic energy absorption<br>cycles.             |
| 13. | Disk Thickness          | mm ( Millimeters )         | The initial, brand-new physical<br>structural thickness of the brake<br>disc/rotor.                                                                              |
| 14. | Pad Thickness           | mm ( Millimeters )         | The initial, brand-new physical<br>thickness of the wearable friction<br>material layer on the brake pad.                                                        |
| 15. | Perf Decrease M M       | ) −1<br>% / mm ( mm        | Global percentage drop in overall<br>braking effi<br>ciency and biting<br>performance for every single<br>millimeter of total pad/disk<br>material lost to wear. |
| 16. | Gamma Correction M<br>M | Dimensionless Exponent     | Non-linear scaling factor;<br>progressively adjusts how material<br>wear non-linearly alters pedal<br>feedback, compliance, and friction<br>behavior over time.  |
| 17. | Mu Reduction M M        | Δμ<br>/mm                  | The literal linear reduction of the<br>raw friction coeffi<br>cient (\$\mu\$)<br>applied as the pads and discs<br>become thinner.                                |
| 18. | Area Reduction M M      | or 2 /mm<br>m<br>%<br>/mm  | The progressive reduction of the<br>effective pad-to-disc contact<br>surface area as the pad material<br>shaves down.                                            |

| ID  | Name             | Unit of Measurement    | Description                                                                                                                                                                 |
|-----|------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 19. | T Reference Wear | °C ( Degress Celsius ) | Threshold reference temperature;<br>defines the thermal boundary<br>above which component wear<br>rates begin to spike exponentially.                                       |
| 20. | Perf Curve       | None ( File path )     | File path pointing to an<br>external .curve look-up table<br>mapping raw operating<br>temperature (X-axis in °C) to<br>friction coeffi<br>cient effi<br>ciency (Y<br>axis). |

#### <span id="page-26-0"></span>**D. Example data**

#### <span id="page-26-1"></span>**I. Chosen Brakes for Example**

- Vintage Road Front ( slug : vintage\_road\_front ) / Vintage Road Rear ( vintage\_road\_rear )
- Racing GT3 [ Pad 2 ] ( slug : racing\_gt3\_pad2 )

# <span id="page-26-2"></span>**II. Example**

#### <span id="page-26-3"></span>**Vintage Road [ Front ]**

- ├ 1. Cool Transfer : 1.30000
- ├ 2. Torque K : 0.70000
- ├ 3. Cool Speed Factor : 1.50000 ├ 4. Rain Cool Factor : 0.80000
- ├ 5. Emissivity : 0.70000
- ├ 6. Surface : 0.20000
- ├ 7. Thermal Capacity : 100.00000
- ├ 8. Core Thermal Capacity : 1600.00000
- ├ 9. Thermal Conductivity : 250.00000
- ├ 10. Conduction Thickness : 0.00500
- ├ 11. Disk Consumption Rate : 0.18000
- ├ 12. Pad Consumption Rate : 0.19800
- ├ 13. Disk Thickness : 32.00000
- ├ 14. Pad Thickness : 29.00000
- ├ 15. Perf Decrease M M : 15.00000
- ├ 16. Gamma Correction M M : 1.50000
- ├ 17. Mu Reduction M M : 0.01000
- ├ 18. Area Reduction M M : 0.16000
- ├ 19. T Reference Wear : 600.00000
- └ 20. Perf Curve :

content\cars\common\_phsx\brakes\vintage\tcurve\_vintage\_front.curve

|    | °C Temperature ( X ) | Friction Coeffi<br>cient Modifier ( Y ) |
|----|----------------------|-----------------------------------------|
| P0 | 0.000                | 0.900                                   |
| P1 | 100.000              | 0.950                                   |

|    | °C Temperature ( X ) | Friction Coeffi<br>cient Modifier ( Y ) |
|----|----------------------|-----------------------------------------|
| P2 | 500.000              | 0.980                                   |
| P3 | 600.000              | 1.000                                   |
| P4 | 800.000              | 0.980                                   |
| P5 | 900.000              | 0.950                                   |
| P6 | 1000.000             | 0.850                                   |
| P7 | 1200.000             | 0.800                                   |

*Friction Coefficient Modifier = Performance Efficiency where 1.000 = 100%*

#### <span id="page-27-0"></span>**Vintage Road [ Rear ]**

├ 1. Cool Transfer : 1.30000

├ 2. Torque K : 0.70000

├ 3. Cool Speed Factor : 1.50000 ├ 4. Rain Cool Factor : 0.80000

├ 5. Emissivity : 0.70000 ├ 6. Surface : 0.20000

├ 7. Thermal Capacity : 100.00000

├ 8. Core Thermal Capacity : 1600.00000 ├ 9. Thermal Conductivity : 250.00000 ├ 10. Conduction Thickness : 0.00500 ├ 11. Disk Consumption Rate : 0.18000 ├ 12. Pad Consumption Rate : 0.19800

├ 13. Disk Thickness : 32.00000

├ 14. Pad Thickness : 29.00000

├ 15. Perf Decrease M M : 15.00000

├ 16. Gamma Correction M M : 1.50000

├ 17. Mu Reduction M M : 0.01000

├ 18. Area Reduction M M : 0.16000

├ 19. T Reference Wear : 600.00000

└ 20. Perf Curve :

content\cars\common\_phsx\brakes\vintage\tcurve\_vintage\_rear.curve

|    | °C Temperature ( X ) | Friction Coeffi<br>cient Modifier ( Y ) |
|----|----------------------|-----------------------------------------|
| P0 | 0.000                | 0.900                                   |
| P1 | 100.000              | 0.950                                   |
| P2 | 500.000              | 0.980                                   |
| P3 | 600.000              | 1.000                                   |
| P4 | 800.000              | 0.980                                   |
| P5 | 900.000              | 0.950                                   |
| P6 | 1000.000             | 0.850                                   |

|    | °C Temperature ( X ) | Friction Coeffi<br>cient Modifier ( Y ) |  |
|----|----------------------|-----------------------------------------|--|
| P7 | 1200.000             | 0.800                                   |  |

*Friction Coefficient Modifier = Performance Efficiency where 1.000 = 100%*

#### <span id="page-28-0"></span>**Racing GT3 [ Pad 2 ]**

├ 1. Cool Transfer : 0.90000

├ 2. Torque K : 0.70000

├ 3. Cool Speed Factor : 1.60000 ├ 4. Rain Cool Factor : 0.80000

├ 5. Emissivity : 0.70000 ├ 6. Surface : 0.40000

├ 7. Thermal Capacity : 100.00000

├ 8. Core Thermal Capacity : 1600.00000 ├ 9. Thermal Conductivity : 250.00000 ├ 10. Conduction Thickness : 0.00500 ├ 11. Disk Consumption Rate : 0.01050 ├ 12. Pad Consumption Rate : 0.02100

├ 13. Disk Thickness : 32.00000 ├ 14. Pad Thickness : 29.00000

├ 15. Perf Decrease M M : 13.00000

├ 16. Gamma Correction M M : 1.00000

├ 17. Mu Reduction M M : 0.01000

├ 18. Area Reduction M M : 0.08000

├ 19. T Reference Wear : 500.00000

└ 20. Perf Curve :

content\cars\common\_phsx\brakes\racing\tcurve\_racing\_GT3\_pad2

|     | °C Temperature ( X ) | Friction Coeffi<br>cient Modifier ( Y ) |  |
|-----|----------------------|-----------------------------------------|--|
| P0  | -84.050              | 0.774                                   |  |
| P1  | -0.905               | 0.839                                   |  |
| P2  | 39.477<br>0.914      |                                         |  |
| P3  | 88.596               | 0.952                                   |  |
| P4  | 121.867              | 0.967                                   |  |
| P5  | 156.821              | 0.974                                   |  |
| P6  | 203.872              | 0.978                                   |  |
| P7  | 252.036              | 0.980                                   |  |
| P8  | 303.284<br>0.980     |                                         |  |
| P9  | 365.345<br>0.980     |                                         |  |
| P10 | 380.803<br>0.979     |                                         |  |
| P11 | 443.598              | 0.977                                   |  |

|     | °C Temperature ( X ) | Friction Coeffi<br>cient Modifier ( Y ) |  |
|-----|----------------------|-----------------------------------------|--|
| P12 | 526.801              | 0.973                                   |  |
| P13 | 599.594              | 0.966                                   |  |
| P14 | 722.684              | 0.945                                   |  |
| P15 | 781.584              | 0.936                                   |  |
| P16 | 849.036              | 0.923                                   |  |
| P17 | 908.993              | 0.898                                   |  |
| P18 | 972.698              | 0.854                                   |  |
| P19 | 1047.645             | 0.734                                   |  |
| P20 | 1245.218             | 0.567                                   |  |

*Friction Coefficient Modifier = Performance Efficiency where 1.000 = 100%*

# <span id="page-30-0"></span>3. Car Data [.car ]

#### <span id="page-30-1"></span>A. Description

# <span id="page-30-2"></span>I. General Description

The **Car Data** asset is the primary foundational master file for a vehicle's physics package in the simulation engine. If BrakeSystem and Brakes represent localized hardware components, Car Data represents the physical carcass, weight distribution, structural constraints, and regulatory rules of the entire vehicle.

It acts as the structural blueprint that holds all other modular components (engine, tires, suspension, and brakes) together by defining how the global mass moves, how the center of gravity shifts, and how the physical dimensions interact with the environment.

#### <span id="page-30-3"></span>II. Area of Influence / Impact on Vehicle Dynamics

The properties configured within the CAR DATA asset dictate the base handling DNA and fundamental physical limits of the vehicle before any specific aerodynamic downforce or mechanical grip is added:

- Weight Distribution & Inertia: Governs the vehicle's resistance to rotational changes (pitch, roll, and yaw). It directly dictates how quick the car changes direction and how much weight transfers under braking, acceleration, or cornering.
- **Dimensional Footprint (Track & Wheelbase):** Determines the baseline mechanical stability. A wider track increases cornering stability, while a longer wheelbase stabilizes the car at high speeds but reduces low-speed agility.
- **Driver Environment & Ergonomics:** Configures the driver's perspective (camera placement, cockpit nodes) and controls the operational boundaries of steering inputs.
- **Fuel Weight Dynamics:** Simulates dynamic mass changes over a race stint. As fuel burns off, the overall vehicle weight drops and the center of gravity shifts, drastically altering handling characteristics over time.

#### <span id="page-30-4"></span>III. Key Architecture & Data Fields Explained

The parameters in this schema are universally categorized into **Mass & Inertia**, **Dimensions & Offsets**, and **Fuel & Regulation Logistics**.

#### <span id="page-30-5"></span>1 - GLOBAL MASS & INERTIA PROPERTIES

- Total Mass / Dry Weight: The baseline mass of the vehicle without fuel, driver, or fluids (expressed in  $\kappa_G$ ). This is the fundamental variable for F=MA calculations.
- Inertia (Pitch, Roll, Yaw Vectors): Critical tensors  $(I_x, I_y, I_z)$  defining how mass is distributed away from the center of gravity. High polar inertia means a car resists spinning but is hard to catch once it breaks traction.

- **• Center of Gravity Height (CG Height):** The vertical position of the balance point. Lower CG decreases body roll and load transfer across tires, significantly increasing overall cornering potential.
- **• Weight Bias (Front/Rear %):** The static balance of the car at rest (e.g. 45/55 for mid-engine layouts). It underpins the car's natural handling bias (understeer vs. oversteer tendency).

# <span id="page-31-0"></span>**2 - DIMENSIONS, TRACK AND ALIGNEMENT COORDINATES**

- **• Wheelbase:** The linear distance between the center lines of the front and rear axles.
- **• Track Width (Front/Rear):** The lateral distance between the center points of the left and right tires on an axle.
- **• Graphics / Collision Mesh Offsets:** Coordinates that align the structural 3D model and physical hitbox with the theoretical center of gravity, ensuring visual impacts and ground scraping clip accurately.
- **• Steer Lock / Rack Ratio:** Max steering angle of the front wheels and the corresponding ratio to the steering wheel column. Defines the vehicle's turning circle and quickness of steering inputs.

#### <span id="page-31-1"></span>**3 - FUEL MANAGEMENT & CONSUMABLES**

- **• Fuel Tank Capacity:** The maximum volume of fuel the car can physically hold (typically in Liters or Gallons).
- **• Fuel Tank Position (X, Y, Z Coordinates):** The exact physical location of the fuel payload inside the chassis. Crucial for calculating how the center of gravity and weight balance shift as the fuel burns down.
- **• Driver Mass Toggle:** Dictates whether the weight of an average driver (e.g., standard regulatory 75 kg - 80 kg) is automatically appended to the physical mass calculations.

#### <span id="page-31-2"></span>**IV. Short Interpretation of Asset Implementation**

When analyzing a vehicle's physics using the Car Data profile, you can immediately predict its handling characteristics through basic parameter archetypes:

- **• The Prototype/Open-Wheel Profile:** Characterized by ultra-low total mass (< 800 kg), a wide track width, and an incredibly low Center of Gravity Height. The inertia tensors are compressed closely to the center, yielding instantaneous directional response.
- **• The GT3/Production Profile:** Features higher total mass (1200 kg 1400 kg), higher CG positions, and a sprawling wheelbase. These vehicles experience heavy weight transfer, demanding careful management of pitch and roll stiffness elsewhere in the setup.
- **• The Endurance Strategy Vector:** By looking at the Fuel Tank Capacity paired with its structural 3D coordinates, you can see how heavily a full stint will punish tire wear. If the tank is behind the rear axle, a full fuel load will temporarily shift the weight bias

significantly rearward, introducing entry understeer that slowly fades into snappier oversteer as the tank empties.

#### <span id="page-32-0"></span>**B. Schema**

```
├ 1. Screen Name : string
├ 2. General : object
│ ├ 2a. Screen Name : string
│ ├ 2b. Total Mass : float
│ ├ 2c. Tank Position : x, y, z float 
│ ├ 2d. Fuel : float
│ ├ 2e. Max Fuel : float
│ ├ 2f. Efficiency : float
│ ├ 2g. Kg Per Liter : float
│ ├ 2h. Body Box Sizes : x, y, z float 
│ ├ 2i. Pickup Front Height : float
│ ├ 2j. Pickup Rear Height : float
│ ├ 2k. Check Rules : boolean
│ ├ 2l. Minimum Height : float
│ ├ 2m. Torsional Stiffness : float
│ ├ 2n. Torsional Damping : float
│ ├ 2o. Body Mesh Offset : object
│ │ ├ 2o1. Position : x, y, z float 
│ │ ├ 2o2. Rotation : x, y, z, float 
│ └ └ 2o3. Scale : x, y, z float 
├ 3. General Path : string - path 
├ 4. Suspensions : object
│ ├ 4a. Wheel Base : float
│ ├ 4b. Longitudinal Cg Location : float
│ ├ 4c. Base Y Front : float
│ ├ 4d. Base Y Rear : float
│ ├ 4e. Track Front : float
│ ├ 4f. Track Rear : float
│ ├ 4g. Damage : object
│ │ ├ 4g1. Min Velocity : float
│ │ ├ 4g2. Gain : float
│ │ ├ 4g3. Max Damage : float
│ │ └ 4g4. Debug Log : boolean
│ ├ 4h. Coilover Front path : string - path 
│ ├ 4i. Coilover Rear Path : string - path 
│ ├ 4j. Front Suspension Path : string - path 
│ ├ 4k. Rear Suspension Path : string - path 
│ ├ 4l. Heavy Springs [x] : object | Can have multiple Heavy Springs, 
where x can be 1, 2, 3, … 
│ │ ├ 4l1. Spring Rate : float
│ │ ├ 4l2. Progressive Sprint Rate : float
│ │ ├ 4l3. Bump Stop Up : object
│ │ │ ├ 4l3a. Range : float
│ │ │ ├ 4l3b. Reference : float
│ │ │ ├ 4l3c. Force : float
│ │ │ ├ 4l3d. Gamma : float
│ │ │ ├ 4l3e. Length : float
│ │ │ └ 4l3f. Damping : float
│ │ ├ 4l4. Bump Stop Down : object
```

```
│ │ │ ├ 4l4a. Range : float
│ │ │ ├ 4l4b. Reference : float
│ │ │ ├ 4l4c. Force : float
│ │ │ ├ 4l4d. Gamma : float
│ │ │ ├ 4l4e. Length : float
│ │ │ └ 4l4f. Damping : float
│ │ ├ 4l5. Collar Position : float
│ │ ├ 4l6. Damper : object
│ │ │ ├ 4l6a. Fast : object
│ │ │ │ ├ 4l6a1. Bump : float
│ │ │ │ └ 4l6a2. Rebound : float
│ │ │ ├ 4l6b. Slow : object
│ │ │ │ ├ 4l6b1. Bump : float
│ │ │ │ └ 4l6b2. Rebound : float
│ │ │ ├ 4l6c. Fast Threshold Bump : float
│ │ │ ├ 4l6d. Fast Threshold Rebound : float
│ │ │ ├ 4l6e. Cooling Surface : float
│ │ │ ├ 4l6f. Nominal Force : float
│ │ │ ├ 4l6g. Min Stress Fatigue : float
│ │ │ ├ 4l6h. Max Stress Fatigue : float
│ │ │ ├ 4l6i. Thermal Capacity : float
│ │ │ ├ 4l6j. Heat Transfer Coefficient : float
│ │ │ ├ 4l6k. Lut List : string - path 
│ │ │ └ 4l6l. Damper Lut Scale : string - path 
│ │ ├ 4l7. Helper K : float
│ │ ├ 4l8. Helper Range : float
│ │ ├ 4l9. Rod Controllers : object with an array of stages within 
│ │ │ ├ 4l9a. Name : string
│ │ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ │ ├ 4l9b1. Input Var : enum
│ │ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ │ ├ 4l9b5. Up Limit : float
│ │ │ │ ├ 4l9b6. Down Limit : float
│ │ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ └ 4l9b8. Const Value : float
│ ├ 4m. Arb Front : object
│ │ ├ 4m1. Stiffness : float
│ │ ├ 4m2. Controller : object
│ │ │ ├ 4l9a. Name : string
│ │ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ │ ├ 4l9b1. Input Var : enum
│ │ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ │ ├ 4l9b5. Up Limit : float
│ │ │ │ ├ 4l9b6. Down Limit : float
│ │ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ └ 4l9b8. Const Value : float 
│ ├ 4n. Arb Rear : object
│ │ ├ 4n1. Stiffness : float
│ │ ├ 4n2. Controller : object
│ │ │ ├ 4l9a. Name : string
```

```
│ │ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ │ ├ 4l9b1. Input Var : enum
│ │ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ │ ├ 4l9b5. Up Limit : float
│ │ │ │ ├ 4l9b6. Down Limit : float
│ │ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ └ 4l9b8. Const Value : float
│ ├ 4o. Flex Bar Front : object
│ │ ├ 4o1. Stiffness : float
│ │ ├ 4o2. Controller : object
│ │ │ ├ 4l9a. Name : string
│ │ │ ├ 4l9b. Stages [x] : float | Rod Controllers can have multiple 
stages 
│ │ │ │ ├ 4l9b1. Input Var : enum
│ │ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ │ ├ 4l9b5. Up Limit : float
│ │ │ │ ├ 4l9b6. Down Limit : float
│ │ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ └ 4l9b8. Const Value : float
│ ├ 4p. Flex Bar Rear : object
│ │ ├ 4p1. Stiffness : float
│ │ ├ 4p2. Controller : object with an array of stages within 
│ │ │ ├ 4l9a. Name : string
│ │ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ │ ├ 4l9b1. Input Var : enum
│ │ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ │ ├ 4l9b5. Up Limit : float
│ │ │ │ ├ 4l9b6. Down Limit : float
│ │ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ └ 4l9b8. Const Value : float
│ ├ 4q. Dampers Controller : object 
│ │ ├ 4q1. Wheel Gain : float
│ │ ├ 4q2. Heave Gain : float
│ │ ├ 4q3. Pitch Gain : float
│ │ ├ 4q4. Roll Gain : float
│ │ ├ 4q5. Front : object
│ │ │ ├ 4q5a. Base : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5b. Heave : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5c. Roll : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5d. Pitch : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5e. Max : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5f. Min : object
│ │ │ └ └ 4q5a1. Type : enum
```

```
│ │ ├ 4q6. Rear : object
│ │ │ ├ 4q5a. Base : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5b. Heave : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5c. Roll : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5d. Pitch : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5e. Max : object
│ │ │ │ └ 4q5a1. Type : enum
│ │ │ ├ 4q5f. Min : object
│ │ │ └ └ 4q5a1. Type : enum 
│ └ 4r. Has Dampers Cockpit Settings : boolean
├ 5. Drivetrain Path : string - path 
├ 6. Gearbox Path : string - path 
├ 7. Clutch Path : string - path 
├ 8. Engine Path : string - path 
├ 9. Brakes Path : string - path 
├ 10. Steering System : object
│ ├ 10a. Four W S Controllers : object with an array of stages within 
│ │ ├ 4l9a. Name : string
│ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ ├ 4l9b1. Input Var : enum
│ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ ├ 4l9b5. Up Limit : float
│ │ │ ├ 4l9b6. Down Limit : float
│ │ │ ├ 4l9b7. Current Value : float
│ └ └ └ 4l9b8. Const Value : float
├ 11. Electronics : object
│ ├ 11a. T C : object 
│ │ ├ 11a1. Has T C2 : boolean 
│ │ ├ 11a2. Frequency Hz : float
│ │ ├ 11a3. Min Speed Kmh : float
│ │ ├ 11a4. Gear Change Time : float
│ │ ├ 11a5. Min Cut Level : float
│ │ ├ 11a6. Max Cut Level : float
│ │ ├ 11a7. Settings [x] : object | T C can have multiple Settings 
│ │ │ ├ 11a7a. Min Slip Ratio : float
│ │ │ ├ 11a7b. Max Slip Ratio : float
│ │ │ ├ 11a7c. Ref Slip Angle Deg : float
│ │ │ ├ 11a7d. Engine Cut Level : float
│ │ │ ├ 11a7e. Angular A C Cgain : float
│ │ │ ├ 11a7f. Oversteer Gain : float
│ │ │ ├ 11a7g. Slip Angle Activation Deg : float
│ ├ 11b. A B S : object 
│ │ ├ 11b1. Settings [x] : object | A B S can have multiple Settings 
│ │ │ ├ 11b1a. Min Slip Ratio : float
│ │ │ ├ 11b1b. Max Slip Ratio : float
│ │ │ ├ 11b1c. Ref Slip Angle Deg : float
│ │ │ ├ 11b1d. Cut Level : float
│ │ │ ├ 11b1f. Max Torque Variation : float
│ │ ├ Frequency : float
```

```
│ │ ├ Channels : integer
│ │ ├ Min Speed Kmh : float 
│ ├ 11c. E D L : object 
│ │ ├ 11c1. Active : boolean
│ │ ├ 11c2. Brake Torque Power : float
│ │ ├ 11c3. Brake Torque Coast : float
│ │ ├ 11c4. Dead Zone Coast : float
│ │ ├ 11c5. Dead Zone Power : float
│ │ ├ 11c6. Max Spin Power : float
│ │ ├ 11c7. Max Spin Coaster : float
│ │ ├ 11c8. Min Speed : float
│ ├ 11d. E S P : object
│ │ ├ 11d1. Frequency Hz : float
│ │ ├ 11d2. Min Speed Kmh : float
│ │ ├ 11d3. Settings [x] : object | E S P can have multiple settings 
│ │ │ ├ 11d3a. Gain : float
│ │ │ ├ 11d3b. Steer Gain : float
│ │ │ ├ 11d3c. Min Steer Gain : float
│ │ │ ├ 11d3d. Steer Gain Max Speed : float
│ │ │ ├ 11d3e. Oversteer Gain : float
│ │ │ ├ 11d3f. Understeer Gain : float
│ │ │ ├ 11d3g. Max Slip Ratio : float
│ │ │ ├ 11d3h. Dead Zone : float
│ │ │ ├ 11d3i. Filter Gain : float
│ │ │ ├ 11d3j. Brake Perc : float
│ └ └ └ 11d3k. Brake Perc Activation : float
├ 12. Electronics Path : string - path 
├ 13. Controls : object
│ ├ 13a. Ff Mult : float
│ ├ 13b. Steer Lock : float
│ ├ 13c. Steer Ratio : float
│ ├ 13d. Linear Steer Rod Ratio : float
│ └ 13e. Steer Assist : float
├ 14. Box Colliders [x] : object | can have multiple Box Colliders 
│ ├ 14a. Center : x, y, z float
│ ├ 14b. Size : x, y, z float 
│ └ 14c. Pitch Rotation Deg : float
├ 15. Front Tyre Compounds [x] : string - path | can have multiple Front 
Tyre Compounds path 
├ 16. Rear Tyre Compounds [x] : string - path | can have multiple Rear 
Tyre Compounds path 
├ 17. Aero : object
│ ├ 17a. Slip Gain Multiple : float
│ ├ 17b. Speed Factor Mult : float
│ ├ 17c. Downforces [x] : object | can have multiple Downforces 
│ │ ├ 17c1. Position : x, y, z float 
│ │ ├ 17c2. Cl Gain : float
│ │ ├ 17c3. Cd Gain : float
│ │ ├ 17c4. Yaw Gain : float
│ │ ├ 17c5. Drag Per Cool Transfer : float
│ │ ├ 17c6. Damage C L [x] : string | can have multiple Damage C L
│ │ ├ 17c7. Damage C D [x] : string | can have multiple Damage C D 
│ │ ├ 17c8. Downforce Controllers [x] : object | can have multiple 
Downforce Controllers 
│ │ │ ├ 17c8a. Combinator Mode : enum
│ │ │ ├ 17c8b. Input : enum
```

```
│ │ │ ├ 17c8c. Filter : float
│ │ │ ├ 17c8d. Up Limit : float
│ │ │ ├ 17c8e. Down Limit : float
│ │ │ └ 17c8f. Lut : string - path 
│ │ ├ 17c9. Lift Per Front Angle : float
│ │ ├ 17c10. Lift Per Rear Angle : float
│ │ ├ 17c11. Drag Per Front Angle : float
│ │ ├ 17c12. Drag Per Rear Angle : float
│ │ ├ 17c13. Default Front Angle : float
│ │ └ 17c14. Default Rear Angle : float
│ ├ 17d. Front Lift : string - path 
│ ├ 17e. Rear Lift : string - path 
│ ├ 17f. Drag : string - path 
│ └ 17g. Wings Path [x] : string - path | can have multiple Wings Path 
├ 18. Drs : object 
│ ├ 18a. Ignore Zones : boolean
│ ├ 18b. Limit G : float
│ ├ 18c. Wing Connections [x] : object | can have multiple Wing 
Connections 
│ │ ├ 18c1. Mode : enum
│ │ ├ 18c2. Connected Wing : integer
│ │ ├ 18c3. Effect : float
│ │ ├ 18c4. Angle : float 
├ 19. Ers : object 
│ ├ 19a. Torque Lut : string - path 
│ ├ 19b. Coast Lut : string - path 
│ ├ 19c. Battery Charge Kj : float
│ ├ 19d. Has Button Override : boolean
│ ├ 19e. Max Kj Per Lap : float
│ ├ 19f. Max Charge Kj Per Lap : float
│ ├ 19g. Heat Charge Perc : float
│ ├ 19h. Heat Power Kw : float
│ ├ 19i. Default Power Controller Index : integer
│ ├ 19j. Power Controllers Front [x] : object | can have multiple Power 
Controllers Front 
│ │ ├ 4l9a. Name : string
│ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ ├ 4l9b1. Input Var : enum
│ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ ├ 4l9b5. Up Limit : float
│ │ │ ├ 4l9b6. Down Limit : float
│ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ 4l9b8. Const Value : float
│ ├ 19k. Power Controllers Rear [x] : object | can have multiple Power 
Controllers Rear 
│ │ ├ 4l9a. Name : string
│ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ ├ 4l9b1. Input Var : enum
│ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ ├ 4l9b5. Up Limit : float
```

```
│ │ │ ├ 4l9b6. Down Limit : float
│ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ 4l9b8. Const Value : float 
│ ├ 19l. Brake Rear Correction : float
│ ├ 19m. Has Cockpit Controls : boolean
│ ├ 19n. Cockpit Controls : object
│ │ ├ 19n1. Delivery Profile : boolean
│ │ ├ 19n2. Mgu H Mode : boolean
│ │ └ 19n3. Recovery : boolean
│ ├ 19o. Has Front Motors : boolean
│ ├ 19p. Front Motors : object
│ │ ├ 19p1. Torque Lut : string - path 
│ │ ├ 19p2 Discharge Time : float
│ │ ├ 19p3. Torque Vectoring Bias : float 
├ 20. Setup Limits : string path 
├ 21. Collider Mesh : string path 
├ 22. Body Mesh Offset : object
│ ├ 22a. Position : x, y, z float 
│ ├ 22b. Rotation: x, y, z float 
│ └ 22c. Scale : x, y, z float 
├ 23. Stock Setup : string path 
├ 24. Ai Setup : string path 
├ 25. Wet Setup : string path 
├ 26. Performance Modes [x] : object | can have multiple Performance 
Modes 
│ ├ 26a. Performance Mode Name : string
│ ├ 26b. Electronics Settings : object 
│ │ ├ 26b1. Tc1 : float
│ │ ├ 26b2. Tc2 : float
│ │ ├ 26b3. Abs : float
│ │ ├ 26b4. Esc : float
│ │ ├ 26b5. Ebb : float
│ │ ├ 26b6. Engine Map : float
│ │ ├ 26b7. Telemetry laps To Record : float
│ │ ├ 26b8. Turbo Boost Lv : float
│ │ ├ 26b9. Ers Deployment Map : float
│ │ ├ 26b10. Ers Recharge Lv : float
│ │ └ 26b11. Ers Heat Charging : float
│ ├ 26c. Brakes Settings : object 
│ │ ├ 26c1. Front Bias : float
│ │ ├ 26c2. Torque Multiplier : float
│ │ ├ 26c3. Brake Ducts [x] : float | can have multiple Brake Ducts 
│ ├ 26d. Damper Settings [x] : object | can have multiple Damper 
Settings 
│ │ ├ 26d1. Slow Bump : float
│ │ ├ 26d2. Fast Bump : float
│ │ ├ 26d3. Slow Rebound : float
│ │ └ 26d4. Fast Rebound : float
│ ├ 26e. Differential Data : object 
│ │ ├ 26e1. Type : enum
│ │ ├ 26e2. Power : float
│ │ ├ 26e3. Coast : float
│ │ ├ 26e4. Preload : float
│ │ ├ 26e5. Front Share : float
│ │ ├ 26e6. Torque Bias Ratio Power : float
│ │ ├ 26e7. Torque Bias Ratio Coast : float
```

```
│ │ ├ 26e8. Thermal Capacity : float
│ │ ├ 26e9. Surface : float
│ │ ├ 26e10. Heat Transfer Coeff : float
│ │ ├ 26e11. Wear Factor : float
│ │ ├ 26e12. Friction Reduction With T : float
│ │ └ 26e13. Friction Ref T : float 
│ ├ 26f. Four W D Differentials : object 
│ │ ├ 26f1. Front Diff : object 
│ │ │ ├ 26e1. Type : enum
│ │ │ ├ 26e2. Power : float
│ │ │ ├ 26e3. Coast : float
│ │ │ ├ 26e4. Preload : float
│ │ │ ├ 26e5. Front Share : float
│ │ │ ├ 26e6. Torque Bias Ratio Power : float
│ │ │ ├ 26e7. Torque Bias Ratio Coast : float
│ │ │ ├ 26e8. Thermal Capacity : float
│ │ │ ├ 26e9. Surface : float
│ │ │ ├ 26e10. Heat Transfer Coeff : float
│ │ │ ├ 26e11. Wear Factor : float
│ │ │ ├ 26e12. Friction Reduction With T : float
│ │ │ └ 26e13. Friction Ref T : float
│ │ ├ 26f2. Center Diff : object 
│ │ │ ├ 26e1. Type : enum
│ │ │ ├ 26e2. Power : float
│ │ │ ├ 26e3. Coast : float
│ │ │ ├ 26e4. Preload : float
│ │ │ ├ 26e5. Front Share : float
│ │ │ ├ 26e6. Torque Bias Ratio Power : float
│ │ │ ├ 26e7. Torque Bias Ratio Coast : float
│ │ │ ├ 26e8. Thermal Capacity : float
│ │ │ ├ 26e9. Surface : float
│ │ │ ├ 26e10. Heat Transfer Coeff : float
│ │ │ ├ 26e11. Wear Factor : float
│ │ │ ├ 26e12. Friction Reduction With T : float
│ │ │ └ 26e13. Friction Ref T : float 
│ │ ├ 26f3. Rear Diff : object 
│ │ │ ├ 26e1. Type : enum
│ │ │ ├ 26e2. Power : float
│ │ │ ├ 26e3. Coast : float
│ │ │ ├ 26e4. Preload : float
│ │ │ ├ 26e5. Front Share : float
│ │ │ ├ 26e6. Torque Bias Ratio Power : float
│ │ │ ├ 26e7. Torque Bias Ratio Coast : float
│ │ │ ├ 26e8. Thermal Capacity : float
│ │ │ ├ 26e9. Surface : float
│ │ │ ├ 26e10. Heat Transfer Coeff : float
│ │ │ ├ 26e11. Wear Factor : float
│ │ │ ├ 26e12. Friction Reduction With T : float
│ │ └ └ 26e13. Friction Ref T : float 
│ ├ 26g. Front Lock Controllers : object 
│ │ ├ 4l9a. Name : string
│ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ ├ 4l9b1. Input Var : enum
│ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ ├ 4l9b3. Lut : string - path
```

```
│ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ ├ 4l9b5. Up Limit : float
│ │ │ ├ 4l9b6. Down Limit : float
│ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ 4l9b8. Const Value : float 
│ ├ 26h. Center Lock Controllers : object 
│ │ ├ 4l9a. Name : string
│ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ ├ 4l9b1. Input Var : enum
│ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ ├ 4l9b5. Up Limit : float
│ │ │ ├ 4l9b6. Down Limit : float
│ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ 4l9b8. Const Value : float 
│ ├ 26i. Rear Lock Controllers : object 
│ │ ├ 4l9a. Name : string
│ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ ├ 4l9b1. Input Var : enum
│ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ ├ 4l9b5. Up Limit : float
│ │ │ ├ 4l9b6. Down Limit : float
│ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ 4l9b8. Const Value : float 
│ ├ 26j. Awd Clutches [x] : object | can have multiple Awd Clutches 
│ │ ├ 26j1. Position : integer
│ │ └ 26j2. Preload : float
│ ├ 26k. Turbo Controllers [x] : object with an array of stages within | 
can have multiple Turbo Controllers 
│ │ ├ 4l9a. Name : string
│ │ ├ 4l9b. Stages [x] : object | Rod Controllers can have multiple 
stages 
│ │ │ ├ 4l9b1. Input Var : enum
│ │ │ ├ 4l9b2. Combinator Mode : enum
│ │ │ ├ 4l9b3. Lut : string - path 
│ │ │ ├ 4l9b4. Filter Gain : float
│ │ │ ├ 4l9b5. Up Limit : float
│ │ │ ├ 4l9b6. Down Limit : float
│ │ │ ├ 4l9b7. Current Value : float
│ │ └ └ 4l9b8. Const Value : float
│ ├ 26l. Turbo Settings : object 
│ └ └ 26l1. Boost Lv : float 
├ 27. Ai Car Data : string - path 
└ 28. mm : integer
```

#### **Enum list - Car Engine**

| ld    | Enum           | Values                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4l9b1 | Input Var      | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear, SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX, SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG, SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor, RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG, LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR, SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight, ErsChargeLevel, ErsCoastTorque |
| 4l9b2 | CombinatorMode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                          |
| 4q5a1 | Туре           | <none>, Poly3, Poly5, Piece Wise, Damper Lut Data</none>                                                                                                                                                                                                                                                                                                                                                                          |
| 18c1  | Mode           | UseEffect, UseAngle                                                                                                                                                                                                                                                                                                                                                                                                               |
| 26e1  | Туре           | LSD, Spool, Torsen, EpicyclicTorsen, EpicyclicLSD, TorqueVectoring                                                                                                                                                                                                                                                                                                                                                                |

#### <span id="page-41-0"></span>C. Measurement Units & Descriptions

| ID | Name | Unit of Measurement | Description |
|----|------|---------------------|-------------|
|    |      |                     |             |
|    |      |                     |             |

#### <span id="page-41-1"></span>D. Example data

#### <span id="page-41-2"></span>I. Chosen Car Data for Example

- Ferrari 296 GTB (slug: ks\_ferrari\_286\_qtb)
- Audi R8 LMS GT3 Evo II (slug: ks\_audi\_r8\_lms\_gt3\_evo\_2)
- Renault 5 GT Turbo (slug: ks renault 5 gt turbo)

# <span id="page-41-3"></span>II. Example

#### <span id="page-41-4"></span>Ferrari 296 GTB

- 1. Screen Name : None

2. General

- 2a. Screen Name : Ferrari 296 GTB - 2b. Total Mass : 1750.00000

- 2c. Tank Position: 0.00000, -0.16715, -032949 - 2d. Fuel: 60.00000 - 2e. Max Fuel: 120.00000 - 2f. Efficiency: 0.00000

```
│ ├ 2g. Kg Per Liter : 0.75500 
│ ├ 2h. Body Box Sizes : 2.00000, 0.70000, 4.22149
│ ├ 2i. Pickup Front Height : -0.35200 
│ ├ 2j. Pickup Rear Height : -0.35200 
│ ├ 2k. Check Rules : false 
│ ├ 2l. Minimum Height : 0.00000 
│ ├ 2m. Torsional Stiffness : 30000.00000 
│ ├ 2n. Torsional Damping : 500.00000 
│ ├ 2o. Body Mesh Offset 
│ │ ├ 2o1. Position : 0.000, 0.000, 0.000
│ │ ├ 2o2. Rotation : 0.000, 0.000, 0.000
│ └ └ 2o3. Scale : 0.000, 0.000, 0.000
├ 3. General Path : None
├ 4. Suspensions 
│ ├ 4a. Wheel Base : 2.60000 
│ ├ 4b. Longitudinal Cg Location : 0.39500 
│ ├ 4c. Base Y Front : -0.11000 
│ ├ 4d. Base Y Rear : -0.08200 
│ ├ 4e. Track Front : 1.72600 
│ ├ 4f. Track Rear : 1.71000 
│ ├ 4g. Damage 
│ │ ├ 4g1. Min Velocity : 40.00000 
│ │ ├ 4g2. Gain : 0.00040 
│ │ ├ 4g3. Max Damage : 0.05000 
│ │ └ 4g4. Debug Log : true 
│ ├ 4h. Coilover Front path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb_front.coilover
│ ├ 4i. Coilover Rear Path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb_rear.coilover 
│ ├ 4j. Front Suspension Path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb_front.suspension
│ ├ 4k. Rear Suspension Path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb_front.suspension
│ ├ 4l. Heavy Springs : None
│ ├ 4m. Arb Front 
│ │ ├ 4m1. Stiffness : 26000.00000 
│ │ ├ 4m2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ └ 4l9b. Stages : None 
│ ├ 4n. Arb Rear 
│ │ ├ 4n1. Stiffness : 20000.00000 
│ │ ├ 4n2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None 
│ ├ 4o. Flex Bar Front 
│ │ ├ 4o1. Stiffness : 0.00000 
│ │ ├ 4o2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None 
│ ├ 4p. Flex Bar Rear 
│ │ ├ 4p1. Stiffness 0.00000 
│ │ ├ 4p2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None
│ ├ 4q. Dampers Controller : None
│ └ 4r. Has Dampers Cockpit Settings : false
```

```
├ 5. Drivetrain Path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb.drivetrain
├ 6. Gearbox Path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb.gearbox
├ 7. Clutch Path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb.clutch
├ 8. Engine Path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb.carengine
├ 9. Brakes Path : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb.brakesystem
├ 10. Steering System 
│ ├ 10a. Four W S Controllers
│ │ ├ 4l9a. Name : None 
│ │ ├ 4l9b. Stages : None 
├ 11. Electronics 
│ ├ 11a. T C
│ │ ├ 11a1. Has T C2 : false
│ │ ├ 11a2. Frequency Hz : 333.00000 
│ │ ├ 11a3. Min Speed Kmh : 35.00000 
│ │ ├ 11a4. Gear Change Time : 0.0800 
│ │ ├ 11a5. Min Cut Level : 8.00000 
│ │ ├ 11a6. Max Cut Level : 0.90000 
│ │ ├ 11a7. Settings 1
│ │ │ ├ 11a7a. Min Slip Ratio : 0.00000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.00000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 0.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.00000 
│ │ │ ├ 11a7e. Angular A C Cgain : 0.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 0.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 0.00000 
│ │ ├ 11a7. Settings 2
│ │ │ ├ 11a7a. Min Slip Ratio : 0.09000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.35000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 15.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.80000 
│ │ │ ├ 11a7e. Angular A C Cgain : 4.50000 
│ │ │ ├ 11a7f. Oversteer Gain : 3.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 6.00000 
│ │ ├ 11a7. Settings 3
│ │ │ ├ 11a7a. Min Slip Ratio : 0.07000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.20000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 12.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.50000 
│ │ │ ├ 11a7e. Angular A C Cgain : 6.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 5.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 5.00000 
│ │ ├ 11a7. Settings 4
│ │ │ ├ 11a7a. Min Slip Ratio : 0.04500 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.15000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.0000 
│ │ │ ├ 11a7e. Angular A C Cgain : 10.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 7.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 3.00000 
│ ├ 11b. A B S
│ │ ├ 11b1. Settings 1
```

```
│ │ │ ├ 11b1a. Min Slip Ratio : -1.00000 
│ │ │ ├ 11b1b. Max Slip Ratio : -1.00000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 0.00000 
│ │ │ ├ 11b1d. Cut Level : 0.00000 
│ │ │ ├ 11b1f. Max Torque Variation : 0.70000 
│ │ ├ 11b1. Settings 2
│ │ │ ├ 11b1a. Min Slip Ratio : 0.07000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.12000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 9.00000 
│ │ │ ├ 11b1d. Cut Level : 0.05000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ Frequency : 40.00000 
│ │ ├ Channels : 4 
│ │ ├ Min Speed Kmh : 0.00000
│ ├ 11c. E D L : None
│ ├ 11d. E S P 
│ │ ├ 11d1. Frequency Hz : 100.00000 
│ │ ├ 11d2. Min Speed Kmh : 20.00000 
│ │ ├ 11d3. Settings 1 
│ │ │ ├ 11d3a. Gain : 0.00000 
│ │ │ ├ 11d3b. Steer Gain : 0.00000 
│ │ │ ├ 11d3c. Min Steer Gain : 0.00000 
│ │ │ ├ 11d3d. Steer Gain Max Speed : 0.00000 
│ │ │ ├ 11d3e. Oversteer Gain : 0.00000 
│ │ │ ├ 11d3f. Understeer Gain : 0.00000 
│ │ │ ├ 11d3g. Max Slip Ratio : 0.00000 
│ │ │ ├ 11d3h. Dead Zone : 0.00000 
│ │ │ ├ 11d3i. Filter Gain : 0.00000 
│ │ │ ├ 11d3j. Brake Perc : 0.00000 
│ │ │ └ 11d3k. Brake Perc Activation : 0.00000 
│ │ ├ 11d3. Settings 2 
│ │ │ ├ 11d3a. Gain : 0.50000 
│ │ │ ├ 11d3b. Steer Gain : 0.50000 
│ │ │ ├ 11d3c. Min Steer Gain : 0.50000 
│ │ │ ├ 11d3d. Steer Gain Max Speed : 0.00000 
│ │ │ ├ 11d3e. Oversteer Gain : 0.50000 
│ │ │ ├ 11d3f. Understeer Gain : 0.50000 
│ │ │ ├ 11d3g. Max Slip Ratio : 0.19000 
│ │ │ ├ 11d3h. Dead Zone : 0.30000 
│ │ │ ├ 11d3i. Filter Gain : 0.95000 
│ │ │ ├ 11d3j. Brake Perc : 0.10000 
│ └ └ └ 11d3k. Brake Perc Activation : 0.90000 
├ 12. Electronics Path : None
├ 13. Controls 
│ ├ 13a. Ff Mult : 1.10000 
│ ├ 13b. Steer Lock : 342.00000 
│ ├ 13c. Steer Ratio : 12.00000 
│ ├ 13d. Linear Steer Rod Ratio : 0.00200 
│ └ 13e. Steer Assist : 1.00000 
├ 14. Box Colliders 1
│ ├ 14a. Center : 0.00000, -0.26000, 0.33000
│ ├ 14b. Size : 1.78000, 0.15000, 3.94000
│ └ 14c. Pitch Rotation Deg : 0.200000 
├ 15. Front Tyre Compounds 1 : 
content\cars\common_phsx\tyres\hypercar\hypercar_245_35_20.tyre
```

```
├ 16. Rear Tyre Compounds 1 : 
content\cars\common_phsx\tyres\hypercar\hypercar_305_35_20.tyre
├ 17. Aero 
│ ├ 17a. Slip Gain Multiple : 1.00000 
│ ├ 17b. Speed Factor Mult : 2.00000 
│ ├ 17c. Downforces : None 
│ ├ 17d. Front Lift : None
│ ├ 17e. Rear Lift : None
│ ├ 17f. Drag : None
│ └ 17g. Wings Path 1 : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb0.wing 
│ └ 17g. Wings Path 2 : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb1.wing 
│ └ 17g. Wings Path 3 : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb2.wing 
│ └ 17g. Wings Path 4 : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb3.wing
├ 18. Drs : None
├ 19. Ers
│ ├ 19a. Torque Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\KERS_TORQUE.curve
│ ├ 19b. Coast Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\KERS_TORQUE.curve
│ ├ 19c. Battery Charge Kj : 26820.00000 
│ ├ 19d. Has Button Override : false 
│ ├ 19e. Max Kj Per Lap : 0.00000 
│ ├ 19f. Max Charge Kj Per Lap : 0.00000 
│ ├ 19g. Heat Charge Perc : 0.00000 
│ ├ 19h. Heat Power Kw : 0.00000 
│ ├ 19i. Default Power Controller Index : 0 
│ ├ 19j. Power Controllers Front : None 
│ ├ 19k. Power Controllers Rear 1
│ │ ├ 4l9a. Name : MAP Q 
│ │ ├ 4l9b. Stages 1
│ │ │ ├ 4l9b1. Input Var : Gas 
│ │ │ ├ 4l9b2. Combinator Mode : Add 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kers_Q_CONTROLLER_G
AS.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 2
│ │ │ ├ 4l9b1. Input Var : Gear 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_GEAR
.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 3
```

```
│ │ │ ├ 4l9b1. Input Var : SlipRatioRearAVG 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_SLIP
.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 4
│ │ │ ├ 4l9b1. Input Var : RPMS 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_RPM.
curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 5
│ │ │ ├ 4l9b1. Input Var : Gas 
│ │ │ ├ 4l9b2. Combinator Mode : Add 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersTHROTTLE_coast.
curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 6
│ │ │ ├ 4l9b1. Input Var : Brake 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_BRAK
E.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ └ └ 4l9b8. Const Value : 0.00000 
│ ├ 19k. Power Controllers Rear 2
│ │ ├ 4l9a. Name : MAP P 
│ │ ├ 4l9b. Stages 1
│ │ │ ├ 4l9b1. Input Var : Gas 
│ │ │ ├ 4l9b2. Combinator Mode : Add 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kers_P_CONTROLLER_G
AS.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000
```

```
│ │ ├ 4l9b. Stages 2
│ │ │ ├ 4l9b1. Input Var : Gear 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_GEAR
.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 3
│ │ │ ├ 4l9b1. Input Var : SlipRatioRearAVG 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_SLIP
.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 4
│ │ │ ├ 4l9b1. Input Var : RPMS 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_RPM.
curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 5
│ │ │ ├ 4l9b1. Input Var : Gas 
│ │ │ ├ 4l9b2. Combinator Mode : Add 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersTHROTTLE_coast.
curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 6
│ │ │ ├ 4l9b1. Input Var : Brake 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_BRAK
E.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ └ └ 4l9b8. Const Value : 0.00000
│ ├ 19k. Power Controllers Rear 3
```

```
│ │ ├ 4l9a. Name : MAP H 
│ │ ├ 4l9b. Stages 1
│ │ │ ├ 4l9b1. Input Var : Gas 
│ │ │ ├ 4l9b2. Combinator Mode : Add 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kers_H_CONTROLLER_G
AS.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 2
│ │ │ ├ 4l9b1. Input Var : Gear 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_GEAR
.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 3
│ │ │ ├ 4l9b1. Input Var : SlipRatioRearAVG 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_SLIP
.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 4
│ │ │ ├ 4l9b1. Input Var : RPMS 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_RPM.
curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000 
│ │ ├ 4l9b. Stages 5
│ │ │ ├ 4l9b1. Input Var : Gas 
│ │ │ ├ 4l9b2. Combinator Mode : Add 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersTHROTTLE_coast.
curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ │ └ 4l9b8. Const Value : 0.00000
```

```
│ │ ├ 4l9b. Stages 6
│ │ │ ├ 4l9b1. Input Var : Brake 
│ │ │ ├ 4l9b2. Combinator Mode : Mult 
│ │ │ ├ 4l9b3. Lut : 
content\cars\ks_ferrari_296_gtb\data\kers\controller_kersCONTROLLER_BRAK
E.curve
│ │ │ ├ 4l9b4. Filter Gain : 0.96000 
│ │ │ ├ 4l9b5. Up Limit : 1.00000 
│ │ │ ├ 4l9b6. Down Limit : -1.00000 
│ │ │ ├ 4l9b7. Current Value : 0.00000 
│ │ └ └ 4l9b8. Const Value : 0.00000
│ ├ 19l. Brake Rear Correction : 5.00000 
│ ├ 19m. Has Cockpit Controls : false 
│ ├ 19n. Cockpit Controls 
│ │ ├ 19n1. Delivery Profile : false 
│ │ ├ 19n2. Mgu H Mode : false 
│ │ └ 19n3. Recovery : false 
│ ├ 19o. Has Front Motors : false 
│ ├ 19p. Front Motors 
│ │ ├ 19p1. Torque Lut : None
│ │ ├ 19p2 Discharge Time : 0.00000 
│ │ └ 19p3. Torque Vectoring Bias : 0.00000
├ 20. Setup Limits : 
content\cars\ks_ferrari_296_gtb\data\setup\limits_f296gtb.carsetuplimits
├ 21. Collider Mesh : 
content\cars\ks_ferrari_296_gtb\collider\ferrari_296_gtb_collider.mesh
├ 22 Body Mesh Offset 
│ ├ 22a. Position : 0.000, -0.482, 0.247
│ ├ 22b. Rotation: 0.100, 0.000, 0.000
│ └ 22c. Scale : 1.000, 1.000, 1.000
├ 23. Stock Setup : content/cars/
ks_ferrari_296_gtb\data\setup\f296gtb_stock.carsetup
├ 24. Ai Setup : None
├ 25. Wet Setup : None
├ 26. Performance Modes 1
│ ├ 26a. Performance Mode Name : QUAL 
│ ├ 26b. Electronics Settings
│ │ ├ 26b1. Tc1 : 2.00000 
│ │ ├ 26b2. Tc2 : 1.00000 
│ │ ├ 26b3. Abs : 1.00000 
│ │ ├ 26b4. Esc : 0.00000 
│ │ ├ 26b5. Ebb : 0.000 
│ │ ├ 26b6. Engine Map : 0.00000 
│ │ ├ 26b7. Telemetry laps To Record : 0.00000 
│ │ ├ 26b8. Turbo Boost Lv : 0.00000 
│ │ ├ 26b9. Ers Deployment Map : 0.000 
│ │ ├ 26b10. Ers Recharge Lv : 100.000 
│ │ └ 26b11. Ers Heat Charging : 0.000 
│ ├ 26c. Brakes Settings : None
│ ├ 26d. Damper Settings : None 
│ ├ 26e. Differential Data : None
│ ├ 26f. Four W D Differentials : None
│ ├ 26g. Front Lock Controllers : None
│ ├ 26h. Center Lock Controllers : None
│ ├ 26i. Rear Lock Controllers : None
│ ├ 26j. Awd Clutches : None
```

```
│ ├ 26k. Turbo Controllers : None 
│ ├ 26l. Turbo Settings : None 
├ 26. Performance Modes 2
│ ├ 26a. Performance Mode Name : PERF 
│ ├ 26b. Electronics Settings
│ │ ├ 26b1. Tc1 : 2.00000 
│ │ ├ 26b2. Tc2 : 1.00000 
│ │ ├ 26b3. Abs : 1.00000 
│ │ ├ 26b4. Esc : 1.00000 
│ │ ├ 26b5. Ebb : 0.000 
│ │ ├ 26b6. Engine Map : 0.00000 
│ │ ├ 26b7. Telemetry laps To Record : 0.00000 
│ │ ├ 26b8. Turbo Boost Lv : 0.00000 
│ │ ├ 26b9. Ers Deployment Map : 1.000 
│ │ ├ 26b10. Ers Recharge Lv : 100.000 
│ │ └ 26b11. Ers Heat Charging : 0.000 
│ ├ 26c. Brakes Settings : None
│ ├ 26d. Damper Settings : None 
│ ├ 26e. Differential Data : None
│ ├ 26f. Four W D Differentials : None
│ ├ 26g. Front Lock Controllers : None
│ ├ 26h. Center Lock Controllers : None
│ ├ 26i. Rear Lock Controllers : None
│ ├ 26j. Awd Clutches : None 
│ ├ 26k. Turbo Controllers : None 
│ ├ 26l. Turbo Settings : None 
├ 26. Performance Modes 3
│ ├ 26a. Performance Mode Name : HYBRID 
│ ├ 26b. Electronics Settings
│ │ ├ 26b1. Tc1 : 2.00000 
│ │ ├ 26b2. Tc2 : 1.00000 
│ │ ├ 26b3. Abs : 1.00000 
│ │ ├ 26b4. Esc : 1.00000 
│ │ ├ 26b5. Ebb : 0.000 
│ │ ├ 26b6. Engine Map : 1.00000 
│ │ ├ 26b7. Telemetry laps To Record : 0.00000 
│ │ ├ 26b8. Turbo Boost Lv : 0.00000 
│ │ ├ 26b9. Ers Deployment Map : 2.000 
│ │ ├ 26b10. Ers Recharge Lv : 100.000 
│ │ └ 26b11. Ers Heat Charging : 0.000 
│ ├ 26c. Brakes Settings : None
│ ├ 26d. Damper Settings : None 
│ ├ 26e. Differential Data : None
│ ├ 26f. Four W D Differentials : None
│ ├ 26g. Front Lock Controllers : None
│ ├ 26h. Center Lock Controllers : None
│ ├ 26i. Rear Lock Controllers : None
│ ├ 26j. Awd Clutches : None 
│ ├ 26k. Turbo Controllers : None 
│ ├ 26l. Turbo Settings : None
├ 27. Ai Car Data : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb.aicardata
└ 28. mm : 1
```

#### <span id="page-51-0"></span>**Audi R8 LMS GT3 Evo II**

```
├ 1. Screen Name : Audi R8 LMS GT3 Evo II 
├ 2. General 
│ ├ 2a. Screen Name : Audi R8 LMS GT3 Evo II 
│ ├ 2b. Total Mass : 1355 
│ ├ 2c. Tank Position : 0.00000, -0.02900, -0.25600
│ ├ 2d. Fuel : 0.00000 
│ ├ 2e. Max Fuel : 120.00000 
│ ├ 2f. Efficiency : 0.40000 
│ ├ 2g. Kg Per Liter : 0.75500 
│ ├ 2h. Body Box Sizes : 1.98000, 1.19000, 4.46000
│ ├ 2i. Pickup Front Height : -0.34900 
│ ├ 2j. Pickup Rear Height : -0.31800 
│ ├ 2k. Check Rules : true 
│ ├ 2l. Minimum Height : 450.00000 
│ ├ 2m. Torsional Stiffness : 40000.00000 
│ ├ 2n. Torsional Damping : 400.00000 
│ ├ 2o. Body Mesh Offset 
│ │ ├ 2o1. Position : 0.000, 0.000, 0.000
│ │ ├ 2o2. Rotation : 0.000, 0.000, 0.000
│ └ └ 2o3. Scale : 0.000, 0.000, 0.000
├ 3. General Path : None
├ 4. Suspensions 
│ ├ 4a. Wheel Base : 2.70000 
│ ├ 4b. Longitudinal Cg Location : 0.42000 
│ ├ 4c. Base Y Front : -0.03500 
│ ├ 4d. Base Y Rear : -0.03500 
│ ├ 4e. Track Front : 1.66700 
│ ├ 4f. Track Rear : 1.67000 
│ ├ 4g. Damage 
│ │ ├ 4g1. Min Velocity : 40.00000 
│ │ ├ 4g2. Gain : 0.00040 
│ │ ├ 4g3. Max Damage : 0.05000 
│ │ └ 4g4. Debug Log : true 
│ ├ 4h. Coilover Front path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2_fron
t.coilover
│ ├ 4i. Coilover Rear Path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2_rear
.coilover
│ ├ 4j. Front Suspension Path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2_fron
t.suspension
│ ├ 4k. Rear Suspension Path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2_rear
.suspension
│ ├ 4l. Heavy Springs : None 
│ ├ 4m. Arb Front 
│ │ ├ 4m1. Stiffness : 56800.00000 
│ │ ├ 4m2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None
│ ├ 4n. Arb Rear
```

```
│ │ ├ 4n1. Stiffness : 39900.00000 
│ │ ├ 4n2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None 
│ ├ 4o. Flex Bar Front 
│ │ ├ 4o1. Stiffness : 0.00000 
│ │ ├ 4o2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None 
│ ├ 4p. Flex Bar Rear 
│ │ ├ 4p1. Stiffness : 0.00000 
│ │ ├ 4p2. Controller
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None 
│ ├ 4q. Dampers Controller : None
│ └ 4r. Has Dampers Cockpit Settings : false 
├ 5. Drivetrain Path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2.driv
etrain
├ 6. Gearbox Path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2.gear
box
├ 7. Clutch Path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2.clut
ch
├ 8. Engine Path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2.care
ngine 
├ 9. Brakes Path : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2.brak
esystem
├ 10. Steering System 
│ ├ 10a. Four W S Controllers
│ │ ├ 4l9a. Name : None 
│ │ ├ 4l9b. Stages : None 
├ 11. Electronics 
│ ├ 11a. T C
│ │ ├ 11a1. Has T C2 : true
│ │ ├ 11a2. Frequency Hz : 333.00000 
│ │ ├ 11a3. Min Speed Kmh : 30.00000 
│ │ ├ 11a4. Gear Change Time : 0.07000 
│ │ ├ 11a5. Min Cut Level : 0.00000 
│ │ ├ 11a6. Max Cut Level : 6.00000 
│ │ ├ 11a7. Settings 1
│ │ │ ├ 11a7a. Min Slip Ratio : 0.00000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.00000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 0.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.00000 
│ │ │ ├ 11a7e. Angular A C Cgain : 0.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 0.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 0.00000 
│ │ ├ 11a7. Settings 2
│ │ │ ├ 11a7a. Min Slip Ratio : 0.18000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.35000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 15.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.50000
```

```
│ │ │ ├ 11a7e. Angular A C Cgain : 1.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 1.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 5.00000 
│ │ ├ 11a7. Settings 3
│ │ │ ├ 11a7a. Min Slip Ratio : 0.15000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.30000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 13.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.50000 
│ │ │ ├ 11a7e. Angular A C Cgain : 1.50000 
│ │ │ ├ 11a7f. Oversteer Gain : 1.50000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 5.00000 
│ │ ├ 11a7. Settings 4
│ │ │ ├ 11a7a. Min Slip Ratio : 0.12000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.28000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 11.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.25000 
│ │ │ ├ 11a7e. Angular A C Cgain : 2.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 2.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 4.50000 
│ │ ├ 11a7. Settings 5
│ │ │ ├ 11a7a. Min Slip Ratio : 0.10000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.25000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 10.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.00000 
│ │ │ ├ 11a7e. Angular A C Cgain : 2.50000 
│ │ │ ├ 11a7f. Oversteer Gain : 2.50000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 4.00000 
│ │ ├ 11a7. Settings 6
│ │ │ ├ 11a7a. Min Slip Ratio : 0.08000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.22000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 8.50000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.00000 
│ │ │ ├ 11a7e. Angular A C Cgain : 3.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 3.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 4.00000 
│ │ ├ 11a7. Settings 7
│ │ │ ├ 11a7a. Min Slip Ratio : 0.07000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.22000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 7.50000 
│ │ │ ├ 11a7d. Engine Cut Level : 1.00000 
│ │ │ ├ 11a7e. Angular A C Cgain : 3.50000 
│ │ │ ├ 11a7f. Oversteer Gain : 3.50000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 3.50000 
│ │ ├ 11a7. Settings 8
│ │ │ ├ 11a7a. Min Slip Ratio : 0.06000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.22000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.50000 
│ │ │ ├ 11a7e. Angular A C Cgain : 4.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 4.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 3.00000 
│ │ ├ 11a7. Settings 9
│ │ │ ├ 11a7a. Min Slip Ratio : 0.05000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.19000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.45000
```

```
│ │ │ ├ 11a7e. Angular A C Cgain : 5.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 5.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 3.00000 
│ │ ├ 11a7. Settings 10
│ │ │ ├ 11a7a. Min Slip Ratio : 0.05000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.17000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.40000 
│ │ │ ├ 11a7e. Angular A C Cgain : 7.50000 
│ │ │ ├ 11a7f. Oversteer Gain : 6.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 3.00000 
│ │ ├ 11a7. Settings 11
│ │ │ ├ 11a7a. Min Slip Ratio : 0.04000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.15000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 6.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.35000 
│ │ │ ├ 11a7e. Angular A C Cgain : 8.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 6.50000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 2.50000 
│ │ ├ 11a7. Settings 12
│ │ │ ├ 11a7a. Min Slip Ratio : 0.03000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.15000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 6.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.30000 
│ │ │ ├ 11a7e. Angular A C Cgain : 8.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 7.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 2.50000 
│ │ ├ 11a7. Settings 13
│ │ │ ├ 11a7a. Min Slip Ratio : 0.03000 
│ │ │ ├ 11a7b. Max Slip Ratio : 0.14000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 5.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.30000 
│ │ │ ├ 11a7e. Angular A C Cgain : 8.50000 
│ │ │ ├ 11a7f. Oversteer Gain : 7.50000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 3.00000 
│ ├ 11b. A B S
│ │ ├ 11b1. Settings 1
│ │ │ ├ 11b1a. Min Slip Ratio : -1.00000 
│ │ │ ├ 11b1b. Max Slip Ratio : -1.00000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 0.00000 
│ │ │ ├ 11b1d. Cut Level : 0.00000 
│ │ │ ├ 11b1f. Max Torque Variation : 0.00000 
│ │ ├ 11b1. Settings 2
│ │ │ ├ 11b1a. Min Slip Ratio : 0.12000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.14000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 3
│ │ │ ├ 11b1a. Min Slip Ratio : 0.11000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.14000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 4
│ │ │ ├ 11b1a. Min Slip Ratio : 0.10000
```

```
│ │ │ ├ 11b1b. Max Slip Ratio : 0.12000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 5
│ │ │ ├ 11b1a. Min Slip Ratio : 0.08000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.10000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 6
│ │ │ ├ 11b1a. Min Slip Ratio : 0.07000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.08000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 7
│ │ │ ├ 11b1a. Min Slip Ratio : 0.06000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.08000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 8
│ │ │ ├ 11b1a. Min Slip Ratio : 0.05000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.07000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 9
│ │ │ ├ 11b1a. Min Slip Ratio : 0.05000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.06000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 10
│ │ │ ├ 11b1a. Min Slip Ratio : 0.04000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.05000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 11
│ │ │ ├ 11b1a. Min Slip Ratio : 0.02500 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.03500 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ 11b1. Settings 12
│ │ │ ├ 11b1a. Min Slip Ratio : 0.01000 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.02000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 7.00000 
│ │ │ ├ 11b1d. Cut Level : 0.20000 
│ │ │ ├ 11b1f. Max Torque Variation : 1.00000 
│ │ ├ Frequency : 40.00000 
│ │ ├ Channels : 4 
│ │ ├ Min Speed Kmh : 20.00000
│ ├ 11c. E D L : None
```

```
│ ├ 11d. E S P 
│ │ ├ 11d1. Frequency Hz : 0.00000 
│ │ ├ 11d2. Min Speed Kmh : 0.00000 
│ │ ├ 11d3. Settings : None 
├ 12. Electronics Path : None
├ 13. Controls 
│ ├ 13a. Ff Mult : 1.50000 
│ ├ 13b. Steer Lock : 240.00000 
│ ├ 13c. Steer Ratio : 14.30000 
│ ├ 13d. Linear Steer Rod Ratio : 0.00235 
│ └ 13e. Steer Assist : 1.00000 
├ 14. Box Colliders 1
│ ├ 14a. Center : 0.00000, -0.23500, 0.30000
│ ├ 14b. Size : 1.78000, 0.20000, 4.07000 
│ └ 14c. Pitch Rotation Deg : 0.65000 
├ 15. Front Tyre Compounds 1 : 
content\cars\common_phsx\tyres\racing_slicks\slick_325_680_18.tyre
├ 16. Rear Tyre Compounds 1 : 
ontent\cars\common_phsx\tyres\racing_slicks\slick_325_705_18.tyre
├ 17. Aero 
│ ├ 17a. Slip Gain Multiple : 1.00000 
│ ├ 17b. Speed Factor Mult : 2.00000 
│ ├ 17c. Downforces 1
│ │ ├ 17c1. Position : 0.82140, -0.34900, 1.57000
│ │ ├ 17c2. Cl Gain : 1.00000 
│ │ ├ 17c3. Cd Gain : 1.00000 
│ │ ├ 17c4. Yaw Gain : 0.00000 
│ │ ├ 17c5. Drag Per Cool Transfer : 0.01500 
│ │ ├ 17c6. Damage C L 1 : 0.01000 
│ │ ├ 17c6. Damage C L 2 : 0.00500 
│ │ ├ 17c6. Damage C L 3 : 0.00300 
│ │ ├ 17c6. Damage C L 4 : 0.00300 
│ │ ├ 17c7. Damage C D 1 : 0.01500 
│ │ ├ 17c7. Damage C D 2 : 0.00500 
│ │ ├ 17c7. Damage C D 3 : 0.00300 
│ │ ├ 17c7. Damage C D 4 : 0.00300
│ │ ├ 17c8. Downforce Controllers : None
│ │ ├ 17c9. Lift Per Front Angle : 0.00000 
│ │ ├ 17c10. Lift Per Rear Angle : 0.00000 
│ │ ├ 17c11. Drag Per Front Angle : 0.00000 
│ │ ├ 17c12. Drag Per Rear Angle : 0.00000 
│ │ ├ 17c13. Default Front Angle : 0.00000 
│ │ └ 17c14. Default Rear Angle : 0.00000 
│ ├ 17c. Downforces 2
│ │ ├ 17c1. Position : 0.82140, -0.34900, 1.57000
│ │ ├ 17c2. Cl Gain : 1.00000 
│ │ ├ 17c3. Cd Gain : 1.00000 
│ │ ├ 17c4. Yaw Gain : 0.00000 
│ │ ├ 17c5. Drag Per Cool Transfer : 0.01500 
│ │ ├ 17c6. Damage C L 1 : 0.01000 
│ │ ├ 17c6. Damage C L 2 : 0.00500 
│ │ ├ 17c6. Damage C L 3 : 0.00300 
│ │ ├ 17c6. Damage C L 4 : 0.00300 
│ │ ├ 17c7. Damage C D 1 : 0.01500 
│ │ ├ 17c7. Damage C D 2 : 0.00500 
│ │ ├ 17c7. Damage C D 3 : 0.00300
```

```
│ │ ├ 17c7. Damage C D 4 : 0.00300
│ │ ├ 17c8. Downforce Controllers : None
│ │ ├ 17c9. Lift Per Front Angle : 0.00000 
│ │ ├ 17c10. Lift Per Rear Angle : 0.00000 
│ │ ├ 17c11. Drag Per Front Angle : 0.00000 
│ │ ├ 17c12. Drag Per Rear Angle : 0.00000 
│ │ ├ 17c13. Default Front Angle : 0.00000 
│ │ └ 17c14. Default Rear Angle : 0.00000 
│ ├ 17c. Downforces 3
│ │ ├ 17c1. Position : 0.82140, -0.31800, -1.13500
│ │ ├ 17c2. Cl Gain : 1.00000 
│ │ ├ 17c3. Cd Gain : 1.00000 
│ │ ├ 17c4. Yaw Gain : -0.10000 
│ │ ├ 17c5. Drag Per Cool Transfer : 0.01000 
│ │ ├ 17c6. Damage C L 1 : 0.00500 
│ │ ├ 17c6. Damage C L 2 : 0.01000 
│ │ ├ 17c6. Damage C L 3 : 0.00300 
│ │ ├ 17c6. Damage C L 4 : 0.00300 
│ │ ├ 17c7. Damage C D 1 : 0.00500 
│ │ ├ 17c7. Damage C D 2 : 0.01500 
│ │ ├ 17c7. Damage C D 3 : 0.00300 
│ │ ├ 17c7. Damage C D 4 : 0.00300
│ │ ├ 17c8. Downforce Controllers : None
│ │ ├ 17c9. Lift Per Front Angle : 0.00000 
│ │ ├ 17c10. Lift Per Rear Angle : 0.00000 
│ │ ├ 17c11. Drag Per Front Angle : 0.00000 
│ │ ├ 17c12. Drag Per Rear Angle : 0.00000 
│ │ ├ 17c13. Default Front Angle : 0.00000 
│ │ └ 17c14. Default Rear Angle : 0.00000 
│ ├ 17c. Downforces 4
│ │ ├ 17c1. Position : 0.82140, -0.31800, -1.13500
│ │ ├ 17c2. Cl Gain : 1.00000 
│ │ ├ 17c3. Cd Gain : 1.00000 
│ │ ├ 17c4. Yaw Gain : -0.10000 
│ │ ├ 17c5. Drag Per Cool Transfer : 0.01000 
│ │ ├ 17c6. Damage C L 1 : 0.00500 
│ │ ├ 17c6. Damage C L 2 : 0.01000 
│ │ ├ 17c6. Damage C L 3 : 0.00300 
│ │ ├ 17c6. Damage C L 4 : 0.00300 
│ │ ├ 17c7. Damage C D 1 : 0.00500 
│ │ ├ 17c7. Damage C D 2 : 0.01500 
│ │ ├ 17c7. Damage C D 3 : 0.00300 
│ │ ├ 17c7. Damage C D 4 : 0.00300
│ │ ├ 17c8. Downforce Controllers : None
│ │ ├ 17c9. Lift Per Front Angle : 0.00000 
│ │ ├ 17c10. Lift Per Rear Angle : 0.00000 
│ │ ├ 17c11. Drag Per Front Angle : 0.00000 
│ │ ├ 17c12. Drag Per Rear Angle : 0.00000 
│ │ ├ 17c13. Default Front Angle : 0.00000 
│ │ └ 17c14. Default Rear Angle : 0.00000 
│ ├ 17d. Front Lift : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\aero\frontczmap.surface3d
│ ├ 17e. Rear Lift : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\aero\rearczmap.surface3d
│ ├ 17f. Drag : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\aero\cxmap.surface3d
```

```
│ └ 17g. Wings Path 1 : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\aero\Audi_R8_GT3_rear_wing_re
ar_modifier.wing 
│ └ 17g. Wings Path 2 : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\aero\Audi_R8_GT3_rear_wing_fr
ont_modifier.wing
├ 18. Drs : None
├ 19. Ers : None
├ 20. Setup Limits : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\aero\Audi_R8_GT3_rear_wing_fr
ont_modifier.wing
├ 21. Collider Mesh : 
content\cars\ks_audi_r8_lms_gt3_evo_2\collider\audi_r8_gt3_evo2_collider
.mesh
├ 22. Body Mesh Offset 
│ ├ 22a. Position : 0.000, -0.419, 0.230
│ ├ 22b. Rotation: 0.650, 0.000, 0.000
│ └ 22c. Scale : 1.000, 1.000, 1.000
├ 23. Stock Setup : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\setup\ks_audi_r8_lms_gt3_evo_
2_safe.carsetup
├ 24. Ai Setup : None
├ 25. Wet Setup : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\setup\ks_audi_r8_lms_gt3_evo_
2_wet.carsetup
├ 26. Performance Modes : None
├ 27. Ai Car Data : 
content\cars\ks_audi_r8_lms_gt3_evo_2\data\ks_audi_r8_lms_gt3_evo_2.aica
rdata
└ 28. mm : 1
```

#### <span id="page-58-0"></span>**Renault 5 GT Turbo**

```
├ 1. Screen Name : None 
├ 2. General 
│ ├ 2a. Screen Name : Renault 5 GT Turbo 
│ ├ 2b. Total Mass : 910.00000 
│ ├ 2c. Tank Position : 0.00000, -0.20000, -1.56750
│ ├ 2d. Fuel : 30.00000 
│ ├ 2e. Max Fuel : 50.00000 
│ ├ 2f. Efficiency : 0.00000 
│ ├ 2g. Kg Per Liter : 0.75500 
│ ├ 2h. Body Box Sizes : 1.60000, 1.10000, 3.30000
│ ├ 2i. Pickup Front Height : -0.49000 
│ ├ 2j. Pickup Rear Height : -0.48000 
│ ├ 2k. Check Rules : false 
│ ├ 2l. Minimum Height : 0.00000 
│ ├ 2m. Torsional Stiffness : 11000.00000 
│ ├ 2n. Torsional Damping : 50.00000 
│ ├ 2o. Body Mesh Offset 
│ │ ├ 2o1. Position : 0.000, 0.000, 0.000
│ │ ├ 2o2. Rotation : 0.000, 0.000, 0.000
│ └ └ 2o3. Scale : 0.000, 0.000, 0.000
├ 3. General Path : None
```

```
├ 4. Suspensions : 
│ ├ 4a. Wheel Base : 2.40700 
│ ├ 4b. Longitudinal Cg Location : 0.64000 
│ ├ 4c. Base Y Front : -0.42000 
│ ├ 4d. Base Y Rear : -0.43000 
│ ├ 4e. Track Front : 1.34000 
│ ├ 4f. Track Rear : 1.31500 
│ ├ 4g. Damage 
│ │ ├ 4g1. Min Velocity : 40.00000 
│ │ ├ 4g2. Gain : 0.00040 
│ │ ├ 4g3. Max Damage : 0.05000 
│ │ └ 4g4. Debug Log : true 
│ ├ 4h. Coilover Front path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_gt_turbo_front.coil
over
│ ├ 4i. Coilover Rear Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_gt_turbo_rear.coilo
ver
│ ├ 4j. Front Suspension Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_gt_turbo_front.susp
ension
│ ├ 4k. Rear Suspension Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_gt_turbo_rear.coilo
ver
│ ├ 4l. Heavy Springs : None 
│ ├ 4m. Arb Front 
│ │ ├ 4m1. Stiffness : 8000.00000 
│ │ ├ 4m2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None
│ ├ 4n. Arb Rear 
│ │ ├ 4n1. Stiffness : 6000.00000 
│ │ ├ 4n2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None 
│ ├ 4o. Flex Bar Front 
│ │ ├ 4o1. Stiffness : 0.00000 
│ │ ├ 4o2. Controller 
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None 
│ ├ 4p. Flex Bar Rear 
│ │ ├ 4p1. Stiffness : 10000.00000 
│ │ ├ 4p2. Controller
│ │ │ ├ 4l9a. Name : None 
│ │ │ ├ 4l9b. Stages : None 
│ ├ 4q. Dampers Controller : None
│ └ 4r. Has Dampers Cockpit Settings : false 
├ 5. Drivetrain Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.drivetrain
├ 6. Gearbox Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.gearbox
├ 7. Clutch Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.clutch
├ 8. Engine Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.carengine
```

```
├ 9. Brakes Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.brakesystem
├ 10. Steering System 
│ ├ 10a. Four W S Controllers
│ │ ├ 4l9a. Name : None 
│ │ ├ 4l9b. Stages : None 
├ 11. Electronics 
│ ├ 11a. T C
│ │ ├ 11a1. Has T C2 : false
│ │ ├ 11a2. Frequency Hz : 150.00000 
│ │ ├ 11a3. Min Speed Kmh : 20.00000 
│ │ ├ 11a4. Gear Change Time : 0.08000 
│ │ ├ 11a5. Min Cut Level : 10.00000 
│ │ ├ 11a6. Max Cut Level : 1.00000 
│ │ ├ 11a7. Settings 1 :
│ │ │ ├ 11a7a. Min Slip Ratio : -1.00000 
│ │ │ ├ 11a7b. Max Slip Ratio : -1.00000 
│ │ │ ├ 11a7c. Ref Slip Angle Deg : 0.00000 
│ │ │ ├ 11a7d. Engine Cut Level : 0.00000 
│ │ │ ├ 11a7e. Angular A C Cgain : 0.00000 
│ │ │ ├ 11a7f. Oversteer Gain : 0.00000 
│ │ │ ├ 11a7g. Slip Angle Activation Deg : 0.00000 
│ ├ 11b. A B S
│ │ ├ 11b1. Settings 1
│ │ │ ├ 11b1a. Min Slip Ratio : -1.00000 
│ │ │ ├ 11b1b. Max Slip Ratio : -1.00000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 0.00000 
│ │ │ ├ 11b1d. Cut Level : 0.00000 
│ │ │ ├ 11b1f. Max Torque Variation : 0.70000 
│ │ ├ 11b1. Settings 2
│ │ │ ├ 11b1a. Min Slip Ratio : 0.06500 
│ │ │ ├ 11b1b. Max Slip Ratio : 0.12000 
│ │ │ ├ 11b1c. Ref Slip Angle Deg : 8.00000 
│ │ │ ├ 11b1d. Cut Level : 0.40000 
│ │ │ ├ 11b1f. Max Torque Variation : 0.75000 
│ │ ├ Frequency : 40.00000 
│ │ ├ Channels : 4 
│ │ ├ Min Speed Kmh : 0.00000
│ ├ 11c. E D L
│ │ ├ 11c1. Active : true 
│ │ ├ 11c2. Brake Torque Power : 40.00000 
│ │ ├ 11c3. Brake Torque Coast : 200.00000 
│ │ ├ 11c4. Dead Zone Coast : 0.05000 
│ │ ├ 11c5. Dead Zone Power : 0.10000 
│ │ ├ 11c6. Max Spin Power : 0.40000 
│ │ ├ 11c7. Max Spin Coaster : 0.20000 
│ │ ├ 11c8. Min Speed : 0.00000
│ ├ 11d. E S P 
│ │ ├ 11d1. Frequency Hz : 0.00000 
│ │ ├ 11d2. Min Speed Kmh : 0.00000 
│ │ ├ 11d3. Settings : None 
├ 12. Electronics Path : None
├ 13. Controls 
│ ├ 13a. Ff Mult : 2.90000 
│ ├ 13b. Steer Lock : 630.00000 
│ ├ 13c. Steer Ratio : -19.60000
```

```
│ ├ 13d. Linear Steer Rod Ratio : 0.00220 
│ └ 13e. Steer Assist : 1.00000 
├ 14. Box Colliders 1
│ ├ 14a. Center : 0.00000, -0.24000, -0.29000
│ ├ 14b. Size : 1.40000, 0.10000, 3.23000
│ └ 14c. Pitch Rotation Deg : 0.00000 
├ 15. Front Tyre Compounds 1 : 
content\cars\common_phsx\tyres\road\road_195_55_13.tyre
├ 16. Rear Tyre Compounds 1 : 
content\cars\common_phsx\tyres\road\road_195_55_13.tyre
├ 17. Aero 
│ ├ 17a. Slip Gain Multiple : 1.00000 
│ ├ 17b. Speed Factor Mult : 2.00000 
│ ├ 17c. Downforces : None 
│ ├ 17d. Front Lift : None
│ ├ 17e. Rear Lift : None
│ ├ 17f. Drag : None
│ └ 17g. Wings Path 1 : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_gt_turbo0.wing
├ 18. Drs : None
├ 19. Ers : None
├ 20. Setup Limits : 
content\cars\ks_renault_5_gt_turbo\data\setup\renault_5_gt_turbo.carsetu
plimits
├ 21. Collider Mesh : 
content\cars\ks_renault_5_gt_turbo\collider\renault_5_gt_turbo_collider.
mesh
├ 22. Body Mesh Offset 
│ ├ 22a. Position : 0.000, -0.632, -0.340
│ ├ 22b. Rotation : 0.700, 0.000, 0.000 
│ └ 22c. Scale : 1.000, 1.000, 1.000
├ 23. Stock Setup : 
content\cars\ks_renault_5_gt_turbo\data\setup\renault_5_gt_turbo.carsetu
p
├ 24. Ai Setup : None
├ 25. Wet Setup : None
├ 26. Performance Modes : None
├ 27. Ai Car Data : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_gt_turbo.aicardata
└ 28. mm : 1
```

# <span id="page-62-0"></span>**4. Car Engine [ .carengine ]**

# <span id="page-62-1"></span>**A. Description**

#### <span id="page-62-2"></span>**I. General Description**

The **Car Engine** asset is the heart of the vehicle's propulsion system within the simulation engine. While previous assets focused on chassis dimensions (Car Data) or deceleration (BrakeSystem), the Car Engine file dictates how the vehicle generates mechanical energy.

It maps the complete thermodynamic and rotational behavior of the internal combustion engine (ICE), electric motor, or hybrid powertrain. It calculates how much raw power is produced at any given RPM, how the engine responds to the driver's throttle inputs, how it builds or sheds rotational speed (inertia), and how its performance is impacted by thermal limits and turbocharging.

#### <span id="page-62-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The parameters configured in the Car Engine asset heavily influence the vehicle's straight-line speed, drivability, and endurance:

- **• Acceleration & Top Speed:** Driven entirely by the torque output across the rev range. The shape of the power curve dictates how fast the car pulls out of corners and its absolute top speed on straights.
- **• Traction Control & Drivability:** How smoothly or aggressively the engine delivers torque when the driver steps on the gas pedal. A snappy engine makes throttle modulation difficult, increasing wheelspin.
- **• Engine Braking & Corner Entry**: When the driver lifts off the throttle, internal engine friction and compression create a drag torque (Engine Brake). This slows down the driven wheels, acting as a natural brake balance shift toward the drive axle.
- **• Fuel Consumption & Thermal Management:** Dictates the fuel burn rate relative to RPM and throttle positioning, directly affecting pit-stop strategy. It also manages engine temperatures, where overheating can cause component failure or power loss.

#### <span id="page-62-4"></span>**III. Key Architecture & Data Fields Explained**

The data within a Car Engine schema is typically divided into **Power Generation**, **Rotational Dynamics**, and **Turbo/Aspiration Systems**.

#### <span id="page-62-5"></span>**1 - POWER GENERATION & POWER CURVES**

**• Torque Curve / Power Curve:** The foundational lookup table mapping **Engine RPM (X-axis)** to **Torque Output (Y-axis, usually in** Nm**)**. The engine's raw horsepower is directly calculated from this relationship.

- **•** M**ax RPM / Limiter:** The absolute maximum rotational speed the engine can achieve before a fuel/ignition cut-off is triggered to prevent damage.
- **• Idle RPM:** The baseline rotational speed at which the engine runs when there is zero driver throttle input.

#### <span id="page-63-0"></span>**2 - ROTATIONAL DYNAMICS & THROTTLE RESPONSE**

- **• Engine Inertia:** The rotational mass of the flywheel, crankshaft, and pistons. A low inertia value allows the engine to rev up and drop RPMs incredibly fast (like a Formula 1 car), while high inertia creates a slower, heavier revving characteristic (like a heavy V8 or diesel truck).
- **• Engine Brake Torque:** The negative torque (resistance) generated by the engine when the throttle is fully released (0%). Crucial for modulating car balance during weight transfers.
- **• Throttle Map / Curve:** A lookup table correlating physical pedal position to actual throttle plate opening. This can be linear, aggressive (for immediate bite), or progressive (for easier throttle control in wet weather).

#### <span id="page-63-1"></span>**3 - ASPIRATION, TURBOCHARGING & THERMAL BEHAVIOR**

- **• Turbo Boost / Wastegate Settings:** Configures turbocharger behavior, including maximum boost pressure, spool-up time (turbo lag), and wastegate limits.
- **• Fuel Consumption Factor:** The efficiency coefficient of fuel burn per unit of power generated, used to compute real-time fuel depletion.
- **• Optimal Temperature & Damage Thresholds:** The ideal operational thermal window for water and oil. Running the engine above these critical thresholds triggers progressive performance degradation or catastrophic engine failure.

#### <span id="page-63-2"></span>**IV. Short Interpretation of Asset Implementation**

When analyzing an engine's physics profile, the data layout reveals the distinct mechanical identity of the powertrain:

- **• The High-Revving Naturally Aspirated Profile (e.g., V10 GT3 / Vintage Race Cars):** Characterized by an ultra-low Engine Inertia and a linear Torque Curve that peaks very high up in the rev range (8000 + RPM). These engines have a sharp, instantaneous response to the throttle and feature high Engine Brake Torque, meaning lifting off the gas sharply stabilizes or upsets the rear axle depending on vehicle balance.
- **• The Modern Turbocharged Profile (e.g., Modern GT3 / Le Mans Hypercars):** Features a flat, wide plateau in the Torque Curve across the mid-range RPMs rather than a steep peak. It includes complex turbocharger data blocks defining spool rates. The throttle map is often configured progressively to mask "turbo kick"—the sudden surge of torque that happens when boost pressure builds up—ensuring the tires aren't instantly overwhelmed.
- **• The Hybrid/EV Assist Profile:** Includes overlaying curves where an electric motor delivers instant maximum torque at 0 RPM, seamlessly tapering off as the internal combustion engine reaches its optimal power band higher up.

### <span id="page-64-0"></span>**B. Schema**

```
├ 1. Engine Type : enum
├ 2. Inertia : float
├ 3. Power Curve : string - path 
├ 4. Coast Curve : string - path 
├ 5. Maps [x] : object | can have multiple Maps 
│ ├ 5a. Type : enum
│ ├ 5b. Power Mult : float
│ ├ 5c. Consumption Mult : float
│ ├ 5d. Throttle Response Curve : string - path 
│ ├ 5e. Throttle Gain K R P M : float
│ ├ 5f. Throttle Ref R P M Move : float
│ ├ 5g. Throttle Lag Up : float
│ ├ 5h. Throttle Lag Dn : float
│ └ 5i. Throttling Factor : float
├ 6. Minimum : integer
├ 7. Limiter : integer
├ 8. Limiter Cycles : integer
├ 9. Throttle Response Curve : string - path
├ 10. Throttle Lag Up : float
├ 11. Throttle Lag Dn : float
├ 12. Throttle Rev Chocking : float
├ 13. Ignition Time S : float
├ 14. Starter Engine Torque : float
├ 15. Start E C U Assist : object
│ ├ 15a. Rpm Range : float
│ ├ 15b. Gain : float
│ ├ 15c. Speed Range K H M : float
│ ├ 15d. Rpm Limiter : float
│ ├ 15e. Limiter Cycles : integer
│ ├ 15f. Use Clutch : boolean
│ ├ 15g. Slip Ratio Target : float
│ ├ 15h. Clutch Gain : float
│ └ 15i. Gas Gain : float
├ 16. Turbo Controllers [x] : object with an array of stages within | 
can have multiple Turbo Controllers
│ ├ 16a. Name : string
│ ├ 16b. Stages [x] | object | can have multiple Stage 
│ │ ├ 16b1. Input Var : enum
│ │ ├ 16b2. Combinator Mode : enum
│ │ ├ 16b3. Lut : string - path 
│ │ ├ 16b4. Filter Gain : float
│ │ ├ 16b5. Up Limit : float
│ │ ├ 16b6. Down Limit : float
│ │ ├ 16b7. Current Value : float
│ └ └ 16b8. Const Value : float
├ 17. Waste Gate Controllers [x] : object with an array of stages within 
| can have multiple Waste Gate Controllers 
│ ├ 16a. Name : string
│ ├ 16b. Stages [x] | object | can have multiple Stage 
│ │ ├ 16b1. Input Var : enum
│ │ ├ 16b2. Combinator Mode : enum
│ │ ├ 16b3. Lut : string - path
```

```
16b4. Filter Gain: float
     16b5. Up Limit : float
     16b6. Down Limit: float
     16b7. Current Value : float
  L 16b8. Const Value : float
 18. Max Turbo Boost : float
 19. Bov Threshold : float
- 20. Turbos To Load [x] : string - path | can have multiple Turbos To
Load
- 21. Battery Data : object
  - 21a. Capacity Kwh : float
  - 21b. Dischage Efficiency : float
   21c. Charge Efficiency: float
  - 21d. Temp Eff Loss Per Deg : float
  - 21e. Convection K : float
   21f. Convection Forced K: float
   21g. Thermal Capacity: float
   21h. Max Temp: float
   21i. Min Temp: float
```

#### **Enum - Car Engine**

| 1    | Engine Type    | motor, combustion                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |  |  |
|------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| 5a   | Туре           | gamma, cervone                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |  |  |
| 16b1 | Input Var      | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear, SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX, SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG, SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor, RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG, LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR, SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight, ErsChargeLevel, ErsCoastTorque |  |  |  |  |
| 16b2 | CombinatorMode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |  |  |

#### <span id="page-65-0"></span>C. Example data

# <span id="page-65-1"></span>I. Chosen Car Engine for Example

- Alpine A290 b (slug: ks\_alpine\_a290\_b)
- Ferrari SF 25 (slug: ks\_ferrari\_sf\_25)
- Chevrolet Camaro ZL1 (slug: ks\_renault\_5\_gt\_turbo)
- Datsun 240z Fairlady (slug: ks\_datsun\_240z\_fairlady)

#### <span id="page-65-2"></span>II. Example

#### <span id="page-65-3"></span>Alpine A290 b

- 1. Engine Type : motor - 2. Inertia : 0.06000

```
├ 3. Power Curve : content\cars\ks_alpine_a290_b\data\HEADER_POWER.curve
├ 4. Coast Curve : content\cars\ks_alpine_a290_b\data\coast.curve
├ 5. Maps : None 
├ 6. Minimum : 0 
├ 7. Limiter : 15200 
├ 8. Limiter Cycles : 20 
├ 9. Throttle Response Curve : 
content\cars\ks_alpine_a290_b\data\throttle.curve 
├ 10. Throttle Lag Up : 0.00000 
├ 11. Throttle Lag Dn : 0.00000 
├ 12. Throttle Rev Chocking : 0.00000 
├ 13. Ignition Time S : 0.00000 
├ 14. Starter Engine Torque : 0.00000 
├ 15. Start E C U Assist 
│ ├ 15a. Rpm Range : 0.00000 
│ ├ 15b. Gain : 0.00000 
│ ├ 15c. Speed Range K H M : 0.00000 
│ ├ 15d. Rpm Limiter : 0.00000 
│ ├ 15e. Limiter Cycles : 0 
│ ├ 15f. Use Clutch : false 
│ ├ 15g. Slip Ratio Target : 0.00000 
│ ├ 15h. Clutch Gain : 0.00000 
│ └ 15i. Gas Gain : 0.00000 
├ 16. Turbo Controllers : None 
├ 17. Waste Gate Controllers : None 
├ 18. Max Turbo Boost : 0.00000 
├ 19. Bov Threshold : 0.00000 
├ 20. Turbos To Load : None
├ 21. Battery Data 
│ ├ 21a. Capacity Kwh : 52.000 
│ ├ 21b. Dischage Efficiency : 0.800 
│ ├ 21c. Charge Efficiency : 0.600 
│ ├ 21d. Temp Eff Loss Per Deg : 0.01000 
│ ├ 21e. Convection K : 0.00100 
│ ├ 21f. Convection Forced K : 0.00050 
│ ├ 21g. Thermal Capacity : 100.000 
│ ├ 21h. Max Temp : 35.000 
└ └ 21i. Min Temp : 15.000
```

# <span id="page-66-0"></span>**Ferrari SF 25**

```
├ 1. Engine Type : combustion 
├ 2. Inertia : None 
├ 3. Power Curve : content\cars\ks_ferrari_sf_25\data\HEADER_POWER.curve
├ 4. Coast Curve : content\cars\ks_ferrari_sf_25\data\coast_smooth.curve
├ 5. Maps 1
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 1.00000 
│ ├ 5c. Consumption Mult : 0.60000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_linear.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000
```

```
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 2
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 1.00000 
│ ├ 5c. Consumption Mult : 0.60000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_aggressive.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 3
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 0.89000 
│ ├ 5c. Consumption Mult : 0.56000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_linear.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 4
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 0.89000 
│ ├ 5c. Consumption Mult : 0.56000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_aggressive.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 5
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 0.82000 
│ ├ 5c. Consumption Mult : 0.55000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_linear.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 6
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 0.82000 
│ ├ 5c. Consumption Mult : 0.55000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_aggressive.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000
```

```
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 7
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 0.72000 
│ ├ 5c. Consumption Mult : 0.50000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_linear.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 8
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 0.72000 
│ ├ 5c. Consumption Mult : 0.50000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_aggressive.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 9
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 0.95000 
│ ├ 5c. Consumption Mult : 0.58500 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_linear.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 10
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 0.95000 
│ ├ 5c. Consumption Mult : 0.58500 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_aggressive.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 5. Maps 11
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 1.00000 
│ ├ 5c. Consumption Mult : 0.60000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_progressive.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000
```

```
├ 5. Maps 12
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 1.00000 
│ ├ 5c. Consumption Mult : 0.60000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_wet.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 6. Minimum : 2000 
├ 7. Limiter : 15000 
├ 8. Limiter Cycles : 60 
├ 9. Throttle Response Curve : 
content\cars\ks_ferrari_sf_25\data\throttle_linear.curve 
├ 10. Throttle Lag Up : 0.00000 
├ 11. Throttle Lag Dn : 0.00000 
├ 12. Throttle Rev Chocking : 0.00000 
├ 13. Ignition Time S : 0.00000 
├ 14. Starter Engine Torque : 40.00000 
├ 15. Start E C U Assist 
│ ├ 15a. Rpm Range : 0.00000 
│ ├ 15b. Gain : 0.00000 
│ ├ 15c. Speed Range K H M : 0.00000 
│ ├ 15d. Rpm Limiter : 0.00000 
│ ├ 15e. Limiter Cycles : 0 
│ ├ 15f. Use Clutch : false 
│ ├ 15g. Slip Ratio Target : 0.00000 
│ ├ 15h. Clutch Gain : 0.00000 
│ └ 15i. Gas Gain : 0.00000 
├ 16. Turbo Controllers 1 
│ ├ 16a. Name : None 
│ ├ 16b. Stages 1
│ │ ├ 16b1. Input Var : RPMS 
│ │ ├ 16b2. Combinator Mode : Add 
│ │ ├ 16b3. Lut : 
content\cars\ks_ferrari_sf_25\data\ctrl_turbo0CONTROLLER_0.curve
│ │ ├ 16b4. Filter Gain : 0.99000 
│ │ ├ 16b5. Up Limit : 10000.00000 
│ │ ├ 16b6. Down Limit : 0.00000 
│ │ ├ 16b7. Current Value : 0.00000 
│ └ └ 16b8. Const Value : 0.00000 
├ 17. Waste Gate Controllers : None 
├ 18. Max Turbo Boost : 2.20000 
├ 19. Bov Threshold : 0.00000 
├ 20. Turbos To Load 1 : 
content\cars\ks_ferrari_sf_25\data\ks_ferrari_sf_250.turbo
├ 21. Battery Data 
│ ├ 21a. Capacity Kwh : 0.000 
│ ├ 21b. Dischage Efficiency : 0.000 
│ ├ 21c. Charge Efficiency : 0.000 
│ ├ 21d. Temp Eff Loss Per Deg : 0.00000 
│ ├ 21e. Convection K : 0.00000 
│ ├ 21f. Convection Forced K : 0.00000 
│ ├ 21g. Thermal Capacity : 0.000
```

```
│ ├ 21h. Max Temp : 0.000 
└ └ 21i. Min Temp : 0.000
```

# <span id="page-70-0"></span>**Chevrolet Camaro ZL1**

```
├ 1. Engine Type : combustion 
├ 2. Inertia : 0.45000 
├ 3. Power Curve : 
content\cars\ks_chevrolet_camaro_zl1\data\HEADER_POWER.curve
├ 4. Coast Curve : content\cars\ks_chevrolet_camaro_zl1\data\coast.curve
├ 5. Maps 1
│ ├ 5a. Type : gamma 
│ ├ 5b. Power Mult : 1.00000 
│ ├ 5c. Consumption Mult : 1.00000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_chevrolet_camaro_zl1\data\throttlemap_response.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.80000 
│ ├ 5h. Throttle Lag Dn : 0.92000 
│ └ 5i. Throttling Factor : 0.00000 
├ 6. Minimum : 900 
├ 7. Limiter : 6600 
├ 8. Limiter Cycles : 30 
├ 9. Throttle Response Curve : 
content\cars\ks_chevrolet_camaro_zl1\data\throttlemap_response.curve 
├ 10. Throttle Lag Up : 0.80000 
├ 11. Throttle Lag Dn : 0.90000 
├ 12. Throttle Rev Chocking : 0.00000 
├ 13. Ignition Time S : 0.00000 
├ 14. Starter Engine Torque : 60.00000 
├ 15. Start E C U Assist 
│ ├ 15a. Rpm Range : 1500.00000 
│ ├ 15b. Gain : 0.10000 
│ ├ 15c. Speed Range K H M : 120.00000 
│ ├ 15d. Rpm Limiter : 3800.00000 
│ ├ 15e. Limiter Cycles : 0 
│ ├ 15f. Use Clutch : true 
│ ├ 15g. Slip Ratio Target : 0.14000 
│ ├ 15h. Clutch Gain : 5.00000 
│ └ 15i. Gas Gain : 1.75000 
├ 16. Turbo Controllers 1 
│ ├ 16a. Name : None 
│ ├ 16b. Stages 1
│ │ ├ 16b1. Input Var : RPMS 
│ │ ├ 16b2. Combinator Mode : Add 
│ │ ├ 16b3. Lut : 
content\cars\ks_chevrolet_camaro_zl1\data\rpms_boost.curve
│ │ ├ 16b4. Filter Gain : 0.00000 
│ │ ├ 16b5. Up Limit : 1.20000 
│ │ ├ 16b6. Down Limit : 0.00000 
│ │ ├ 16b7. Current Value : 0.00000 
│ └ └ 16b8. Const Value : 0.00000 
├ 17. Waste Gate Controllers : None
```

```
├ 18. Max Turbo Boost : 0.60000 
├ 19. Bov Threshold : 0.00000 
├ 20. Turbos To Load 1 : 
content\cars\ks_chevrolet_camaro_zl1\data\ks_chevrolet_camaro_zl1_compre
ssor.turbo
├ 21. Battery Data 
│ ├ 21a. Capacity Kwh : 0.000 
│ ├ 21b. Dischage Efficiency : 0.000 
│ ├ 21c. Charge Efficiency : 0.000 
│ ├ 21d. Temp Eff Loss Per Deg : 0.00000 
│ ├ 21e. Convection K : 0.00000 
│ ├ 21f. Convection Forced K : 0.00000 
│ ├ 21g. Thermal Capacity : 0.000 
│ ├ 21h. Max Temp : 0.000 
└ └ 21i. Min Temp : 0.000 
                            Datsun 240z Fairlady 
├ 1. Engine Type : combustion 
├ 2. Inertia : 0.18000 
├ 3. Power Curve : 
content\cars\ks_datsun_240z_fairlady\data\HEADER_POWER.curve
├ 4. Coast Curve : 
content\cars\ks_datsun_240z_fairlady\data\ks_datsun_240z_fairlady_coast1
.curve
├ 5. Maps 1
│ ├ 5a. Type : cervone 
│ ├ 5b. Power Mult : 1.00000 
│ ├ 5c. Consumption Mult : 1.00000 
│ ├ 5d. Throttle Response Curve : 
content\cars\ks_datsun_240z_fairlady\data\throttle.curve
│ ├ 5e. Throttle Gain K R P M : 0.00000 
│ ├ 5f. Throttle Ref R P M Move : 0.00000 
│ ├ 5g. Throttle Lag Up : 0.00000 
│ ├ 5h. Throttle Lag Dn : 0.00000 
│ └ 5i. Throttling Factor : 0.00000 
├ 6. Minimum : 600 
├ 7. Limiter : 7000 
├ 8. Limiter Cycles : 8 
├ 9. Throttle Response Curve : 
content\cars\ks_datsun_240z_fairlady\data\throttle.curve 
├ 10. Throttle Lag Up : 0.00000 
├ 11. Throttle Lag Dn : 0.00000 
├ 12. Throttle Rev Chocking : 0.00000 
├ 13. Ignition Time S : 0.00000 
├ 14. Starter Engine Torque : 30.00000 
├ 15. Start E C U Assist 
│ ├ 15a. Rpm Range : 0.00000 
│ ├ 15b. Gain : 0.00000 
│ ├ 15c. Speed Range K H M : 0.00000 
│ ├ 15d. Rpm Limiter : 0.00000 
│ ├ 15e. Limiter Cycles : 0 
│ ├ 15f. Use Clutch : false 
│ ├ 15g. Slip Ratio Target : 0.00000
```

│ ├ 15h. Clutch Gain : 0.00000

- │ └ 15i. Gas Gain : 0.00000
- ├ 16. Turbo Controllers : None
- ├ 17. Waste Gate Controllers : None
- ├ 18. Max Turbo Boost : 0.00000
- ├ 19. Bov Threshold : 0.00000
- ├ 20. Turbos To Load : None
- ├ 21. Battery Data
- │ ├ 21a. Capacity Kwh : 0.000
- │ ├ 21b. Dischage Efficiency : 0.000
- │ ├ 21c. Charge Efficiency : 0.000
- │ ├ 21d. Temp Eff Loss Per Deg : 0.00000
- │ ├ 21e. Convection K : 0.00000
- │ ├ 21f. Convection Forced K : 0.00000
- │ ├ 21g. Thermal Capacity : 0.000
- │ ├ 21h. Max Temp : 0.000
- └ └ 21i. Min Temp : 0.000

# <span id="page-73-0"></span>**5. Car Setup [ .carsetup ]**

# <span id="page-73-1"></span>**A. Description**

### <span id="page-73-2"></span>**I. General Description**

The **Car Setup** asset is the primary adjustment interface that translates mechanical physics constants into highly customizable track settings. While other files define the immovable physical constraints of a vehicle (like the frame weight or engine potential), the Car Setup file acts as the pit garage dashboard.

It stores all adjustable parameters that engineers and drivers modify to adapt the vehicle to specific racetracks, weather conditions, or driving styles. It acts as a set of instructions applied on top of the base suspension, aerodynamics, and drivetrain geometries to maximize grip, control stability, and balance the car's handling.

#### <span id="page-73-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The variables configured in the Car Setup asset have an immediate and dramatic impact on every dynamic phase of lap execution:

- **• Mechanical Grip & Tire Patch Optimization:** By altering alignment and tire pressures, this asset controls how flat the tire stays against the tarmac during high-load cornering, directly maximizing lateral adhesion.
- **• Aerodynamic Platform Control:** Ride heights and rake (the angle of the car's floor relative to the track) dictate how much downforce wings and underbody diffusers generate, dramatically shifting high-speed stability and drag.
- **• Transient Phase Handling (Weight Transfer):** Springs and dampers regulate *how fast* and *how far* the body rolls when cornering, pitches under braking, or squats under acceleration, giving the driver a predictable or snappy platform.
- **• Corner Exit Propulsion (Power Delivery):** Differential settings govern how power shifts between the drive wheels, dictating whether a car neatly clips an exit apex or snaps into wheelspin/snap-oversteer.

#### <span id="page-73-4"></span>**III. Key Architecture & Data Fields Explained**

The parameters in a Car Setup file are traditionally compartmentalized into five core operational groups: **Tyres**, **Aerodynamics**, **Suspension (Springs/Alignment)**, **Dampers (Shock Absorbers)**, and **Drivetrain (Differential)**.

#### <span id="page-73-5"></span>**1 - TYRES ( THE CONTACT PATCH )**

**• Cold Pressure:** The initial inflating pressure of the tire before leaving the pitlane. It directly influences the hot operating pressure and optimal carcass temperature window.

- **• Camber (Front/Rear):** The inward or outward tilt of the wheels when viewed from the front. Negative camber ensures that when the car rolls into a corner, the outer tire leans flat against the asphalt for maximum cornering grip.
- **• Toe (Front/Rear):** The angle of the wheels relative to the vehicle's longitudinal centerline. Front *toe-out* increases turn-in agility, while rear *toe-in* stabilizes the rear end during straight-line acceleration and heavy braking.

#### <span id="page-74-0"></span>**2 - AERODYNAMICS ( THE AIRFLOW PLATFORM )**

- **• Wing Angles (Front/Rear Spoiler):** The mechanical inclination of aero planes. Higher rear wing angles increase downforce (stability in fast corners) at the expense of higher straight-line drag (lower top speed).
- **• Ride Height (Front/Rear):** The clearance between the car's floor and the ground. Lowering the car increases venturi/ground-effect downforce, but going too low can cause the floor to bottom out on bumps, destroying all grip instantly.

## <span id="page-74-1"></span>**3 - SUSPENSION GEOMETRY & RATES**

- **• Wheel Rate / Spring Stiffness:** The stiffness of the main suspension coil springs. Stiffer springs stabilize the aero platform and stop body roll, but reduce compliance on bumpy circuits or kerbs.
- **• Anti-Roll Bar (ARB Front/Rear):** A torsion bar linking the left and right suspension sides. It purely resists body roll in corners. Adjusting the stiffness ratio between front and rear ARBs is the primary tool for shifting handling balance between understeer and oversteer.

#### <span id="page-74-2"></span>**4 - DAMPERS ( TRANSIENT SHOCK ABSORPTION )**

Dampers control the speed of suspension movement and are split into travel directions and shaft speeds:

- **• Bump / Compression (Slow & Fast):** Resists the suspension compressing. *Slow Bump* manages body roll from driver inputs; *Fast Bump* absorbs high-speed impacts like hitting a track kerb or bump.
- **• Rebound / Extension (Slow & Fast):** Resists the suspension extending back out. *Slow Rebound* regulates how the car settles as it exits a corner or releases the brakes; *Fast Rebound* controls how fast the tire snaps back down to touch the track after a kerb strike.

#### <span id="page-74-3"></span>**5 - DRIVETRAIN & DIFFERENTIAL**

- **• Diff Preload:** The static friction locking the differential when zero throttle is applied. Higher preload stabilizes the car during snappy, mid-corner lift-offs.
- **• Diff Power (Lock):** The locking percentage under acceleration. High lock forces both tires to spin together for maximum exit drive, but can cause powerundersteer or sudden power-oversteer if traction breaks.
- **• Diff Coast (Lock):** The locking percentage under deceleration/braking. High coast lock keeps the rear stable under heavy braking into a corner but resists initial turn-in agility.

### <span id="page-75-0"></span>**IV. Interpretation of Setup Configuration Strategies**

When reading a car's exported .setup file, the values map out a very specific racing engineering intent based on the target circuit layout:

- **• The High-Downforce Monza/Spa vs. Monaco Profile:** For high-speed tracks like Spa-Francorchamps or Monza, you will notice ultra-low wing angles to minimize drag, stiffer springs to support the high aero load compressing the suspension, and lower ride heights. For Monaco, the wings are cranked to the absolute maximum, springs are softened to absorb bumpy street surfaces, and toe angles are aggressive to force the car around tight hairpins.
- **• The Endurance Balance Management:** In high-tier setups, engineers deliberately leave a margin in the ride heights and tire pressures. This accommodates changing ambient temperatures over a multi-hour race stint and accounts for structural components wearing out, ensuring the aerodynamic floor platform stays stable regardless of fuel burn or tyre degradation.

#### <span id="page-75-1"></span>**B. Schema**

```
├ 1. Import Setup : string - path 
├ 2. Mechanical Balance : object
│ ├ 2a. Arbs [x] : float | can have multiple Arbs 
│ ├ 2b. Steer Ratio : float
│ ├ 2c. Brakes : object
│ │ ├ 2c1. Front Bias : float
│ │ ├ 2c2. Torque Multiplier : float
│ │ └ 2c3. Brake Ducts [x] : float | can have multiple Brake Ducts
│ ├ 2d. Differential : object
│ │ ├ 2d1. Power : float
│ │ ├ 2d2. Coast : float
│ └ └ 2d3. Preload : float
├ 3. Suspensions [x] : object
│ ├ 3a. Wheel Rate : float
│ ├ 3b. Bump Stop Up : object
│ │ ├ 3b1. Range : float
│ │ └ 3b2. Rate : float
│ ├ 3c. Bump Stop Down : object
│ │ ├ 3c1. Range : float
│ │ └ 3c2. Rate : float
│ ├ 3d. Helper Rate : float
│ └ 3e. Helper Range : float 
├ 4. Dampers [x] : object | can have multiple Dampers
│ ├ 4a. Slow Bump : float
│ ├ 4b. Fast Bump : float
│ ├ 4c. Slow Rebound : float
│ └ 4e. Fast Rebound : float
├ 5. Alignements [x] : object | can have multiple Alignements
│ ├ 5a. Pressure : float
│ ├ 5b. Camber : float
│ ├ 5c. Toe : float
│ ├ 5d. Caster : float
│ ├ 5e. Static Camber : float
```

```
- 5f. Toe Out Linear : float 5g. Compound : float
 6. Electronics : object
   6a. Tc1 : float
   6b. Tc2: float
   6c. Abs : float
   6d. Esc: float
   6e. Ebb : float
   6f. Engine Map : float
   6g. Telemetry Laps to Record: float
  - 6h. Turbo Boost Lv : float
  - 6i. Ers Deployment Map : float
   6j. Ers Recharge Lv : float
  6k. Ers Heat Charging : float
 7. Aero: object
 |- 7a. Collar Positions Mm [x] : float | can have multiple Collar
Positions Mm
  - 7b. Front Target Height : float
   7c. Rear Target Height : float
  7d. Front Wing Angle : float
  7e. Rear Wing Angle : float
 8. Fuel Strategy : object
 L 8a. Fuel : float
 9. Final State Name: string - path
 10. Version : integer
 11. Is Setup Shared : boolean
```

#### <span id="page-76-0"></span>C. Example data

#### <span id="page-76-1"></span>I. Chosen Car Engine for Example

- Ausi Sport Quattro (slug : ks\_audi\_sport\_quattro)
- Alfa Romeo Junior (slug: ks\_alfa\_romeo\_junior)
- Ferrari 488 Challenge Evo (slug: ks\_ferrari\_488\_challenge\_evo [preset: safe\_1]

#### <span id="page-76-2"></span>II. Example

#### <span id="page-76-3"></span>**Audi Sport Quattro**

```
- 1. Import Setup : None
- 2. Mechanical Balance
- 2a. Arbs 1 : 25000.00000
- 2a. Arbs 2 : 20000.00000
- 2b. Steer Ratio : 18.00000
- 2c. Brakes
- 2c1. Front Bias : 72.00000
- 2c2. Torque Multiplier : 100.00000
- 2c3. Brake Ducts : None
- 2d. Differential
- 2d1. Power : 0.00000
- 2d2. Coast : 0.00000
```

```
├ 3. Suspensions 1 
│ ├ 3a. Wheel Rate : 50000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.02645 
│ │ └ 3b2. Rate : 650.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.11855 
│ │ └ 3c2. Rate : 650.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 3. Suspensions 2 
│ ├ 3a. Wheel Rate : 50000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.02645 
│ │ └ 3b2. Rate : 650.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.11855 
│ │ └ 3c2. Rate : 650.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 3. Suspensions 3 
│ ├ 3a. Wheel Rate : 42750.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.04487 
│ │ └ 3b2. Rate : 400.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.04513 
│ └ └ 3c2. Rate : 400.00000 
├ 3. Suspensions 4 
│ ├ 3a. Wheel Rate : 42750.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.04487 
│ │ └ 3b2. Rate : 400.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.04513 
│ │ └ 3c2. Rate : 400.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 4. Dampers 1 
│ ├ 4a. Slow Bump : 6000.00000 
│ ├ 4b. Fast Bump : 1500.00000 
│ ├ 4c. Slow Rebound : 8000.00000 
│ └ 4e. Fast Rebound : 2300.00000 
├ 4. Dampers 2 
│ ├ 4a. Slow Bump : 6000.00000 
│ ├ 4b. Fast Bump : 1500.00000 
│ ├ 4c. Slow Rebound : 8000.00000 
│ └ 4e. Fast Rebound : 2300.00000 
├ 4. Dampers 3 
│ ├ 4a. Slow Bump : 5000.00000 
│ ├ 4b. Fast Bump : 1200.00000 
│ ├ 4c. Slow Rebound : 7000.00000 
│ └ 4e. Fast Rebound : 1900.00000 
├ 4. Dampers 4 
│ ├ 4a. Slow Bump : 5000.00000 
│ ├ 4b. Fast Bump : 1200.00000
```

```
│ ├ 4c. Slow Rebound : 7000.00000 
│ └ 4e. Fast Rebound : 1900.00000 
├ 5. Alignements 1 
│ ├ 5a. Pressure : 28.00000 
│ ├ 5b. Camber : -1.00000 
│ ├ 5c. Toe : -0.03000 
│ ├ 5d. Caster : -0.04510 
│ ├ 5e. Static Camber : -1.69155 
│ ├ 5f. Toe Out Linear : 0.00098 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 2 
│ ├ 5a. Pressure : 28.00000 
│ ├ 5b. Camber : -1.00000 
│ ├ 5c. Toe : -0.03000 
│ ├ 5d. Caster : -0.04510 
│ ├ 5e. Static Camber : -1.76592 
│ ├ 5f. Toe Out Linear : 0.00095 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 3 
│ ├ 5a. Pressure : 28.00000 
│ ├ 5b. Camber : -0.60000 
│ ├ 5c. Toe : 0.05000 
│ ├ 5d. Caster : 0.00000 
│ ├ 5e. Static Camber : -0.66797 
│ ├ 5f. Toe Out Linear : 0.00022 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 4 
│ ├ 5a. Pressure : 28.00000 
│ ├ 5b. Camber : -0.60000 
│ ├ 5c. Toe : 0.05000 
│ ├ 5d. Caster : 0.00000 
│ ├ 5e. Static Camber : -0.75145 
│ ├ 5f. Toe Out Linear : 0.00022 
│ └ 5g. Compound : 0.00000 
├ 6. Electronics 
│ ├ 6a. Tc1 : 0.00000 
│ ├ 6b. Tc2 : 0.00000 
│ ├ 6c. Abs : 1.00000 
│ ├ 6d. Esc : 0.00000 
│ ├ 6e. Ebb : 0.000 
│ ├ 6f. Engine Map : 0.00000 
│ ├ 6g. Telemetry Laps to Record : 0.00000 
│ ├ 6h. Turbo Boost Lv : 0.00000 
│ ├ 6i. Ers Deployment Map : 0.000 
│ ├ 6j. Ers Recharge Lv : 0.000 
│ └ 6k. Ers Heat Charging : 0.000 
├ 7. Aero 
│ ├ 7a. Collar Positions Mm 1 : 112.59116 
│ ├ 7a. Collar Positions Mm 2 : 107.20738 
│ ├ 7a. Collar Positions Mm 3 : 76.21446 
│ ├ 7a. Collar Positions Mm 4 : 75.33346 
│ ├ 7b. Front Target Height : 200.00000 
│ ├ 7c. Rear Target Height : 200.00000 
│ ├ 7d. Front Wing Angle : 0.00000 
│ └ 7e. Rear Wing Angle : 0.00000 
├ 8. Fuel Strategy
```

```
│ └ 8a. Fuel : 30.00000 
├ 9. Final State Name : 
ks_audi_sport_quattro_preset_sq_mech_1_preset_sq_visual_1 
├ 10. Version : None 
├ 11. Is Setup Shared : false
```

### <span id="page-79-0"></span>**Alfa Romeo Junior**

```
├ 1. Import Setup
├ 2. Mechanical Balance 
│ ├ 2a. Arbs 1 : 40000.00000 
│ ├ 2a. Arbs 1 : 38000.00000
│ ├ 2b. Steer Ratio : -14.60000 
│ ├ 2c. Brakes 
│ │ ├ 2c1. Front Bias : 80.00000 
│ │ ├ 2c2. Torque Multiplier : 100.00000 
│ │ └ 2c3. Brake Ducts : None 
│ ├ 2d. Differential 
│ │ ├ 2d1. Power : 0.00000 
│ │ ├ 2d2. Coast : 0.00000 
│ └ └ 2d3. Preload : 0.00000 
├ 3. Suspensions 1 
│ ├ 3a. Wheel Rate : 49000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.01194 
│ │ └ 3b2. Rate : 400.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.07306 
│ │ └ 3c2. Rate : 400.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 3. Suspensions 2 
│ ├ 3a. Wheel Rate : 49000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.01194 
│ │ └ 3b2. Rate : 400.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.07306 
│ │ └ 3c2. Rate : 400.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 3. Suspensions 3 
│ ├ 3a. Wheel Rate : 45000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : -0.00872 
│ │ └ 3b2. Rate : 400.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.0372 
│ │ └ 3c2. Rate : 500.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 3. Suspensions 4 
│ ├ 3a. Wheel Rate : 45000.00000 
│ ├ 3b. Bump Stop Up
```

```
│ │ ├ 3b1. Range : -0.00872 
│ │ └ 3b2. Rate : 400.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.09372 
│ │ └ 3c2. Rate : 500.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 4. Dampers 1 
│ ├ 4a. Slow Bump : 8200.00000 
│ ├ 4b. Fast Bump : 3000.00000 
│ ├ 4c. Slow Rebound : 10500.00000 
│ └ 4e. Fast Rebound : 3300.00000 
├ 4. Dampers 2 
│ ├ 4a. Slow Bump : 8200.00000 
│ ├ 4b. Fast Bump : 3000.00000 
│ ├ 4c. Slow Rebound : 10500.00000 
│ └ 4e. Fast Rebound : 3300.00000 
├ 4. Dampers 3 
│ ├ 4a. Slow Bump : 5000.00000 
│ ├ 4b. Fast Bump : 3500.00000 
│ ├ 4c. Slow Rebound : 6500.00000 
│ └ 4e. Fast Rebound : 3300.00000 
├ 4. Dampers 4 
│ ├ 4a. Slow Bump : 5000.00000 
│ ├ 4b. Fast Bump : 3500.00000 
│ ├ 4c. Slow Rebound : 6500.00000 
│ └ 4e. Fast Rebound : 3300.00000 
├ 5. Alignements 1 
│ ├ 5a. Pressure : 26.00000 
│ ├ 5b. Camber : -1.30000 
│ ├ 5c. Toe : -0.05000 
│ ├ 5d. Caster : -0.04980 
│ ├ 5e. Static Camber : -1.57347 
│ ├ 5f. Toe Out Linear : 0.00018 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 2 
│ ├ 5a. Pressure : 26.00000 
│ ├ 5b. Camber : -1.30000 
│ ├ 5c. Toe : -0.05000 
│ ├ 5d. Caster : -0.04980 
│ ├ 5e. Static Camber : -1.56779 
│ ├ 5f. Toe Out Linear : 0.00016 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 3 
│ ├ 5a. Pressure : 27.00000 
│ ├ 5b. Camber : -1.40000 
│ ├ 5c. Toe : 0.05000 
│ ├ 5d. Caster : -0.12000 
│ ├ 5e. Static Camber : -1.39969 
│ ├ 5f. Toe Out Linear : -0.00142 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 4 
│ ├ 5a. Pressure : 27.00000 
│ ├ 5b. Camber : -1.40000 
│ ├ 5c. Toe : 0.05000 
│ ├ 5d. Caster : -0.12000
```

```
│ ├ 5e. Static Camber : -1.39560 
│ ├ 5f. Toe Out Linear : -0.00143 
│ └ 5g. Compound : 0.00000 
├ 6. Electronics 
│ ├ 6a. Tc1 : 1.00000 
│ ├ 6b. Tc2 : 1.00000 
│ ├ 6c. Abs : 1.00000 
│ ├ 6d. Esc : 0.00000 
│ ├ 6e. Ebb : 0.000 
│ ├ 6f. Engine Map : 0.00000 
│ ├ 6g. Telemetry Laps to Record : 0.00000 
│ ├ 6h. Turbo Boost Lv : 0.00000 
│ ├ 6i. Ers Deployment Map : 0.000 
│ ├ 6j. Ers Recharge Lv : 0.000 
│ └ 6k. Ers Heat Charging : 0.000 
├ 7. Aero 
│ ├ 7a. Collar Positions Mm 1 : 102.44676 
│ ├ 7a. Collar Positions Mm 2 : 102.44756 
│ ├ 7a. Collar Positions Mm 3 : 105.31527 
│ ├ 7a. Collar Positions Mm 4 : 105.31618
│ ├ 7b. Front Target Height : 185.00000 
│ ├ 7c. Rear Target Height : 190.00000 
│ ├ 7d. Front Wing Angle : 0.00000 
│ └ 7e. Rear Wing Angle : 0.00000 
├ 8. Fuel Strategy 
│ └ 8a. Fuel : 3.00000 
├ 9. Final State Name : 
ks_alfa_romeo_junior_preset_mln_mech_1_preset_mln_visual_1 
├ 10. Version : 0 
├ 11. Is Setup Shared : false
```

#### <span id="page-81-0"></span>**Ferrari 488 Challenge Evo [ preset : safe\_1 ]**

```
├ 1. Import Setup : None
├ 2. Mechanical Balance 
│ ├ 2a. Arbs 1 : 34000.00000 
│ ├ 2a. Arbs 2 : 17000.00000
│ ├ 2b. Steer Ratio : 15.00000 
│ ├ 2c. Brakes 
│ │ ├ 2c1. Front Bias : 64.00000 
│ │ ├ 2c2. Torque Multiplier : 100.00000 
│ │ └ 2c3. Brake Ducts : None 
│ ├ 2d. Differential 
│ │ ├ 2d1. Power : 0.00000 
│ │ ├ 2d2. Coast : 0.30000 
│ └ └ 2d3. Preload : 10.00000 
├ 3. Suspensions 1 
│ ├ 3a. Wheel Rate : 160000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.02748 
│ │ └ 3b2. Rate : 500.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.01252
```

```
│ │ └ 3c2. Rate : 300.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 3. Suspensions 2 
│ ├ 3a. Wheel Rate : 160000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.02748 
│ │ └ 3b2. Rate : 500.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.01252 
│ │ └ 3c2. Rate : 300.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 3. Suspensions 3 
│ ├ 3a. Wheel Rate : 150000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.01958 
│ │ └ 3b2. Rate : 300.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.04042 
│ │ └ 3c2. Rate : 300.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 3. Suspensions 4 
│ ├ 3a. Wheel Rate : 150000.00000 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range : 0.01958 
│ │ └ 3b2. Rate : 300.00000 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3c1. Range : 0.04042 
│ │ └ 3c2. Rate : 300.00000 
│ ├ 3d. Helper Rate : 0.00000 
│ └ 3e. Helper Range : 0.00000 
├ 4. Dampers 1 
│ ├ 4a. Slow Bump : 8.00000 
│ ├ 4b. Fast Bump : 5000.00000 
│ ├ 4c. Slow Rebound : 9.00000 
│ └ 4e. Fast Rebound : 5000.00000 
├ 4. Dampers 2 
│ ├ 4a. Slow Bump : 8.00000 
│ ├ 4b. Fast Bump : 5000.00000 
│ ├ 4c. Slow Rebound : 9.00000 
│ └ 4e. Fast Rebound : 5000.00000 
├ 4. Dampers 3 
│ ├ 4a. Slow Bump : 9.00000 
│ ├ 4b. Fast Bump : 5000.00000 
│ ├ 4c. Slow Rebound : 10.00000 
│ └ 4e. Fast Rebound : 5000.00000 
├ 4. Dampers 4 
│ ├ 4a. Slow Bump : 9.00000 
│ ├ 4b. Fast Bump : 5000.00000 
│ ├ 4c. Slow Rebound : 10.00000 
│ └ 4e. Fast Rebound : 5000.00000 
├ 5. Alignements 1 
│ ├ 5a. Pressure : 24.00000 
│ ├ 5b. Camber : -3.50000
```

```
│ ├ 5c. Toe : -0.10000 
│ ├ 5d. Caster : -0.07000 
│ ├ 5e. Static Camber : -3.09347 
│ ├ 5f. Toe Out Linear : 0.00055 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 2 
│ ├ 5a. Pressure : 24.00000 
│ ├ 5b. Camber : -3.50000 
│ ├ 5c. Toe : -0.10000 
│ ├ 5d. Caster : -0.07000 
│ ├ 5e. Static Camber : -3.09532 
│ ├ 5f. Toe Out Linear : 0.00056 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 3 
│ ├ 5a. Pressure : 23.50000 
│ ├ 5b. Camber : -3.00000 
│ ├ 5c. Toe : 0.10000 
│ ├ 5d. Caster : 0.00000 
│ ├ 5e. Static Camber : -3.21468 
│ ├ 5f. Toe Out Linear : -0.00023 
│ └ 5g. Compound : 0.00000 
├ 5. Alignements 4 
│ ├ 5a. Pressure : 23.50000 
│ ├ 5b. Camber : -3.00000 
│ ├ 5c. Toe : 0.10000 
│ ├ 5d. Caster : 0.00000 
│ ├ 5e. Static Camber : -3.21772 
│ ├ 5f. Toe Out Linear : -0.00023 
│ └ 5g. Compound : 0.00000 
├ 6. Electronics 
│ ├ 6a. Tc1 : 3.00000 
│ ├ 6b. Tc2 : 3.00000 
│ ├ 6c. Abs : 3.00000 
│ ├ 6d. Esc : 0.00000 
│ ├ 6e. Ebb : 0.000 
│ ├ 6f. Engine Map : 0.00000 
│ ├ 6g. Telemetry Laps to Record : 5.00000 
│ ├ 6h. Turbo Boost Lv : 1.00000 
│ ├ 6i. Ers Deployment Map : 0.000 
│ ├ 6j. Ers Recharge Lv : 0.000 
│ └ 6k. Ers Heat Charging : 0.000 
├ 7. Aero 
│ ├ 7a. Collar Positions Mm 1 : 0.88076 
│ ├ 7a. Collar Positions Mm 2 : 0.88185 
│ ├ 7a. Collar Positions Mm 3 : 29.68013 
│ ├ 7a. Collar Positions Mm 4 : 29.68015
│ ├ 7b. Front Target Height : 75.00000 
│ ├ 7c. Rear Target Height : 90.00000 
│ ├ 7d. Front Wing Angle : 0.00000 
│ └ 7e. Rear Wing Angle : 12.00000 
├ 8. Fuel Strategy 
│ └ 8a. Fuel : 30.00000 
├ 9. Final State Name : 
ks_ferrari_488_challenge_evo_preset_f488ce_mech_1_preset_f488ce_visual_1 
├ 10. Version : 0 
├ 11. Is Setup Shared : false
```

# <span id="page-84-0"></span>**6. Car Setup Limits [ .carsetuplimits ]**

# <span id="page-84-1"></span>**A. Description**

### <span id="page-84-2"></span>**I. General Description**

The Car Setup Limits asset is the structural and regulatory counterpart to the vehicle configuration file (Car Setup). While a setup file dictates the specific mechanical settings active on a vehicle at any given moment, the Car Setup Limits file defines the rigid boundaries, rules, and user interface properties governing those adjustments.

It serves as the master blueprint for the garage interface and simulation engine. It specifies which mechanical components can be altered by the user, the absolute minimum and maximum allowable physics values, the precise increments (steps) for tuning, and how data fields should be formatted, displayed, converted, or masked within the user interface.

#### <span id="page-84-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The parameters configured within the Car Setup Limits file act as a critical control filter over a vehicle's performance envelope and user accessibility:

- **• Preservation of Vehicle Identity (Road vs. Race):** It prevents unrealistic modifications, ensuring a standard production street car cannot be fitted with fully adjustable racing spoilers, bespoke motorsport suspension systems, or pure open-wheel steering ratios
- **• Exploration of the Performance Envelope:** It defines how far a race engineer can push tuning boundaries. If the minimum front ride height threshold is restricted too high, the vehicle will be fundamentally blocked from exploiting ground-effect underbody aerodynamics.
- **• Garage User Interface and User Experience:** By setting precise incremental adjustments, it determines whether a value changes smoothly millimeter by millimeter or clicks through coarse mechanical steps. It also translates raw backend physics numbers into legible cockpit metrics (e.g., clicks, degrees, bars, or PSI).
- **• Performance Balancing & Fair Play (BOP):** In competitive multiplayer and esports environments, locking down or narrowing these limits is the primary method used to standardize hardware components across different vehicle models, ensuring a balanced grid without rewriting core chassis physics meshes..

#### <span id="page-84-4"></span>**III. Key Architecture & Data Fields Explained**

The schema for this asset mirrors the organizational layout of the standard setup file (Tyres, Aerodynamics, Suspension, Dampers, Drivetrain). However, instead of storing a single static setting, every individual parameter is transformed into a **nested object** containing regulatory and interface variables:

#### <span id="page-84-5"></span>**1 - THE ANATOMY OF A PARAMETER LIMIT OBJECT**

Every adjustable mechanical setting utilizes the following structural parameters:

- **• Min / Max:** The absolute lower and upper physical boundaries allowed by the simulation engine for this component.
- **• Step:** The exact mechanical increment or decrement applied per single "click" inside the garage menu.
- **• Is Modifiable:** A boolean flag (true/false). When set to false, the adjustment slider is locked and greyed out in the user interface.
- **• Hide Value:** A toggle allowing developers to obscure the raw physical value from the user screen (often used in high-level motorsport to simulate proprietary team data secrecy).
- **• Unit:** The textual unit label rendered on screen to contextualize the value (e.g., mm, Nm, Hz, Psi, deg).
- **• Fractional Digits:** Specifies the decimal point precision displayed on the user interface screen.
- **• Lut (Look-Up Table):** Maps the adjustment steps to an external curve, allowing linear menu clicks to translate into non-linear physical changes.

#### <span id="page-85-0"></span>**2 - CORE CATEGORIES OF APPLICATION**

- **• Tyres:** Enforces minimum safe cold inflation pressures to prevent tire carcass deflation/delamination, alongside maximum ranges for wheel alignment geometry (camber and toe).
- **• Aerodynamics:** Locks down the operational angles of front splitters and rear wings (often constrained to 1-degree or 0.5-degree steps) and limits the safe compression clearance of the underbody floor.
- **• Suspension Geometry & Rates:** Dictates the stiffest and softest allowable coil spring options (Wheel Rate) and limits the structural thickness options for front and rear anti-roll bars (Arbs).
- **• Dampers:** Defines the total number of valving adjustments ("clics") available for shock absorber damping across low-speed and high-speed compression (Bump) and extension (Rebound) cycles.
- **• Drivetrain & Differential:** Sets boundaries on differential clutch locking percentages under acceleration (Power), deceleration (Coast), and static resistance (Preload).

### <span id="page-85-1"></span>**IV. Interpretation of Setup Limits Strategies**

By reading a vehicle's specific limits file, developers and players can immediately identify its structural classification and engineering intent:

**• The Stock Production Profile:** In standard road vehicles, the vast majority of Is Modifiable flags are hard-locked to false. Parameters like spring rates, dampers, differential

behaviors, and aerodynamics are frozen to factory settings. Only basic tyre pressures and minor alignment tolerances remain adjustable for track days.

- **• The Pure Motorsport Profile (GT3 / Prototypes / Open-Wheel):** Almost all mechanical and aerodynamic flags are set to true. However, the window between Min and Max is deliberately narrow, engineered strictly to keep the car operating within its designed aerodynamic or suspension kinematic sweet spot. Increments match real-world race hardware (e.g., fixed damper click values).
- **• The BOP (Balance of Performance) Regulation Strategy:** Rather than altering a vehicle's engine power or weight mesh directly, series organizers can adjust this file to restrict tuning freedom. For instance, raising the Min value of a rear wing angle forces a car to run higher minimum downforce—intentionally increasing straight-line drag to slow it down on high-speed circuits.

### <span id="page-86-0"></span>**B. Schema**

```
├ 1. Car Data : string - path
├ 2. Mechanical Balance : object
│ ├ 2a. Arbs [x] : object | can have multiple Arbs
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 2b. Steer Ratio : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 2c. Brakes : object
│ │ ├ 2c1. Front Bias : object
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ │ │ └ 2a10. Treat As Boolean : boolean
│ │ ├ 2c2. Torque Multiplier : object
```

```
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ │ │ └ 2a10. Treat As Boolean : boolean
│ │ ├ 2c3. Brake Ducts [x] : object | can have multiple Brake Ducts
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ │ └ └ 2a10. Treat As Boolean : boolean
│ ├ 2d. Differential : object
│ │ ├ 2d1. Power : object
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ │ │ └ 2a10. Treat As Boolean : boolean
│ │ ├ 2d2. Coast : object
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ │ │ └ 2a10. Treat As Boolean : boolean
│ │ ├ 2d3. Preload : object
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ └ └ └ 2a10. Treat As Boolean : boolean
├ 3. Suspensions [x] : object | can have multiple Suspensions
```

```
│ ├ 3a. Wheel Rate : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 3b. Bump Stop Up : object
│ │ ├ 3b1. Range : object
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ │ │ └ 2a10. Treat As Boolean : boolean
│ │ ├ 3b2. Rate : object
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ │ └ └ 2a10. Treat As Boolean : boolean
│ ├ 3c. Bump Stop Down : object
│ │ ├ 3b1. Range : object
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
│ │ │ └ 2a10. Treat As Boolean : boolean
│ │ ├ 3b2. Range : object
│ │ │ ├ 2a1. Step : float
│ │ │ ├ 2a2. Min : float
│ │ │ ├ 2a3. Max : float
│ │ │ ├ 2a4. Lut : string - path
│ │ │ ├ 2a5. Is Modifiable : boolean
│ │ │ ├ 2a6. Hide Value : boolean
│ │ │ ├ 2a7. Is Negative : boolean
│ │ │ ├ 2a8. Unit : string
│ │ │ ├ 2a9. Fractional Digits : integer
```

```
│ │ └ └ 2a10. Treat As Boolean : boolean
│ ├ 3d. Helper Rate : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 3e. Helper Range : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
├ 4. Dampers [x] : object | can have multiple Dampers
│ ├ 4a. Slow Bump : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 4b. Fast Bump : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 4c. Slow Rebound : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
```

```
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 4d. Fast Rebound : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
├ 5. Alignments [x] : object | can have multiple Alignments
│ ├ 5a. Pressure : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 5b. Camber : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 5c. Toe : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 5d. Caster : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
```

```
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 5e. Static Camber : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 5f. Toe Out Linear : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 5g. Compound : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ └ └ 2a10. Treat As Boolean : boolean
├ 6. Electronics : object
│ ├ 6a. Tc1 : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6b. Tc2 : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
```

```
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6c. Abs : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6d. Esc : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6e. Ebb : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6f. Engine Map : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6g. Telemetry Laps To Record : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
```

```
│ ├ 6h. Turbo Boost Lv : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6i. Ers Deployment Map : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6j. Ers Recharge Lv : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 6k. Ers Heat Charging : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ └ └ 2a10. Treat As Boolean : boolean
├ 7. Aero : object
│ ├ 7a. Collar Positions [x] : object | can have multiple Collar 
Positions
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
```

```
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 7b. Front Target Height : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 7c. Rear Target Height : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 7d. Front Wing Angle : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ │ └ 2a10. Treat As Boolean : boolean
│ ├ 7e. Rear Wing Angle : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ └ └ 2a10. Treat As Boolean : boolean
├ 8. Fuel Strategy : object
│ ├ 7a. Fuel : object
│ │ ├ 2a1. Step : float
│ │ ├ 2a2. Min : float
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
```

```
│ └ └ 2a10. Treat As Boolean : boolean
└ 9. Use Single Compound : boolean
```

#### <span id="page-95-0"></span>**C. Example data**

#### <span id="page-95-1"></span>**I. Chosen Car Engine for Example**

- BMW M4 CSL ( slug : ks\_bmw\_m4\_csl )
- Lamborghini Countach ( slug : ks\_lamborghini\_countach )

#### <span id="page-95-2"></span>**II. Example**

#### <span id="page-95-3"></span>**BMW M4 CSL**

```
├ 1. Car Data : None 
├ 2. Mechanical Balance 
│ ├ 2a. Arbs 1 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 30000.00000 
│ │ ├ 2a3. Max : 30000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 2a. Arbs 2 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 11000.00000 
│ │ ├ 2a3. Max : 11000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 2b. Steer Ratio 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 15.00000 
│ │ ├ 2a3. Max : 15.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : None 
│ │ └ 2a10. Treat As Boolean : 0 
│ ├ 2c. Brakes 
│ │ ├ 2c1. Front Bias 
│ │ │ ├ 2a1. Step : 1.00000
```

```
│ │ │ ├ 2a2. Min : 0.00000 
│ │ │ ├ 2a3. Max : 100.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : None 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 2c2. Torque Multiplier 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 100.00000 
│ │ │ ├ 2a3. Max : 100.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ ├ 2d. Differential 
│ │ ├ 2d1. Power 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.25000 
│ │ │ ├ 2a3. Max : 0.25000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 2d2. Coast 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.55000 
│ │ │ ├ 2a3. Max : 0.55000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 2d3. Preload 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 1.00000 
│ │ │ ├ 2a3. Max : 1.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
├ 3. Suspensions 1 
│ ├ 3a. Wheel Rate
```

```
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 47000.00000 
│ │ ├ 2a3. Max : 47000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.01000 
│ │ │ ├ 2a2. Min : -0.09036 
│ │ │ ├ 2a3. Max : 0.15964 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 600.00000 
│ │ │ ├ 2a3. Max : 600.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.07036 
│ │ │ ├ 2a3. Max : 0.07036 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 1000.00000 
│ │ │ ├ 2a3. Max : 1000.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false
```

```
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 5000.00000 
│ │ ├ 2a3. Max : 5000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.03000 
│ │ ├ 2a3. Max : 0.03000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 3. Suspensions 2 
│ ├ 3a. Wheel Rate 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 47000.00000 
│ │ ├ 2a3. Max : 47000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.01000 
│ │ │ ├ 2a2. Min : -0.09036 
│ │ │ ├ 2a3. Max : 0.15964 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 600.00000 
│ │ │ ├ 2a3. Max : 600.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0
```

```
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.07036 
│ │ │ ├ 2a3. Max : 0.07036 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 1000.00000 
│ │ │ ├ 2a3. Max : 1000.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 5000.00000 
│ │ ├ 2a3. Max : 5000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.03000 
│ │ ├ 2a3. Max : 0.03000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 3. Suspensions 3 
│ ├ 3a. Wheel Rate 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 33000.00000 
│ │ ├ 2a3. Max : 33000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None
```

```
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.13069 
│ │ │ ├ 2a3. Max : 0.13069 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 500.00000 
│ │ │ ├ 2a3. Max : 500.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.10431 
│ │ │ ├ 2a3. Max : 0.10431 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 1000.00000 
│ │ │ ├ 2a3. Max : 1000.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 5000.00000 
│ │ ├ 2a3. Max : 5000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false
```

```
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.03000 
│ │ ├ 2a3. Max : 0.03000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 3. Suspensions 4 
│ ├ 3a. Wheel Rate 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 33000.00000 
│ │ ├ 2a3. Max : 33000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.13069 
│ │ │ ├ 2a3. Max : 0.13069 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 500.00000 
│ │ │ ├ 2a3. Max : 500.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.10431 
│ │ │ ├ 2a3. Max : 0.10431 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false
```

```
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 1000.00000 
│ │ │ ├ 2a3. Max : 1000.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 5000.00000 
│ │ ├ 2a3. Max : 5000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.03000 
│ │ ├ 2a3. Max : 0.03000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 4. Dampers 1 
│ ├ 4a. Slow Bump 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 5500.00000 
│ │ ├ 2a3. Max : 5500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4b. Fast Bump 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 1500.00000 
│ │ ├ 2a3. Max : 1500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false
```

```
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4c. Slow Rebound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 7500.00000 
│ │ ├ 2a3. Max : 7500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4d. Fast Rebound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 4750.00000 
│ │ ├ 2a3. Max : 4750.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 4. Dampers 2 
│ ├ 4a. Slow Bump 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 5500.00000 
│ │ ├ 2a3. Max : 5500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4b. Fast Bump 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 1500.00000 
│ │ ├ 2a3. Max : 1500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4c. Slow Rebound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 7500.00000 
│ │ ├ 2a3. Max : 7500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false
```

```
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4d. Fast Rebound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 4750.00000 
│ │ ├ 2a3. Max : 4750.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 4. Dampers 3 
│ ├ 4a. Slow Bump 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 4500.00000 
│ │ ├ 2a3. Max : 4500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4b. Fast Bump 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 2000.00000 
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4c. Slow Rebound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 6500.00000 
│ │ ├ 2a3. Max : 6500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4d. Fast Rebound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 4250.00000 
│ │ ├ 2a3. Max : 4250.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false
```

```
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 4. Dampers 4 
│ ├ 4a. Slow Bump 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 4500.00000 
│ │ ├ 2a3. Max : 4500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4b. Fast Bump 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 2000.00000 
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4c. Slow Rebound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 6500.00000 
│ │ ├ 2a3. Max : 6500.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4d. Fast Rebound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 4250.00000 
│ │ ├ 2a3. Max : 4250.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 5. Alignments 1 
│ ├ 5a. Pressure 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None
```

```
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5b. Camber 
│ │ ├ 2a1. Step : 0.10000 
│ │ ├ 2a2. Min : -2.50000 
│ │ ├ 2a3. Max : -1.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5c. Toe 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.15000 
│ │ ├ 2a3. Max : 0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5d. Caster 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.09195 
│ │ ├ 2a3. Max : 0.02195 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5e. Static Camber 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : -1.50000 
│ │ ├ 2a3. Max : -1.50000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5f. Toe Out Linear 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00050 
│ │ ├ 2a3. Max : 0.00050 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false
```

```
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5g. Compound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 2.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 5. Alignments 2 
│ ├ 5a. Pressure 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5b. Camber 
│ │ ├ 2a1. Step : 0.10000 
│ │ ├ 2a2. Min : -2.50000 
│ │ ├ 2a3. Max : -1.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5c. Toe 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.15000 
│ │ ├ 2a3. Max : 0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5d. Caster 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.09195 
│ │ ├ 2a3. Max : 0.02195 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false
```

```
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5e. Static Camber 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : -1.50000 
│ │ ├ 2a3. Max : -1.50000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5f. Toe Out Linear 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00050 
│ │ ├ 2a3. Max : 0.00050 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5g. Compound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 2.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 5. Alignments 3 
│ ├ 5a. Pressure 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5b. Camber 
│ │ ├ 2a1. Step : 0.10000 
│ │ ├ 2a2. Min : -3.00000 
│ │ ├ 2a3. Max : -0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true
```

```
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5c. Toe 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.15000 
│ │ ├ 2a3. Max : 0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5d. Caster 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5e. Static Camber 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : -2.00000 
│ │ ├ 2a3. Max : -2.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5f. Toe Out Linear 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00020 
│ │ ├ 2a3. Max : 0.00020 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5g. Compound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 2.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false
```

```
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 5. Alignments 4 
│ ├ 5a. Pressure 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5b. Camber 
│ │ ├ 2a1. Step : 0.10000 
│ │ ├ 2a2. Min : -3.00000 
│ │ ├ 2a3. Max : -0.50000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5c. Toe 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.15000 
│ │ ├ 2a3. Max : -0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5d. Caster 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5e. Static Camber 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : -2.00000 
│ │ ├ 2a3. Max : -2.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false
```

```
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5f. Toe Out Linear 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00020 
│ │ ├ 2a3. Max : 0.00020 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5g. Compound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 2.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 6. Electronics 
│ ├ 6a. Tc1 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 10.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6b. Tc2 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6c. Abs 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false
```

```
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6d. Esc 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 2.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6e. Ebb 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6f. Engine Map 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6g. Telemetry Laps To Record 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 99.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6h. Turbo Boost Lv 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false
```

```
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6i. Ers Deployment Map 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6j. Ers Recharge Lv 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6k. Ers Heat Charging 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 7. Aero 
│ ├ 7a. Collar Positions 1 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 140.00000 
│ │ ├ 2a3. Max : 140.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7a. Collar Positions 2 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 140.00000 
│ │ ├ 2a3. Max : 140.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false
```

```
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7a. Collar Positions 3 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 70.00000 
│ │ ├ 2a3. Max : 70.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7a. Collar Positions 4 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 70.00000 
│ │ ├ 2a3. Max : 70.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7b. Front Target Height 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 50.00000 
│ │ ├ 2a3. Max : 200.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7c. Rear Target Height 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 50.00000 
│ │ ├ 2a3. Max : 200.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7d. Front Wing Angle 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None
```

```
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7e. Rear Wing Angle 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 8. Fuel Strategy 
│ ├ 7a. Fuel 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 2.00000 
│ │ ├ 2a3. Max : 59.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
└ 9. Use Single Compound : false
```

# <span id="page-115-0"></span>**Lamborghini Countach**

```
├ 1. Car Data : None 
├ 2. Mechanical Balance 
│ ├ 2a. Arbs 1 
│ │ ├ 2a1. Step : 4000.00000 
│ │ ├ 2a2. Min : 28000.00000 
│ │ ├ 2a3. Max : 68000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 2a. Arbs 2 
│ │ ├ 2a1. Step : 5000.00000 
│ │ ├ 2a2. Min : 5000.00000 
│ │ ├ 2a3. Max : 50000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false
```

```
│ ├ 2b. Steer Ratio 
│ │ ├ 2a1. Step : 1.45000 
│ │ ├ 2a2. Min : -14.50000 
│ │ ├ 2a3. Max : -14.50000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : None 
│ │ └ 2a10. Treat As Boolean : 0 
│ ├ 2c. Brakes 
│ │ ├ 2c1. Front Bias 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 0.00000 
│ │ │ ├ 2a3. Max : 100.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : None 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 2c2. Torque Multiplier 
│ │ │ ├ 2a1. Step : 10.00000 
│ │ │ ├ 2a2. Min : 100.00000 
│ │ │ ├ 2a3. Max : 100.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ ├ 2d. Differential 
│ │ ├ 2d1. Power 
│ │ │ ├ 2a1. Step : 0.02000 
│ │ │ ├ 2a2. Min : 0.20000 
│ │ │ ├ 2a3. Max : 0.20000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 2d2. Coast 
│ │ │ ├ 2a1. Step : 0.04000 
│ │ │ ├ 2a2. Min : 0.40000 
│ │ │ ├ 2a3. Max : 0.40000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0
```

```
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 2d3. Preload 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 10.00000 
│ │ │ ├ 2a3. Max : 10.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
├ 3. Suspensions 1 
│ ├ 3a. Wheel Rate 
│ │ ├ 2a1. Step : 4000.00000 
│ │ ├ 2a2. Min : 50000.00000 
│ │ ├ 2a3. Max : 100000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.01200 
│ │ │ ├ 2a2. Min : 0.02933 
│ │ │ ├ 2a3. Max : 0.02933 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 35.00000 
│ │ │ ├ 2a2. Min : 350.00000 
│ │ │ ├ 2a3. Max : 350.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.00150 
│ │ │ ├ 2a2. Min : 0.10567 
│ │ │ ├ 2a3. Max : 0.010567 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false
```

```
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 35.00000 
│ │ │ ├ 2a2. Min : 350.00000 
│ │ │ ├ 2a3. Max : 350.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 3. Suspensions 2 
│ ├ 3a. Wheel Rate 
│ │ ├ 2a1. Step : 4000.00000 
│ │ ├ 2a2. Min : 50000.00000 
│ │ ├ 2a3. Max : 100000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.01200 
│ │ │ ├ 2a2. Min : 0.02933 
│ │ │ ├ 2a3. Max : 0.02933 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false
```

```
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 35.00000 
│ │ │ ├ 2a2. Min : 350.00000 
│ │ │ ├ 2a3. Max : 350.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.00150 
│ │ │ ├ 2a2. Min : 0.10567 
│ │ │ ├ 2a3. Max : 0.010567 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 35.00000 
│ │ │ ├ 2a2. Min : 350.00000 
│ │ │ ├ 2a3. Max : 350.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false
```

```
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 3. Suspensions 3 
│ ├ 3a. Wheel Rate 
│ │ ├ 2a1. Step : 4000.00000 
│ │ ├ 2a2. Min : 50000.00000 
│ │ ├ 2a3. Max : 100000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.01200 
│ │ │ ├ 2a2. Min : 0.02911 
│ │ │ ├ 2a3. Max : 0.02911 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 35.00000 
│ │ │ ├ 2a2. Min : 350.00000 
│ │ │ ├ 2a3. Max : 350.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.00150 
│ │ │ ├ 2a2. Min : 0.10589 
│ │ │ ├ 2a3. Max : 0.10589 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 35.00000 
│ │ │ ├ 2a2. Min : 350.00000 
│ │ │ ├ 2a3. Max : 350.00000 
│ │ │ ├ 2a4. Lut : None
```

```
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 3. Suspensions 4 
│ ├ 3a. Wheel Rate 
│ │ ├ 2a1. Step : 4000.00000 
│ │ ├ 2a2. Min : 50000.00000 
│ │ ├ 2a3. Max : 100000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.01200 
│ │ │ ├ 2a2. Min : 0.02911 
│ │ │ ├ 2a3. Max : 0.02911 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 35.00000 
│ │ │ ├ 2a2. Min : 350.00000 
│ │ │ ├ 2a3. Max : 350.00000
```

```
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 0.00150 
│ │ │ ├ 2a2. Min : 0.10589 
│ │ │ ├ 2a3. Max : 0.10589 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate 
│ │ │ ├ 2a1. Step : 35.00000 
│ │ │ ├ 2a2. Min : 350.00000 
│ │ │ ├ 2a3. Max : 350.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 4. Dampers 1 
│ ├ 4a. Slow Bump 
│ │ ├ 2a1. Step : 1000.00000 
│ │ ├ 2a2. Min : 10000.00000
```

```
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4b. Fast Bump 
│ │ ├ 2a1. Step : 100.00000 
│ │ ├ 2a2. Min : -2000.00000 
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4c. Slow Rebound 
│ │ ├ 2a1. Step : 1000.00000 
│ │ ├ 2a2. Min : 10000.00000 
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4d. Fast Rebound 
│ │ ├ 2a1. Step : 100.00000 
│ │ ├ 2a2. Min : -2000.00000 
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 4. Dampers 2 
│ ├ 4a. Slow Bump 
│ │ ├ 2a1. Step : 1000.00000 
│ │ ├ 2a2. Min : 10000.00000 
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4b. Fast Bump 
│ │ ├ 2a1. Step : 100.00000 
│ │ ├ 2a2. Min : -2000.00000
```

```
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4c. Slow Rebound 
│ │ ├ 2a1. Step : 1000.00000 
│ │ ├ 2a2. Min : 10000.00000 
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4d. Fast Rebound 
│ │ ├ 2a1. Step : 100.00000 
│ │ ├ 2a2. Min : -2000.00000 
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 4. Dampers 3 
│ ├ 4a. Slow Bump 
│ │ ├ 2a1. Step : 1000.00000 
│ │ ├ 2a2. Min : 10000.00000 
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4b. Fast Bump 
│ │ ├ 2a1. Step : 100.00000 
│ │ ├ 2a2. Min : -2000.00000 
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4c. Slow Rebound 
│ │ ├ 2a1. Step : 1000.00000 
│ │ ├ 2a2. Min : 10000.00000
```

```
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4d. Fast Rebound 
│ │ ├ 2a1. Step : 100.00000 
│ │ ├ 2a2. Min : -2000.00000 
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 4. Dampers 4 
│ ├ 4a. Slow Bump 
│ │ ├ 2a1. Step : 1000.00000 
│ │ ├ 2a2. Min : 10000.00000 
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4b. Fast Bump 
│ │ ├ 2a1. Step : 100.00000 
│ │ ├ 2a2. Min : -2000.00000 
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4c. Slow Rebound 
│ │ ├ 2a1. Step : 1000.00000 
│ │ ├ 2a2. Min : 10000.00000 
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 4d. Fast Rebound 
│ │ ├ 2a1. Step : 100.00000 
│ │ ├ 2a2. Min : -2000.00000
```

```
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 5. Alignments 1 
│ ├ 5a. Pressure 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : psi 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5b. Camber 
│ │ ├ 2a1. Step : 0.10000 
│ │ ├ 2a2. Min : -2.50000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : Deg 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5c. Toe 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.20000 
│ │ ├ 2a3. Max : 0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : Deg 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5d. Caster 
│ │ ├ 2a1. Step : 0.00166 
│ │ ├ 2a2. Min : -0.02000 
│ │ ├ 2a3. Max : -0.02000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5e. Static Camber 
│ │ ├ 2a1. Step : 0.18000 
│ │ ├ 2a2. Min : -1.80000
```

```
│ │ ├ 2a3. Max : -1.80000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5f. Toe Out Linear 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5g. Compound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 1.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 5. Alignments 2 
│ ├ 5a. Pressure 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : psi 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5b. Camber 
│ │ ├ 2a1. Step : 0.10000 
│ │ ├ 2a2. Min : -2.50000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : Deg 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5c. Toe 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.20000
```

```
│ │ ├ 2a3. Max : 0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : Deg 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5d. Caster 
│ │ ├ 2a1. Step : 0.00166 
│ │ ├ 2a2. Min : -0.02000 
│ │ ├ 2a3. Max : -0.02000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5e. Static Camber 
│ │ ├ 2a1. Step : 0.18000 
│ │ ├ 2a2. Min : -1.80000 
│ │ ├ 2a3. Max : -1.80000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5f. Toe Out Linear 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5g. Compound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 1.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 5. Alignments 3 
│ ├ 5a. Pressure 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000
```

```
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : psi 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5b. Camber 
│ │ ├ 2a1. Step : 0.10000 
│ │ ├ 2a2. Min : -2.50000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : Deg 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5c. Toe 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.20000 
│ │ ├ 2a3. Max : 0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : Deg 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5d. Caster 
│ │ ├ 2a1. Step : 0.00166 
│ │ ├ 2a2. Min : -0.02000 
│ │ ├ 2a3. Max : -0.02000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5e. Static Camber 
│ │ ├ 2a1. Step : 0.18000 
│ │ ├ 2a2. Min : -1.80000 
│ │ ├ 2a3. Max : -1.80000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5f. Toe Out Linear 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000
```

```
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5g. Compound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 1.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 5. Alignments 4 
│ ├ 5a. Pressure 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : psi 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5b. Camber 
│ │ ├ 2a1. Step : 0.10000 
│ │ ├ 2a2. Min : -2.50000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : Deg 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5c. Toe 
│ │ ├ 2a1. Step : 0.01000 
│ │ ├ 2a2. Min : -0.20000 
│ │ ├ 2a3. Max : 0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : Deg 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5d. Caster 
│ │ ├ 2a1. Step : 0.00166 
│ │ ├ 2a2. Min : -0.02000 
│ │ ├ 2a3. Max : -0.02000
```

```
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5e. Static Camber 
│ │ ├ 2a1. Step : 0.18000 
│ │ ├ 2a2. Min : -1.80000 
│ │ ├ 2a3. Max : -1.80000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5f. Toe Out Linear 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 5g. Compound 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 1.00000 
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 6. Electronics 
│ ├ 6a. Tc1 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 1.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6b. Tc2 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000
```

```
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6c. Abs 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6d. Esc 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6e. Ebb 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6f. Engine Map 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6g. Telemetry Laps To Record 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 99.00000 
│ │ ├ 2a4. Lut : None
```

```
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6h. Turbo Boost Lv 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6i. Ers Deployment Map 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6j. Ers Recharge Lv 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6k. Ers Heat Charging 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
├ 7. Aero 
│ ├ 7a. Collar Positions 1 
│ │ ├ 2a1. Step : 7.00000 
│ │ ├ 2a2. Min : 70.00000 
│ │ ├ 2a3. Max : 70.00000 
│ │ ├ 2a4. Lut : None
```

```
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7a. Collar Positions 2 
│ │ ├ 2a1. Step : 7.00000 
│ │ ├ 2a2. Min : 70.00000 
│ │ ├ 2a3. Max : 70.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7a. Collar Positions 3 
│ │ ├ 2a1. Step : 5.00000 
│ │ ├ 2a2. Min : 50.00000 
│ │ ├ 2a3. Max : 50.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7a. Collar Positions 4 
│ │ ├ 2a1. Step : 5.00000 
│ │ ├ 2a2. Min : 50.00000 
│ │ ├ 2a3. Max : 50.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7b. Front Target Height 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 180.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7c. Rear Target Height 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 20.00000 
│ │ ├ 2a3. Max : 180.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false
```

```
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7d. Front Wing Angle 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7e. Rear Wing Angle 
│ │ ├ 2a1. Step : 0.00000 
│ │ ├ 2a2. Min : 0.00000 
│ │ ├ 2a3. Max : 0.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
├ 8. Fuel Strategy 
│ ├ 7a. Fuel 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 1.00000 
│ │ ├ 2a3. Max : 120.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false 
└ 9. Use Single Compound : false
```

# <span id="page-136-0"></span>**7. Car Setup Units [ .carsetupunits ]**

#### <span id="page-136-1"></span>**A. Description**

### <span id="page-136-2"></span>**I. General Description**

The **Car Setup Units** asset is the primary translation matrix that standardizes how physical metrics are rendered visually within the simulation's user interface. While other physics files handle raw mathematical processing (often utilizing raw SI metrics like Newtons, meters, or Kelvin internally), the Car Setup Units file dictates the exact localization string, data labels, and scaling rules for what the player sees on screen.

It ensures that complex mechanics—such as hydraulic pressure, kinetic stiffness, or geometric angles—are mapped out into readable, intuitive measurements that real-world mechanics and simulation drivers can interact with seamlessly across different regions.

#### <span id="page-136-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

While the Car Setup Units asset does not modify the vehicle's physics engine computations directly, its architecture heavily influences the configuration pipeline and user experience:

- **• Tuning Accuracy and Readability:** It prevents telemetry translation errors. By mapping clear unit tokens (e.g., matching a dampening constant to a specific text string), it guides modders to configure logical tuning increments.
- **• Localization & Community Usability:** It serves as the primary system allowing global simulation players to quickly comprehend the vehicle state. It dictates whether a driver works with Metric systems, Imperial defaults, or hardware-specific indicators (like "valving clicks").
- **• Telemetry Data Alignment:** It simplifies the correlation between in-game setup adjustments and exported engineering telemetry graphs (e.g., matching MoTeC worksheets to the exact garage presentation units).

#### <span id="page-136-4"></span>**III. Key Architecture & Data Fields Explained**

The file structure maps directly over the variable names found in the global tuning schemas. Instead of assigning thresholds or steps, it assigns text strings, dimensional values, and contextual formatting markers.

#### <span id="page-136-5"></span>**1 - WHEEL AND TYRE TELEMETRY ALIGNMENT**

Every adjustable mechanical setting utilizes the following structural parameters:

**• Pressure Units:** Dictates the presentation of pneumatic pressure vectors. Typically configured to display as PSI (Pounds per Square Inch) or bar, ensuring drivers can balance the thermal expanding footprint accurately.

**• Alignment Angles:** Sets the formatting label for spatial geometric alignment. Variables like Camber, Toe, and Caster are universally assigned the degrees symbol (°) or millimeter targets (mm) to track wheel placement relative to the contact patch.

#### <span id="page-137-0"></span>**2 - SUSPENSION COMPONENTS & KINEMATICS**

- **• Spring Stiffness / Wheel Rates:** Controls the representation of pure compression resistance. These strings translate internal structural forces into readable loads, standardizing on metrics like N/mm (Newtons per millimeter), kg/ mm, or specialized frequency descriptors like Hz (Hertz)
- **• Damper Damping Coefficients:** Maps out energy dissipation factors. Because raw internal forces use complex scientific units like Ns/m (Newton-seconds per meter), this asset often simplifies the interface display to strings like Ns/m or redirects the interface to parse numbers as absolute hardware steps labeled as clics or clicks.

#### <span id="page-137-1"></span>**3 - AERODYNAMICS & AEROSTATIC CLEARANCE**

- **• Ride Heights / Ground Clearance:** Dictates the unit configuration for the aerostatic floor platform tracking. It handles structural frame clearances, mapping them cleanly to localized metric length units, universally defined as mm (millimeters) to allow precise platform rake tracking.
- **• Aero Wing Inclinometers:** Configures the visual representation of adjustable wing blades, setting the display string to absolute angular units (such as degrees °) or fixed geometric positions.

#### <span id="page-137-2"></span>**IV. Interpretation of Setup Units Strategies**

When interpreting a vehicle's exported architecture, the units configuration immediately establishes the target simulation profile and intended engineering depth:

- **• The Scientific Engineering Profile:** Characterized by pure, unmodified physical engineering notations. Damper configurations read strictly as Ns/m, and spring configurations read as N/mm. This gives advanced race engineers absolute mathematical transparency when calculating real-time dynamic weight transfer or suspension frequencies.
- **• The Driver-Centric / Click Profile:** Simplifies high-tier internal metrics to match active physical components. Instead of displaying a confusing velocity value like 1500 Ns/m, the unit system references the hardware's detent steps, displaying simply as integers. This replicates a real racing driver counting physical clicks on an adjustable Ohlins or Penske shock absorber matrix while sitting in the pitlane.

# <span id="page-137-3"></span>**B. Schema**

```
├ 1. Mechanical Balance : object
│ ├ 1a. Arbs [x] : string | can have multiple Arbs
│ ├ 1b Steer Ratio : string
│ ├ 1c. Brakes : object
```

```
│ │ ├ 1c1. Front Bias : string
│ │ ├ 1c2. Torque Multiplier : string
│ │ └ 1c3. Brake Ducts [x] : string | can have multiple Brake Ducts 
│ ├ 1d. Differential : object
│ │ ├ 1d1. Power : string 
│ │ ├ 1d2. Coast : string
│ └ └ 1d3. Preload : string
├ 2. Suspensions [x] : object | can have multiple Suspensions
│ ├ 2a. Wheel Rate : string
│ ├ 2b. Bump Stop Up : object
│ │ ├ 2b1. Range : string
│ │ └ 2b2. Rate : string
│ ├ 2c. Bump Stop Down : object
│ │ ├ 2b1. Range : string
│ │ └ 2b2. Rate : string
│ ├ 2d. Helper Rate : string
│ └ 2e. Helper Range : string
├ 3. Dampers [x] : object | can have multiple Dampers
│ ├ 3a. Slow Bump : string
│ ├ 3b. Fast Bump : string
│ ├ 3c. Slow Rebound : string
│ └ 3d. Fast Rebound : string
├ 4. Alignments [x] : object | can have multiple Alignments
│ ├ 4a. Pressure : string
│ ├ 4b. Camber : string
│ ├ 4c. Toe : string
│ ├ 4d. Caster : string
│ ├ 4e. Static Camber : string
│ ├ 4f. Toe Out Camber : string
│ └ 4g. Compound : string
├ 5. Electronics : object
│ ├ 5a. Tc1 : string
│ ├ 5b. Tc2 : string
│ ├ 5c. Abs : string
│ ├ 5d. Esc : string
│ ├ 5e. Ebb : string
│ ├ 5f. Engine Map : string
│ ├ 5g. Telemetry Laps To Record : string
│ ├ 5h. Turbo Boost Lv : string
│ ├ 5i. Ers Deployment Map : string
│ ├ 5j. Ers Recharge Lv : string
│ └ 5k. Ers Heat Charging : string
├ 6. Aero : object
│ ├ 6a. Collar Positions [x] : string | can have multiple Collar 
Positions
│ ├ 6b. Front Target Height : string
│ ├ 6c. Rear Target Height : string
│ ├ 6e. Front Wing Angle : string
│ └ 6f. Rear Wing Angle : string
├ 7. Fuel Strategy : object
│ └ 7a. Fuel : string
└ 8. Use Single Compound : string
```

#### <span id="page-139-0"></span>**C. Example data**

# <span id="page-139-1"></span>**I. Chosen Car Engine for Example**

- Setup Units ( slug : setup\_units ) [ common\_phsx ]

#### <span id="page-139-2"></span>**II. Example**

#### <span id="page-139-3"></span>**Setup Units**

```
├ 1. Mechanical Balance 
│ ├ 1a. Arbs 1 : N/m 
│ ├ 1a. Arbs 2 : N/m 
│ ├ 1b Steer Ratio : None 
│ ├ 1c. Brakes 
│ │ ├ 1c1. Front Bias : % 
│ │ ├ 1c2. Torque Multiplier : % 
│ │ └ 1c3. Brake Ducts : None
│ ├ 1d. Differential 
│ │ ├ 1d1. Power : None 
│ │ ├ 1d2. Coast : None 
│ └ └ 1d3. Preload : Nm 
├ 2. Suspensions 1 
│ ├ 2a. Wheel Rate : N/m 
│ ├ 2b. Bump Stop Up 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2c. Bump Stop Down 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2d. Helper Rate : N/m 
│ └ 2e. Helper Range : m 
├ 2. Suspensions 2 
│ ├ 2a. Wheel Rate : N/m 
│ ├ 2b. Bump Stop Up 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2c. Bump Stop Down 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2d. Helper Rate : N/m 
│ └ 2e. Helper Range : m 
├ 2. Suspensions 3 
│ ├ 2a. Wheel Rate : N/m 
│ ├ 2b. Bump Stop Up 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2c. Bump Stop Down 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2d. Helper Rate : N/m 
│ └ 2e. Helper Range : m
```

```
├ 2. Suspensions 4 
│ ├ 2a. Wheel Rate : N/m 
│ ├ 2b. Bump Stop Up 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2c. Bump Stop Down 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2d. Helper Rate : N/m 
│ └ 2e. Helper Range : m 
├ 2. Suspensions 5 
│ ├ 2a. Wheel Rate : N/m 
│ ├ 2b. Bump Stop Up 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2c. Bump Stop Down 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2d. Helper Rate : N/m 
│ └ 2e. Helper Range : m 
├ 2. Suspensions 6 
│ ├ 2a. Wheel Rate : N/m 
│ ├ 2b. Bump Stop Up 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2c. Bump Stop Down 
│ │ ├ 2b1. Range : m 
│ │ └ 2b2. Rate : N 
│ ├ 2d. Helper Rate : N/m 
│ └ 2e. Helper Range : m 
├ 3. Dampers 1 
│ ├ 3a. Slow Bump : Ns/m 
│ ├ 3b. Fast Bump : Ns/m 
│ ├ 3c. Slow Rebound : Ns/m 
│ └ 3d. Fast Rebound : Ns/m 
├ 3. Dampers 2 
│ ├ 3a. Slow Bump : Ns/m 
│ ├ 3b. Fast Bump : Ns/m 
│ ├ 3c. Slow Rebound : Ns/m 
│ └ 3d. Fast Rebound : Ns/m 
├ 3. Dampers 3 
│ ├ 3a. Slow Bump : Ns/m 
│ ├ 3b. Fast Bump : Ns/m 
│ ├ 3c. Slow Rebound : Ns/m 
│ └ 3d. Fast Rebound : Ns/m 
├ 3. Dampers 4 
│ ├ 3a. Slow Bump : Ns/m 
│ ├ 3b. Fast Bump : Ns/m 
│ ├ 3c. Slow Rebound : Ns/m 
│ └ 3d. Fast Rebound : Ns/m 
├ 3. Dampers 5 
│ ├ 3a. Slow Bump : Ns/m 
│ ├ 3b. Fast Bump : Ns/m 
│ ├ 3c. Slow Rebound : Ns/m 
│ └ 3d. Fast Rebound : Ns/m 
├ 3. Dampers 6
```

```
│ ├ 3a. Slow Bump : Ns/m 
│ ├ 3b. Fast Bump : Ns/m 
│ ├ 3c. Slow Rebound : Ns/m 
│ └ 3d. Fast Rebound : Ns/m 
├ 4. Alignments 1 
│ ├ 4a. Pressure : PSI 
│ ├ 4b. Camber : ° 
│ ├ 4c. Toe : ° 
│ ├ 4d. Caster : None 
│ ├ 4e. Static Camber : ° 
│ ├ 4f. Toe Out Camber : ° 
│ └ 4g. Compound : None 
├ 4. Alignments 2 
│ ├ 4a. Pressure : PSI 
│ ├ 4b. Camber : ° 
│ ├ 4c. Toe : ° 
│ ├ 4d. Caster : None 
│ ├ 4e. Static Camber : ° 
│ ├ 4f. Toe Out Camber : ° 
│ └ 4g. Compound : None 
├ 4. Alignments 3 
│ ├ 4a. Pressure : PSI 
│ ├ 4b. Camber : ° 
│ ├ 4c. Toe : ° 
│ ├ 4d. Caster : None 
│ ├ 4e. Static Camber : ° 
│ ├ 4f. Toe Out Camber : ° 
│ └ 4g. Compound : None 
├ 4. Alignments 4 
│ ├ 4a. Pressure : PSI 
│ ├ 4b. Camber : ° 
│ ├ 4c. Toe : ° 
│ ├ 4d. Caster : None 
│ ├ 4e. Static Camber : ° 
│ ├ 4f. Toe Out Camber : ° 
│ └ 4g. Compound : None 
├ 5. Electronics 
│ ├ 5a. Tc1 : None 
│ ├ 5b. Tc2 : None 
│ ├ 5c. Abs : None 
│ ├ 5d. Esc : None 
│ ├ 5e. Ebb : None 
│ ├ 5f. Engine Map : None 
│ ├ 5g. Telemetry Laps To Record : None 
│ ├ 5h. Turbo Boost Lv : None 
│ ├ 5i. Ers Deployment Map : None 
│ ├ 5j. Ers Recharge Lv : None 
│ └ 5k. Ers Heat Charging : None 
├ 6. Aero 
│ ├ 6a. Collar Positions 1 : m 
│ ├ 6a. Collar Positions 2 : m 
│ ├ 6a. Collar Positions 3 : m 
│ ├ 6a. Collar Positions 4 : m 
│ ├ 6b. Front Target Height : mm 
│ ├ 6c. Rear Target Height : mm 
│ ├ 6e. Front Wing Angle : °
```

│ └ 6f. Rear Wing Angle : °

├ 7. Fuel Strategy │ └ 7a. Fuel : L

└ 8. Use Single Compound : None

# <span id="page-143-0"></span>**8. Car Tuning Parts [ .tuningpart ]**

# <span id="page-143-1"></span>**A. Description**

### <span id="page-143-2"></span>**I. General Description**

The **Car Tuning Parts** asset (typically using the .tuningpart extension) acts as the modular configuration switchboard for vehicle variants within the simulation engine. While other assets define the unyielding mechanical foundations of a baseline model, the Car Tuning Parts file defines optional component swaps, performance packages, upgrades, or regulatory restrictors.

It serves as an administrative routing layer that points directly to secondary sub-physics files (such as alternative engines, custom gearboxes, specialized aerodynamics profiles, or strict setup limits). When a specific tuning part is selected, the physics engine hot-swaps or overrides the default baseline references with the nested paths specified inside this module.

### <span id="page-143-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The configurations set within the Car Tuning Parts asset fundamentally alter a vehicle's mechanical identity, eligibility, and on-track physics behavior:

- **• Variant and Package Management:** It dictates whether a car operates in a standard street trim, a modified track-day package, or a fully restricted competitive racing spec (e.g., converting a baseline road car into an upgraded GT-spec variant).
- **• Dynamic Physics Overrides:** It intercepts default component behaviors. By changing structural paths, a single vehicle folder can dynamically simulate completely distinct power units, differential units, or aerodynamic maps depending on the activated part.
- **• Electronic and System Level Toggles:** It regulates driver aids and system availability on a per-variant basis, allowing developers to cleanly toggle entire sub-systems—such as completely removing ABS and Traction Control—without altering the baseline vehicle architecture.
- **• Targeted Balance of Performance (BOP):** It provides a clean vector for balancing competitive series by forcing specific tuning parts (like alternative engine limiters or forced ballast matrices) onto specific cars depending on the event configuration.

#### <span id="page-143-4"></span>**III. Key Architecture & Data Fields Explained**

The internal hierarchy of a Car Tuning Parts object is built around system classification tags (Physics Tuning / Car Part Type) paired with explicit operational file pathways (Path).

#### <span id="page-143-5"></span>**1 - TUNING PART CORE DEFINITIONS**

**• Tuning Part Edit / Name:** The distinct identifier string labeling the specific package or modification option displayed inside the user selection menus.

- **• Physics Tuning Type:** An enum declaration stating which core mechanical domain this modification controls or replaces (e.g., Drivetrain, Engine, Setup Limits, <None>).
- **• Car Part Type:** Defines the structural categorization string for the modification package, standardizing on system nodes such as Mechanics\_Engine, Mechanics\_Drivetrain, or Mechanics\_Electronics.

# <span id="page-144-0"></span>**2 - COMPONENT PATH OVERRIDES**

- **• Engine Path Redirects:** Links directly to standalone, alternative propulsion blueprints (e.g., swapping a stock motor configuration path for a highperformance .carengine profile).
- **• Drivetrain Path Redirects:** Points to custom transmission or differential assets (e.g., swapping an open differential map for a highly specific Limited-Slip Differential .drivetrain asset).
- **• Setup Limits Redirects:** Routes the vehicle garage interface to alternative slider constraints (e.g., enforcing an entirely unique .carsetuplimits file when a "No ABS/ No TC" motorsport variant is active).

### <span id="page-144-1"></span>**IV. Interpretation of Tuning Part Strategies**

Analyzing a vehicle's .tuningpart matrix reveals how developers structure component modularity across different racing series:

- **• The Upgraded Component Profile:** Used to simulate aftermarket mechanical parts or step-by-step performance stages. For example, a vintage car might feature a tuning part named Limited-Slip Differential. Its internal fields explicitly route the Physics Tuning: Drivetrain node to a custom path containing tighter clutch plates and locking ramps, replacing the stock open differential behavior seamlessly when purchased or activated.
- **• The Electronic Restrictor Profile (e.g., GT3 Cup / Monoregulation):** Used to strip consumer aids for pure motorsport specifications. A tuning part like No ABS No TC sets the Physics Tuning pointer to <None> or redirects the hardware paths to lock out secondary algorithmic calculations, forcing the braking model to bypass anti-lock logic loops and rely purely on linear hydraulic pressure limits

#### <span id="page-144-2"></span>**B. Schema**

```
├ 1. Physics Tuning : enum
├ 2. [physics_tuning] : object | object key take the value of 1. Physics 
Tuning. Key-Value on this object will depend on 1. selection
│ ├ 2a. (Engine, Gearbox, Drivetrain, Clutch, Brake System, Electronics, 
Wing, Setup, Setup Limits) Path : string - path
│ ├ 2b. (Engine Tune) Multiplier : float
│ ├ 2c. (Engine Tune) Add : float
│ ├ 2d. (Engine Tune) Cos Ampl : float
│ ├ 2e. (Engine Tune) Cos Period : float
│ ├ 2f. (Engine Tune) Cos Phase : float
│ ├ 2g. (Brakes) Front Path : string - path
│ ├ 2h. (Brakes) Rear Path : float
```

```
│ ├ 2i. (Suspensions) Coilover Path Front : string - path
│ ├ 2j. (Suspensions) Coilover Path Rear : string - path
│ ├ 2k. (Suspensions Geometry) Geometry Path Front : string - path
│ ├ 2l. (Suspensions Geometry) Geometry Path Rear : string - path
│ ├ 2m. (Wing) Wing Index Override : integer
│ ├ 2n. (Aero Package) Data : object
│ │ ├ 2n1. Slip Gain Mult : float
│ │ ├ 2n2. Speed Factor Mult : float
│ │ ├ 2n3. Downforces [x] : object | can have multiple Downforces
│ │ │ ├ 2n3a. Position : x, y, z float
│ │ │ ├ 2n3b. Cl Gain : float
│ │ │ ├ 2n3c. Cd Gain : float
│ │ │ ├ 2n3d. Yaw Gain : float
│ │ │ ├ 2n3e. Drag Per Cool Transfer : float
│ │ │ ├ 2n3f. Damage C L [x] : float | can have multiple Damage C L
│ │ │ ├ 2n3g. Damage C D [x] : float | can have multiple Damage C D
│ │ │ ├ 2n3h. Downforce Controllers [x] : object | can have multiple 
Downforce Controllers
│ │ │ │ ├ 2n3h1. Combinator Mode : enum
│ │ │ │ ├ 2n3h2. Input : enum
│ │ │ │ ├ 2n3h3. Filter : float
│ │ │ │ ├ 2n3h4. Up Limit : float
│ │ │ │ ├ 2n3h5. Down Limit : float
│ │ │ │ └ 2n3h6. Lut : string - path
│ │ │ ├ 2n3i. Lift Per Front Angle : float
│ │ │ ├ 2n3j. Lift Per Rear Angle : float
│ │ │ ├ 2n3k. Drag Per Front Angle : float
│ │ │ ├ 2n3l. Drag Per Rear Angle : float
│ │ │ ├ 2n3m. Default Front Angle : float
│ │ │ └ 2n3n. Default Rear Angle : float
│ │ ├ 2n4. Front Lift : string - path
│ │ ├ 2n5. Rear Lift : string - path
│ │ ├ 2n6. Drag : string - path
│ │ └ 2n7. Wings Path [x] : string - path
│ ├ 2o. (Performance Modes Tuning) Performance Modes [x] : object | can 
have multiple Performance Modes
│ │ ├ 2o1. Performance Mode Name : string
│ │ ├ 2o2. Electronics Settings : object
│ │ │ ├ 2o2a. Tc1 : float
│ │ │ ├ 2o2b. Tc2 : float
│ │ │ ├ 2o2c. Abs : float
│ │ │ ├ 2o2d. Esc : float
│ │ │ ├ 2o2e. Ebb : float
│ │ │ ├ 2o2f. Engine Map : float
│ │ │ ├ 2o2g. Telemetry Laps To Record : float
│ │ │ ├ 2o2h. Turbo Boost Lv : float
│ │ │ ├ 2o2i. Ers Deployment Map : float
│ │ │ ├ 2o2j. Ers Recharge Lv : float
│ │ │ └ 2o2k. Ers Heat Charging : float
│ │ ├ 2o3. Brake Settings : object
│ │ │ ├ 2o3a. Front Brias : float
│ │ │ ├ 2o3b. Torque Multiplier : float
│ │ │ └ 2o3c. Brake Ducts [x] : float | can have multiple Brake Ducts
│ │ ├ 2o4. Damper Settings [x] : object | can have multiple Damper 
Settings
│ │ │ ├ 2o4a. Slow Bump : float
```

```
│ │ │ ├ 2o4b. Fast Bump : float
│ │ │ ├ 2o4c. Slow Rebound : float
│ │ │ └ 2o4d. Fast Rebound : float
│ │ ├ 2o5. Differential Data : object
│ │ │ ├ 2o5a. Type : enum
│ │ │ ├ 2o5b. Power : float
│ │ │ ├ 2o5c. Coast : float
│ │ │ ├ 2o5d. Preload : float
│ │ │ ├ 2o5e. Front Share : float
│ │ │ ├ 2o5f. Torque Bias Ratio Power : float
│ │ │ ├ 2o5g. Torque Bias Ratio Coast : float
│ │ │ ├ 2o5h. Thermal Capacity : float
│ │ │ ├ 2o5i. Surface : float
│ │ │ ├ 2o5j. Heat Transfer Coeff : float
│ │ │ ├ 2o5k. Wear Factor : float
│ │ │ ├ 2o5l. Friction Reduction With T : float
│ │ │ └ 2o5m. Friction Ref T : float
│ │ ├ 2o6. Four W D Differentials : object
│ │ │ ├ 2o6a. Front Diff : object
│ │ │ │ ├ 2o6a1. Type : enum
│ │ │ │ ├ 2o6a2. Power : float
│ │ │ │ ├ 2o6a3. Coast : float
│ │ │ │ ├ 2o6a4. Preload : float
│ │ │ │ ├ 2o6a5. Front Share : float
│ │ │ │ ├ 2o6a6. Torque Bias Ratio Power : float
│ │ │ │ ├ 2o6a7. Torque Bias Ratio Coast : float
│ │ │ │ ├ 2o6a8. Thermal Capacity : float
│ │ │ │ ├ 2o6a9. Surface : float
│ │ │ │ ├ 2o6a10. Heat Transfer Coeff : float
│ │ │ │ ├ 2o6a11. Wear Factor : float
│ │ │ │ ├ 2o6a12. Friction Reduction With T : float
│ │ │ │ └ 2o6a13. Friction Ref T : float
│ │ │ ├ 2o6b. Center Diff : object
│ │ │ │ ├ 2o6b1. Type : enum
│ │ │ │ ├ 2o6b2. Power : float
│ │ │ │ ├ 2o6b3. Coast : float
│ │ │ │ ├ 2o6b4. Preload : float
│ │ │ │ ├ 2o6b5. Front Share : float
│ │ │ │ ├ 2o6b6. Torque Bias Ratio Power : float
│ │ │ │ ├ 2o6b7. Torque Bias Ratio Coast : float
│ │ │ │ ├ 2o6b8. Thermal Capacity : float
│ │ │ │ ├ 2o6b9. Surface : float
│ │ │ │ ├ 2o6b10. Heat Transfer Coeff : float
│ │ │ │ ├ 2o6b11. Wear Factor : float
│ │ │ │ ├ 2o6b12. Friction Reduction With T : float
│ │ │ │ └ 2o6b13. Friction Ref T : float
│ │ │ └ 2o6c. Rear Diff : object
│ │ │ │ ├ 2o6c1. Type : enum
│ │ │ ├ 2o6c2. Power : float
│ │ │ ├ 2o6c3. Coast : float
│ │ │ ├ 2o6c4. Preload : float
│ │ │ ├ 2o6c5. Front Share : float
│ │ │ ├ 2o6c6. Torque Bias Ratio Power : float
│ │ │ ├ 2o6c7. Torque Bias Ratio Coast : float
│ │ │ ├ 2o6c8. Thermal Capacity : float
│ │ │ ├ 2o6c9. Surface : float
```

```
│ │ │ ├ 2o6c10. Heat Transfer Coeff : float
│ │ │ ├ 2o6c11. Wear Factor : float
│ │ │ ├ 2o6c12. Friction Reduction With T : float
│ │ │ └ 2o6c13. Friction Ref T : float
│ │ ├ 2o7. Front Lock Controllers : object
│ │ │ ├ 2o7a. Name : string
│ │ │ └ 2o7b. Stages [x] : object | can have multiple Stages
│ │ │ ├ 2o7b1. Input Var : enum
│ │ │ ├ 2o7b2. Combinator Mode : enum
│ │ │ ├ 2o7b3. Lut : string - path
│ │ │ ├ 2o7b4. Filter Gain : float
│ │ │ ├ 2o7b5. Up Limit : float
│ │ │ ├ 2o7b6. Down Limit : float
│ │ │ ├ 2o7b7. Current Value : float
│ │ │ └ 2o7b8. Const Value : float
│ │ ├ 2o8. Center Lock Controllers : object
│ │ │ ├ 2o8a. Name : string
│ │ │ └ 2o8b. Stages [x] : object
│ │ │ ├ 2o8b1. Input Var : enum
│ │ │ ├ 2o8b2. Combinator Mode : enum
│ │ │ ├ 2o8b3. Lut : string - path
│ │ │ ├ 2o8b4. Filter Gain : float
│ │ │ ├ 2o8b5. Up Limit : float
│ │ │ ├ 2o8b6. Down Limit : float
│ │ │ ├ 2o8b7. Current Value : float
│ │ │ └ 2o8b8. Const Value : float
│ │ ├ 2o9. Rear Lock Controllers : object
│ │ │ ├ 2o9a. Name : string
│ │ │ └ 2o9b. Stages [x] : object
│ │ │ ├ 2o9b1. Input Var : enum
│ │ │ ├ 2o9b2. Combinator Mode : enum
│ │ │ ├ 2o9b3. Lut : string - path
│ │ │ ├ 2o9b4. Filter Gain : float
│ │ │ ├ 2o9b5. Up Limit : float
│ │ │ ├ 2o9b6. Down Limit : float
│ │ │ ├ 2o9b7. Current Value : float
│ │ │ └ 2o9b8. Const Value : float
│ │ ├ 2o10. Awd Clutches [x] : object
│ │ │ ├ 2o10a. Position : integer
│ │ │ ├ 2o10b. Preload : float
│ │ │ └ 2o10c. Controllers : object
│ │ │ ├ 2o10c1. Name : string
│ │ │ └ 2o10c2. Stages [x] : object
│ │ │ ├ 2o10c2a. Input Var : enum
│ │ │ ├ 2o10c2b. Combinator Mode : enum
│ │ │ ├ 2o10c2c. Lut : string - path
│ │ │ ├ 2o10c2d. Filter Gain : float
│ │ │ ├ 2o10c2e. Up Limit : float
│ │ │ ├ 2o10c2f. Down Limit : float
│ │ │ ├ 2o10c2g. Current Value : float
│ │ │ └ 2o10c2h. Const Value : float
│ │ ├ 2o11. Turbo Controllers [x] : object
│ │ │ ├ 2o11a. Name : string
│ │ │ └ 2o11b. Stages [x] : object
│ │ │ ├ 2o11b1. Input Var : enum
│ │ │ ├ 2o11b2. Combinator Mode : enum
```

```
│ │ │ ├ 2o11b3. Lut : string - path
│ │ │ ├ 2o11b4. Filter Gain : float
│ │ │ ├ 2o11b5. Up Limit : float
│ │ │ ├ 2o11b6. Down Limit : float
│ │ │ ├ 2o11b7. Current Value : float
│ │ │ └ 2o11b8. Const Value : float
│ │ └ 2o12. Turbo Settings : object
│ │ └ 2o12a. Boost Lv : float
└ 3. Car Part Type : enum
```

#### **Enum - Car Tuning Pars**

| 1     | Physics Tuning  | <none>, Engine Tune, Engine, Gearbox, Drivetrain, Clutch,<br/>Brakes, Brake System, Electronics, Suspensions, Suspensions<br/>Geometry, Wing, Aero Package, Setup, Setup Limits,<br/>Performance Modes Tuning</none>                                                                                                                                                                                                                                   |
|-------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2n3h1 | Combinator Mode | UndefinedMode, AddH, MultH, AddYawGain, MultYawGain,<br>AddClGain, MultClGain                                                                                                                                                                                                                                                                                                                                                                          |
| 2n3h2 | Input           | UndefinedInput, Brake, Gas, Yaw, LatG, LonG, Steer, Speed,<br>SusTravelLR, SusTravelRR                                                                                                                                                                                                                                                                                                                                                                 |
| 2o5a  | Type            | LSD, Spool, Torsen, EpicyclicTorsen, EpicyclicLSD,<br>TorqueVectoring                                                                                                                                                                                                                                                                                                                                                                                  |
| 2o7b1 | Input Var       | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear,<br>SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX,<br>SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG,<br>SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor,<br>RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG,<br>LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR,<br>SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight,<br>ErsChargeLevel, ErsCoastTorque |
| 2o7b2 | Combinator Mode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                                               |

| 3 | Car Part Type | <none>, Exterior_Body, Exterior_FrontBumper,</none>                        |
|---|---------------|----------------------------------------------------------------------------|
|   |               | Exterior_FrontBumperLip, Exterior_FrontFogLights,                          |
|   |               | Exterior_FrontBumberCanards, Exterior_FrontLights,                         |
|   |               | Exterior_RearLights, Exterior_RearFogLights,                               |
|   |               | Exterior_AuxLights, Exterior_FrontAirIntakeGrid,                           |
|   |               | Exterior_FrontWindshield, Exterior_Hood,                                   |
|   |               | Exterior_HoodAirscopes, Exterior_SlideFrontBody,                           |
|   |               | Exterior_SlideMirrors, Exterior_LeftDoor, Exterior_RightDoor,              |
|   |               | Exterior_Skirts, Exterior_SlideRearBody, Exterior_RearDi<br>ffuser,        |
|   |               | Exterior_RearTailgateSpoiler, Exterior_RearSpoiler,                        |
|   |               | Exterior_RoofAirScopes, Exterior_RearWindshield,                           |
|   |               | Exterior_RimFL, Exterior_RimFR, Exterior_RimRL,                            |
|   |               | Exterior_RimRR, Exterior_RimBlurFL, Exterior_RimBlurFR,                    |
|   |               | Exterior_RimBlurRL, Exterior_RimBlurRR, Exterior_TyreFL,                   |
|   |               | Exterior_TyreFR, Exterior_TyreRL, Exterior_TyreRR,                         |
|   |               | Exterior_CaliperFL, Exterior_CaliperFR, Exterior_CaliperRL,                |
|   |               | Exterior_CaliperRR, Exterior_DiscFL, Exterior_DiscFR,                      |
|   |               | Exterior_DiscRL, Exterior_DiscRR, Exterior_PlateFront,                     |
|   |               | Exterior_PlateRear, Exterior_Exhaust, Exterior_Lumirank,                   |
|   |               | Exterior_FrontSplitter, Exterior_FuelCap, Exterior_Decal,                  |
|   |               | Exterior_Storage, Exterior_Top, Interior_Body,                             |
|   |               | Interior_FrontSeats, Interior_RearSeats,                                   |
|   |               | Interior_FireExtinguisher, Interior_SteeringWheelAndHub,                   |
|   |               | Interior_MirrorGadget, Interior_FloorCarpets,                              |
|   |               | Interior_HandbrakeLever, Interior_GearShifterLever,                        |
|   |               | Interior_RollbarOrCage, Interior_CameraDevice,                             |
|   |               | Interior_CockpitLights, Interior_AnalogDashboard,                          |
|   |               | Interior_DigitalDashboard, Interior_SeatbeltOn,                            |
|   |               | Interior_SeatbeltO<br>ff, Interior_HarnessOn, Interior_HarnessO<br>ff<br>, |
|   |               | Interior_SafetyNetOn, Interior_SafetyNetO<br>ff<br>,                       |
|   |               | Interior_PedalAccelerator, Interior_PedalBrake,                            |
|   |               | Interior_PedalClutch, Interior_Storage, Interior_CupHolder,                |
|   |               | Mechanics_SuspensionGeometry_Front,                                        |
|   |               | Mechanics_SuspensionGeometry_Rear,                                         |
|   |               | Mechanics_SuspensionCoilover_Front,                                        |
|   |               | Mechanics_SuspensionCoilover_Rear, Mechanics_Engine,                       |
|   |               | Mechanics_Turbo, Mehanics_Ecu, Mechanics_Pistons,                          |
|   |               | Mechanics_Rod, Mechanics_Cam_Shaft,                                        |
|   |               | Mechanics_Crank_Shaft, Mechanics_Head,                                     |
|   |               | Mechanics_Injection_System, Mechanics_Radiator,                            |
|   |               | Mechanics_Oil_Radiator, Mechanics_Intercooler,                             |
|   |               | Mechanics_Air_Filter, Mechanics_Intake_Manifold,                           |
|   |               | Mechanics_Exhaust_Manifold, Mechanics_Catalitic_Converter,                 |
|   |               | Mechanics_Center_Pipe, Mechanics_Mu<br>ffler,                              |
|   |               | Mechanics_Di<br>fferential, Mechanics_Clutch,                              |
|   |               | Mechanics_Gearbox, Mechanics_Electronics,                                  |
|   |               | Mechanics_Drivetrain, Mechanics_Aero_0, Mechanics_Aero_1,                  |
|   |               |                                                                            |
|   |               | Mechanics_Aero_2, Mechanics_Aero_3, Mechanics_Aero_4,                      |
|   |               | Mechanics_Aero_5, Mechanics_Aero_6, Mechanics_Aero_7,                      |
|   |               | Mechanics_Aero_8, Mechanics_Aero_9,                                        |
|   |               | Mechanics_Downforce_0, Mechanics_Downforce_1,                              |
|   |               | Mechanics_Downforce_2, Mechanics_Downforce_3,                              |
|   |               | Mechanics_PadsFL, Mechanics_PadsFR, Mechanics_PadsRL,                      |
|   |               | Mechanics_PadsRR, Mechanics_CaliperFL,                                     |
|   |               | Mechanics_CaliperFR, Mechanics_CaliperRL,                                  |
|   |               | Mechanics_CaliperRR, Mechanics_DiscFL,                                     |
|   |               | Mechanics_DiscFR, Mechanics_DiscRL, Mechanics_DiscRR                       |

#### <span id="page-150-0"></span>C. Example data

#### <span id="page-150-1"></span>**Chosen Cars for Example**

- Toyota Supra MK IV (slug; ks toyota supra mkiy) [7 tuning parts]
- Datsun 240z Fairlady ( slug : ks datsun 240z fairlady ) [ 8 tuning parts ]
- Porsche 992 GT3 Cup (slug : ks. porsche 992 gt3 cup) [4 tuning parts]

#### <span id="page-150-2"></span>II. Example

#### <span id="page-150-3"></span>Tovota Supra MK IV

1. Drift Front Geometry (file:

ks\_toyota\_supra\_geometry\_front\_drift\_geometry.tuningpart)

- 1. Physics Tuning : Suspensions Geometry
- 2. Suspensions Geometry
- | 2a. Geometry Path Front:

content\cars\ks toyota supra mkiv\data\ks toyota supra mkiv front drift. suspension

L 2b. Geometry Path Rear:

content\cars\ks toyota supra mkiv\data\ks toyota supra mkiv rear suspens ion

- L 3. Car Part Type: Mechanics SuspensionGeometry Front
- 2. Drift Drivetrain (file: ks toyota supra mkiv drivetrain drift.tuningpart)
- ├ 1. Physics Tuning : Drivetrain
- 2. Drivetrain
- L 2a. Path:

content\cars\ks toyota supra mkiv\data\ks toyota supra mkiv drift.drivet

- L 3. Car Part Type : Mechanics\_Drivetrain
- 3. Drift Engine (file: ks toyota supra mkiv engine drift.tuningpart)
- 1. Physics Tuning : Engine
  - 2. Engine
- <sup>L</sup> 2a. Path :

content\cars\ks toyota supra mkiv\data\ks toyota supra mkiv drift.careng

- L 3. Car Part Type : Mechanics\_Engine
- 4. Drift Front Suspension (file: ks toyota supra mkiv front susp drift.tuningpart)
- 1. Physics Tuning : Suspensions
  - 2. Suspensions
- | 2a. Coilover Path Front :

content\cars\ks toyota supra mkiv\data\ks toyota supra mkiv front.coilov er

```
│ └ 2b. Coilover Path Rear : 
content\cars\ks_toyota_supra_mkiv\data\ks_toyota_supra_mkiv_rear.coilove
r 
└ 1c. Car Part Type : Mechanics_SuspensionCoilover_Front 
5. Drift Gearbox ( file : ks_toyota_supra_mkiv_gearbox_drift.tuningpart ) 
├ 1. Physics Tuning : Gearbox 
├ 2. Gearbox 
│ └ 2a. Path : 
content\cars\ks_toyota_supra_mkiv\data\ks_toyota_supra_mkiv_drift.gearbo
x 
└ 3. Car Part Type : Mechanics_Gearbox 
6. Drift Setup ( file : ks_toyota_supra_mkiv_setup_drift.tuningpart ) 
├ 1. Physics Tuning : Setup 
├ 2. Setup 
│ └ 2a. Path : 
content\cars\ks_toyota_supra_mkiv\data\setup\supra_drift.carsetup 
└ 3. Car Part Type : None 
7. Drift Setup Limits ( file : ks_toyota_supra_mkiv_setuplimits_drift.tuningpart ) 
├ 1. Physics Tuning : Setup Limits 
├ 2. Setup Limits 
│ └ 2a. Path : 
content\cars\ks_toyota_supra_mkiv\data\setup\supra_mk_iv_limits_drift.ca
rsetuplimits 
└ 3. Car Part Type : None 
                             Datsun 240z Fairlady 
1. 5 Speed Gearbox ( file : ks_datsun_240z_fairlady_5speed.tuningpart ) 
├ 1. Physics Tuning : Gearbox 
├ 2. Gearbox 
│ ├ 2a. Path : 
content\cars\ks_datsun_240z_fairlady\data\tuning\ks_datsun_240z_fairlady
_5speed.gearbox 
└ 3. Car Part Type : Mechanics_Gearbox 
2. Brake ( file : ks_datsun_240z_fairlady_brake.tuningpart ) 
├ 1. Physics Tuning : Brake System 
├ 2. Gearbox 
│ └ 2a. Path : 
content\cars\ks_datsun_240z_fairlady\data\tuning\ks_datsun_240z_fairlady
_brakes.brakesystem 
└ 3. Car Part Type : Mechanics_CaliperFL 
3. 5 Speed Clutch ( file : ks_datsun_240z_fairlady_clutch_5speed.tuningpart )
```

```
├ 1. Physics Tuning : Clutch 
├ 2. Clutch 
│ └ 2a. Path : 
content\cars\ks_datsun_240z_fairlady\data\tuning\ks_datsun_240z_fairlady
_clutch_5speed.clutch 
└ 3. Car Part Type : Mechanics_Clutch 
4. G Nose Coilovers ( file : ks_datsun_240z_fairlady_g_nose_coilovers.tuningpart ) 
├ 1. Physics Tuning : Suspensions 
├ 2. Suspensions 
│ ├ 2a. Coilover Path Front : 
content\cars\ks_datsun_240z_fairlady\data\tuning\ks_datsun_240z_fairlady
_g_nose_front.coilover
│ └ 2b. Coilover Path Rear : 
content\cars\ks_datsun_240z_fairlady\data\tuning\ks_datsun_240z_fairlady
_g_nose_rear.coilover 
└ 3. Car Part Type : Mechanics_SuspensionCoilover_Front 
5. Setup ( file : ks_datsun_240z_fairlady_g_nose_setup.tuningpart ) 
├ 1. Physics Tuning : Setup 
├ 2. Setup 
│ └ 2a. Path : 
content\cars\ks_datsun_240z_fairlady\data\setup\ks_datsun_240z_fairlady_
g_nose.carsetup 
└ 3. Car Part Type : None 
6. Setup Limits ( file : ks_datsun_240z_fairlady_g_nose_setuplimits.tuningpart ) 
├ 1. Physics Tuning : Setup Limits 
├ 2. Setup Limits 
│ └ 2a. Path : 
content\cars\ks_datsun_240z_fairlady\data\setup\ks_datsun_240z_fairlady_
g_nose.carsetuplimits 
└ 3. Car Part Type : None 
7. L28 Engine ( file : ks_datsun_240z_fairlady_l28engine.tuningpart ) 
├ 1. Physics Tuning : Engine 
├ 2. Engine 
│ └ 2a. Path : 
content\cars\ks_datsun_240z_fairlady\data\tuning\ks_datsun_240z_fairlady
_L28engine.carengine 
└ 3. Car Part Type : Mechanics_Engine 
8. Limited-Slip Differential ( file : ks_datsun_240z_fairlady_lsd.tuningpart ) 
├ 1. Physics Tuning : Drivetrain 
├ 2. Drivetrain 
│ ├ 2a. Path : 
content\cars\ks_datsun_240z_fairlady\data\tuning\ks_datsun_240z_fairlady
_LSD.drivetrain 
└ 3. Car Part Type : Mechanics_Drivetrain
```

# <span id="page-153-0"></span>**Porsche 992 GT3 Cup**

*1. No ABS No TC ( file : 992\_gt3\_no\_abs\_no\_tc.tuningpart )* 

├ 1. Physics Tuning : <None> └ 2. Car Part Type : Mechanics\_Electronics *2. No ABS No TC Setup Limits ( file : 992\_gt3\_no\_abs\_no\_tc\_setuplimits.tuningpart )*  ├ 1. Physics Tuning : Setup Limits ├ 2. Setup Limits │ └ 2a. Path : content\cars\ks\_porsche\_992\_gt3\_cup\data\Setup\limitsporsche992cup\_no\_ab s\_no\_tc.carsetuplimits └ 3. Car Part Type : None *3. Only ABS ( file : 992\_gt3\_only\_abs.tuningpart )*  ├ 1. Physics Tuning : <None> └ 2. Car Part Type : Mechanics\_Electronics *4. Only ABS Setup Limits ( file : 992\_gt3\_only\_abs\_setuplimits.tuningpart )*  ├ 1. Physics Tuning : Setup Limits ├ 2. Setup Limits │ └ 2a. Path : content\cars\ks\_porsche\_992\_gt3\_cup\data\Setup\limitsporsche992cup\_only\_ abs.carsetuplimits └ 3. Car Part Type : None

# <span id="page-154-0"></span>**9. Car Electronics [ .carelectronics ]**

# <span id="page-154-1"></span>**A. Description**

### <span id="page-154-2"></span>**I. General Description**

The **Car Electronics** asset serves as the central processing unit for all algorithmic driver aids, active chassis controls, and safety sub-systems within the vehicle. While other files handle pure mechanical reactions (such as steel twisting or hydraulics compressing), this asset defines the software layer that intercepts driver inputs and wheel telemetry in real time.

It processes raw kinematic metrics—such as wheel speed deltas, steering wheel rotation, and longitudinal/lateral slip ratios—and calculates targeted mitigation interventions. This file maps the operational behavior of high-level motorsports electronic suites, most notably **ABS (Anti-lock Braking System)** and **TC (Traction Control)**.

# <span id="page-154-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The variables configured within the Car Electronics asset dictate how aggressively the car's digital systems manage performance and stability thresholds:

- **• Traction Optimization (Corner Exit Propulsion):** Traction Control systems actively monitor drive-wheel spin. When the slip exceeds predefined thresholds, the system limits engine torque output to preserve lateral stability and maximize forward bite without spinning the car.
- **• Braking Deceleration Stability:** The ABS module continuously samples wheel lockup parameters during heavy braking. By dynamically modulating hydraulic line pressure, it prevents tires from skidding, preserving steering authority and optimal braking distances.
- **• Transient Phase Control and Safety Windows:** It maps out the exact operating window between a skilled driver sliding the car for lap time versus a catastrophic loss of control, acting as a electronic safety net customized across various preset dashboard maps

#### <span id="page-154-4"></span>**III. Key Architecture & Data Fields Explained**

The internal framework of a Car Electronics file is highly structured around multi-stage **Settings Matrices** (e.g., Maps 1 through 12) to allow drivers to toggle intervention intensity on the fly from the cockpit.

#### <span id="page-154-5"></span>**1 - TRACTION CONTROL (TC) LOGIC MATRIX**

For each step or map preset, the system evaluates the following core parameters:

**• Min Slip Ratio / Max Slip Ratio:** Defines the target allowable longitudinal tire slippage window (e.g., 0.04 to 0.06). Slippage below the minimum is ignored; slippage exceeding the maximum triggers full system suppression.

- **• Ref Slip Angle (Degrees):** Establishes the baseline lateral slide tolerance. This prevents the system from prematurely cutting power during controlled, high-load cornering yaw angles.
- **• Cut Level:** Dictates the severity of engine torque reduction when wheelspin occurs, utilizing ignition cuts, fuel cuts, or electronic throttle body modulation to choke power.
- **• Max Torque Variation:** Governs the dampening and smoothing factor of the engine power re-engagement, preventing harsh shockwaves from upsetting the chassis as grip is recovered.

# <span id="page-155-0"></span>**2 - ANTI-LOCK BRAKING SYSTEM (ABS) MAP SETTINGS**

- **• Target Slip Sliders:** Defines how much a tire is allowed to slip relative to vehicle ground speed under heavy braking before the ABS hydraulic valves cycle open to release line pressure.
- **• Frequency and Response Cycles:** Sets the operational speed (measured in Hz) at which the digital controller samples data and updates valve adjustments, determining how smooth or violent the pedal feedback pulses.

#### <span id="page-155-1"></span>**IV. Interpretation of Tuning Part Strategies**

By examining the .carelectronics maps, developers can identify the exact racing category and setup complexity built into the vehicle:

- **• The Multi-Map Pro-Motorsport Profile (e.g., GT3 / GT4):** Features an expansive matrix spanning up to 10 or 12 selectable map configurations. Lower-numbered maps (e.g., Setting 1 or 2) feature loose slip parameters and subtle cut levels optimized for professional drivers on fresh slick tyres. Higher-numbered maps dramatically narrow the allowed slip ratios and maximize cut levels, configured specifically to stabilize the vehicle on worn tyres or during heavy rain.
- **• The Simplified Production / Historic Profile:** Often completely empty, hard-locked to a single rigid mapping with non-adjustable entries, or disabled entirely via modular tuning parts. This accurately reflects vehicles running vintage mechanical setups or baseline road cars with binary, non-adjustable factory safety systems.

#### <span id="page-155-2"></span>**B. Schema**

```
├ 1. T C : object 
│ ├ 1a. Has T C2 : boolean
│ ├ 1b. Frequency Hz : float
│ ├ 1c. Min Speed Kmh : float
│ ├ 1d. Gear Change Time : float
│ ├ 1e. Min Cut Level : float
│ ├ 1f. Max Cut Level : float
│ ├ 1g. Settings [x] : object | can have multiple Settings
│ │ ├ 1g1. Min Slip Ratio : float
│ │ ├ 1g2. Max Slip Ratio : float
│ │ ├ 1g3. Ref Slip Angle Deg : float
│ │ ├ 1g4. Engine Cut Level : float
│ │ ├ 1g5. Angular A C Cgain : float
```

```
- 1g6. Oversteer Gain : float
1g7. Slip Angle Activation Deg : float
2. A B S : object
- 2a. Settings [x] : object | can have multiple Settings
  - 2a1. Min Slip Ratio : float
   - 2a2. Max Slip Ratio : float
  - 2a3. Ref Slip Angledeg : float
   - 2a4. Cut Level : float
  2a5. Max Torque Variation : float
 2b. Frequency: float
 2c. Channels: integer
L 2d. Min Speed Kmh : float
3. E D L : object
- 3a. Active : boolean
 - 3b. Braketorquepower : float
  3c. Braketorquecoast : float
 3d. Deadzonecoast : float
 3e. Deadzonepower: float
 3f. Maxspinpower : float
 3g. Maxspincoast : float
3h. Minspeed : float
4. E S P : object
 - 4a. Frequency Hz : float
 4b. Min Speed Kmh : float
 4c. Settings [x] : object | can have multiple Settings
  - 4c1. Gain : float
    4c2. Steer Gain: float
    4c3. Min Steer Gain : float
    4c4. Steer Gain Max Speed: float
    4c5. Oversteer Gain: float
    4c6. Understeer Gain : float
    4c7. Max Slip Ratio : float
    4c8. Dead Zone : float
    4c9. Filter Gain: float
    4c10. Brake Perc : float
    4c11. Brake Perc Activation : float
```

#### <span id="page-156-0"></span>C. Example data

#### <span id="page-156-1"></span>I. Chosen Cars for Example

- Lamborghini Huracan ST Evo 2 (slug: ks lamborghini huracan st evo2)
- Maserati MC20 GT2 (slug : ks\_maserati\_mc20\_gt2)
- Porsche 992 GT3 Cup ( slug : ks\_porsche\_992\_gt3\_cup ) [ 2 variants ]

# <span id="page-156-2"></span>II. Example

#### <span id="page-156-3"></span>Lamborghini Huracan ST Evo 2

```
- 1. T C

- 1a. Has T C2 : false

- 1b. Frequency Hz : 333.00000
```

```
│ ├ 1c. Min Speed Kmh : 40.00000 
│ ├ 1d. Gear Change Time : 0.04500 
│ ├ 1e. Min Cut Level : 1000.00000 
│ ├ 1f. Max Cut Level : 1.00000 
│ ├ 1g. Settings 1 
│ │ ├ 1g1. Min Slip Ratio : 0.00000 
│ │ ├ 1g2. Max Slip Ratio : 0.00000 
│ │ ├ 1g3. Ref Slip Angle Deg : 0.00000 
│ │ ├ 1g4. Engine Cut Level : 0.00000 
│ │ ├ 1g5. Angular A C Cgain : 0.00000 
│ │ ├ 1g6. Oversteer Gain : 0.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 100.00000 
│ ├ 1g. Settings 2 
│ │ ├ 1g1. Min Slip Ratio : 0.18000 
│ │ ├ 1g2. Max Slip Ratio : 0.45000 
│ │ ├ 1g3. Ref Slip Angle Deg : 10.00000 
│ │ ├ 1g4. Engine Cut Level : 1.50000 
│ │ ├ 1g5. Angular A C Cgain : 3.00000 
│ │ ├ 1g6. Oversteer Gain : 3.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 6.00000 
│ ├ 1g. Settings 3 
│ │ ├ 1g1. Min Slip Ratio : 0.15000 
│ │ ├ 1g2. Max Slip Ratio : 0.40000 
│ │ ├ 1g3. Ref Slip Angle Deg : 9.50000 
│ │ ├ 1g4. Engine Cut Level : 1.50000 
│ │ ├ 1g5. Angular A C Cgain : 4.00000 
│ │ ├ 1g6. Oversteer Gain : 4.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 5.25000 
│ ├ 1g. Settings 4 
│ │ ├ 1g1. Min Slip Ratio : 0.12000 
│ │ ├ 1g2. Max Slip Ratio : 0.35000 
│ │ ├ 1g3. Ref Slip Angle Deg : 9.00000 
│ │ ├ 1g4. Engine Cut Level : 1.50000 
│ │ ├ 1g5. Angular A C Cgain : 5.00000 
│ │ ├ 1g6. Oversteer Gain : 5.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 4.75000 
│ ├ 1g. Settings 5 
│ │ ├ 1g1. Min Slip Ratio : 0.10000 
│ │ ├ 1g2. Max Slip Ratio : 0.30000 
│ │ ├ 1g3. Ref Slip Angle Deg : 9.00000 
│ │ ├ 1g4. Engine Cut Level : 1.50000 
│ │ ├ 1g5. Angular A C Cgain : 6.50000 
│ │ ├ 1g6. Oversteer Gain : 6.50000 
│ │ └ 1g7. Slip Angle Activation Deg : 4.50000 
│ ├ 1g. Settings 6 
│ │ ├ 1g1. Min Slip Ratio : 0.09000 
│ │ ├ 1g2. Max Slip Ratio : 0.25000 
│ │ ├ 1g3. Ref Slip Angle Deg : 8.50000 
│ │ ├ 1g4. Engine Cut Level : 1.50000 
│ │ ├ 1g5. Angular A C Cgain : 7.50000 
│ │ ├ 1g6. Oversteer Gain : 7.50000
```

```
│ │ └ 1g7. Slip Angle Activation Deg : 4.50000 
│ ├ 1g. Settings 7 
│ │ ├ 1g1. Min Slip Ratio : 0.08000 
│ │ ├ 1g2. Max Slip Ratio : 0.25000 
│ │ ├ 1g3. Ref Slip Angle Deg : 8.00000 
│ │ ├ 1g4. Engine Cut Level : 1.25000 
│ │ ├ 1g5. Angular A C Cgain : 8.50000 
│ │ ├ 1g6. Oversteer Gain : 7.50000 
│ │ └ 1g7. Slip Angle Activation Deg : 4.50000 
│ ├ 1g. Settings 8 
│ │ ├ 1g1. Min Slip Ratio : 0.07000 
│ │ ├ 1g2. Max Slip Ratio : 0.20000 
│ │ ├ 1g3. Ref Slip Angle Deg : 8.00000 
│ │ ├ 1g4. Engine Cut Level : 1.25000 
│ │ ├ 1g5. Angular A C Cgain : 8.50000 
│ │ ├ 1g6. Oversteer Gain : 7.50000 
│ │ └ 1g7. Slip Angle Activation Deg : 4.50000 
│ ├ 1g. Settings 9 
│ │ ├ 1g1. Min Slip Ratio : 0.06000 
│ │ ├ 1g2. Max Slip Ratio : 0.20000 
│ │ ├ 1g3. Ref Slip Angle Deg : 7.50000 
│ │ ├ 1g4. Engine Cut Level : 1.25000 
│ │ ├ 1g5. Angular A C Cgain : 8.50000 
│ │ ├ 1g6. Oversteer Gain : 7.50000 
│ │ └ 1g7. Slip Angle Activation Deg : 4.00000 
│ └ 1g. Settings 10 
│ ├ 1g1. Min Slip Ratio : 0.05000 
│ ├ 1g2. Max Slip Ratio : 0.15000 
│ ├ 1g3. Ref Slip Angle Deg : 7.00000 
│ ├ 1g4. Engine Cut Level : 1.00000 
│ ├ 1g5. Angular A C Cgain : 9.00000 
│ ├ 1g6. Oversteer Gain : 7.50000 
│ └ 1g7. Slip Angle Activation Deg : 3.50000 
├ 2. A B S 
│ ├ 2a. Settings 1 
│ │ ├ 2a1. Min Slip Ratio : -1.00000 
│ │ ├ 2a2. Max Slip Ratio : -1.00000 
│ │ ├ 2a3. Ref Slip Angledeg : 0.00000 
│ │ ├ 2a4. Cut Level : 0.00000 
│ │ └ 2a5. Max Torque Variation : 0.00000 
│ ├ 2a. Settings 2 
│ │ ├ 2a1. Min Slip Ratio : 0.08000 
│ │ ├ 2a2. Max Slip Ratio : 0.12000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 3 
│ │ ├ 2a1. Min Slip Ratio : 0.07000 
│ │ ├ 2a2. Max Slip Ratio : 0.11000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.00000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 4 
│ │ ├ 2a1. Min Slip Ratio : 0.06000
```

```
│ │ ├ 2a2. Max Slip Ratio : 0.08000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 5 
│ │ ├ 2a1. Min Slip Ratio : 0.05000 
│ │ ├ 2a2. Max Slip Ratio : 0.07000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 6 
│ │ ├ 2a1. Min Slip Ratio : 0.04000 
│ │ ├ 2a2. Max Slip Ratio : 0.06000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 7 
│ │ ├ 2a1. Min Slip Ratio : 0.03200 
│ │ ├ 2a2. Max Slip Ratio : 0.07500 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 8 
│ │ ├ 2a1. Min Slip Ratio : 0.03000 
│ │ ├ 2a2. Max Slip Ratio : 0.07000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 9 
│ │ ├ 2a1. Min Slip Ratio : 0.03000 
│ │ ├ 2a2. Max Slip Ratio : 0.07000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 10 
│ │ ├ 2a1. Min Slip Ratio : 0.02900 
│ │ ├ 2a2. Max Slip Ratio : 0.06500 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 11 
│ │ ├ 2a1. Min Slip Ratio : 0.02900 
│ │ ├ 2a2. Max Slip Ratio : 0.06500 
│ │ ├ 2a3. Ref Slip Angledeg : 4.50000 
│ │ ├ 2a4. Cut Level : 0.10000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 12 
│ │ ├ 2a1. Min Slip Ratio : 0.03000 
│ │ ├ 2a2. Max Slip Ratio : 0.06500 
│ │ ├ 2a3. Ref Slip Angledeg : 4.25000 
│ │ ├ 2a4. Cut Level : 0.00000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2b. Frequency : 200.00000 
│ ├ 2c. Channels : 4
```

```
│ └ 2d. Min Speed Kmh : 20.00000 
├ 3. E D L : None 
├ 4. E S P 
│ ├ 4a. Frequency Hz : 0.00000 
└ └ 4b. Min Speed Kmh : 0.0
```

### <span id="page-160-0"></span>**Maserati MC20 GT2**

```
├ 1. T C 
│ ├ 1a. Has T C2 : false 
│ ├ 1b. Frequency Hz : 333.00000 
│ ├ 1c. Min Speed Kmh : 40.00000 
│ ├ 1d. Gear Change Time : 0.02500 
│ ├ 1e. Min Cut Level : 1.50000 
│ ├ 1f. Max Cut Level : 0.10000 
│ ├ 1g. Settings 1 
│ │ ├ 1g1. Min Slip Ratio : 0.00000 
│ │ ├ 1g2. Max Slip Ratio : 0.00000 
│ │ ├ 1g3. Ref Slip Angle Deg : 0.00000 
│ │ ├ 1g4. Engine Cut Level : 0.00000 
│ │ ├ 1g5. Angular A C Cgain : 0.20000 
│ │ ├ 1g6. Oversteer Gain : 0.50000 
│ │ └ 1g7. Slip Angle Activation Deg : 0.20000 
│ ├ 1g. Settings 2 
│ │ ├ 1g1. Min Slip Ratio : 0.25000 
│ │ ├ 1g2. Max Slip Ratio : 0.50000 
│ │ ├ 1g3. Ref Slip Angle Deg : 18.00000 
│ │ ├ 1g4. Engine Cut Level : 1.50000 
│ │ ├ 1g5. Angular A C Cgain : 2.00000 
│ │ ├ 1g6. Oversteer Gain : 2.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 4.00000 
│ ├ 1g. Settings 3 
│ │ ├ 1g1. Min Slip Ratio : 0.23000 
│ │ ├ 1g2. Max Slip Ratio : 0.31000 
│ │ ├ 1g3. Ref Slip Angle Deg : 14.80000 
│ │ ├ 1g4. Engine Cut Level : 1.25000 
│ │ ├ 1g5. Angular A C Cgain : 3.50000 
│ │ ├ 1g6. Oversteer Gain : 4.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 3.50000 
│ ├ 1g. Settings 4 
│ │ ├ 1g1. Min Slip Ratio : 0.20000 
│ │ ├ 1g2. Max Slip Ratio : 0.30000 
│ │ ├ 1g3. Ref Slip Angle Deg : 13.00000 
│ │ ├ 1g4. Engine Cut Level : 1.10000 
│ │ ├ 1g5. Angular A C Cgain : 5.00000 
│ │ ├ 1g6. Oversteer Gain : 6.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 3.00000 
│ ├ 1g. Settings 5 
│ │ ├ 1g1. Min Slip Ratio : 0.18000 
│ │ ├ 1g2. Max Slip Ratio : 0.30000 
│ │ ├ 1g3. Ref Slip Angle Deg : 11.00000 
│ │ ├ 1g4. Engine Cut Level : 0.95000 
│ │ ├ 1g5. Angular A C Cgain : 4.00000 
│ │ ├ 1g6. Oversteer Gain : 10.00000
```

```
│ │ └ 1g7. Slip Angle Activation Deg : 2.50000 
│ ├ 1g. Settings 6 
│ │ ├ 1g1. Min Slip Ratio : 0.17000 
│ │ ├ 1g2. Max Slip Ratio : 0.28000 
│ │ ├ 1g3. Ref Slip Angle Deg : 9.00000 
│ │ ├ 1g4. Engine Cut Level : 0.80000 
│ │ ├ 1g5. Angular A C Cgain : 13.00000 
│ │ ├ 1g6. Oversteer Gain : 11.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 2.25000 
│ ├ 1g. Settings 7 
│ │ ├ 1g1. Min Slip Ratio : 0.15000 
│ │ ├ 1g2. Max Slip Ratio : 0.24000 
│ │ ├ 1g3. Ref Slip Angle Deg : 8.90000 
│ │ ├ 1g4. Engine Cut Level : 0.65000 
│ │ ├ 1g5. Angular A C Cgain : 20.00000 
│ │ ├ 1g6. Oversteer Gain : 14.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 2.00000 
│ ├ 1g. Settings 8 
│ │ ├ 1g1. Min Slip Ratio : 0.15000 
│ │ ├ 1g2. Max Slip Ratio : 0.24000 
│ │ ├ 1g3. Ref Slip Angle Deg : 8.90000 
│ │ ├ 1g4. Engine Cut Level : 0.65000 
│ │ ├ 1g5. Angular A C Cgain : 20.00000 
│ │ ├ 1g6. Oversteer Gain : 14.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 1.80000 
│ ├ 1g. Settings 9 
│ │ ├ 1g1. Min Slip Ratio : 0.12000 
│ │ ├ 1g2. Max Slip Ratio : 0.25000 
│ │ ├ 1g3. Ref Slip Angle Deg : 8.90000 
│ │ ├ 1g4. Engine Cut Level : 0.65000 
│ │ ├ 1g5. Angular A C Cgain : 20.00000 
│ │ ├ 1g6. Oversteer Gain : 14.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 1.80000 
│ ├ 1g. Settings 10 
│ │ ├ 1g1. Min Slip Ratio : 0.10000 
│ │ ├ 1g2. Max Slip Ratio : 0.24000 
│ │ ├ 1g3. Ref Slip Angle Deg : 8.90000 
│ │ ├ 1g4. Engine Cut Level : 0.65000 
│ │ ├ 1g5. Angular A C Cgain : 20.00000 
│ │ ├ 1g6. Oversteer Gain : 14.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 1.70000 
│ ├ 1g. Settings 11 
│ │ ├ 1g1. Min Slip Ratio : 0.08000 
│ │ ├ 1g2. Max Slip Ratio : 0.18000 
│ │ ├ 1g3. Ref Slip Angle Deg : 8.00000 
│ │ ├ 1g4. Engine Cut Level : 0.10000 
│ │ ├ 1g5. Angular A C Cgain : 0.00000 
│ │ ├ 1g6. Oversteer Gain : 1.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 1.60000 
│ ├ 1g. Settings 12 
│ │ ├ 1g1. Min Slip Ratio : 0.08000 
│ │ ├ 1g2. Max Slip Ratio : 0.18000 
│ │ ├ 1g3. Ref Slip Angle Deg : 7.00000 
│ │ ├ 1g4. Engine Cut Level : 0.10000
```

```
│ │ ├ 1g5. Angular A C Cgain : 0.00000 
│ │ ├ 1g6. Oversteer Gain : 1.00000 
│ │ └ 1g7. Slip Angle Activation Deg : 1.60000 
│ └ 1g. Settings 13 
│ ├ 1g1. Min Slip Ratio : 0.06000 
│ ├ 1g2. Max Slip Ratio : 0.18000 
│ ├ 1g3. Ref Slip Angle Deg : 5.00000 
│ ├ 1g4. Engine Cut Level : 0.10000 
│ ├ 1g5. Angular A C Cgain : 0.00000 
│ ├ 1g6. Oversteer Gain : 1.00000 
│ └ 1g7. Slip Angle Activation Deg : 1.50000 
├ 2. A B S 
│ ├ 2a. Settings 1 
│ │ ├ 2a1. Min Slip Ratio : -1.00000 
│ │ ├ 2a2. Max Slip Ratio : -1.00000 
│ │ ├ 2a3. Ref Slip Angledeg : 0.00000 
│ │ ├ 2a4. Cut Level : 0.00000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 2 
│ │ ├ 2a1. Min Slip Ratio : 0.02000 
│ │ ├ 2a2. Max Slip Ratio : 0.30000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.60000 
│ ├ 2a. Settings 3 
│ │ ├ 2a1. Min Slip Ratio : 0.03800 
│ │ ├ 2a2. Max Slip Ratio : 0.09000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.80000 
│ ├ 2a. Settings 4 
│ │ ├ 2a1. Min Slip Ratio : 0.03300 
│ │ ├ 2a2. Max Slip Ratio : 0.08400 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.80000 
│ ├ 2a. Settings 5 
│ │ ├ 2a1. Min Slip Ratio : 0.03100 
│ │ ├ 2a2. Max Slip Ratio : 0.08200 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.80000 
│ ├ 2a. Settings 6 
│ │ ├ 2a1. Min Slip Ratio : 0.03000 
│ │ ├ 2a2. Max Slip Ratio : 0.07900 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.80000 
│ ├ 2a. Settings 7 
│ │ ├ 2a1. Min Slip Ratio : 0.02000 
│ │ ├ 2a2. Max Slip Ratio : 0.07500 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.80000
```

```
│ ├ 2a. Settings 8 
│ │ ├ 2a1. Min Slip Ratio : 0.04000 
│ │ ├ 2a2. Max Slip Ratio : 0.07000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 9 
│ │ ├ 2a1. Min Slip Ratio : 0.03700 
│ │ ├ 2a2. Max Slip Ratio : 0.07000 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 10 
│ │ ├ 2a1. Min Slip Ratio : 0.03000 
│ │ ├ 2a2. Max Slip Ratio : 0.06500 
│ │ ├ 2a3. Ref Slip Angledeg : 5.00000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 11 
│ │ ├ 2a1. Min Slip Ratio : 0.03000 
│ │ ├ 2a2. Max Slip Ratio : 0.06500 
│ │ ├ 2a3. Ref Slip Angledeg : 4.50000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2a. Settings 12 
│ │ ├ 2a1. Min Slip Ratio : 0.03000 
│ │ ├ 2a2. Max Slip Ratio : 0.06500 
│ │ ├ 2a3. Ref Slip Angledeg : 4.50000 
│ │ ├ 2a4. Cut Level : 0.15000 
│ │ └ 2a5. Max Torque Variation : 0.70000 
│ ├ 2b. Frequency : 200.00000 
│ ├ 2c. Channels : 4 
│ └ 2d. Min Speed Kmh : 20.00000 
├ 3. E D L : None 
├ 4. E S P 
│ ├ 4a. Frequency Hz : 0.00000 
│ ├ 4b. Min Speed Kmh : 0.00000 
└ └ 4c. Settings : None
```

#### <span id="page-163-0"></span>**Porsche 992 GT3 Cup**

*1. No ABS No TC ( file : 992\_gt3\_no\_abs\_no\_tc.carelectronics )* 

```
├ 1. T C : None 
├ 2. A B S : None 
├ 3. E D L : None 
├ 4. E S P 
│ ├ 4a. Frequency Hz : 0.00000 
│ ├ 4b. Min Speed Kmh : 0.00000 
└ └ 4c. Settings : None
```

*2. Only ABS ( file : 992\_gt3\_only\_abs.carelectronics )* 

```
├ 1. T C : None
```

```
├ 2. A B S 
│ ├ 2a. Settings 1 
│ │ ├ 2a1. Min Slip Ratio : -1.00000│ │ ├ 2a2. Max Slip Ratio : -1.00000 
│ │ ├ 2a3. Ref Slip Angledeg : 0.00000 
│ │ ├ 2a4. Cut Level : 0.00000 
│ │ └ 2a5. Max Torque Variation : 0.00000 
│ ├ 2a. Settings 2 
│ │ ├ 2a1. Min Slip Ratio : 0.12000 
│ │ ├ 2a2. Max Slip Ratio : 0.14000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 3 
│ │ ├ 2a1. Min Slip Ratio : 0.11000 
│ │ ├ 2a2. Max Slip Ratio : 0.14000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 4 
│ │ ├ 2a1. Min Slip Ratio : 0.10000 
│ │ ├ 2a2. Max Slip Ratio : 0.12000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 5 
│ │ ├ 2a1. Min Slip Ratio : 0.08000 
│ │ ├ 2a2. Max Slip Ratio : 0.10000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.02000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 6 
│ │ ├ 2a1. Min Slip Ratio : 0.07000 
│ │ ├ 2a2. Max Slip Ratio : 0.08000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 7 
│ │ ├ 2a1. Min Slip Ratio : 0.06000 
│ │ ├ 2a2. Max Slip Ratio : 0.08000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 8 
│ │ ├ 2a1. Min Slip Ratio : 0.05000 
│ │ ├ 2a2. Max Slip Ratio : 0.07000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 9 
│ │ ├ 2a1. Min Slip Ratio : 0.05000 
│ │ ├ 2a2. Max Slip Ratio : 0.06000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 10 
│ │ ├ 2a1. Min Slip Ratio : 0.04000
```

```
│ │ ├ 2a2. Max Slip Ratio : 0.05000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 11 
│ │ ├ 2a1. Min Slip Ratio : 0.02500 
│ │ ├ 2a2. Max Slip Ratio : 0.03500 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2a. Settings 12 
│ │ ├ 2a1. Min Slip Ratio : 0.01000 
│ │ ├ 2a2. Max Slip Ratio : 0.02000 
│ │ ├ 2a3. Ref Slip Angledeg : 7.00000 
│ │ ├ 2a4. Cut Level : 0.20000 
│ │ └ 2a5. Max Torque Variation : 1.00000 
│ ├ 2b. Frequency : 200.00000 
│ ├ 2c. Channels : 4 
│ └ 2d. Min Speed Kmh : 20.00000 
├ 3. E D L : None 
├ 4. E S P 
│ ├ 4a. Frequency Hz : 0.00000 
│ ├ 4b. Min Speed Kmh : 0.00000 
└ └ 4c. Settings : None
```

# <span id="page-166-0"></span>**10. Clutch [ .clutch ]**

# <span id="page-166-1"></span>**A. Description**

### <span id="page-166-2"></span>**I. General Description**

The **Clutchs** asset defines the mechanical and operational physics of the vehicle's decoupling mechanism between the engine's crankshaft and the transmission input shaft. It acts as the primary thermal, friction, and kinetic bridge during gear synchronization and stationary launches.

This asset governs how engine torque is progressively transferred to the drivetrain, defining both the physical properties of the clutch assembly (such as mass and maximum holding capacity) and the automated behaviors or electronic overrides that assist with shifting and stall prevention.

### <span id="page-166-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The parameters configured within the Clutchs asset have a direct and critical impact on the vehicle's powertrain response and drivability:

- **• Torque Transfer Efficiency:** It dictates the maximum power threshold the transmission can receive before slipping. If engine modifications increase torque beyond the clutch's mechanical limit, the asset causes the plates to slip, wasting power and slowing acceleration.
- **• Shift Performance & Transition Smoothness:** During shifting phases, this asset regulates the speed and characteristics of the clamp engagement. It determines whether a gear change creates a sharp kinetic shockwave that can break rear-wheel traction (shift-lock) or slurs smoothly through a progressive friction zone.
- **• Launch Control and Standing Starts:** It defines the bite-point characteristics. The structural settings determine how effectively a vehicle can launch from a dead stop without bogging down the engine RPM or inducing uncontrollable wheelspin.
- **• Driver Assistance and Accessibility:** Through its automated profile parameters, it controls the electronic logic that bridges the gap between raw manual three-pedal mechanics and automated, paddle-activated, or software-assisted shifting maneuvers.

#### <span id="page-166-4"></span>**III. Key Architecture & Data Fields Explained**

The internal structure of the Clutchs asset isolates core physical constants from algorithmic shift profiles.

#### <span id="page-166-5"></span>**1 - BASE MECHANICAL & INTERTIAL PARAMETERS**

**• Clutch Inertia:** The rotational mass moment of inertia of the clutch pressure plates and disc assembly. Lower inertia allows the engine to rev up and drop RPMs faster when decoupled, while higher inertia stores kinetic energy, easing standing starts on road cars.

- **• Clutch Max Torque:** The maximum torque holding threshold (measured in Nm) that the friction plates can withstand when fully clamped. This acts as a physical fuse in the powertrain mesh.
- **• Clutch Curve:** A look-up table or reference curve mapping the clamping force and friction coefficient relative to pedal travel or electronic actuator engagement, determining the progressive nature of the bite point.

#### <span id="page-167-0"></span>**2 - AUTOCLUTCH PROFILE PARAMETERS**

When physical assistances or automated transmissions are active, the system routes logic through specific profile fields:

- **• Upshift Profile / Down Shift Profile:** Explicit file paths pointing to external curve blueprints (.curve). These specify the exact engagement/disengagement timing, speed, and dampening curves applied to the clutch actuator during gear changes.
- **• Forced On:** A boolean flag (true/false). When forced on, the simulation completely automates clutch operation, rendering a manual physical clutch pedal or binding obsolete.
- **• Min Rpms / Max Rpms:** Defines the operational threshold window for automated anti-stall and launch logic. If engine speed drops below the minimum RPM, the automated actuator slips or completely pulls the clutch in to prevent an engine stall.
- **• Use On Changes:** Dictates whether the automated clutch actuator should intervene only during active gear shifts or remain dynamically involved during low-speed maneuvers..

#### <span id="page-167-1"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-referencing these fields across various vehicle archetypes, specific mechanical and competitive design philosophies become apparent:

- **• The Analog Historic Profile (e.g., Caterham 485 CSR):** Features a balanced Clutch Inertia and a realistic Clutch Max Torque overhead. In this profile, Forced On is set to false and Use On Changes is bypassed. The physics model relies entirely on the driver's manual execution of the friction zone, leaving no electronic safety net against stalls if the car spins or launches poorly.
- **• The High-Performance Motorsport Profile (e.g., Formula Cars / Modern GT):** Designed with ultra-low Clutch Inertia (e.g., 0.00500) to maximize engine responsiveness. The Clutch Max Torque is tightly calculated to handle massive peak launch forces. Advanced shifting profiles (Upshift/Downshift .curve) are meticulously tuned to match the rapid millimeterprecision cuts of pneumatic or hydraulic actuators, completing engagements in milliseconds without upsetting the vehicle's balance.

#### <span id="page-167-2"></span>**B. Schema**

├ 1. Clutch Inertia : float

```
- 2. Clutch Max Torque: float
- 3. Autoclutch: object
- 3a. Upshift Profile: string - path
- 3b. Down Shift Profile: string - path
- 3c. Forced On: boolean
- 3d. Min Rpms: float
- 3e. Max Rpms: float
- 3f. Use On Changes: boolean
- 4. Clutch Curve: string - path
```

#### <span id="page-168-0"></span>C. Example data

# <span id="page-168-1"></span>I. Chosen Cars for Example

- Caterham 485 CSR (slug: ks\_caterham\_485\_csr)
- Ferrari F2004 (slug: ks\_ferrari\_f2004)
- Volkswagen Golf GTI mk8 ( slug : ks\_volkswagen\_golf\_gti\_mk8 )

#### <span id="page-168-2"></span>II. Example

#### <span id="page-168-3"></span>Caterham 485 CSR

```
- 1. Clutch Inertia : 0.01700
- 2. Clutch Max Torque : 500.00000
- 3. Autoclutch
- 3a. Upshift Profile :
content\cars\ks_caterham_485_csr\data\upShiftProfile.curve
- 3b. Down Shift Profile :
content\cars\ks_caterham_485_csr\data\downShiftProfile.curve
- 3c. Forced On : false
- 3d. Min Rpms : 1200.00000
- 3e. Max Rpms : 2000.00000
- 3f. Use On Changes : false
- 4. Clutch Curve : None
```

#### <span id="page-168-4"></span>Ferrari F2004

```
- 1. Clutch Inertia: 0.00500
- 2. Clutch Max Torque: 700.00000
- 3. Autoclutch
- 3a. Upshift Profile: None
- 3b. Down Shift Profile:
content\cars\ks_ferrari_f2004\data\downShiftProfile.curve
- 3c. Forced On: false
- 3d. Min Rpms: 4300.00000
- 3e. Max Rpms: 4900.00000
3f. Use On Changes: true
4. Clutch Curve: None
```

#### <span id="page-168-5"></span>Volkswagen Golf GTI mk8

- 1. Clutch Inertia: 0.01000
- 2. Clutch Max Torque : 450.00000

├ 3. Autoclutch

│ ├ 3a. Upshift Profile : None

│ ├ 3b. Down Shift Profile : None

│ ├ 3c. Forced On : true

│ ├ 3d. Min Rpms : 1500.00000

│ ├ 3e. Max Rpms : 2400.00000

│ └ 3f. Use On Changes : true

└ 4. Clutch Curve : None

# <span id="page-170-0"></span>**11. Coilover [ .coilover ]**

# <span id="page-170-1"></span>**A. Description**

#### <span id="page-170-2"></span>**I. General Description**

The **Coilovers** asset defines the mechanical, damping, and geometric physics of the vehicle's primary suspension assemblies. It acts as the central structural, kinetic, and dampening bridge between the unsprung mass (wheels, hubs, brakes) and the sprung mass (chassis and bodywork).

This asset governs how vertical, lateral, and longitudinal forces generated by track irregularities and aerodynamic loads are managed, defining both the physical properties of the suspension units (such as spring rates, helper springs, and bump stops) and the precise hydraulic damping profiles (bump and rebound) that control the velocity of suspension travel.

Additionally, it integrates wheel alignment parameters to establish the static and dynamic geometry of the tire contact patch.

### <span id="page-170-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics**

The parameters configured within the Coilovers asset have a direct and critical impact on the vehicle's mechanical grip, aerodynamic stability, and overall handling balance:

- **• Mechanical Grip and Tire Compliance**: It dictates how effectively the tires maintain contact with the track surface over bumps, kerbs, and undulations. Optimizing spring and damper rates prevents the tires from overloading or losing contact, directly impacting traction and braking efficiency.
- **• Platform Control and Aerodynamic Stability**: On downforce-heavy vehicles, this asset regulates pitch, roll, and ride height variations. By controlling chassis movement under braking, acceleration, and cornering, it ensures the aerodynamic undertray and wings operate within their optimal performance window.
- **• Transient Handling and Response**: During corner entry, apex, and exit phases, the dampers regulate the speed of weight transfer. This asset determines whether the vehicle responds sharply to driver inputs or exhibits sluggish transitions, directly influencing understeer and oversteer characteristics.
- **• Endurance and Structural Management**: Through the configuration of progressive bump stops and helper springs, it defines how the vehicle absorbs severe impacts (such as highspeed kerb strikes) without destabilizing the chassis or causing harsh mechanical bottoming-out.

#### <span id="page-170-4"></span>**III. Key Architecture & Data Fields Explained**

The internal structure of the Coilovers asset isolates core elastic elements, hydraulic damping forces, and static alignment geometry.

#### <span id="page-170-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**

- **• Wheel Rate**: The effective stiffness of the suspension spring measured at the wheel. It determines the basic mechanical resistance to vertical loads and establishes the natural frequency of the chassis.
- **• Bump Stop Up (Range & Rate)**: Defines the clearance distance and progressive stiffness of the compression bump stop. It acts as a secondary, highly stiff spring to prevent the suspension from bottoming out mechanically against the chassis.
- **• Bump Stop Down (Range & Rate)**: Defines the travel limit and stiffness of the rebound stop, restricting the maximum extension of the suspension to prevent unsettled chassis behavior during severe unloading or airborne phases.
- **• Helper Rate & Range**: Configures the characteristics of the helper (or tender) spring. It maintains tension on the main spring when the suspension is fully extended, ensuring predictable tire re-engagement under heavy droop conditions.

# <span id="page-171-0"></span>**2 - DAMPER PROFILE PARAMETERS**

The hydraulic dampening logic isolates low-speed chassis control from high-speed surface absorption:

- **• Slow Bump / Slow Rebound**: Controls low-velocity suspension movements typically induced by driver inputs, such as body roll during cornering, pitching under braking, and squatting under acceleration..
- **• Fast Bump / Fast Rebound**: Controls high-velocity suspension movements triggered by track inputs, such as hitting kerbs, ripples, or sudden track compression changes.
- **• Damping Strategy Profiles**: Determines whether the asset operates on a Scientific Profile (exporting absolute raw forces like Ns/m for telemetry analysis in software like MoTeC) or a Driver-Centric Profile (mapping adjustments to discrete, tactile clicks on the damper valves).

#### <span id="page-171-1"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS**

- **• Pressure**: Establishes the cold and hot tire inflation targets, which directly interact with the vertical spring rate of the tire sidewall.
- **• Camber & Static Camber**: The angular inclination of the wheel relative to the ground. It optimizes the tire's contact patch under heavy cornering loads to maximize lateral grip.
- **• Toe / Toe Out Linear**: The static angle of the wheels relative to the vehicle's longitudinal centerline, critical for tuning straight-line stability, turn-in response, and tire temperature generation.
- **• Caster**: The forward or backward tilt of the steering axis, dictating the selfcentering steering force and dynamic camber gain when turning the wheel.
- **• Compound**: Links the alignment geometry to the specific tire construction metadata, ensuring the suspension mechanics align with the thermal and grip characteristics of the selected rubber.

# <span id="page-172-0"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-referencing these fields across various vehicle archetypes, specific mechanical and competitive design philosophies become apparent:

- **• The Compliant Road / Historic Profile (e.g., Caterham 485 CSR)**: Features lower Wheel Rates and generous Bump Stop Ranges to allow significant suspension travel, prioritizing mechanical compliance and driver feedback over flat platform control. Dampers are tuned with softer Slow Bump settings to absorb road imperfections, and tires utilize higher profiles with conservative camber angles to maintain a forgiving, predictable slip angle progression.
- **• The High-Downforce Motorsport Profile (e.g., Formula Cars / Modern GT)**: Designed with ultra-stiff Wheel Rates and minimal ride heights to lock down the aerodynamic platform. Bump stops are short and aggressive, engaging almost immediately under high aero loads to maintain a stable splitter and diffuser height. Dampers utilize highly sophisticated fast/slow blow-off valves, tuned with millimeter precision to absorb track kerbs rapidly without letting the aerodynamic floor stall or upsetting the car's high-speed stability.

#### <span id="page-172-1"></span>**B. Schema**

```
├ 1. Sprint Rate : float
├ 2. Progressive Spring Rate : float
├ 3. Bump Stop Up : object
│ ├ 3a. Range : float
│ ├ 3b. Reference : float
│ ├ 3c. Force : float
│ ├ 3d. Gamma : float
│ ├ 3e. Length : float
│ └ 3f. Damping : float
├ 4. Bump Stop Down : object
│ ├ 4a. Range : float
│ ├ 4b. Reference : float
│ ├ 4c. Force : float
│ ├ 4d. Gamma : float
│ ├ 4e. Length : float
│ └ 4f. Damping : float
├ 5. Collar Position : float
├ 6. Damper : object
│ ├ 6a. Fast : object
│ │ ├ 6a1. Bump : float
│ │ └ 6a2. Rebound : float
│ ├ 6b. Slow : object
│ │ ├ 6a1. Bump : float
│ │ └ 6a2. Rebound : float
│ ├ 6c. Fast Threshold Bump : float
│ ├ 6d. Fast Threshold Rebound : float
│ ├ 6e. Cooling Surface : float
│ ├ 6f. Nominal Force : float
│ ├ 6g. Min Stress Fatigue : float
│ ├ 6h. Max Stress Fatigue : float
│ ├ 6i. Thermal Capacity : float
│ ├ 6j. Heat Transfer Coef : float
```

```
- 6k. Lut List: string - path
6l. Damper Lut Scale: float
7. Helper K: float
8. Helper Range: float
9. Rod Controllers: object
9a. Name: string
9b. Stages [x]: object | can have multiple Stages
| 9b1. Input Var: enum
| 9b2. Combinator Mode: enum
| 9b3. Lut: string - path
| 9b4. Filter Gain: float
| 9b5. Up Limit: float
| 9b6. Down Limit: float
| 9b7. Current Value: float
| 9b8. Const Value: float
```

#### **Enum - Car Coilover**

| 9b2 | Input Var       | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear, SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX, SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG, SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor, RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG, LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR, SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight, ErsChargeLevel, ErsCoastTorque |
|-----|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 9b2 | Combinator Mode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                          |

#### <span id="page-173-0"></span>C. Example data

#### <span id="page-173-1"></span>I. Chosen Cars for Example

- Caterham 485 CSR (slug: ks\_caterham\_485\_csr)
- Alpine A110s (slug: ks\_alpine\_a110\_s)
- Dallara EXP (slug: ks\_dallara\_exp)

#### <span id="page-173-2"></span>II. Example

#### <span id="page-173-3"></span>Caterham 485 CSR

Front Coilover (file: caterham\_485\_csr\_fr\_coil.coilover)

```
- 1. Sprint Rate: 14000.00000
- 2. Progressive Spring Rate: 0.00000
- 3. Bump Stop Up: object
- 3a. Range: 0.04539
- 3b. Reference: 0.01000
- 3c. Force: 100.00000
- 3d. Gamma: 2.00000
- 3e. Length: 0.02000
3f. Damping: 300.00000
```

```
├ 4. Bump Stop Down : object 
│ ├ 4a. Range : 0.06961 
│ ├ 4b. Reference : 0.01000 
│ ├ 4c. Force : 80.00000 
│ ├ 4d. Gamma : 2.00000 
│ ├ 4e. Length : 0.02000 
│ └ 4f. Damping : 100.00000 
├ 5. Collar Position : 0.04961 
├ 6. Damper : object 
│ ├ 6a. Fast : object 
│ │ ├ 6a1. Bump : 700.00000 
│ │ └ 6a2. Rebound : 1700.00000 
│ ├ 6b. Slow : object 
│ │ ├ 6b1. Bump : 2000.00000 
│ │ └ 6b2. Rebound : 3000.00000 
│ ├ 6c. Fast Threshold Bump : 0.15000 
│ ├ 6d. Fast Threshold Rebound : 0.15000 
│ ├ 6e. Cooling Surface : 0.00000 
│ ├ 6f. Nominal Force : 0.00000 
│ ├ 6g. Min Stress Fatigue : 0.00000 
│ ├ 6h. Max Stress Fatigue : 0.00000 
│ ├ 6i. Thermal Capacity : 0.00000 
│ ├ 6j. Heat Transfer Coef : 0.00000 
│ ├ 6k. Lut List : None 
│ └ 6l. Damper Lut Scale : 0.00000 
├ 7. Helper K : 0.00000 
├ 8. Helper Range : 0.00000 
├ 9. Rod Controllers : object 
│ ├ 9a. Name : None 
└ └ 9b. Stages [x] : None 
2. Rear Coilover ( file : caterham_485_csr_r_coil.coilover ) 
├ 1. Sprint Rate : 16000.00000 
├ 2. Progressive Spring Rate : 0.00000 
├ 3. Bump Stop Up : object 
│ ├ 3a. Range : 0.04031 
│ ├ 3b. Reference : 0.01000 
│ ├ 3c. Force : 100.00000 
│ ├ 3d. Gamma : 2.00000 
│ ├ 3e. Length : 0.02000 
│ └ 3f. Damping : 300.00000 
├ 4. Bump Stop Down : object 
│ ├ 4a. Range : 0.04469 
│ ├ 4b. Reference : 0.01000 
│ ├ 4c. Force : 80.00000 
│ ├ 4d. Gamma : 2.00000 
│ ├ 4e. Length : 0.02000 
│ └ 4f. Damping : 100.00000 
├ 5. Collar Position : 0.06969 
├ 6. Damper : object 
│ ├ 6a. Fast : object 
│ │ ├ 6a1. Bump : 700.00000 
│ │ └ 6a2. Rebound : 1700.00000 
│ ├ 6b. Slow : object
```

```
│ │ ├ 6b1. Bump : 2000.00000 
│ │ └ 6b2. Rebound : 3000.00000 
│ ├ 6c. Fast Threshold Bump : 0.15000 
│ ├ 6d. Fast Threshold Rebound : 0.15000 
│ ├ 6e. Cooling Surface : 0.00000 
│ ├ 6f. Nominal Force : 0.00000 
│ ├ 6g. Min Stress Fatigue : 0.00000 
│ ├ 6h. Max Stress Fatigue : 0.00000 
│ ├ 6i. Thermal Capacity : 0.00000 
│ ├ 6j. Heat Transfer Coef : 0.00000 
│ ├ 6k. Lut List : None 
│ └ 6l. Damper Lut Scale : 0.00000 
├ 7. Helper K : 0.00000 
├ 8. Helper Range : 0.00000 
├ 9. Rod Controllers : object 
│ ├ 9a. Name : None 
└ └ 9b. Stages [x] : None
```

# <span id="page-175-0"></span>**Alpine A110s**

### *1. Front Coilover ( file : ks\_alpine\_a110\_s\_front.coilover )*

```
├ 1. Sprint Rate : 31000.00000 
├ 2. Progressive Spring Rate : 30000.00000 
├ 3. Bump Stop Up : object 
│ ├ 3a. Range : 0.01616 
│ ├ 3b. Reference : 0.00600 
│ ├ 3c. Force : 300.00000 
│ ├ 3d. Gamma : 3.00000 
│ ├ 3e. Length : 0.02000 
│ └ 3f. Damping : 400.00000 
├ 4. Bump Stop Down : object 
│ ├ 4a. Range : 0.05184 
│ ├ 4b. Reference : 0.01000 
│ ├ 4c. Force : 300.00000 
│ ├ 4d. Gamma : 1.50000 
│ ├ 4e. Length : 0.04500 
│ └ 4f. Damping : 400.00000 
├ 5. Collar Position : 0.07184 
├ 6. Damper : object 
│ ├ 6a. Fast : object 
│ │ ├ 6a1. Bump : 1500.00000 
│ │ └ 6a2. Rebound : 3500.00000 
│ ├ 6b. Slow : object 
│ │ ├ 6b1. Bump : 3000.00000 
│ │ └ 6b2. Rebound : 7000.00000 
│ ├ 6c. Fast Threshold Bump : 0.50000 
│ ├ 6d. Fast Threshold Rebound : 0.80000 
│ ├ 6e. Cooling Surface : 0.00000 
│ ├ 6f. Nominal Force : 0.00000 
│ ├ 6g. Min Stress Fatigue : 0.00000 
│ ├ 6h. Max Stress Fatigue : 0.00000 
│ ├ 6i. Thermal Capacity : 0.00000 
│ ├ 6j. Heat Transfer Coef : 0.00000 
│ ├ 6k. Lut List : None
```

```
│ └ 6l. Damper Lut Scale : 0.00000 
├ 7. Helper K : 0.00000 
├ 8. Helper Range : 0.00000 
│ 9. Rod Controllers : object 
│ ├ 9a. Name : None 
└ └ 9b. Stages [x] : None 
2. Rear Coilover ( file : ks_alpine_a110_s_rear.coilover ) 
├ 1. Sprint Rate : 40000.00000 
├ 2. Progressive Spring Rate : 40000.00000 
├ 3. Bump Stop Up : object 
│ ├ 3a. Range : 0.06087 
│ ├ 3b. Reference : 0.00600 
│ ├ 3c. Force : 400.00000 
│ ├ 3d. Gamma : 2.00000 
│ ├ 3e. Length : 0.02000 
│ └ 3f. Damping : 500.00000 
├ 4. Bump Stop Down : object 
│ ├ 4a. Range : -0.00887 
│ ├ 4b. Reference : 0.01000 
│ ├ 4c. Force : 400.00000 
│ ├ 4d. Gamma : 1.50000 
│ ├ 4e. Length : 0.02000 
│ └ 4f. Damping : 500.00000 
├ 5. Collar Position : 0.00913 
├ 6. Damper : object 
│ ├ 6a. Fast : object 
│ │ ├ 6a1. Bump : 1500.00000 
│ │ └ 6a2. Rebound : 2300.00000 
│ ├ 6b. Slow : object 
│ │ ├ 6b1. Bump : 4200.00000 
│ │ └ 6b2. Rebound : 7500.00000 
│ ├ 6c. Fast Threshold Bump : 0.50000 
│ ├ 6d. Fast Threshold Rebound : 0.80000 
│ ├ 6e. Cooling Surface : 0.00000 
│ ├ 6f. Nominal Force : 0.00000 
│ ├ 6g. Min Stress Fatigue : 0.00000 
│ ├ 6h. Max Stress Fatigue : 0.00000 
│ ├ 6i. Thermal Capacity : 0.00000 
│ ├ 6j. Heat Transfer Coef : 0.00000 
│ ├ 6k. Lut List : None 
│ └ 6l. Damper Lut Scale : 0.00000 
├ 7. Helper K : 0.00000 
├ 8. Helper Range : 0.00000 
├ 9. Rod Controllers : object 
│ ├ 9a. Name : None 
└ └ 9b. Stages [x] : None
```

# <span id="page-176-0"></span>**Dallara EXP**

*1. Front Coilover ( file : ks\_dallara\_exp\_front\_coil.coilover )* 

```
├─ 1. Sprint Rate : 50000.00000 
├─ 2. Progressive Spring Rate : 0.00000
```

```
├ 3. Bump Stop Up : object 
│ ├ 3a. Range : -0.01135 
│ ├ 3b. Reference : 0.08000 
│ ├ 3c. Force : 350.00000 
│ ├ 3d. Gamma : 3.00000 
│ ├ 3e. Length : 0.01500 
│ └ 3f. Damping : 1000.00000 
├ 4. Bump Stop Down : object 
│ ├ 4a. Range : 0.05635 
│ ├ 4b. Reference : 0.01000 
│ ├ 4c. Force : 350.00000 
│ ├ 4d. Gamma : 1.50000 
│ ├ 4e. Length : 0.02000 
│ └ 4f. Damping : 500.00000 
├ 5. Collar Position : 0.05135 
├ 6. Damper : object 
│ ├ 6a. Fast : object 
│ │ ├ 6a1. Bump : 1234.00000 
│ │ └ 6a2. Rebound : 2889.00000 
│ ├ 6b. Slow : object 
│ │ ├ 6b1. Bump : 5500.00000 
│ │ └ 6b2. Rebound : 8200.00000 
│ ├ 6c. Fast Threshold Bump : 0.80000 
│ ├ 6d. Fast Threshold Rebound : 0.80000 
│ ├ 6e. Cooling Surface : 0.00000 
│ ├ 6f. Nominal Force : 0.00000 
│ ├ 6g. Min Stress Fatigue : 0.00000 
│ ├ 6h. Max Stress Fatigue : 0.00000 
│ ├ 6i. Thermal Capacity : 0.00000 
│ ├ 6j. Heat Transfer Coef : 0.00000 
│ ├ 6k. Lut List : 
content\cars\common_phsx\dampers\penske\damper_penske.dampercurves 
│ └ 6l. Damper Lut Scale : 1.00000 
├ 7. Helper K : 0.00000 
├ 8. Helper Range : 0.00000 
├ 9. Rod Controllers : object 
│ ├ 9a. Name : None 
└ └ 9b. Stages [x] : None 
2. Rear Coilover ( file : ks_dallara_exp_rear_coil.coilover ) 
├ 1. Sprint Rate : 80000.00000 
├ 2. Progressive Spring Rate : 0.00000 
├ 3. Bump Stop Up : object 
│ ├ 3a. Range : 0.01310 
│ ├ 3b. Reference : 0.08000 
│ ├ 3c. Force : 400.00000 
│ ├ 3d. Gamma : 3.00000 
│ ├ 3e. Length : 0.01500 
│ └ 3f. Damping : 1000.00000 
├ 4. Bump Stop Down : object 
│ ├ 4a. Range : 0.03490 
│ ├ 4b. Reference : 0.01000 
│ ├ 4c. Force : 400.00000 
│ ├ 4d. Gamma : 1.50000
```

```
│ ├ 4e. Length : 0.02000 
│ └ 4f. Damping : 1000.00000 
├ 5. Collar Position : 0.02690 
├ 6. Damper : object 
│ ├ 6a. Fast : object 
│ │ ├ 6a1. Bump : 2042.00000 
│ │ └ 6a2. Rebound : 6889.00000 
│ ├ 6b. Slow : object 
│ │ ├ 6b1. Bump : 7056.00000 
│ │ └ 6b2. Rebound : 12800.00000 
│ ├ 6c. Fast Threshold Bump : 0.80000 
│ ├ 6d. Fast Threshold Rebound : 0.80000 
│ ├ 6e. Cooling Surface : 0.00000 
│ ├ 6f. Nominal Force : 0.00000 
│ ├ 6g. Min Stress Fatigue : 0.00000 
│ ├ 6h. Max Stress Fatigue : 0.00000 
│ ├ 6i. Thermal Capacity : 0.00000 
│ ├ 6j. Heat Transfer Coef : 0.00000 
│ ├ 6k. Lut List : 
content\cars\common_phsx\dampers\penske\damper_penske.dampercurves 
│ └ 6l. Damper Lut Scale : 1.00000 
├ 7. Helper K : 0.00000 
├ 8. Helper Range : 0.00000 
├ 9. Rod Controllers : object 
│ ├ 9a. Name : None 
└ └ 9b. Stages [x] : None
```

# <span id="page-179-0"></span>**12. Damper Curves [ .dampercurves ]**

<span id="page-179-1"></span>

| A. | Description |
|----|-------------|
|    |             |

<span id="page-179-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-179-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-179-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-179-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-179-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-179-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx

#### <span id="page-179-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

<span id="page-179-9"></span>**B. Schema** 

[ Data in a "Damper Curves List Edit" object ]

└ 1. Damper Lut [x] : string - path | can have multiple Damper Lut

#### <span id="page-180-0"></span>C. Example data

#### <span id="page-180-1"></span>I. Chosen Cars for Example

- Ford GT3 Dampers (common\_phsx) [2 dampers]
- Penske Dampers (common phsx)
- Porsche Cayman Dampers (common phsx) [2 dampers]

#### <span id="page-180-2"></span>II. Example

#### <span id="page-180-3"></span>Ford - GT3 Dampers

Front Damper (file: ford\_gt3\_front\_damper.dampercurves)

```
| 1. Damper Lut 1 :
content\cars\common_phsx\dampers\ford\ford_damper_front_1.curve
| 1. Damper Lut 2 :
content\cars\common_phsx\dampers\ford\ford_damper_front_2.curve
| 1. Damper Lut 3 :
content\cars\common_phsx\dampers\ford\ford_damper_front_3.curve
| 1. Damper Lut 4 :
content\cars\common_phsx\dampers\ford\ford_damper_front_4.curve
| 1. Damper Lut 5 :
content\cars\common_phsx\dampers\ford\ford_damper_front_5.curve
```

- 2. Rear Damper (file: ford gt3 rear damper.dampercurves)
- | 1. Damper Lut 1 :
  content\cars\common\_phsx\dampers\ford\ford\_damper\_rear\_1.curve
  | 1. Damper Lut 2 :
  content\cars\common\_phsx\dampers\ford\ford\_damper\_rear\_2.curve
  | 1. Damper Lut 3 :
  content\cars\common\_phsx\dampers\ford\ford\_damper\_rear\_3.curve
  | 1. Damper Lut 4 :
  content\cars\common\_phsx\dampers\ford\ford\_damper\_rear\_4.curve
  | 1. Damper Lut 5 :
  content\cars\common\_phsx\dampers\ford\ford\_damper\_rear\_5.curve

#### <span id="page-180-4"></span>**Penske**

```
| 1. Damper Lut 1 :
content\cars\common_phsx\dampers\penske\damper_1.curve
| 1. Damper Lut 2 :
content\cars\common_phsx\dampers\penske\damper_2.curve
| 1. Damper Lut 3 :
content\cars\common_phsx\dampers\penske\damper_3.curve
| 1. Damper Lut 4 :
content\cars\common_phsx\dampers\penske\damper_4.curve
| 1. Damper Lut 5 :
content\cars\common_phsx\dampers\penske\damper_5.curve
```

```
├ 1. Damper Lut 6 : 
content\cars\common_phsx\dampers\penske\damper_6.curve 
├ 1. Damper Lut 7 : 
content\cars\common_phsx\dampers\penske\damper_7.curve 
├ 1. Damper Lut 8 : 
content\cars\common_phsx\dampers\penske\damper_8.curve 
├ 1. Damper Lut 9 : 
content\cars\common_phsx\dampers\penske\damper_9.curve 
├ 1. Damper Lut 10 : 
content\cars\common_phsx\dampers\penske\damper_10.curve 
├ 1. Damper Lut 11 : 
content\cars\common_phsx\dampers\penske\damper_11.curve 
├ 1. Damper Lut 12 : 
content\cars\common_phsx\dampers\penske\damper_12.curve 
├ 1. Damper Lut 13 : 
content\cars\common_phsx\dampers\penske\damper_13.curve 
├ 1. Damper Lut 14 : 
content\cars\common_phsx\dampers\penske\damper_14.curve 
├ 1. Damper Lut 15 : 
content\cars\common_phsx\dampers\penske\damper_15.curve 
├ 1. Damper Lut 16 : 
content\cars\common_phsx\dampers\penske\damper_16.curve 
├ 1. Damper Lut 17 : 
content\cars\common_phsx\dampers\penske\damper_17.curve 
├ 1. Damper Lut 18 : 
content\cars\common_phsx\dampers\penske\damper_18.curve 
├ 1. Damper Lut 19 : 
content\cars\common_phsx\dampers\penske\damper_19.curve 
├ 1. Damper Lut 20 : 
content\cars\common_phsx\dampers\penske\damper_20.curve 
├ 1. Damper Lut 21 : 
content\cars\common_phsx\dampers\penske\damper_21.curve 
├ 1. Damper Lut 22 : 
content\cars\common_phsx\dampers\penske\damper_22.curve 
├ 1. Damper Lut 23 : 
content\cars\common_phsx\dampers\penske\damper_23.curve 
├ 1. Damper Lut 24 : 
content\cars\common_phsx\dampers\penske\damper_24.curve 
├ 1. Damper Lut 25 : 
content\cars\common_phsx\dampers\penske\damper_25.curve 
├ 1. Damper Lut 26 : 
content\cars\common_phsx\dampers\penske\damper_26.curve 
├ 1. Damper Lut 27 : 
content\cars\common_phsx\dampers\penske\damper_27.curve 
├ 1. Damper Lut 28 : 
content\cars\common_phsx\dampers\penske\damper_28.curve 
├ 1. Damper Lut 29 : 
content\cars\common_phsx\dampers\penske\damper_29.curve 
├ 1. Damper Lut 30 : 
content\cars\common_phsx\dampers\penske\damper_30.curve 
├ 1. Damper Lut 31 : 
content\cars\common_phsx\dampers\penske\damper_31.curve 
├ 1. Damper Lut 32 : 
content\cars\common_phsx\dampers\penske\damper_32.curve 
├ 1. Damper Lut 33 : 
content\cars\common_phsx\dampers\penske\damper_33.curve
```

```
├ 1. Damper Lut 34 : 
content\cars\common_phsx\dampers\penske\damper_34.curve 
├ 1. Damper Lut 35 : 
content\cars\common_phsx\dampers\penske\damper_35.curve 
├ 1. Damper Lut 36 : 
content\cars\common_phsx\dampers\penske\damper_36.curve 
├ 1. Damper Lut 37 : 
content\cars\common_phsx\dampers\penske\damper_37.curve 
├ 1. Damper Lut 38 : 
content\cars\common_phsx\dampers\penske\damper_38.curve 
├ 1. Damper Lut 39 : 
content\cars\common_phsx\dampers\penske\damper_39.curve 
├ 1. Damper Lut 40 : 
content\cars\common_phsx\dampers\penske\damper_40.curve 
├ 1. Damper Lut 41 : 
content\cars\common_phsx\dampers\penske\damper_41.curve 
├ 1. Damper Lut 42 : 
content\cars\common_phsx\dampers\penske\damper_42.curve 
├ 1. Damper Lut 43 : 
content\cars\common_phsx\dampers\penske\damper_43.curve 
├ 1. Damper Lut 44 : 
content\cars\common_phsx\dampers\penske\damper_44.curve 
├ 1. Damper Lut 45 : 
content\cars\common_phsx\dampers\penske\damper_45.curve 
├ 1. Damper Lut 46 : 
content\cars\common_phsx\dampers\penske\damper_46.curve 
├ 1. Damper Lut 47 : 
content\cars\common_phsx\dampers\penske\damper_47.curve 
├ 1. Damper Lut 48 : 
content\cars\common_phsx\dampers\penske\damper_48.curve 
├ 1. Damper Lut 49 : 
content\cars\common_phsx\dampers\penske\damper_49.curve 
├ 1. Damper Lut 50 : 
content\cars\common_phsx\dampers\penske\damper_50.curve 
├ 1. Damper Lut 51 : 
content\cars\common_phsx\dampers\penske\damper_51.curve 
├ 1. Damper Lut 52 : 
content\cars\common_phsx\dampers\penske\damper_52.curve 
├ 1. Damper Lut 53 : 
content\cars\common_phsx\dampers\penske\damper_53.curve 
├ 1. Damper Lut 54 : 
content\cars\common_phsx\dampers\penske\damper_54.curve 
├ 1. Damper Lut 55 : 
content\cars\common_phsx\dampers\penske\damper_55.curve 
├ 1. Damper Lut 56 : 
content\cars\common_phsx\dampers\penske\damper_56.curve 
├ 1. Damper Lut 57 : 
content\cars\common_phsx\dampers\penske\damper_57.curve 
├ 1. Damper Lut 58 : 
content\cars\common_phsx\dampers\penske\damper_58.curve 
├ 1. Damper Lut 59 : 
content\cars\common_phsx\dampers\penske\damper_59.curve 
└ 1. Damper Lut 60 : 
content\cars\common_phsx\dampers\penske\damper_60.curve
```

#### <span id="page-183-0"></span>**Porsche Cayman Dampers**

#### *1. Front Damper ( file : cayman\_gt4\_front.dampercurves )*

```
├ 1. Damper Lut 1 : 
content\cars\common_phsx\dampers\porsche\cayman\front1.curve 
├ 1. Damper Lut 2 : 
content\cars\common_phsx\dampers\porsche\cayman\front2.curve 
├ 1. Damper Lut 3 : 
content\cars\common_phsx\dampers\porsche\cayman\front3.curve 
├ 1. Damper Lut 4 : 
content\cars\common_phsx\dampers\porsche\cayman\front4.curve 
├ 1. Damper Lut 5 : 
content\cars\common_phsx\dampers\porsche\cayman\front5.curve 
├ 1. Damper Lut 6 : 
content\cars\common_phsx\dampers\porsche\cayman\front6.curve 
├ 1. Damper Lut 7 : 
content\cars\common_phsx\dampers\porsche\cayman\front7.curve 
├ 1. Damper Lut 8 : 
content\cars\common_phsx\dampers\porsche\cayman\front8.curve 
├ 1. Damper Lut 9 : 
content\cars\common_phsx\dampers\porsche\cayman\front9.curve 
├ 1. Damper Lut 10 : 
content\cars\common_phsx\dampers\porsche\cayman\front10.curve 
├ 1. Damper Lut 11 : 
content\cars\common_phsx\dampers\porsche\cayman\front11.curve 
└ 1. Damper Lut 12 : 
content\cars\common_phsx\dampers\porsche\cayman\front12.curve
```

#### *2. Rear Damper ( file : cayman\_gt4\_rear.dampercurves )*

```
├ 1. Damper Lut 1 : 
content\cars\common_phsx\dampers\porsche\cayman\rear1.curve 
├ 1. Damper Lut 2 : 
content\cars\common_phsx\dampers\porsche\cayman\rear2.curve 
├ 1. Damper Lut 3 : 
content\cars\common_phsx\dampers\porsche\cayman\rear3.curve 
├ 1. Damper Lut 4 : 
content\cars\common_phsx\dampers\porsche\cayman\rear4.curve 
├ 1. Damper Lut 5 : 
content\cars\common_phsx\dampers\porsche\cayman\rear5.curve 
├ 1. Damper Lut 6 : 
content\cars\common_phsx\dampers\porsche\cayman\rear6.curve 
├ 1. Damper Lut 7 : 
content\cars\common_phsx\dampers\porsche\cayman\rear7.curve 
├ 1. Damper Lut 8 : 
content\cars\common_phsx\dampers\porsche\cayman\rear8.curve 
├ 1. Damper Lut 9 : 
content\cars\common_phsx\dampers\porsche\cayman\rear9.curve 
├ 1. Damper Lut 10 : 
content\cars\common_phsx\dampers\porsche\cayman\rear10.curve 
├ 1. Damper Lut 11 : 
content\cars\common_phsx\dampers\porsche\cayman\rear11.curve
```

└ 1. Damper Lut 12 : content\cars\common\_phsx\dampers\porsche\cayman\rear12.curve

# <span id="page-185-0"></span>**13. Drivetrain [ .drivetrain ]**

# <span id="page-185-1"></span>**A. Description**

<span id="page-185-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-185-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-185-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-185-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-185-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-185-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx

#### <span id="page-185-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

#### <span id="page-185-9"></span>**B. Schema**

```
├ 1. Traction Type : enum
├ 2. Differential Data : object
│ ├ 2a. Type : enum
│ ├ 2b. Power : float
│ ├ 2c. Coast : float
│ ├ 2d. Preload : float
│ ├ 2e. Front Share : float
│ ├ 2f. Torque Bias Ratio Power : float
│ ├ 2g. Torque Bias Ratio Coast : float
│ ├ 2h. Thermal Capacity : float
```

```
│ ├ 2i. Surface : float
│ ├ 2j. Heat Transfer Coeff : float
│ ├ 2k. Wear Factor : float
│ ├ 2l. Friction Reduction With T : float
│ └ 2m. Friction Ref T : float
├ 3. Four W D Differentials : object
│ ├ 3a. Front Diff : object
│ │ ├ 2a. Type : float
│ │ ├ 2b. Power : float
│ │ ├ 2c. Coast : float
│ │ ├ 2d. Preload : float
│ │ ├ 2e. Front Share : float
│ │ ├ 2f. Torque Bias Ratio Power : float
│ │ ├ 2g. Torque Bias Ratio Coast : float
│ │ ├ 2h. Thermal Capacity : float
│ │ ├ 2i. Surface : float
│ │ ├ 2j. Heat Transfer Coeff : float
│ │ ├ 2k. Wear Factor : float
│ │ ├ 2l. Friction Reduction With T : float
│ │ └ 2m. Friction Ref T : float
│ ├ 3b. Center Diff : object
│ │ ├ 2a. Type : enum
│ │ ├ 2b. Power : float
│ │ ├ 2c. Coast : float
│ │ ├ 2d. Preload : float
│ │ ├ 2e. Front Share : float
│ │ ├ 2f. Torque Bias Ratio Power : float
│ │ ├ 2g. Torque Bias Ratio Coast : float
│ │ ├ 2h. Thermal Capacity : float
│ │ ├ 2i. Surface : float
│ │ ├ 2j. Heat Transfer Coeff : float
│ │ ├ 2k. Wear Factor : float
│ │ ├ 2l. Friction Reduction With T : float
│ │ └ 2m. Friction Ref T : float
│ ├ 3c. Rear Diff : object
│ │ ├ 2a. Type : enum
│ │ ├ 2b. Power : float
│ │ ├ 2c. Coast : float
│ │ ├ 2d. Preload : float
│ │ ├ 2e. Front Share : float
│ │ ├ 2f. Torque Bias Ratio Power : float
│ │ ├ 2g. Torque Bias Ratio Coast : float
│ │ ├ 2h. Thermal Capacity : float
│ │ ├ 2i. Surface : float
│ │ ├ 2j. Heat Transfer Coeff : float
│ │ ├ 2k. Wear Factor : float
│ │ ├ 2l. Friction Reduction With T : float
│ └ └ 2m. Friction Ref T : float
├ 4. Stiffness : float
├ 5. Stiffness Mult : float
├ 6. Damping Ratio : float
├ 7. Max Torsion Deg : float
├ 8. Non Linear Model : boolean
├ 9. Max Between Lsd And Elsd : boolean
├ 10. Has Cockpit Controls : boolean
├ 11. Front Lock Controllers : object
```

```
│ ├ 11a. Name : string
│ ├ 11b. Stages [x] : object | can have multiple Stages
│ │ ├ 11b1. Input Var : enum
│ │ ├ 11b2. Combinator Mode : enum
│ │ ├ 11b3. Lut : string - path
│ │ ├ 11b4. Filter Gain : float
│ │ ├ 11b5. Up Limit : float
│ │ ├ 11b6. Down Limit : float
│ │ ├ 11b7. Current Value : float
│ │ └ 11b8. Const Value : float
├ 12. Center Lock Controllers : object
│ ├ 11a. Name : string
│ ├ 11b. Stages [x] : object | can have multiple Stages
│ │ ├ 11b1. Input Var : enum
│ │ ├ 11b2. Combinator Mode : enum
│ │ ├ 11b3. Lut : string - path
│ │ ├ 11b4. Filter Gain : float
│ │ ├ 11b5. Up Limit : float
│ │ ├ 11b6. Down Limit : float
│ │ ├ 11b7. Current Value : float
│ └ └ 11b8. Const Value : float
├ 13. Rear Lock Controllers : object
│ ├ 11a. Name : string
│ ├ 11b. Stages [x] : object | can have multiple Stages
│ │ ├ 11b1. Input Var : enum
│ │ ├ 11b2. Combinator Mode : enum
│ │ ├ 11b3. Lut : string - path
│ │ ├ 11b4. Filter Gain : float
│ │ ├ 11b5. Up Limit : float
│ │ ├ 11b6. Down Limit : float
│ │ ├ 11b7. Current Value : float
│ └ └ 11b8. Const Value : float
├ 14. Left Lock Controllers : object
│ ├ 11a. Name : string
│ ├ 11b. Stages [x] : object | can have multiple Stages
│ │ ├ 11b1. Input Var : enum
│ │ ├ 11b2. Combinator Mode : enum
│ │ ├ 11b3. Lut : string - path
│ │ ├ 11b4. Filter Gain : float
│ │ ├ 11b5. Up Limit : float
│ │ ├ 11b6. Down Limit : float
│ │ ├ 11b7. Current Value : float
│ └ └ 11b8. Const Value : float
├ 15. Right Lock Controllers : object
│ ├ 11a. Name : string
│ ├ 11b. Stages [x] : object | can have multiple Stages
│ │ ├ 11b1. Input Var : enum
│ │ ├ 11b2. Combinator Mode : enum
│ │ ├ 11b3. Lut : string - path
│ │ ├ 11b4. Filter Gain : float
│ │ ├ 11b5. Up Limit : float
│ │ ├ 11b6. Down Limit : float
│ │ ├ 11b7. Current Value : float
│ └ └ 11b8. Const Value : float
├ 16. Awd Clutches [x] : object | can have multiple Awd Clutches
│ ├ 16a. Position : integer
```

```
- 16b. Preload : float
- 16c. Controllers : object
- 11a. Name : string
- 11b. Stages [x] : object | can have multiple Stages
- 11b1. Input Var : enum
- 11b2. Combinator Mode : enum
- 11b3. Lut : string - path
- 11b4. Filter Gain : float
- 11b5. Up Limit : float
- 11b6. Down Limit : float
- 11b7. Current Value : float
11b8. Const Value : float
```

#### <span id="page-188-0"></span>C. Example data

#### <span id="page-188-1"></span>I. Chosen Cars for Example

- Audi RS3 Sportback (slug : ks\_audi\_rs\_3\_sportback)
- Ferrari F40 LM ( slug : ks\_ferrari\_f40\_lm )
- Abarth 695 Biposto (slug: ks\_abarth\_695\_biposto)

#### <span id="page-188-2"></span>II. Example

### <span id="page-188-3"></span>**Audi RS3 Sportback**

```
1. Traction Type : AWDF
2. Differential Data
 - 2a. Type : LSD
  2b. Power : 0.00000
  2c. Coast: 0.00000
  2d. Preload: 0.00000
  2e. Front Share: 0.00000
  2f. Torque Bias Ratio Power: 0.00000
  2g. Torque Bias Ratio Coast: 0.00000
  2h. Thermal Capacity: 0.00000
 - 2i. Surface : 0.00000
 - 2i. Heat Transfer Coeff : 0.00000
  2k. Wear Factor: 0.00000
  21. Friction Reduction With T: 0.00000
 L 2m. Friction Ref T: 0.00000
3. Four W D Differentials
 · 3a. Front Diff
   - 2a. Type : LSD
    2b. Power: 0.50000
   - 2c. Coast : 0.10000
   - 2d. Preload : 30.00000
    2e. Front Share: 0.00000
    2f. Torque Bias Ratio Power: 0.00000
   - 2g. Torque Bias Ratio Coast : 0.00000
    2h. Thermal Capacity: 0.00000
    2i. Surface: 0.00000
    2j. Heat Transfer Coeff: 0.00000
    2k. Wear Factor: 0.00000
```

```
│ │ ├ 2l. Friction Reduction With T : 0.00000 
│ │ └ 2m. Friction Ref T : 0.00000 
│ ├ 3b. Center Diff 
│ │ ├ 2a. Type : EpicyclicLSD 
│ │ ├ 2b. Power : 0.03000 
│ │ ├ 2c. Coast : 0.03000 
│ │ ├ 2d. Preload : 1.00000 
│ │ ├ 2e. Front Share : 0.40000 
│ │ ├ 2f. Torque Bias Ratio Power : 0.00000 
│ │ ├ 2g. Torque Bias Ratio Coast : 0.00000 
│ │ ├ 2h. Thermal Capacity : 0.00000 
│ │ ├ 2i. Surface : 0.00000 
│ │ ├ 2j. Heat Transfer Coeff : 0.00000 
│ │ ├ 2k. Wear Factor : 0.00000 
│ │ ├ 2l. Friction Reduction With T : 0.00000 
│ │ └ 2m. Friction Ref T : 0.00000 
│ ├ 3c. Rear Diff 
│ │ ├ 2a. Type : Spool 
│ │ ├ 2b. Power : 0.03000 
│ │ ├ 2c. Coast : 0.03000 
│ │ ├ 2d. Preload : 0.00000 
│ │ ├ 2e. Front Share : 0.00000 
│ │ ├ 2f. Torque Bias Ratio Power : 2.50000 
│ │ ├ 2g. Torque Bias Ratio Coast : 2.00000 
│ │ ├ 2h. Thermal Capacity : 0.00000 
│ │ ├ 2i. Surface : 0.00000 
│ │ ├ 2j. Heat Transfer Coeff : 0.00000 
│ │ ├ 2k. Wear Factor : 0.00000 
│ │ ├ 2l. Friction Reduction With T : 0.00000 
│ └ └ 2m. Friction Ref T : 0.00000 
├ 4. Stiffness : 0.00000 
├ 5. Stiffness Mult : 0.00000 
├ 6. Damping Ratio : 0.00000 
├ 7. Max Torsion Deg : 0.00000 
├ 8. Non Linear Model : false 
├ 9. Max Between Lsd And Elsd : false 
├ 10. Has Cockpit Controls : false 
├ 11. Front Lock Controllers 
│ ├ 11a. Name : None 
│ └ 11b. Stages : None 
├ 12. Center Lock Controllers 
│ ├ 11a. Name : None 
│ └ 11b. Stages : None 
├ 13. Rear Lock Controllers 
│ ├ 11a. Name : None 
│ └ 11b. Stages : None 
├ 14. Left Lock Controllers 
│ ├ 11a. Name : None 
│ └ 11b. Stages : None 
├ 15. Right Lock Controllers 
│ ├ 11a. Name : None 
│ └ 11b. Stages : None 
├ 16. Awd Clutches 1 
│ ├ 16a. Position : 2 
│ ├ 16b. Preload : 0.000 
│ ├ 16c. Controllers
```

```
│ │ ├ 11a. Name : None 
│ │ ├ 11b. Stages 1
│ │ │ ├ 11b1. Input Var : Gas 
│ │ │ ├ 11b2. Combinator Mode : Add 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_sportback_awd_gas_add.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ │ │ └ 11b8. Const Value : 0.00000 
│ │ ├ 11b. Stages 2
│ │ │ ├ 11b1. Input Var : SlipRatioFrontAVG 
│ │ │ ├ 11b2. Combinator Mode : Add 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_awd_clutch_SRavg.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ │ │ └ 11b8. Const Value : 0.00000 
│ │ ├ 11b. Stages 3
│ │ │ ├ 11b1. Input Var : LatG 
│ │ │ ├ 11b2. Combinator Mode : Mult 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_sportback_steer_right_clutch_Perf1.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ │ │ └ 11b8. Const Value : 0.00000 
│ │ ├ 11b. Stages 4
│ │ │ ├ 11b1. Input Var : OversteerFactor 
│ │ │ ├ 11b2. Combinator Mode : Mult 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_sportback_awd_clutch_oversteer.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ │ │ └ 11b8. Const Value : 0.00000 
│ │ ├ 11b. Stages 5
│ │ │ ├ 11b1. Input Var : Speed 
│ │ │ ├ 11b2. Combinator Mode : Mult 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_awd_clutch_speed_power.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ └ └ └ 11b8. Const Value : 0.00000
```

```
├ 16. Awd Clutches 2 
│ ├ 16a. Position : 3 
│ ├ 16b. Preload : 0.000 
│ ├ 16c. Controllers 
│ │ ├ 11a. Name : None 
│ │ ├ 11b. Stages 1
│ │ │ ├ 11b1. Input Var : Gas 
│ │ │ ├ 11b2. Combinator Mode : Add 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_sportback_awd_gas_add.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ │ │ └ 11b8. Const Value : 0.00000 
│ │ ├ 11b. Stages 2
│ │ │ ├ 11b1. Input Var : SlipRatioFrontAVG 
│ │ │ ├ 11b2. Combinator Mode : Add 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_awd_clutch_SRavg.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ │ │ └ 11b8. Const Value : 0.00000 
│ │ ├ 11b. Stages 3
│ │ │ ├ 11b1. Input Var : LatG 
│ │ │ ├ 11b2. Combinator Mode : Mult 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_sportback_steer_right_clutch_Perf1.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ │ │ └ 11b8. Const Value : 0.00000 
│ │ ├ 11b. Stages 4
│ │ │ ├ 11b1. Input Var : OversteerFactor 
│ │ │ ├ 11b2. Combinator Mode : Mult 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_sportback_awd_clutch_oversteer.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
│ │ │ └ 11b8. Const Value : 0.00000 
│ │ ├ 11b. Stages 5
│ │ │ ├ 11b1. Input Var : Speed 
│ │ │ ├ 11b2. Combinator Mode : Mult 
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_awd_clutch_speed_power.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000
```

```
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
└ └ └ └ 11b8. Const Value : 0.00000
```

### <span id="page-192-0"></span>**Ferrari F40 LM**

```
├ 1. Traction Type : RWD 
├ 2. Differential Data 
│ ├ 2a. Type : LSD 
│ ├ 2b. Power : 0.00000 
│ ├ 2c. Coast : 0.00000 
│ ├ 2d. Preload : 0.00000 
│ ├ 2e. Front Share : 0.00000 
│ ├ 2f. Torque Bias Ratio Power : 0.00000 
│ ├ 2g. Torque Bias Ratio Coast : 0.00000 
│ ├ 2h. Thermal Capacity : 0.00000 
│ ├ 2i. Surface : 0.00000 
│ ├ 2j. Heat Transfer Coeff : 0.00000 
│ ├ 2k. Wear Factor : 0.00000 
│ ├ 2l. Friction Reduction With T : 0.00000 
│ └ 2m. Friction Ref T : 0.00000 
├ 3. Four W D Differentials 
│ ├ 3a. Front Diff 
│ │ ├ 2a. Type : LSF 
│ │ ├ 2b. Power : 0.00000 
│ │ ├ 2c. Coast : 0.00000 
│ │ ├ 2d. Preload : 0.00000 
│ │ ├ 2e. Front Share : 0.00000 
│ │ ├ 2f. Torque Bias Ratio Power : 0.00000 
│ │ ├ 2g. Torque Bias Ratio Coast : 0.00000 
│ │ ├ 2h. Thermal Capacity : 0.00000 
│ │ ├ 2i. Surface : 0.00000 
│ │ ├ 2j. Heat Transfer Coeff : 0.00000 
│ │ ├ 2k. Wear Factor : 0.00000 
│ │ ├ 2l. Friction Reduction With T : 0.00000 
│ │ └ 2m. Friction Ref T : 0.00000 
│ ├ 3b. Center Diff 
│ │ ├ 2a. Type : LSD 
│ │ ├ 2b. Power : 0.00000 
│ │ ├ 2c. Coast : 0.00000 
│ │ ├ 2d. Preload : 0.00000 
│ │ ├ 2e. Front Share : 0.00000 
│ │ ├ 2f. Torque Bias Ratio Power : 0.00000 
│ │ ├ 2g. Torque Bias Ratio Coast : 0.00000 
│ │ ├ 2h. Thermal Capacity : 0.00000 
│ │ ├ 2i. Surface : 0.00000 
│ │ ├ 2j. Heat Transfer Coeff : 0.00000 
│ │ ├ 2k. Wear Factor : 0.00000 
│ │ ├ 2l. Friction Reduction With T : 0.00000 
│ │ └ 2m. Friction Ref T : 0.00000 
│ ├ 3c. Rear Diff 
│ │ ├ 2a. Type : LSD 
│ │ ├ 2b. Power : 0.00000
```

│ │ ├ 2c. Coast : 0.00000 │ │ ├ 2d. Preload : 0.00000 │ │ ├ 2e. Front Share : 0.00000 │ │ ├ 2f. Torque Bias Ratio Power : 0.00000 │ │ ├ 2g. Torque Bias Ratio Coast : 0.00000 │ │ ├ 2h. Thermal Capacity : 0.00000 │ │ ├ 2i. Surface : 0.00000 │ │ ├ 2j. Heat Transfer Coeff : 0.00000 │ │ ├ 2k. Wear Factor : 0.00000 │ │ ├ 2l. Friction Reduction With T : 0.00000 │ └ └ 2m. Friction Ref T : 0.00000 ├ 4. Stiffness : 4500.00000 ├ 5. Stiffness Mult : 2.00000 ├ 6. Damping Ratio : 0.05000 ├ 7. Max Torsion Deg : 40.00000 ├ 8. Non Linear Model : true ├ 9. Max Between Lsd And Elsd : false ├ 10. Has Cockpit Controls : false ├ 11. Front Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None ├ 12. Center Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None ├ 13. Rear Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None ├ 14. Left Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None ├ 15. Right Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None └ 16. Awd Clutches : None

# <span id="page-193-0"></span>**Abarth 695 Biposto**

```
├ 1. Traction Type : FWD 
├ 2. Differential Data 
│ ├ 2a. Type : LSD 
│ ├ 2b. Power : 0.25000 
│ ├ 2c. Coast : 0.25000 
│ ├ 2d. Preload : 20.00000 
│ ├ 2e. Front Share : 0.00000 
│ ├ 2f. Torque Bias Ratio Power : 0.00000 
│ ├ 2g. Torque Bias Ratio Coast : 0.00000 
│ ├ 2h. Thermal Capacity : 0.00000 
│ ├ 2i. Surface : 0.00000 
│ ├ 2j. Heat Transfer Coeff : 0.00000 
│ ├ 2k. Wear Factor : 0.00000 
│ ├ 2l. Friction Reduction With T : 0.00000 
│ └ 2m. Friction Ref T : 0.00000 
├ 3. Four W D Differentials 
│ ├ 3a. Front Diff
```

```
│ │ ├ 2a. Type : LSD 
│ │ ├ 2b. Power : 0.00000 
│ │ ├ 2c. Coast : 0.00000 
│ │ ├ 2d. Preload : 0.00000 
│ │ ├ 2e. Front Share : 0.00000 
│ │ ├ 2f. Torque Bias Ratio Power : 0.00000 
│ │ ├ 2g. Torque Bias Ratio Coast : 0.00000 
│ │ ├ 2h. Thermal Capacity : 0.00000 
│ │ ├ 2i. Surface : 0.00000 
│ │ ├ 2j. Heat Transfer Coeff : 0.00000 
│ │ ├ 2k. Wear Factor : 0.00000 
│ │ ├ 2l. Friction Reduction With T : 0.00000 
│ │ └ 2m. Friction Ref T : 0.00000 
│ ├ 3b. Center Diff 
│ │ ├ 2a. Type : LSD 
│ │ ├ 2b. Power : 0.00000 
│ │ ├ 2c. Coast : 0.00000 
│ │ ├ 2d. Preload : 0.00000 
│ │ ├ 2e. Front Share : 0.00000 
│ │ ├ 2f. Torque Bias Ratio Power : 0.00000 
│ │ ├ 2g. Torque Bias Ratio Coast : 0.00000 
│ │ ├ 2h. Thermal Capacity : 0.00000 
│ │ ├ 2i. Surface : 0.00000 
│ │ ├ 2j. Heat Transfer Coeff : 0.00000 
│ │ ├ 2k. Wear Factor : 0.00000 
│ │ ├ 2l. Friction Reduction With T : 0.00000 
│ │ └ 2m. Friction Ref T : 0.00000 
│ ├ 3c. Rear Diff 
│ │ ├ 2a. Type : LSD 
│ │ ├ 2b. Power : 0.00000 
│ │ ├ 2c. Coast : 0.00000 
│ │ ├ 2d. Preload : 0.00000 
│ │ ├ 2e. Front Share : 0.00000 
│ │ ├ 2f. Torque Bias Ratio Power : 0.00000 
│ │ ├ 2g. Torque Bias Ratio Coast : 0.00000 
│ │ ├ 2h. Thermal Capacity : 0.00000 
│ │ ├ 2i. Surface : 0.00000 
│ │ ├ 2j. Heat Transfer Coeff : 0.00000 
│ │ ├ 2k. Wear Factor : 0.00000 
│ │ ├ 2l. Friction Reduction With T : 0.00000 
│ └ └ 2m. Friction Ref T : 0.00000 
├ 4. Stiffness : 0.00000 
├ 5. Stiffness Mult : 0.00000 
├ 6. Damping Ratio : 0.00000 
├ 7. Max Torsion Deg : 0.00000 
├ 8. Non Linear Model : false 
├ 9. Max Between Lsd And Elsd : false 
├ 10. Has Cockpit Controls : false 
├ 11. Front Lock Controllers 
│ ├ 11a. Name : None 
│ └ 11b. Stages : None 
├ 12. Center Lock Controllers 
│ ├ 11a. Name : None 
│ └ 11b. Stages : None 
├ 13. Rear Lock Controllers 
│ ├ 11a. Name : None
```

│ └ 11b. Stages : None

├ 14. Left Lock Controllers

│ ├ 11a. Name : None │ └ 11b. Stages : None

├ 15. Right Lock Controllers

│ ├ 11a. Name : None │ └ 11b. Stages : None ├ 16. Awd Clutches : None

# <span id="page-196-0"></span>**14. Gearbox [ .gearbox ]**

# <span id="page-196-1"></span>**A. Description**

<span id="page-196-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-196-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-196-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-196-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-196-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-196-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx

#### <span id="page-196-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

#### <span id="page-196-9"></span>**B. Schema**

```
├ 1. Gear Count : integer
├ 2. Gears [x] : object | can have multiple Gears
│ ├ 2a. Name : string
│ └ 2b. Ratio : float
├ 3. Final Ratio : float
├ 4. Gear Up Time : float
├ 5. Gear Dn Time : float
├ 6. Auto Cut Off Time : float
├ 7. Gas Cut Off Level : float
├ 8. Has Dual Clutch : boolean
```

```
9. Is Shifter Supported: boolean
 10. Downshift Protection : object
  - 10a. Is Active : boolean
 - 10b. Is Debug : boolean
  - 10c. Overrev : integer
 10d. Lock N : boolean
 11. Damage Rpm Window: float
 12. Valid Shift Rpm Window: float
 13. Controls Window Gain: float
 14. Gearbox Inertia : float
 15. Autoblip : object
  - 15a. Profile : float
 15a. Is Electronic : boolean
 16. Autoshifter: object
 - 16a. Up : integer
 - 16b. Down Rpm Threshold : integer
  16c. Slip Threshold: float
 16d. Gas Cutoff Time : float
 17. Gears Fatigue Log10 A : float
 18. Gears Fatigue Nominal Torque : float
19. Gears Fatigue Max Stress: float
<sup>L</sup> 20. Gears Fatigue Min Stress : float
```

#### <span id="page-197-0"></span>C. Example data

#### <span id="page-197-1"></span>I. Chosen Cars for Example

- Porsche 718 Cayman GT4 CS MR ( slug : ks\_porsche\_718\_cayman\_gt4\_cs\_mr )
- Alpine A290 b (slug: ks\_alpine\_a290\_b)
- Renault 5 GT Turbo (slug: ks\_renault\_5\_gt\_turbo)

#### <span id="page-197-2"></span>II. Example

#### <span id="page-197-3"></span>Porsche 718 Cayman GT4 CS MR

```
1. Gear Count : 6
2. Gears 1
2a. Name : R
2b. Ratio : -3.55000
2. Gears 2
 - 2a. Name : N
L 2b. Ratio : 0.00000
2. Gears 3
- 2a. Name . . 2b. Ratio : 3.90900
  2a. Name : 1
2. Gears 4
 - 2a. Name : 2
L 2b. Ratio : 2.29167
2. Gears 5
 - 2a. Name : 3
2b. Ratio : 1.65384
2. Gears 6
- 2a. Name : 4
```

```
│ └ 2b. Ratio : 1.30303 
├ 2. Gears 7 
│ ├ 2a. Name : 5 
│ └ 2b. Ratio : 1.08108 
├ 2. Gears 8 
│ ├ 2a. Name : 6 
│ └ 2b. Ratio : 0.88095 
├ 3. Final Ratio : 3.72461 
├ 4. Gear Up Time : 30.00000 
├ 5. Gear Dn Time : 80.00000 
├ 6. Auto Cut Off Time : 30.00000 
├ 7. Gas Cut Off Level : 0.70000 
├ 8. Has Dual Clutch : true 
├ 9. Is Shifter Supported : false 
├ 10. Downshift Protection 
│ ├ 10a. Is Active : true 
│ ├ 10b. Is Debug : false 
│ ├ 10c. Overrev : 300 
│ └ 10d. Lock N : true 
├ 11. Damage Rpm Window : 100.00000 
├ 12. Valid Shift Rpm Window : 800.00000 
├ 13. Controls Window Gain : 0.40000 
├ 14. Gearbox Inertia : 0.01200 
├ 15. Autoblip 
│ ├ 15a. Profile : 
content\cars\ks_porsche_718_cayman_gt4_cs_mr\data\curves\718_gt4_autobli
p.curve 
│ └ 15a. Is Electronic : true 
├ 16. Autoshifter 
│ ├ 16a. Up : 7700 
│ ├ 16b. Down Rpm Threshold : 0 
│ ├ 16c. Slip Threshold : 0.96000 
│ └ 16d. Gas Cutoff Time : 0.06300 
├ 17. Gears Fatigue Log10 A : 0.00000 
├ 18. Gears Fatigue Nominal Torque : 0.00000 
├ 19. Gears Fatigue Max Stress : 0.00000 
└ 20. Gears Fatigue Min Stress : 0.00000
```

#### <span id="page-198-0"></span>**Alpine A290 b**

```
├ 1. Gear Count : 1 
├ 2. Gears 1 
│ ├ 2a. Name : R 
│ └ 2b. Ratio : -9.00000 
├ 2. Gears 2 
│ ├ 2a. Name : N 
│ └ 2b. Ratio : 0.00000 
├ 2. Gears 3 
│ ├ 2a. Name : 1 
│ └ 2b. Ratio : 9.00000 
├ 3. Final Ratio : 1.00000 
├ 4. Gear Up Time : 10.00000 
├ 5. Gear Dn Time : 16.00000 
├ 6. Auto Cut Off Time : 11.00000
```

```
├ 7. Gas Cut Off Level : 0.00000 
├ 8. Has Dual Clutch : false 
├ 9. Is Shifter Supported : false 
├ 10. Downshift Protection 
│ ├ 10a. Is Active : true 
│ ├ 10b. Is Debug : false 
│ ├ 10c. Overrev : 100 
│ └ 10d. Lock N : true 
├ 11. Damage Rpm Window : 100.00000 
├ 12. Valid Shift Rpm Window : 800.00000 
├ 13. Controls Window Gain : 0.40000 
├ 14. Gearbox Inertia : 0.00800 
├ 15. Autoblip 
│ ├ 15a. Profile : 
content\cars\ks_alpine_a290_b\data\autoBlipProfile.curve 
│ └ 15a. Is Electronic : true 
├ 16. Autoshifter 
│ ├ 16a. Up : 6850 
│ ├ 16b. Down Rpm Threshold : 0 
│ ├ 16c. Slip Threshold : 0.95000 
│ └ 16d. Gas Cutoff Time : 0.15000 
├ 17. Gears Fatigue Log10 A : 0.00000 
├ 18. Gears Fatigue Nominal Torque : 0.00000 
├ 19. Gears Fatigue Max Stress : 0.00000 
└ 20. Gears Fatigue Min Stress : 0.00000
```

#### <span id="page-199-0"></span>**Renault 5 GT Turbo**

```
├ 1. Gear Count : 5 
├ 2. Gears 1 
│ ├ 2a. Name : R 
│ └ 2b. Ratio : -3.54500 
├ 2. Gears 2 
│ ├ 2a. Name : N 
│ └ 2b. Ratio : 0.00000 
├ 2. Gears 3 
│ ├ 2a. Name : 1 
│ └ 2b. Ratio : 3.09100 
├ 2. Gears 4 
│ ├ 2a. Name : 2 
│ └ 2b. Ratio : 1.84200 
├ 2. Gears 5 
│ ├ 2a. Name : 3 
│ └ 2b. Ratio : 1.32100 
├ 2. Gears 6 
│ ├ 2a. Name : 4 
│ └ 2b. Ratio : 0.96700 
├ 2. Gears 7 
│ ├ 2a. Name : 5 
│ └ 2b. Ratio : 0.75800 
├ 3. Final Ratio : 3.73300 
├ 4. Gear Up Time : 250.00000 
├ 5. Gear Dn Time : 270.00000 
├ 6. Auto Cut Off Time : 0.00000
```

```
├ 7. Gas Cut Off Level : 0.00000 
├ 8. Has Dual Clutch : false 
├ 9. Is Shifter Supported : true 
├ 10. Downshift Protection 
│ ├ 10a. Is Active : false 
│ ├ 10b. Is Debug : false 
│ ├ 10c. Overrev : 0 
│ └ 10d. Lock N : false 
├ 11. Damage Rpm Window : 100.00000 
├ 12. Valid Shift Rpm Window : 1000.00000 
├ 13. Controls Window Gain : 0.40000 
├ 14. Gearbox Inertia : 0.01700 
├ 15. Autoblip 
│ ├ 15a. Profile : 
content\cars\ks_renault_5_gt_turbo\data\autoBlipProfile.curve 
│ └ 15a. Is Electronic : false 
├ 16. Autoshifter 
│ ├ 16a. Up : 6000 
│ ├ 16b. Down Rpm Threshold : 0 
│ ├ 16c. Slip Threshold : 0.95000 
│ └ 16d. Gas Cutoff Time : 0.30000 
├ 17. Gears Fatigue Log10 A : 0.00000 
├ 18. Gears Fatigue Nominal Torque : 0.00000 
├ 19. Gears Fatigue Max Stress : 0.00000 
└ 20. Gears Fatigue Min Stress : 0.00000
```

# <span id="page-201-0"></span>**15. General [ .generalcar ]**

# <span id="page-201-1"></span>**A. Description**

<span id="page-201-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-201-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-201-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-201-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-201-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-201-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx

#### <span id="page-201-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

# <span id="page-201-9"></span>**B. Schema**

```
├ 1. Screen Name : string
├ 2. Total Mass : float
├ 3. Tank Position : x, y, z float
├ 4. Fuel : float
├ 5. Max Fuel : float
├ 6. Efficiency : float
├ 7. Kg Per Liter : float
├ 8. Body Box Sizes : x, y, z float
├ 9. Pickup Front Height : float
├ 10. Pickup Rear Height : float
```

```
├ 11. Check Rules : boolean
├ 12. Minimum Height : float
├ 13. Torsional Stiffness : float
├ 14. Torsional Damping : float
├ 15. Body Mesh Offset : object
│ ├ 15a. Position : x, y, z float
│ ├ 15b. Rotation : x, y, z float
└ └ 15c. Scale : x, y, z float
```

# <span id="page-202-0"></span>**C. Example data**

#### <span id="page-202-1"></span>**I. Chosen Cars for Example**

No cars or common assets use an asset of the "generalcar" type.

# <span id="page-203-0"></span>**16. Surface 3D [ .surface3d ]**

# <span id="page-203-1"></span>**A. Description**

<span id="page-203-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-203-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-203-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-203-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-203-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-203-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx

#### <span id="page-203-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

# <span id="page-203-9"></span>**B. Schema**

```
├ 1. Downforce h mm : string - path 
├ 2. Downforce dh mm : string - path
├ 3. size rear : range integer ( 0 - 30 )
├ 4. size front : range integer ( 0 - 30 )
├ 5. min rear : float
├ 6. max rear : float
├ 7. min front : float
├ 8. max front : float 
├ (9). Interpolation Table : table of size "3. size rear" * "4. size 
front"
```

```
- 10. interpolation done : boolean
- 11. Interp Map : object
- 11a. min val : float
- 11b. max val : float
- 11c. resolution front : range integer ( 3 - 90 )
- 11d. resolution rear : range integer ( 3 - 90 )
- 12. Import front : boolean
- 13. Import range x y : boolean
- 14. CSV import path : string - path
- 15. CSV export name : string - path
```

#### <span id="page-204-0"></span>C. Example data

#### <span id="page-204-1"></span>I. Chosen Cars for Example

- Mercedes AMG GT2 (slug: ks\_mercedes\_amg\_gt2)[3 surface 3d]
- Audi R8 LMS GT3 Evo 2 (slug: ks\_audi\_r8\_lms\_gt3\_evo\_2) [3 surface 3d]
- Dallara Stradale Coupe (slug: ks\_dallara\_stradale\_coupe) [3 surface 3d]

#### <span id="page-204-2"></span>II. Example

#### <span id="page-204-3"></span>**Mercedes AMG GT2**

### 1. Drag map (file: drag\_map.surface3d)

- 1. Downforce h mm : None - 2. Downforce dh mm : None - 3. size rear : 8 - 4. size front : 8
- 5. min rear : 65.338 - 6. max rear : 160.227 - 7. min front : 65.338 - 8. max front : 160.227 - (9). Interpolation Table

| Front v /<br>Rear | 65.3  | 78.9  | 92.4  | 106.0 | 119.6 | 133.1 | 146.7 | 160.2 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 65.3              | 0.454 | 0.475 | 0.487 | 0.498 | 0.509 | 0.539 | 0.579 | 0.671 |
| 78.9              | 0.487 | 0.456 | 0.476 | 0.489 | 0.506 | 0.522 | 0.545 | 0.582 |
| 92.4              | 0.515 | 0.489 | 0.457 | 0.478 | 0.497 | 0.519 | 0.528 | 0.548 |
| 106.0             | 0.540 | 0.516 | 0.490 | 0.459 | 0.486 | 0.510 | 0.525 | 0.531 |
| 119.6             | 0.556 | 0.541 | 0.518 | 0.492 | 0.467 | 0.499 | 0.516 | 0.528 |
| 133.1             | 0.572 | 0.557 | 0.542 | 0.520 | 0.500 | 0.480 | 0.505 | 0.519 |
| 146.7             | 0.597 | 0.573 | 0.558 | 0.545 | 0.528 | 0.513 | 0.486 | 0.508 |
| 160.2             | 0.642 | 0.599 | 0.574 | 0.561 | 0.553 | 0.541 | 0.519 | 0.489 |

├ 10. interpolation done : false

├ 11. Interp Map : None

├ 12. Import front : false

├ 13. Import range x y : false

├ 14. CSV import path : None

└ 15. CSV export name : None

# *2. Front downforce ( file : front\_downforce.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

├ 3. size rear : 8 ├ 4. size front : 8 ├ 5. min rear : 20.039 ├ 6. max rear : 154.236 ├ 7. min front : 20.039 ├ 8. max front : 154.236 ├ (9). Interpolation Table

| Front v /<br>Rear | 20.0  | 39.2  | 58.4  | 77.6  | 96.7  | 115.9 | 135.1 | 154.2 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 20.0              | 0.210 | 0.273 | 0.288 | 0.282 | 0.272 | 0.260 | 0.255 | 0.255 |
| 39.2              | 0.176 | 0.211 | 0.273 | 0.288 | 0.283 | 0.272 | 0.261 | 0.256 |
| 58.4              | 0.172 | 0.177 | 0.212 | 0.275 | 0.289 | 0.284 | 0.273 | 0.262 |
| 77.6              | 0.175 | 0.175 | 0.180 | 0.215 | 0.277 | 0.292 | 0.287 | 0.276 |
| 96.7              | 0.181 | 0.175 | 0.176 | 0.181 | 0.215 | 0.278 | 0.293 | 0.287 |
| 115.9             | 0.184 | 0.174 | 0.169 | 0.169 | 0.174 | 0.209 | 0.271 | 0.286 |
| 135.1             | 0.189 | 0.180 | 0.170 | 0.164 | 0.164 | 0.169 | 0.204 | 0.266 |
| 154.2             | 0.187 | 0.187 | 0.178 | 0.168 | 0.162 | 0.163 | 0.167 | 0.202 |

├ 10. interpolation done : true

├ 11. Interp Map

│ ├ 11a. min val : -0.500 │ ├ 11b. max val : 2.000

│ ├ 11c. resolution front : 18 │ └ 11d. resolution rear : 18

├ 12. Import front : false

├ 13. Import range x y : false

├ 14. CSV import path : None

└ 15. CSV export name : None

#### *3. Rear downforce ( file : rear\_downforce.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

├ 3. size rear : 8 ├ 4. size front : 8 ├ 5. min rear : 1.732 ├ 6. max rear : 288.196 ├ 7. min front : 1.732 ├ 8. max front : 288.196 ├ (9). Interpolation Table

| Front v /<br>Rear | 1.7   | 42.7  | 83.6  | 124.5 | 165.4 | 206.3 | 247.3 | 288.2 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 1.7               | 0.444 | 0.431 | 0.453 | 0.439 | 0.440 | 0.422 | 0.384 | 0.346 |
| 42.7              | 0.445 | 0.477 | 0.452 | 0.439 | 0.440 | 0.422 | 0.384 | 0.346 |
| 83.6              | 0.443 | 0.477 | 0.499 | 0.438 | 0.440 | 0.422 | 0.384 | 0.346 |
| 124.5             | 0.443 | 0.475 | 0.499 | 0.484 | 0.439 | 0.422 | 0.384 | 0.346 |
| 165.4             | 0.443 | 0.475 | 0.497 | 0.484 | 0.485 | 0.421 | 0.384 | 0.346 |
| 206.3             | 0.443 | 0.475 | 0.497 | 0.482 | 0.486 | 0.467 | 0.383 | 0.346 |
| 247.3             | 0.443 | 0.475 | 0.497 | 0.482 | 0.484 | 0.467 | 0.429 | 0.45  |
| 288.2             | 0.443 | 0.475 | 0.497 | 0.482 | 0.484 | 0.465 | 0.430 | 0.391 |

├ 10. interpolation done : true

├ 11. Interp Map

│ ├ 11a. min val : -0.500 │ ├ 11b. max val : 2.000

│ ├ 11c. resolution front : 18 │ └ 11d. resolution rear : 18

├ 12. Import front : false

├ 13. Import range x y : false ├ 14. CSV import path : None

└ 15. CSV export name : None

#### <span id="page-206-0"></span>**Audi R8 LMS GT3 Evo 2**

# *1. CX Map ( file : cxmap.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

├ 3. size rear : 8 ├ 4. size front : 6 ├ 5. min rear : 30.000 ├ 6. max rear : 100.000 ├ 7. min front : 30.000 ├ 8. max front : 80.000 ├ (9). Interpolation Table

| Front v /<br>Rear | 30.0  | 40.0  | 50.0  | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 30.0              | 1.041 | 1.049 | 1.051 | 1.054 | 1.057 | 1.061 | 1.065 | 1.068 |

| Front v /<br>Rear | 30.0  | 40.0  | 50.0  | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 40.0              | 1.076 | 1.080 | 1.080 | 1.078 | 1.080 | 1.085 | 1.089 | 1.092 |
| 50.0              | 1.092 | 1.104 | 1.108 | 1.113 | 1.121 | 1.119 | 1.123 | 1.127 |
| 60.0              | 1.098 | 1.110 | 1.119 | 1.127 | 1.129 | 1.137 | 1.141 | 1.145 |
| 70.0              | 1.110 | 1.123 | 1.131 | 1.140 | 1.141 | 1.145 | 1.152 | 1.153 |
| 80.0              | 1.120 | 1.134 | 1.141 | 1.146 | 1.149 | 1.152 | 1.158 | 1.164 |

├ 10. interpolation done : true

├ 11. Interp Map

│ ├ 11a. min val : -0.500 │ ├ 11b. max val : 2.000 │ ├ 11c. resolution front : 18 │ └ 11d. resolution rear : 18 ├ 12. Import front : false ├ 13. Import range x y : false ├ 14. CSV import path : None └ 15. CSV export name : None

### *2. Front CZ Map ( file : frontczmap.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

├ 3. size rear : 8 ├ 4. size front : 6 ├ 5. min rear : 30.000 ├ 6. max rear : 100.000 ├ 7. min front : 30.000 ├ 8. max front : 80.000 ├ (9). Interpolation Table

| Front v /<br>Rear | 30.0  | 40.0  | 50.0  | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 30.0              | 0.913 | 1.056 | 1.197 | 1.323 | 1.428 | 1.516 | 1.581 | 1.633 |
| 40.0              | 0.784 | 0.911 | 1.022 | 1.120 | 1.215 | 1.300 | 1.384 | 1.455 |
| 50.0              | 0.616 | 0.726 | 0.836 | 0.946 | 1.051 | 1.138 | 1.214 | 1.281 |
| 60.0              | 0.415 | 0.508 | 0.618 | 0.740 | 0.854 | 0.954 | 1.035 | 1.100 |
| 70.0              | 0.214 | 0.311 | 0.415 | 0.519 | 0.621 | 0.721 | 0.816 | 0.898 |
| 80.0              | 0.011 | 0.116 | 0.223 | 0.333 | 0.431 | 0.516 | 0.605 | 0.689 |

├ 10. interpolation done : true

├ 11. Interp Map

│ ├ 11a. min val : -0.500 │ ├ 11b. max val : 2.000

│ ├ 11c. resolution front : 18

│ └ 11d. resolution rear : 18 ├ 12. Import front : false ├ 13. Import range x y : false ├ 14. CSV import path : None └ 15. CSV export name : None

# *3. Rear CZ Map ( file : rearczmap.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

├ 3. size rear : 8 ├ 4. size front : 6 ├ 5. min rear : 30.000 ├ 6. max rear : 100.000 ├ 7. min front : 30.000 ├ 8. max front : 80.000 ├ (9). Interpolation Table

| Front v /<br>Rear | 30.0  | 40.0  | 50.0  | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 30.0              | 1.927 | 2.011 | 2.026 | 1.953 | 1.905 | 1.892 | 1.859 | 1.823 |
| 40.0              | 2.085 | 2.122 | 2.125 | 2.074 | 2.015 | 1.965 | 1.917 | 1.871 |
| 50.0              | 2.267 | 2.262 | 2.240 | 2.191 | 2.124 | 2.053 | 1.992 | 1.934 |
| 60.0              | 2.428 | 2.407 | 2.365 | 2.299 | 2.227 | 2.151 | 2.080 | 2.005 |
| 70.0              | 2.542 | 2.513 | 2.464 | 2.395 | 2.316 | 2.232 | 2.156 | 2.079 |
| 80.0              | 2.633 | 2.591 | 2.539 | 2.481 | 2.401 | 2.305 | 2.217 | 2.138 |

├ 10. interpolation done : true

├ 11. Interp Map

│ ├ 11a. min val : -0.500 │ ├ 11b. max val : 2.000

│ ├ 11c. resolution front : 18 │ └ 11d. resolution rear : 18

├ 12. Import front : false

├ 13. Import range x y : false

├ 14. CSV import path : None

└ 15. CSV export name : None

### <span id="page-208-0"></span>**Dallara Stradale Coupe**

#### *1. Drag map ( file : drag\_map.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

├ 3. size rear : 7 ├ 4. size front : 4 ├ 5. min rear : 60.000 ├ 6. max rear : 120.000 ├ 7. min front : 60.000 ├ 8. max front : 120.000 ├ (9). Interpolation Table

| Front v /<br>Rear | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 | 110.0 | 120.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|
| 60.0              | 0.930 | 0.943 | 0.950 | 0.960 | 0.986 | 0.994 | 1.010 |
| 80.0              | 0.945 | 0.960 | 0.965 | 0.980 | 1.000 | 1.016 | 1.040 |
| 100.0             | 0.960 | 0.970 | 0.974 | 0.990 | 1.001 | 1.015 | 1.023 |
| 120.0             | 0.970 | 0.972 | 0.976 | 0.995 | 1.003 | 1.010 | 1.022 |

├ 10. interpolation done : false

├ 11. Interp Map : None

├ 12. Import front : false

├ 13. Import range x y : false

├ 14. CSV import path : None

└ 15. CSV export name : None

# *2. Front lift map ( file : front\_lift\_map.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

├ 3. size rear : 7 ├ 4. size front : 4 ├ 5. min rear : 60.000 ├ 6. max rear : 120.000 ├ 7. min front : 60.000 ├ 8. max front : 120.000 ├ (9). Interpolation Table

| Front v /<br>Rear | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 | 110.0 | 120.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|
| 60.0              | 0.930 | 0.943 | 0.950 | 0.960 | 0.986 | 0.994 | 1.010 |
| 80.0              | 0.945 | 0.960 | 0.965 | 0.980 | 1.000 | 1.016 | 1.040 |
| 100.0             | 0.960 | 0.970 | 0.974 | 0.990 | 1.001 | 1.015 | 1.023 |
| 120.0             | 0.970 | 0.972 | 0.976 | 0.995 | 1.003 | 1.010 | 1.022 |

├ 10. interpolation done : false

├ 11. Interp Map : None

├ 12. Import front : false

├ 13. Import range x y : false

├ 14. CSV import path : None

└ 15. CSV export name : None

#### *3. Rear lift map ( file : rear\_lift\_map.surface3d )*

├ 1. Downforce h mm : None

├ 2. Downforce dh mm : None

├ 3. size rear : 7 ├ 4. size front : 4 ├ 5. min rear : 60.000 ├ 6. max rear : 120.000 ├ 7. min front : 60.000 ├ 8. max front : 120.000 ├ (9). Interpolation Table

| Front v /<br>Rear | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 | 110.0 | 120.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|
| 60.0              | 1.619 | 1.562 | 1.482 | 1.414 | 1.402 | 1.365 | 1.396 |
| 80.0              | 1.766 | 1.751 | 1.664 | 1.575 | 1.517 | 1.474 | 1.428 |
| 100.0             | 1.716 | 1.739 | 1.754 | 2.096 | 1.645 | 1.551 | 1.534 |
| 120.0             | 1.833 | 1.837 | 1.835 | 1.754 | 1.711 | 1.613 | 1.597 |

├ 10. interpolation done : false

├ 11. Interp Map : None

├ 12. Import front : false

├ 13. Import range x y : false

├ 14. CSV import path : None

└ 15. CSV export name : None

# <span id="page-211-0"></span>**17. Suspension [ .suspension ]**

# <span id="page-211-1"></span>**A. Description**

<span id="page-211-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-211-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-211-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-211-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-211-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-211-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx

#### <span id="page-211-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

# <span id="page-211-9"></span>**B. Schema**

```
├ 1. Basic Data : object 
│ ├ 1a. Hub Mass : float
│ ├ 1b. Toe Out Linear : float
│ ├ 1c. Static Camber : float
│ └ 1d. Rim Offset : float
├ 2. D W Data : object
│ ├ 2a. Car Top Front : x, y, z float 
│ ├ 2b. Car Top Rear : x, y, z float
│ ├ 2c. Tyre Top : x, y, z float
│ ├ 2d. Car Bottom Front : x, y, z float
```

```
│ ├ 2e. Car Bottom Rear : x, y, z float
│ ├ 2f. Tyre Bottom : x, y, z float
│ ├ 2g. Car Steer : x, y, z float
│ └ 2h. Tyre Steer : x, y, z float
├ 3. Strut : object
│ ├ 3a. Car Strut : x, y, z float
│ ├ 3b. Tyre Strut : x, y, z float
│ ├ 3c. Car Bottom W B F : x, y, z float
│ ├ 3d. Car Bottom W B R : x, y, z float
│ ├ 3e. Tyre Bottom W B : x, y, z float
│ ├ 3f. Car Steer : x, y, z float
│ └ 3g. Tyre Steer : x, y, z float
├ 4. Strut Ml : object
│ ├ 4a. Car Strut : x, y, z float
│ ├ 4b. Tyre Strut : x, y, z float
│ ├ 4c. Car Bottom W B F : x, y, z float
│ ├ 4d. Car Bottom W B R : x, y, z float
│ ├ 4e. Tyre Bottom W B : x, y, z float
│ ├ 4f. Car Thrust Ball1 : x, y, z float
│ ├ 4g. Car Thrust Ball2 : x, y, z float
│ ├ 4h. Tyre Thrust Arm : x, y, z float
│ ├ 4i. Car Steer : x, y, z float
│ └ 4j. Tyre Steer : x, y, z float
├ 5. Axle : object
│ ├ 5a. Attach Relative Pos : float
│ ├ 5b. Link Count : integer
│ ├ 5c. Car Side [x] : x, y, z float | can have multiple Car Side
│ ├ 5d. Axle Side [x] : x, y, z float | can have multiple Axle Side
│ ├ 5e. Hub Mass : float 
│ ├ 5f. Leaf Spring Lat K : float
│ └ 5g. Torquereaction : float
├ 6. Multi Link Data : object
│ ├ 6a. Joint Car [x] : x, y, z float | can have multiple Joint Car
│ └ 6b. Joint Type [x] : x, y, z float | can have multiple Joint Type
├ 7. Trailing Arm Data : object
│ ├ 7a. Car Hinge Int : x, y, z float
│ ├ 7b. Car Hinge Ext : x, y, z float
│ ├ 7c. Tyre Top : x, y, z float
│ ├ 7d. Tyre Bottom : x, y, z float
│ ├ 7e. Car Steer : x, y, z float
│ ├ 7f. Tyre Steer : x, y, z float
│ └ 7g. Steer Link To Body : boolean
├ 8. Multi Link New Data : object
│ ├ 8a. Links [x] : object | can have multiple Links
│ │ ├ 8a1. Name : string
│ │ ├ 8a2. Ball Car : x, y, z float
│ │ ├ 8a3. Ball Tyre : x, y, z float
│ │ ├ 8a4. Has Coilover Attached : boolean
│ │ └ 8a5. Is Toe : boolean
│ ├ 8b. Arms [x] : object | can have multiple Arms
│ │ ├ 8b1. Name : string
│ │ ├ 8b2. Ball Car 1 : x, y, z float
│ │ ├ 8b3. Ball Car 2 : x, y, z float
│ │ ├ 8b4. Ball Tyre : x, y, z float
│ │ └ 8b5. Has Coilover Attached : boolean
│ ├ 8c. Car Coilover : x, y, z float
```

```
L 8d. Bottom Coilover: x, y, z float
- 9. Dw Coil Data: object
- 9a. Car Top Front: x, y, z float
- 9b. Car Top Rear: x, y, z float
- 9c. Tyre Top: x, y, z float
- 9d. Car Bottom Front: x, y, z float
- 9e. Car Bottom Rear: x, y, z float
- 9f. Tyre Bottom: x, y, z float
- 9g. Car Steer: x, y, z float
- 9h. Tyre Steer: x, y, z float
- 9i. Car Coilover: x, y, z float
9j. Bottom Coilover: x, y, z float
```

#### <span id="page-213-0"></span>C. Example data

#### <span id="page-213-1"></span>I. Chosen Cars for Example

- Volkswagen Golf GTI Mk1 ( slug : ks\_volkswagen\_golf\_gti\_mk1 ) [ 2 suspensions ]
- Honda S2000 AP1 (slug: ks\_honda\_s2000\_ap1) [3 suspensions]
- Porsche 992 GT3 R Rennsport ( slug : ks\_porsche\_992\_gt3\_r\_rennsport ) [ 2 suspensions ]

#### <span id="page-213-2"></span>II. Example

#### <span id="page-213-3"></span>Volkswagen Golf GTI Mk1

1. Front Suspension (file: ks\_volkswagen\_golf\_gti\_mk1\_front.suspension)

```
1. Basic Data
  - 1a. Hub Mass : 50.00000
  - 1b. Toe Out Linear : 0.00030
   1c. Static Camber: -0.30000
 L 1d. Rim Offset : 0.00000
2. D W Data : None
 3. Strut
  - 3a. Car Strut : 0.13200, 0.38800, -0.01050
  - 3b. Tyre Strut : 0.05200, -0.05000, 0.01500
  3c. Car Bottom W B F: 0.41000, -0.05700, 0.32500
  - 3d. Car Bottom W B R : 0.39000, -0.05000, -0.04000
 ├ 3e. Tyre Bottom W B : 0.05200, -0.05000, 0.01500
   3f. Car Steer: 0.39000, -0.05250, 0.06000
 3g. Tyre Steer: 0.05200, -0.05000, 0.15000
 4. Strut Ml : None
 5. Axle: None
 6. Multi Link Data: None
- 7. Trailing Arm Data : None
8. Multi Link New Data: None
- 9. Dw Coil Data : None
```

- 2. Rear Suspension (file: ks volkswagen golf gti mk1 rear.suspension)
- ├ 1. Basic Data

```
│ ├ 1a. Hub Mass : 45.00000 
│ ├ 1b. Toe Out Linear : 0.00025 
│ ├ 1c. Static Camber : -1.00000 
│ └ 1d. Rim Offset : 0.00000 
├ 2. D W Data : None 
├ 3. Strut : None 
├ 4. Strut Ml : None 
├ 5. Axle : None 
├ 6. Multi Link Data : None 
├ 7. Trailing Arm Data 
│ ├ 7a. Car Hinge Int : 1.40000, 0.00000, 0.35000 
│ ├ 7b. Car Hinge Ext : 1.30000, 0.00000, 0.40000 
│ ├ 7c. Tyre Top : 0.09622, 0.49070, -0.01650 
│ ├ 7d. Tyre Bottom : 0.04602, 0.03294, 0.00870 
│ ├ 7e. Car Steer : 0.48002, -0.07906, -010540 
│ ├ 7f. Tyre Steer : 0.04602, -0.07506, -0.04540 
│ └ 7g. Steer Link To Body : false 
├ 8. Multi Link New Data : None 
├ 9. Dw Coil Data : None 
                             Honda S2000 AP1 
1. Front Suspension ( file : ks_honda_s2000_ap1_front.suspension ) 
├ 1. Basic Data
│ ├ 1a. Hub Mass : 37.00000 
│ ├ 1b. Toe Out Linear : -0.00020 
│ ├ 1c. Static Camber : -0.40000 
│ └ 1d. Rim Offset : 0.04500 
├ 2. D W Data 
│ ├ 2a. Car Top Front : 0.34203, 0.12311, 0.08000
│ ├ 2b. Car Top Rear : 0.34302, 0.12451, -0.08000 
│ ├ 2c. Tyre Top : 0.12479, 0.10951, -0.02210 
│ ├ 2d. Car Bottom Front : 0.45520, -0.06960, -0.26000 
│ ├ 2e. Car Bottom Rear : 0.42590, -0.08110, 0.03000 
│ ├ 2f. Tyre Bottom : 0.09050, -0.13502, 0.01250 
│ ├ 2g. Car Steer : 0.45520, -0.02000, 0.05890 
│ └ 2h. Tyre Steer : 0.09480, -0.06012, 0.11691 
├ 3. Strut : None 
├ 4. Strut Ml : None 
├ 5. Axle : None 
├ 6. Multi Link Data : None 
├ 7. Trailing Arm Data : None 
├ 8. Multi Link New Data : None 
├ 9. Dw Coil Data : None 
2. Front Drift Suspension ( file : ks_honda_s2000_ap1_front_drift.suspension ) 
├ 1. Basic Data
│ ├ 1a. Hub Mass : 37.00000 
│ ├ 1b. Toe Out Linear : -0.00020 
│ ├ 1c. Static Camber : -0.40000 
│ └ 1d. Rim Offset : 0.04500
```

├ 2. D W Data

```
│ ├ 2a. Car Top Front : 0.34302, 0.08311, 0.08000
│ ├ 2b. Car Top Rear : 0.34302, 0.08451, -0.08000 
│ ├ 2c. Tyre Top : 0.11479, 0.10951, -0.02210 
│ ├ 2d. Car Bottom Front : 0.45520, -0.06960, -0.26000 
│ ├ 2e. Car Bottom Rear : 0.42590, -0.08110, 0.03000 
│ ├ 2f. Tyre Bottom : 0.08050, -0.10502, 0.01250 
│ ├ 2g. Car Steer : 0.45520, -0.05000, 0.05890 
│ └ 2h. Tyre Steer : 0.09480, -0.06012, 0.11691 
├ 3. Strut : None 
├ 4. Strut Ml : None 
├ 5. Axle : None 
├ 6. Multi Link Data : None 
├ 7. Trailing Arm Data : None 
├ 8. Multi Link New Data : None 
├ 9. Dw Coil Data : None 
3. Rear Suspension ( file : ks_honda_s2000_ap1_front_drift.suspension ) 
├ 1. Basic Data
│ ├ 1a. Hub Mass : 44.50000 
│ ├ 1b. Toe Out Linear : -0.00030 
│ ├ 1c. Static Camber : -1.60000 
│ └ 1d. Rim Offset : 0.03700 
├ 2. D W Data 
│ ├ 2a. Car Top Front : 0.39022, 0.08701, 0.04129
│ ├ 2b. Car Top Rear : 0.42022, 0.09469, -0.24111 
│ ├ 2c. Tyre Top : 0.11000, 0.11220, 0.00000 
│ ├ 2d. Car Bottom Front : 0.44100, -0.07010, 0.22113 
│ ├ 2e. Car Bottom Rear : 0.44042, -0.08989, -0.10935 
│ ├ 2f. Tyre Bottom : 0.09130, -0.10511, -0.01000 
│ ├ 2g. Car Steer : 0.38990, -0.04540, 0.16020 
│ └ 2h. Tyre Steer : 0.09130, -0.05342, 0.14988 
├ 3. Strut : None 
├ 4. Strut Ml : None 
├ 5. Axle : None 
├ 6. Multi Link Data : None 
├ 7. Trailing Arm Data : None 
├ 8. Multi Link New Data : None 
├ 9. Dw Coil Data : None 
                        Porsche 992 GT3 R Rennport 
1. Front Suspension ( file : ks_porsche_992_gt3_r_rennsport_front.suspension ) 
├ 1. Basic Data
│ ├ 1a. Hub Mass : 51.00000 
│ ├ 1b. Toe Out Linear : 0.00044 
│ ├ 1c. Static Camber : -5.70000 
│ └ 1d. Rim Offset : 0.00000 
├ 2. D W Data : None 
├ 3. Strut : None
```

<span id="page-215-0"></span>├ 4. Strut Ml : None ├ 5. Axle : None

├ 6. Multi Link Data : None

```
├ 7. Trailing Arm Data : None 
├ 8. Multi Link New Data : None 
├ 9. Dw Coil Data 
│ ├ 9a. Car Top Front : 0.36128, 0.06671, 0.10834 
│ ├ 9b. Car Top Rear : 0.36128, 0.03131, -0.14089 
│ ├ 9c. Tyre Top : 0.08582, 0.10517, -0.01868 
│ ├ 9d. Car Bottom Front : 0.45261, -0.15879, 0.21226 
│ ├ 9e. Car Bottom Rear : 0.45095, -0.14676, -0.08504 
│ ├ 9f. Tyre Bottom : 0.03941, -0.11288, 0.01898 
│ ├ 9g. Car Steer : 0.49910, -0.11521, 0.13421 
│ ├ 9h. Tyre Steer : 0.03338, -0.06370, 0.13886 
│ ├ 9i. Car Coilover : 0.40708, 0.21593, -0.04583 
└ └ 9j. Bottom Coilover : 0.10508, -0.11831, 0.00237 
2. Rear Suspension ( file : ks_porsche_992_gt3_r_rennsport_rear.suspension ) 
├ 1. Basic Data
│ ├ 1a. Hub Mass : 46.00000 
│ ├ 1b. Toe Out Linear : -0.00110 
│ ├ 1c. Static Camber : -4.40000 
│ └ 1d. Rim Offset : 0.00000 
├ 2. D W Data : None 
├ 3. Strut : None 
├ 4. Strut Ml : None 
├ 5. Axle : None 
├ 6. Multi Link Data : None 
├ 7. Trailing Arm Data : None 
├ 8. Multi Link New Data 
│ ├ 8a. Links 1 
│ │ ├ 8a1. Name : None 
│ │ ├ 8a2. Ball Car : 0.45733, -0.21779, -0.03274 
│ │ ├ 8a3. Ball Tyre : 0.05940, -0.15917, -0.05147 
│ │ ├ 8a4. Has Coilover Attached : true 
│ │ └ 8a5. Is Toe : false 
│ ├ 8a. Links 2 
│ │ ├ 8a1. Name : None 
│ │ ├ 8a2. Ball Car : 0.33837, -0.13867, 0.26058 
│ │ ├ 8a3. Ball Tyre : 0.07196, -0.16195, 0.00295 
│ │ ├ 8a4. Has Coilover Attached : false 
│ │ └ 8a5. Is Toe : false 
│ ├ 8a. Links 3 
│ │ ├ 8a1. Name : None 
│ │ ├ 8a2. Ball Car : 0.29399, -0.00924, 0.18603 
│ │ ├ 8a3. Ball Tyre : 0.08416, 0.09013, 0.15594 
│ │ ├ 8a4. Has Coilover Attached : false 
│ │ └ 8a5. Is Toe : false 
│ ├ 8a. Links 4 
│ │ ├ 8a1. Name : None 
│ │ ├ 8a2. Ball Car : 0.31754, 0.04240, 0.18574 
│ │ ├ 8a3. Ball Tyre : 0.06361, 0.16582, -0.00746 
│ │ ├ 8a4. Has Coilover Attached : false 
│ │ └ 8a5. Is Toe : false 
│ ├ 8a. Links 5 
│ │ ├ 8a1. Name : steer
```

│ │ ├ 8a2. Ball Car : 0.32123, -0.00156, -0.12150

```
│ │ ├ 8a3. Ball Tyre : 0.05699, 0.10790, -0.12715 
│ │ ├ 8a4. Has Coilover Attached : false 
│ │ └ 8a5. Is Toe : true 
│ ├ 8b. Arms : None 
│ ├ 8c. Car Coilover : 0.32123, -0.00156, -0.12150 
│ └ 8d. Bottom Coilover : 0.05699, 0.10790, -0.12715 
├ 9. Dw Coil Data : None
```

# <span id="page-218-0"></span>**18. Turbo [ .turbo ]**

#### <span id="page-218-1"></span>**A. Description**

<span id="page-218-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-218-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-218-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-218-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-218-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-218-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx

#### <span id="page-218-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

# <span id="page-218-9"></span>**B. Schema**

```
├ 1. Max Boost : float
├ 2. Lag U P : float
├ 3. Lag D N : float
├ 4. Rpm Ref : float
├ 5. Gamma Rpm : float
├ 6. Gamma Gas : float
├ 7. Watergate : float
├ 8. Is Adjustable : boolean
├ 9. CarData : string - path
└ 10. Turbo no : integer
```

#### <span id="page-219-0"></span>C. Example data

#### <span id="page-219-1"></span>I. Chosen Cars for Example

- Peugeot 205 T16 (slug: ks\_peugeot\_205\_t16) [2 turbos]
- Chevrolet Camaro ZL1 ( slug : ks\_chevrolet\_camaro\_zl1 ) [ compressor ]
- Toyota Supra MKIV (slug: ks toyota supra mkiv) [2 turbos / 2 types]

#### <span id="page-219-2"></span>II. Example

#### <span id="page-219-3"></span>Peugeot 205 T16

#### 1. Turbo 0 (file: ks\_peugeot\_205\_t15.turbo)

```
- 1. Max Boost : 0.70000

- 2. Lag U P : 0.99500

- 3. Lag D N : 0.99000

- 4. Rpm Ref : 2300.00000

- 5. Gamma Rpm : 2.50000

- 6. Gamma Gas : 2.50000

- 7. Watergate : 0.70000

- 8. Is Adjustable : false

- 9. CarData : None

10. Turbo no : 0
```

### 2. Turbo 1 (file: ks\_peugeot\_205\_t15\_turbo0.turbo)

```
- 1. Max Boost : 1.20000

- 2. Lag U P : 0.99500

- 3. Lag D N : 0.99000

- 4. Rpm Ref : 4100.00000

- 5. Gamma Rpm : 2.50000

- 6. Gamma Gas : 2.50000

- 7. Watergate : 1.20000

- 8. Is Adjustable : false

- 9. CarData : None

10. Turbo no : 0
```

#### <span id="page-219-4"></span>**Chevrolet Camaro ZL1**

```
- 1. Max Boost : 1.00000

- 2. Lag U P : 0.00000

- 3. Lag D N : 0.00000

- 4. Rpm Ref : 6000.00000

- 5. Gamma Rpm : 1.00000

- 6. Gamma Gas : 0.00000

- 7. Watergate : 0.90000

- 8. Is Adjustable : false

- 9. CarData : None

- 10. Turbo no : 0
```

#### <span id="page-220-0"></span>**Toyota Supra MKIV**

# *1. Turbo 0 ( file : ks\_toyota\_supra\_mkiv0.turbo )* ├ 1. Max Boost : 0.00000 ├ 2. Lag U P : 0.99500 ├ 3. Lag D N : 0.99000 ├ 4. Rpm Ref : 3500.00000 ├ 5. Gamma Rpm : 0.50000 ├ 6. Gamma Gas : 0.50000 ├ 7. Watergate : 0.00000 ├ 8. Is Adjustable : false ├ 9. CarData : None └ 10. Turbo no : 0 *2. Turbo 1 ( file : ks\_toyota\_supra\_mkiv1.turbo )* ├ 1. Max Boost : 0.00000 ├ 2. Lag U P : 0.99100 ├ 3. Lag D N : 0.98800 ├ 4. Rpm Ref : 4000.00000 ├ 5. Gamma Rpm : 0.50000 ├ 6. Gamma Gas : 0.50000 ├ 7. Watergate : 0.00000 ├ 8. Is Adjustable : false ├ 9. CarData : None └ 10. Turbo no : 0 *3. Drift Turbo 0 ( file : ks\_toyota\_supra\_mkiv\_drift0.turbo )* ├ 1. Max Boost : 0.30000 ├ 2. Lag U P : 0.99750 ├ 3. Lag D N : 0.98800 ├ 4. Rpm Ref : 3200.00000 ├ 5. Gamma Rpm : 1.00000 ├ 6. Gamma Gas : 1.00000 ├ 7. Watergate : 0.30000 ├ 8. Is Adjustable : true ├ 9. CarData : None └ 10. Turbo no : 0 *4. Drift Turbo 1 ( file : ks\_toyota\_supra\_mkiv\_drift1.turbo )* ├ 1. Max Boost : 2.00000 ├ 2. Lag U P : 0.99650 ├ 3. Lag D N : 0.99700 ├ 4. Rpm Ref : 4400.00000 ├ 5. Gamma Rpm : 3.00000 ├ 6. Gamma Gas : 1.00000 ├ 7. Watergate : 1.50000 ├ 8. Is Adjustable : true

├ 9. CarData : None └ 10. Turbo no : 0

# <span id="page-221-0"></span>**19. Tyre [ .tyre ]**

# <span id="page-221-1"></span>**A. Description**

<span id="page-221-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-221-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-221-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-221-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-221-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-221-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx
- <span id="page-221-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

# <span id="page-221-9"></span>**B. Schema**

```
├ 1. Name : string
├ 2. Short Name : string
├ 3. Tyre Compound : enum
├ 4. Tyre Data : object
│ ├ 4a. Width : float
│ ├ 4b. Radius : float
│ ├ 4c. Rate : float
│ ├ 4d. Progressive Rate : float
│ ├ 4e. Damping : float
```

```
│ ├ 4f. Angular Inertia : float
│ ├ 4g. Rim Radius : float
│ ├ 4h. Radius Raise K : float
│ ├ 4i. Tread Height M M : float
│ ├ 4j. Tread Consumption K : float
│ ├ 4k. Mass : float
│ ├ 4l. Lateral Flex K : float
│ ├ 4m. Lateral Flex C : float
│ ├ 4n. Longitudinal Flex K : float
│ ├ 4o. Longitudinal Flex C : float
│ ├ 4p. Explosion Temperature : float
│ ├ 4q. Blanket Temperature : float
│ ├ 4r. Flat Spot K : float
│ ├ 4s. Normal To Flex Ratio : float
│ ├ 4t. Contact Camber : float
│ ├ 4u. Contact Flex : float
│ ├ 4v. Contact Vertical Flex : float
│ ├ 4w. Damping Mode : enum
│ ├ 4x. Maxwell Damping Peak Frequency : float
│ ├ 4y. Maxwell Stiffening Percent : float
│ ├ 4z. Damping Threshold Speed Ms : float
│ ├ 4aa. Speed Damping Factor : float
│ └ 4ab. Deflection Damping Factor : float
├ 5. Model Data : object
│ ├ 5a. Dy0 : float
│ ├ 5b. Dx0 : float
│ ├ 5c. Ls Exp Y : float
│ ├ 5d. Ls Exp X : float
│ ├ 5e. Fz0 : float
│ ├ 5f. Friction Limit Angle : float
│ ├ 5g. Flex Gain : float
│ ├ 5h. Cf Xmult : float
│ ├ 5i. Brake D X Mod : float
│ ├ 5j. Combined Factor : float
│ ├ 5k. Grip Slip Factor : float
│ ├ 5l. Wear Curve : string - path
│ ├ 5m. Grain Factor : float
│ ├ 5n. Contact Wear I M O : float
│ ├ 5o. Relaxation Length Y : float
│ ├ 5p. Relaxation Length X : float
│ ├ 5q. Mz Tweak Mult : float
│ ├ 5r. Mz Scale : float
│ ├ 5s. Mz Trail Nd Slip Reduction : float
│ ├ 5t. Mz Trail Remap : float
│ └ 5u. Brush Exponent : float
├ 6. Thermal Data : object
│ ├ 6a. Vertical Spring : float
│ ├ 6b. Vertical Damp K : float
│ ├ 6c. Wear Mult : float
│ ├ 6d. Density : float
│ ├ 6e. Specific Heat : float
│ ├ 6f. Surface Core Mass Ratio : float
│ ├ 6g. Cool Factor Rain : float
│ ├ 6h. Cool Factor : float
│ ├ 6i. Heat Partition Coeff : float
│ ├ 6j. Road Conduction : float
```

```
│ ├ 6k. Thermal Conductivity : float
│ ├ 6l. Rolling Factor : float
│ ├ 6m. Grain Gain : float
│ ├ 6n. Grain Gamma : float
│ ├ 6o. Grain Slip Angle Gain : float
│ ├ 6p. Grain Slip Angle Gamma : float
│ ├ 6q. Grain Slip Angle Threshold : float
│ ├ 6r. Blister Gain : float
│ ├ 6s. Blister Gamma : float
│ ├ 6t. Practical Temp Source : float
│ ├ 6u. Brake Transfer Factor : float
│ ├ 6v. Thermal Performance Curve : string - path
│ ├ 6w. Contact I M O : float
│ ├ 6x. Tref Friction Limit Angle : float
│ └ 6y. Friction Limit Angle T Sensitivity : float
├ 7. Pressure Data : object
│ ├ 7a. Pressure Flex Gain : float
│ ├ 7b. Rolling Resistance Gain : float
│ ├ 7c. Rolling Heat Gain : float
│ ├ 7d. Gain D : float
│ ├ 7e. Ideal Pressure : float
│ ├ 7f. Pressure Reference : float
│ ├ 7g. Pressure Spring Curve : string - path
│ ├ 7h. Pressure Spring Gain : float
│ ├ 7i. Curb Pressure Loss Must : float
│ └ 7j. Curb Pressure Loss Threshold : float
├ 8. Camber Data : object
│ ├ 8a. Camber Gain : float
│ ├ 8b. Camber Vertical K Range Deg : float
│ ├ 8c. Camber Vertical K Gain : float
│ ├ 8d. Dcamber0 : float
│ └ 8e. Dcamber1 : float
├ 9. Speed Sensitivity : object
│ ├ 9a. Mu0 T : float
│ ├ 9b. Ref Speed : float
│ ├ 9c. Mu Speed Sensitivity : float
│ ├ 9d. Mu T Sensitivity : float
│ ├ 9e. Tref Mu T : float
│ ├ 9f. Mu0 T X : float
│ ├ 9g. Ref Speed X : float
│ ├ 9h. Mu Speed Sensitivity X : float
│ ├ 9i. Mu T Sensitivity X : float
│ └ 9j. Tref Mu T X : float
├ 10. Rolling Resistance : object
│ ├ 10a. Rr0 : float
│ ├ 10b. Rr1 : float
│ ├ 10c. Rr Slip : float
│ └ 10d. Rr Wear Mult : float
├ 11. Groove Data : object
│ ├ 11a. Groove Factor : float
│ ├ 11b. Groove S A Factor : float
│ └ 11c. Groove S R Factor : float
├ 12. Pressure : float
├ 13. Init Data : object
│ ├ 13a. Width : float
│ ├ 13b. Aspect Ratio : float
```

- 13c. Diameter : float - 13d. Load Index : float - 13e. Pressure : float

#### **Enum - Car Tyre**

| 3  | Tyre Compound | Eco, Road, SuperCar, HyperCar, Slick_Medium, Wet, Racing_Vintage, F1_Soft, F1_Medium, F1_Hard, F1_Wet, F1_Intermediate |
|----|---------------|------------------------------------------------------------------------------------------------------------------------|
| 4w | Damping Mode  | Simple, hystereticMaxwell, hystereticNando                                                                             |

#### <span id="page-224-0"></span>C. Example data

#### <span id="page-224-1"></span>I. Chosen Tyres for Example

- Eco (slug: eco\_165\_60\_12)

- Vintage (slug: vintage\_195\_60\_15)

- F1 2025 Wet (slug: f12025\_wet\_305\_720\_18)

#### <span id="page-224-2"></span>II. Example

<span id="page-224-3"></span>Eco | Size : 165 - 60 - 12

1. Name: Eco (E) 2. Short Name : E 3. Tyre Compound : Eco 4. Tyre Data - 4a. Width : 0.16500 4b. Radius: 0.25140 4c. Rate: 306900.00000 4d. Progressive Rate: 0.00000 4e. Damping: 549.08398 4f. Angular Inertia: 0.91034 4g. Rim Radius : 0.15240 4h. Radius Raise K: 0.00100 4i. Tread Height M M : 8.00000 4j. Tread Consumption K: 6.00000 4k. Mass: 6.00000 41. Lateral Flex K : 28000.00000 4m. Lateral Flex C : 2.00000 4n. Longitudinal Flex K: 18000.00000 4o. Longitudinal Flex C: 2.50000 4p. Explosion Temperature: 450.00000 4q. Blanket Temperature: 40.00000 4r. Flat Spot K : 0.10000 4s. Normal To Flex Ratio: 0.00000 4t. Contact Camber: 2.79367 4u. Contact Flex: 0.02293 4v. Contact Vertical Flex: 3.58828 4w. Damping Mode: hystereticNando

```
│ ├ 4x. Maxwell Damping Peak Frequency : 0.00000 
│ ├ 4y. Maxwell Stiffening Percent : 0.00000 
│ ├ 4z. Damping Threshold Speed Ms : 1.00000 
│ ├ 4aa. Speed Damping Factor : 0.50000 
│ └ 4ab. Deflection Damping Factor : 3.00000 
├ 5. Model Data 
│ ├ 5a. Dy0 : 0.96160 
│ ├ 5b. Dx0 : 1.00483 
│ ├ 5c. Ls Exp Y : 0.82088 
│ ├ 5d. Ls Exp X : 1.07088 
│ ├ 5e. Fz0 : 4170.00000 
│ ├ 5f. Friction Limit Angle : 8.56818 
│ ├ 5g. Flex Gain : 0.02070 
│ ├ 5h. Cf Xmult : 2.00000 
│ ├ 5i. Brake D X Mod : 0.05000 
│ ├ 5j. Combined Factor : 1.90000 
│ ├ 5k. Grip Slip Factor : 0.78000 
│ ├ 5l. Wear Curve : content\cars\common_phsx\tyres\eco\wear_eco.curve 
│ ├ 5m. Grain Factor : 0.00100 
│ ├ 5n. Contact Wear I M O : 4.00000 
│ ├ 5o. Relaxation Length Y : 0.10051 
│ ├ 5p. Relaxation Length X : 0.10051 
│ ├ 5q. Mz Tweak Mult : 0.60000 
│ ├ 5r. Mz Scale : 0.12000 
│ ├ 5s. Mz Trail Nd Slip Reduction : 0.50000 
│ ├ 5t. Mz Trail Remap : 0.20000 
│ └ 5u. Brush Exponent : 3.00000 
├ 6. Thermal Data 
│ ├ 6a. Vertical Spring : 40.00000 
│ ├ 6b. Vertical Damp K : 2.00000 
│ ├ 6c. Wear Mult : 0.20000 
│ ├ 6d. Density : 1100.00000 
│ ├ 6e. Specific Heat : 1600.00000 
│ ├ 6f. Surface Core Mass Ratio : 0.15000 
│ ├ 6g. Cool Factor Rain : 3.00000 
│ ├ 6h. Cool Factor : 1.40000 
│ ├ 6i. Heat Partition Coeff : 0.50000 
│ ├ 6j. Road Conduction : 1000.00000 
│ ├ 6k. Thermal Conductivity : 0.20000 
│ ├ 6l. Rolling Factor : 0.60000 
│ ├ 6m. Grain Gain : 0.01700 
│ ├ 6n. Grain Gamma : 0.01700 
│ ├ 6o. Grain Slip Angle Gain : 0.16500 
│ ├ 6p. Grain Slip Angle Gamma : 0.24500 
│ ├ 6q. Grain Slip Angle Threshold : 11.26818 
│ ├ 6r. Blister Gain : 0.00000 
│ ├ 6s. Blister Gamma : 0.00000 
│ ├ 6t. Practical Temp Source : 0.80000 
│ ├ 6u. Brake Transfer Factor : 0.00070 
│ ├ 6v. Thermal Performance Curve : 
content\cars\common_phsx\tyres\eco\tcurve_eco.curve 
│ ├ 6w. Contact I M O : 1.60000 
│ ├ 6x. Tref Friction Limit Angle : 75.00000 
│ └ 6y. Friction Limit Angle T Sensitivity : 0.06000 
├ 7. Pressure Data 
│ ├ 7a. Pressure Flex Gain : 0.25000
```

```
│ ├ 7b. Rolling Resistance Gain : 1.20000 
│ ├ 7c. Rolling Heat Gain : 0.10000 
│ ├ 7d. Gain D : 0.00260 
│ ├ 7e. Ideal Pressure : 31.00000 
│ ├ 7f. Pressure Reference : 30.00000 
│ ├ 7g. Pressure Spring Curve : None
│ ├ 7h. Pressure Spring Gain : 10890.00000 
│ ├ 7i. Curb Pressure Loss Must : 1.00000 
│ └ 7j. Curb Pressure Loss Threshold : 10.00000 
├ 8. Camber Data 
│ ├ 8a. Camber Gain : 0.20000 
│ ├ 8b. Camber Vertical K Range Deg : 5.00000 
│ ├ 8c. Camber Vertical K Gain : -0.10000 
│ ├ 8d. Dcamber0 : 0.60000 
│ └ 8e. Dcamber1 : -11.00000 
├ 9. Speed Sensitivity 
│ ├ 9a. Mu0 T : 0.78000 
│ ├ 9b. Ref Speed : 4.50000 
│ ├ 9c. Mu Speed Sensitivity : 0.78000 
│ ├ 9d. Mu T Sensitivity : 0.02500 
│ ├ 9e. Tref Mu T : 70.00000 
│ ├ 9f. Mu0 T X : 0.70000 
│ ├ 9g. Ref Speed X : 3.50000 
│ ├ 9h. Mu Speed Sensitivity X : 0.62000 
│ ├ 9i. Mu T Sensitivity X : 0.09500 
│ └ 9j. Tref Mu T X : 70.00000 
├ 10. Rolling Resistance 
│ ├ 10a. Rr0 : 17.79780 
│ ├ 10b. Rr1 : 0.00200 
│ ├ 10c. Rr Slip : 646.00000 
│ └ 10d. Rr Wear Mult : 0.14000 
├ 11. Groove Data 
│ ├ 11a. Groove Factor : 0.49000 
│ ├ 11b. Groove S A Factor : 0.45000 
│ └ 11c. Groove S R Factor : 0.45000 
├ 12. Pressure : 30.00000 
├ 13. Init Data 
│ ├ 13a. Width : 165.00000 
│ ├ 13b. Aspect Ratio : 60.00000 
│ ├ 13c. Diameter : 12.00000 
│ ├ 13d. Load Index : 99.00000 
└ └ 13e. Pressure : 30.00000
```

#### <span id="page-226-0"></span>**Vintage | Size : 195 - 60 - 15**

├ 1. Name : Racing Vintage (RV) ├ 2. Short Name : RV ├ 3. Tyre Compound : Racing\_Vintage ├ 4. Tyre Data │ ├ 4a. Width : 0.19500 │ ├ 4b. Radius : 0.30750 │ ├ 4c. Rate : 272800.00000 │ ├ 4d. Progressive Rate : 0.00000

```
│ ├ 4e. Damping : 488.07468 
│ ├ 4f. Angular Inertia : 2.26550 
│ ├ 4g. Rim Radius : 0.19050 
│ ├ 4h. Radius Raise K : 0.00100 
│ ├ 4i. Tread Height M M : 8.00000 
│ ├ 4j. Tread Consumption K : 6.00000 
│ ├ 4k. Mass : 6.00000 
│ ├ 4l. Lateral Flex K : -10000.00000 
│ ├ 4m. Lateral Flex C : 2.00000 
│ ├ 4n. Longitudinal Flex K : -1800.00000 
│ ├ 4o. Longitudinal Flex C : 2.00000 
│ ├ 4p. Explosion Temperature : 450.00000 
│ ├ 4q. Blanket Temperature : 40.00000 
│ ├ 4r. Flat Spot K : 0.10000 
│ ├ 4s. Normal To Flex Ratio : 0.00000 
│ ├ 4t. Contact Camber : 9.33809 
│ ├ 4u. Contact Flex : 0.16605 
│ ├ 4v. Contact Vertical Flex : 14.45922 
│ ├ 4w. Damping Mode : hystereticNando 
│ ├ 4x. Maxwell Damping Peak Frequency : 0.00000 
│ ├ 4y. Maxwell Stiffening Percent : 0.00000 
│ ├ 4z. Damping Threshold Speed Ms : 1.00000 
│ ├ 4aa. Speed Damping Factor : 0.50000 
│ └ 4ab. Deflection Damping Factor : 3.00000 
├ 5. Model Data 
│ ├ 5a. Dy0 : 1.10844 
│ ├ 5b. Dx0 : 1.14557 
│ ├ 5c. Ls Exp Y : 0.85581 
│ ├ 5d. Ls Exp X : 0.88381 
│ ├ 5e. Fz0 : 3840.00000 
│ ├ 5f. Friction Limit Angle : 8.30538 
│ ├ 5g. Flex Gain : 0.02070 
│ ├ 5h. Cf Xmult : 2.00000 
│ ├ 5i. Brake D X Mod : 0.05000 
│ ├ 5j. Combined Factor : 1.80000 
│ ├ 5k. Grip Slip Factor : 0.76000 
│ ├ 5l. Wear Curve : 
content\cars\common_phsx\tyres\vintage\wear_vintage_racing.curve 
│ ├ 5m. Grain Factor : 0.00100 
│ ├ 5n. Contact Wear I M O : 4.00000 
│ ├ 5o. Relaxation Length Y : 0.10051 
│ ├ 5p. Relaxation Length X : 0.10051 
│ ├ 5q. Mz Tweak Mult : 0.60000 
│ ├ 5r. Mz Scale : 0.12000 
│ ├ 5s. Mz Trail Nd Slip Reduction : 0.50000 
│ ├ 5t. Mz Trail Remap : 0.20000 
│ └ 5u. Brush Exponent : 3.00000 
├ 6. Thermal Data 
│ ├ 6a. Vertical Spring : 40.00000 
│ ├ 6b. Vertical Damp K : 2.00000 
│ ├ 6c. Wear Mult : 0.20000 
│ ├ 6d. Density : 1100.00000 
│ ├ 6e. Specific Heat : 1600.00000 
│ ├ 6f. Surface Core Mass Ratio : 0.15000 
│ ├ 6g. Cool Factor Rain : 3.00000 
│ ├ 6h. Cool Factor : 0.70000
```

```
│ ├ 6i. Heat Partition Coeff : 0.70000 
│ ├ 6j. Road Conduction : 1000.00000 
│ ├ 6k. Thermal Conductivity : 0.28000 
│ ├ 6l. Rolling Factor : 1.00000 
│ ├ 6m. Grain Gain : 0.27000 
│ ├ 6n. Grain Gamma : 0.27000 
│ ├ 6o. Grain Slip Angle Gain : 0.26500 
│ ├ 6p. Grain Slip Angle Gamma : 0.34500 
│ ├ 6q. Grain Slip Angle Threshold : 11.00538 
│ ├ 6r. Blister Gain : 0.00000 
│ ├ 6s. Blister Gamma : 0.00000 
│ ├ 6t. Practical Temp Source : 0.80000 
│ ├ 6u. Brake Transfer Factor : 0.00070 
│ ├ 6v. Thermal Performance Curve : 
content\cars\common_phsx\tyres\vintage\tcurve_vintage_racing.curve 
│ ├ 6w. Contact I M O : 1.60000 
│ ├ 6x. Tref Friction Limit Angle : 75.00000 
│ └ 6y. Friction Limit Angle T Sensitivity : 0.06000 
├ 7. Pressure Data 
│ ├ 7a. Pressure Flex Gain : 0.25000 
│ ├ 7b. Rolling Resistance Gain : 1.20000 
│ ├ 7c. Rolling Heat Gain : 0.10000 
│ ├ 7d. Gain D : 0.00250 
│ ├ 7e. Ideal Pressure : 31.00000 
│ ├ 7f. Pressure Reference : 28.00000 
│ ├ 7g. Pressure Spring Curve : None 
│ ├ 7h. Pressure Spring Gain : 9860.00000 
│ ├ 7i. Curb Pressure Loss Must : 1.00000 
│ └ 7j. Curb Pressure Loss Threshold : 10.00000 
├ 8. Camber Data 
│ ├ 8a. Camber Gain : 0.20000 
│ ├ 8b. Camber Vertical K Range Deg : 5.00000 
│ ├ 8c. Camber Vertical K Gain : -0.10000 
│ ├ 8d. Dcamber0 : 0.60000 
│ └ 8e. Dcamber1 : -11.00000 
├ 9. Speed Sensitivity 
│ ├ 9a. Mu0 T : 0.78000 
│ ├ 9b. Ref Speed : 4.50000 
│ ├ 9c. Mu Speed Sensitivity : 0.78000 
│ ├ 9d. Mu T Sensitivity : 0.02500 
│ ├ 9e. Tref Mu T : 70.00000 
│ ├ 9f. Mu0 T X : 0.80000 
│ ├ 9g. Ref Speed X : 2.00000 
│ ├ 9h. Mu Speed Sensitivity X : 0.82000 
│ ├ 9i. Mu T Sensitivity X : 0.08500 
│ └ 9j. Tref Mu T X : 70.00000 
├ 10. Rolling Resistance 
│ ├ 10a. Rr0 : 18.36000 
│ ├ 10b. Rr1 : 0.00200 
│ ├ 10c. Rr Slip : 646.00000 
│ └ 10d. Rr Wear Mult : 0.14000 
├ 11. Groove Data 
│ ├ 11a. Groove Factor : 0.49000 
│ ├ 11b. Groove S A Factor : 0.45000 
│ └ 11c. Groove S R Factor : 0.45000 
├ 12. Pressure : 28.00000
```

```
├ 13. Init Data 
│ ├ 13a. Width : 195.00000 
│ ├ 13b. Aspect Ratio : 60.00000 
│ ├ 13c. Diameter : 15.00000 
│ ├ 13d. Load Index : 88.00000 
└ └ 13e. Pressure : 28.00000 
                     F1 2025 [ Wet ] | Size : 305 - 720 - 18 
├ 1. Name : Wet (W) 
├ 2. Short Name : W 
├ 3. Tyre Compound : F1_Wet 
├ 4. Tyre Data 
│ ├ 4a. Width : 0.30500 
│ ├ 4b. Radius : 0.35975 
│ ├ 4c. Rate : 262600.00000 
│ ├ 4d. Progressive Rate : 0.00000 
│ ├ 4e. Damping : 845.68597 
│ ├ 4f. Angular Inertia : 4.66531 
│ ├ 4g. Rim Radius : 0.22860 
│ ├ 4h. Radius Raise K : 0.00100 
│ ├ 4i. Tread Height M M : 3.00000 
│ ├ 4j. Tread Consumption K : 6.00000 
│ ├ 4k. Mass : 6.00000 
│ ├ 4l. Lateral Flex K : 30000.00000 
│ ├ 4m. Lateral Flex C : 2.00000 
│ ├ 4n. Longitudinal Flex K : 20000.00000 
│ ├ 4o. Longitudinal Flex C : 2.50000 
│ ├ 4p. Explosion Temperature : 450.00000 
│ ├ 4q. Blanket Temperature : 40.00000 
│ ├ 4r. Flat Spot K : 0.10000 
│ ├ 4s. Normal To Flex Ratio : 0.00000 
│ ├ 4t. Contact Camber : 10.98116 
│ ├ 4u. Contact Flex : 0.34464 
│ ├ 4v. Contact Vertical Flex : 16.61791 
│ ├ 4w. Damping Mode : hystereticNando 
│ ├ 4x. Maxwell Damping Peak Frequency : 0.00000 
│ ├ 4y. Maxwell Stiffening Percent : 0.00000 
│ ├ 4z. Damping Threshold Speed Ms : 1.00000 
│ ├ 4aa. Speed Damping Factor : 0.500000 
│ └ 4ab. Deflection Damping Factor : 3.00000 
├ 5. Model Data 
│ ├ 5a. Dy0 : 1.46825 
│ ├ 5b. Dx0 : 1.56499 
│ ├ 5c. Ls Exp Y : 0.86528 
│ ├ 5d. Ls Exp X : 0.83328 
│ ├ 5e. Fz0 : 4230.00000 
│ ├ 5f. Friction Limit Angle : 7.81311 
│ ├ 5g. Flex Gain : 0.02070 
│ ├ 5h. Cf Xmult : 1.80000 
│ ├ 5i. Brake D X Mod : 0.00000 
│ ├ 5j. Combined Factor : 2.00000 
│ ├ 5k. Grip Slip Factor : 0.82000
```

```
│ ├ 5l. Wear Curve : 
content\cars\common_phsx\tyres\f1_2025\wear_f12025_wet.curve 
│ ├ 5m. Grain Factor : 0.00100 
│ ├ 5n. Contact Wear I M O : 4.00000 
│ ├ 5o. Relaxation Length Y : 0.10051 
│ ├ 5p. Relaxation Length X : 0.10051 
│ ├ 5q. Mz Tweak Mult : 0.60000 
│ ├ 5r. Mz Scale : 0.12000 
│ ├ 5s. Mz Trail Nd Slip Reduction : 0.50000 
│ ├ 5t. Mz Trail Remap : 0.20000 
│ └ 5u. Brush Exponent : 3.00000 
├ 6. Thermal Data 
│ ├ 6a. Vertical Spring : 40.00000 
│ ├ 6b. Vertical Damp K : 2.00000 
│ ├ 6c. Wear Mult : 0.20000 
│ ├ 6d. Density : 1100.00000 
│ ├ 6e. Specific Heat : 1600.00000 
│ ├ 6f. Surface Core Mass Ratio : 0.15000 
│ ├ 6g. Cool Factor Rain : 3.00000 
│ ├ 6h. Cool Factor : 0.90000 
│ ├ 6i. Heat Partition Coeff : 1.40000 
│ ├ 6j. Road Conduction : 1000.00000 
│ ├ 6k. Thermal Conductivity : 0.35000 
│ ├ 6l. Rolling Factor : 1.60000 
│ ├ 6m. Grain Gain : 0.47000 
│ ├ 6n. Grain Gamma : 0.47000 
│ ├ 6o. Grain Slip Angle Gain : 0.56500 
│ ├ 6p. Grain Slip Angle Gamma : 0.84500 
│ ├ 6q. Grain Slip Angle Threshold : 10.51311 
│ ├ 6r. Blister Gain : 0.00000 
│ ├ 6s. Blister Gamma : 0.00000 
│ ├ 6t. Practical Temp Source : 0.80000 
│ ├ 6u. Brake Transfer Factor : 0.00070 
│ ├ 6v. Thermal Performance Curve : 
content\cars\common_phsx\tyres\f1_2025\tcurve_f12025_wet.curve 
│ ├ 6w. Contact I M O : 1.60000 
│ ├ 6x. Tref Friction Limit Angle : 75.00000 
│ └ 6y. Friction Limit Angle T Sensitivity : 0.06000 
├ 7. Pressure Data 
│ ├ 7a. Pressure Flex Gain : 0.25000 
│ ├ 7b. Rolling Resistance Gain : 1.20000 
│ ├ 7c. Rolling Heat Gain : 0.10000 
│ ├ 7d. Gain D : 0.00250 
│ ├ 7e. Ideal Pressure : 26.00000 
│ ├ 7f. Pressure Reference : 17.00000 
│ ├ 7g. Pressure Spring Curve : None 
│ ├ 7h. Pressure Spring Gain : 11110.00000 
│ ├ 7i. Curb Pressure Loss Must : 1.00000 
│ └ 7j. Curb Pressure Loss Threshold : 30.00000 
├ 8. Camber Data 
│ ├ 8a. Camber Gain : 0.20000 
│ ├ 8b. Camber Vertical K Range Deg : 5.00000 
│ ├ 8c. Camber Vertical K Gain : -0.10000 
│ ├ 8d. Dcamber0 : 0.60000 
│ └ 8e. Dcamber1 : -11.00000 
├ 9. Speed Sensitivity
```

```
│ ├ 9a. Mu0 T : 0.85000 
│ ├ 9b. Ref Speed : 4.50000 
│ ├ 9c. Mu Speed Sensitivity : 1.20000 
│ ├ 9d. Mu T Sensitivity : 0.03500 
│ ├ 9e. Tref Mu T : 80.00000 
│ ├ 9f. Mu0 T X : 0.68000 
│ ├ 9g. Ref Speed X : 2.60000 
│ ├ 9h. Mu Speed Sensitivity X : 1.80000 
│ ├ 9i. Mu T Sensitivity X : 0.03500 
│ └ 9j. Tref Mu T X : 80.00000 
├ 10. Rolling Resistance 
│ ├ 10a. Rr0 : 20.11450 
│ ├ 10b. Rr1 : 0.00200 
│ ├ 10c. Rr Slip : 646.00000 
│ └ 10d. Rr Wear Mult : 0.14000 
├ 11. Groove Data 
│ ├ 11a. Groove Factor : 68.00000 
│ ├ 11b. Groove S A Factor : 0.45000 
│ └ 11c. Groove S R Factor : 0.45000 
├ 12. Pressure : 17.00000 
├ 13. Init Data 
│ ├ 13a. Width : 305.00000 
│ ├ 13b. Aspect Ratio : 43.00000 
│ ├ 13c. Diameter : 18.00000 
│ ├ 13d. Load Index : 101.00000 
└ └ 13e. Pressure : 17.00000
```

# <span id="page-232-0"></span>**20. Wing [ .wing ]**

# <span id="page-232-1"></span>**A. Description**

<span id="page-232-2"></span>**I. General Description** 

Xxxxxxx

<span id="page-232-3"></span>**II. Area of Influence / Impact on Vehicle Dynamics** 

Xxxxxxx

<span id="page-232-4"></span>**III. Key Architecture & Data Fields Explained** 

xxxxxxxx

- <span id="page-232-5"></span>**1 - WHEEL RATE & SPRING PARAMETERS**
  - **•** Xxxx
- <span id="page-232-6"></span>**2 - DAMPER PROFILE PARAMETERS**

XXxxxxx

- <span id="page-232-7"></span>**3 - ALIGNMENTS & GEOMETRY FIELDS** 
  - **• Pressure**: EXxxxxxxx
- <span id="page-232-8"></span>**IV. Interpretation of Tuning Part Strategies**

By cross-Xxxxxxxxxx

# <span id="page-232-9"></span>**B. Schema**

```
├ 1. Vertical : boolean
├ 2. Name : string
├ 3. Chord : float
├ 4. Span : float
├ 5. Position : x, y, z float
├ 6. Lut A O A C L : string - path
├ 7. Lut A O A C D : string - path
├ 8. Lut G H C L Mult : string - path
├ 9. Lut G H C D Mult : string - path
```

```
10. Cd Gain : float
11. Cl Gain : float
12. Angle : float
13. Yaw Gain : float
14. Drag Per Cool Transfer: float
15. Has Fan : boolean
16. Fan Speed : float
17. Damage C D [x] : float | can have multiple Damage C D
18. Damage C L [x] : float | can have multiple Damage C L
19. Wing Controllers [x] : object | can have multiple Wing Controllers
 - 19a. Combinator Mode : enum
 - 19b. Input : enum
 - 19c. Filter : float
 - 19d. Up Limit : float
 - 19e. Down Limit : float
 - 19f. Lut : string - path
```

#### **Enum - Car Wing**

| 19a | Combinator Mode | UndefinedMode, Add, Must                                                            |
|-----|-----------------|-------------------------------------------------------------------------------------|
| 19b | Input           | UndefinedInput, Brake, Gas, Yaw, LatG, LonG, Steer, Speed, SusTraveILR, SusTraveIRR |

# <span id="page-233-0"></span>C. Example data

### <span id="page-233-1"></span>I. Chosen Tyres for Example

- Audi RS6 Avant (slug: ks audi rs 6 avant) [3 wings]
- Lotus Emira (slug: ks lotus emira)
- Ferrari SF-25 ( slug : ks\_ferrari\_sf\_25 )

#### <span id="page-233-2"></span>II. Example

#### <span id="page-233-3"></span>**Audi RS6 Avant**

#### 1. Wing 0 [ Body ] (file: ks audi rs 6 avant0.wing)

```
- 1. Vertical : false
- 2. Name : BODY
- 3. Chord : 1.00000
- 4. Span : 2.41000
- 5. Position : 0.00000, 0.18000, -0.10000
- 6. Lut A O A C L :
content\cars\ks_audi_rs_6_avant\data\wing_body_AOA_CL.curve
- 7. Lut A O A C D :
content\cars\ks_audi_rs_6_avant\data\wing_body_AOA_CD.curve
- 8. Lut G H C L Mult : None
- 9. Lut G H C D Mult : None
- 10. Cd Gain : 1.60000
```

```
├ 11. Cl Gain : 0.00000 
├ 12. Angle : 0.00000 
├ 13. Yaw Gain : 0.00000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00500 
├ 17. Damage C D 2 : 0.00500 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None 
1. Wing 1 [ Front ] ( file : ks_audi_rs_6_avant1.wing ) 
├ 1. Vertical : false 
├ 2. Name : FRONT 
├ 3. Chord : 1.00000 
├ 4. Span : 2.41000 
├ 5. Position : 0.00000, -0.34000, 1.90000 
├ 6. Lut A O A C L : 
content\cars\ks_audi_rs_6_avant\data\wing_front_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_audi_rs_6_avant\data\wing_front_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_audi_rs_6_avant\data\height_front_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_audi_rs_6_avant\data\height_front_CD.curve 
├ 10. Cd Gain : 0.00000 
├ 11. Cl Gain : 1.00000 
├ 12. Angle : 2.00000 
├ 13. Yaw Gain : 0.00000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01500 
├ 17. Damage C D 2 : 0.00500 
├ 17. Damage C D 3 : 0.00000 
├ 17. Damage C D 4 : 0.00000 
├ 18. Damage C L 1 : 0.01500 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None 
1. Wing 2 [ Rear ] ( file : ks_audi_rs_6_avant2.wing ) 
├ 1. Vertical : false 
├ 2. Name : REAR 
├ 3. Chord : 1.00000 
├ 4. Span : 2.41000 
├ 5. Position : 0.00000, 0.80000, -2.10000
```

```
├ 6. Lut A O A C L : 
content\cars\ks_audi_rs_6_avant\data\wing_rear_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_audi_rs_6_avant\data\wing_rear_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 0.00000 
├ 11. Cl Gain : 1.00000 
├ 12. Angle : 0.00000 
├ 13. Yaw Gain : 0.00000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00000 
├ 17. Damage C D 2 : 0.01500 
├ 17. Damage C D 3 : 0.00000 
├ 17. Damage C D 4 : 0.00000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.01000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None
```

## <span id="page-235-0"></span>**Lotus Emira**

# *1. Wing 0 [ Body ] ( file : ks\_lotus\_emira0.wing )*

```
├ 1. Vertical : false 
├ 2. Name : BODY 
├ 3. Chord : 1.00000 
├ 4. Span : 1.94500 
├ 5. Position : 0.00000, 0.20000, 0.50000 
├ 6. Lut A O A C L : 
content\cars\ks_lotus_emira\data\wing_body_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_lotus_emira\data\wing_body_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 1.00000 
├ 11. Cl Gain : 0.00000 
├ 12. Angle : 0.00000 
├ 13. Yaw Gain : 0.00000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00500 
├ 17. Damage C D 2 : 0.00500 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None
```

### *1. Wing 1 [ Front ] ( file : ks\_lotus\_emira1.wing )*

```
├ 1. Vertical : false 
├ 2. Name : FRONT 
├ 3. Chord : 1.00000 
├ 4. Span : 1.94500 
├ 5. Position : 0.00000, -0.30000, 1.48700 
├ 6. Lut A O A C L : 
content\cars\ks_lotus_emira\data\wing_front_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_lotus_emira\data\wing_front_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 0.00000 
├ 11. Cl Gain : 2.00000 
├ 12. Angle : 2.00000 
├ 13. Yaw Gain : 0.00000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01500 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.00000 
├ 17. Damage C D 4 : 0.00000 
├ 18. Damage C L 1 : 0.01500 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None 
1. Wing 2 [ Rear ] ( file : ks_lotus_emira2.wing ) 
├ 1. Vertical : false 
├ 2. Name : REAR 
├ 3. Chord : 1.00000 
├ 4. Span : 1.94500 
├ 5. Position : 0.00000, 0.10000, -1.00000 
├ 6. Lut A O A C L : 
content\cars\ks_lotus_emira\data\wing_rear_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_lotus_emira\data\wing_rear_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 0.00000 
├ 11. Cl Gain : 2.20000 
├ 12. Angle : 2.00000 
├ 13. Yaw Gain : 0.00000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false
```

├ 16. Fan Speed : 0.00000 ├ 17. Damage C D 1 : 0.00000 ├ 17. Damage C D 2 : 0.01500 ├ 17. Damage C D 3 : 0.00000 ├ 17. Damage C D 4 : 0.00000

```
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.01000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None
```

### <span id="page-237-0"></span>**Ferrari SF-25**

### *1. Wing 0 [ Body ] ( file : ks\_ferrari\_sf\_250.wing )*

```
├ 1. Vertical : false 
├ 2. Name : BODY 
├ 3. Chord : 1.00000 
├ 4. Span : 1.36600 
├ 5. Position : 0.00000, 0.15000, -0.08000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_body_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_body_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 0.50000 
├ 11. Cl Gain : 1.00000 
├ 12. Angle : 3.50000 
├ 13. Yaw Gain : -0.20000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00000 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None
```

#### *2. Wing 1 [ Front ] ( file : ks\_ferrari\_sf\_251.wing )*

```
├ 1. Vertical : false 
├ 2. Name : FRONT 
├ 3. Chord : 1.00000 
├ 4. Span : 0.42000 
├ 5. Position : -0.56000, -0.09000, 2.90000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_front_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_front_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_frontwing_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_frontwing_CD.curve 
├ 10. Cd Gain : 1.25000
```

```
├ 11. Cl Gain : 3.90000 
├ 12. Angle : 6.00000 
├ 13. Yaw Gain : -0.57100 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01000 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.00000 
├ 17. Damage C D 4 : 0.00000 
├ 18. Damage C L 1 : 0.01000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None 
3. Wing 2 [ Front ] ( file : ks_ferrari_sf_252.wing ) 
├ 1. Vertical : false 
├ 2. Name : FRONT 
├ 3. Chord : 1.00000 
├ 4. Span : 0.42000 
├ 5. Position : 0.56000, -0.09000, 2.90000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_front_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_front_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_frontwing_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_frontwing_CD.curve 
├ 10. Cd Gain : 1.25000 
├ 11. Cl Gain : 3.90000 
├ 12. Angle : 6.00000 
├ 13. Yaw Gain : -0.57100 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01000 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.00000 
├ 17. Damage C D 4 : 0.00000 
├ 18. Damage C L 1 : 0.01000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None 
4. Wing 3 [ Rear ] ( file : ks_ferrari_sf_253.wing ) 
├ 1. Vertical : false 
├ 2. Name : REAR 
├ 3. Chord : 0.45000 
├ 4. Span : 2.00000 
├ 5. Position : 0.00000, 0.55000, -1.70000
```

```
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_rear_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_rear_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 1.50000 
├ 11. Cl Gain : 0.70000 
├ 12. Angle : 12.00000 
├ 13. Yaw Gain : -1.50000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00000 
├ 17. Damage C D 2 : 0.01000 
├ 17. Damage C D 3 : 0.00000 
├ 17. Damage C D 4 : 0.00000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.01000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None 
5. Wing 4 [ Diffuser Front ] ( file : ks_ferrari_sf_254.wing ) 
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_F 
├ 3. Chord : 2.50000 
├ 4. Span : 1.36600 
├ 5. Position : 0.00000, -0.16000, 0.00000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CD.curve 
├ 10. Cd Gain : 1.00000 
├ 11. Cl Gain : 0.80000 
├ 12. Angle : 3.50000 
├ 13. Yaw Gain : -0.07000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01000 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.01000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.01000 
├ 18. Damage C L 4 : 0.01000 
├ 19. Wing Controllers : None
```

#### *6. Wing 5 [ Diffuser Rear Left ] ( file : ks\_ferrari\_sf\_255.wing )*

```
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_RL 
├ 3. Chord : 1.00000 
├ 4. Span : 0.68300 
├ 5. Position : -0.34230, -0.17500, -1.57000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_rear_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_rear_CD.curve 
├ 10. Cd Gain : 0.55000 
├ 11. Cl Gain : 0.71000 
├ 12. Angle : 3.50000 
├ 13. Yaw Gain : -1.00000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00000 
├ 17. Damage C D 2 : 0.01000 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.01000 
├ 18. Damage C L 3 : 0.01000 
├ 18. Damage C L 4 : 0.01000 
├ 19. Wing Controllers : None 
7. Wing 6 [ Diffuser Rear Right ] ( file : ks_ferrari_sf_256.wing ) 
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_RR 
├ 3. Chord : 1.00000 
├ 4. Span : 0.68300 
├ 5. Position : 0.34230, -0.17500, -1.57000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_rear_CL.curve 
├ 9. Lut G H C D Mult :
```

content\cars\ks\_ferrari\_sf\_25\data\aero\height\_diffuser\_rear\_CD.curve

├ 10. Cd Gain : 0.55000 ├ 11. Cl Gain : 0.71000 ├ 12. Angle : 3.50000 ├ 13. Yaw Gain : -1.00000

├ 15. Has Fan : false ├ 16. Fan Speed : 0.00000 ├ 17. Damage C D 1 : 0.00000

├ 14. Drag Per Cool Transfer : 0.00000

```
├ 17. Damage C D 2 : 0.01000 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.01000 
├ 18. Damage C L 3 : 0.01000 
├ 18. Damage C L 4 : 0.01000 
├ 19. Wing Controllers : None 
8. Wing 7 [ DRS ] ( file : ks_ferrari_sf_257.wing ) 
├ 1. Vertical : false 
├ 2. Name : DRS 
├ 3. Chord : 1.00000 
├ 4. Span : 1.36600 
├ 5. Position : 0.00000, 0.59000, -1.80000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_rear2_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_rear2_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 1.70000 
├ 11. Cl Gain : 2.00000 
├ 12. Angle : 17.00000 
├ 13. Yaw Gain : -1.00000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00000 
├ 17. Damage C D 2 : 0.01000 
├ 17. Damage C D 3 : 0.00000 
├ 17. Damage C D 4 : 0.00000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.01000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None 
9. Wing 8 [ Monkeyseat ] ( file : ks_ferrari_sf_258.wing ) 
├ 1. Vertical : false 
├ 2. Name : DRS 
├ 3. Chord : 1.00000 
├ 4. Span : 1.36600 
├ 5. Position : 0.00000, -0.10000, -1.80000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_monkey_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_monkey_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 1.00000 
├ 11. Cl Gain : 1.00000 
├ 12. Angle : 10.00000
```

```
├ 13. Yaw Gain : -0.15000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00000 
├ 17. Damage C D 2 : 0.01000 
├ 17. Damage C D 3 : 0.00000 
├ 17. Damage C D 4 : 0.00000 
├ 18. Damage C L 1 : 0.00000 
├ 18. Damage C L 2 : 0.01000 
├ 18. Damage C L 3 : 0.00000 
├ 18. Damage C L 4 : 0.00000 
├ 19. Wing Controllers : None 
10. Wing 9 [ Diffuser Front Left ] ( file : ks_ferrari_sf_diff_l.wing ) 
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_FL 
├ 3. Chord : 2.50000 
├ 4. Span : 0.35000 
├ 5. Position : 0.31000, -0.16000, 0.00000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CD.curve 
├ 10. Cd Gain : 0.83000 
├ 11. Cl Gain : 1.70000 
├ 12. Angle : 3.50000 
├ 13. Yaw Gain : -0.07000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01000 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.01000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.01000 
├ 18. Damage C L 4 : 0.01000 
├ 19. Wing Controllers : None 
11. Wing 10 [ Diffuser Front Left L ] ( file : ks_ferrari_sf_diff_ll.wing ) 
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_FLL 
├ 3. Chord : 2.50000 
├ 4. Span : 0.35000 
├ 5. Position : 0.66000, -0.16000, 0.00000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CL.curve
```

```
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CD.curve 
├ 10. Cd Gain : 0.83000 
├ 11. Cl Gain : 1.10000 
├ 12. Angle : 3.50000 
├ 13. Yaw Gain : -0.07000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01000 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.01000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.01000 
├ 18. Damage C L 4 : 0.01000 
├ 19. Wing Controllers : None 
12. Wing 11 [ Diffuser Front Right ] ( file : ks_ferrari_sf_diff_r.wing ) 
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_FR 
├ 3. Chord : 2.50000 
├ 4. Span : 0.35000 
├ 5. Position : -0.31000, -0.16000, 0.00000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CD.curve 
├ 10. Cd Gain : 0.83000 
├ 11. Cl Gain : 1.70000 
├ 12. Angle : 3.50000 
├ 13. Yaw Gain : -0.07000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01000 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.01000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.01000 
├ 18. Damage C L 4 : 0.01000
```

├ 19. Wing Controllers : None

#### *13. Wing 12 [ Diffuser Front Right R ] ( file : ks\_ferrari\_sf\_diff\_rr.wing )*

```
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_FRR 
├ 3. Chord : 2.50000 
├ 4. Span : 0.35000 
├ 5. Position : -0.66000, -0.16000, 0.00000 
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CD.curve 
├ 10. Cd Gain : 0.83000 
├ 11. Cl Gain : 1.10000 
├ 12. Angle : 3.50000 
├ 13. Yaw Gain : -0.07000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.01000 
├ 17. Damage C D 2 : 0.00000 
├ 17. Damage C D 3 : 0.01000 
├ 17. Damage C D 4 : 0.01000 
├ 18. Damage C L 1 : 0.01000 
├ 18. Damage C L 2 : 0.00000 
├ 18. Damage C L 3 : 0.01000 
├ 18. Damage C L 4 : 0.01000
```

├ 19. Wing Controllers : None