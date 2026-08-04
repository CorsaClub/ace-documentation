![](_page_0_Picture_0.jpeg)

# **Assetto Corsa EVO**

Game Version : **0.7.1**

Assets Type : **Cars**

Subtype : **Car Physics Assets** 

![](_page_0_Picture_5.jpeg)

# **Preface**

This document is an independent, community-driven technical reference for the vehicle physics assets of **Assetto Corsa EVO**. It is **not** an official publication of Kunos Simulazioni, nor is it endorsed, reviewed, or maintained by the studio. Assetto Corsa EVO and related marks remain the property of their respective owners.

The material herein was compiled through careful inspection of shipped physics assets, comparative analysis across vehicle configurations, and reasoned interpretation of field names, value ranges, and observed behavior. Where the engine's internal implementation is not publicly specified, units, roles and relationships are **inferred**. They should therefore be treated as working hypotheses - useful for modding, research, and discussion - rather than as authoritative studio specifications.

Readers should expect that some entries may contain inaccuracies, incomplete coverage, or interpretations that later evidence revises. Game updates, newly examined assets, and community verification may all require corrections. This reference is published so that knowledge of otherwise opaque systems can be shared, challenged, and improved openly.

Use this guide as a structured starting point. Cross-check critical parameters against in-game behaviour and primary asset data before relying on any single conclusion. Contributions that refine descriptions, confirm units, or document previously unmapped fields are welcome and strengthen the ressource for everyone.

### **Reporting Corrections**

If you find an error, an incomplete field, or a more convincing interpretation of a unit or description, please report it on GitHub using the **Documentation correction** issue template :

**[https://github.com/CorsaClub/ace-documentation/issues/new?template=documentation](https://github.com/CorsaClub/ace-documentation/issues/new?template=documentation-correction.yml)[correction.yml](https://github.com/CorsaClub/ace-documentation/issues/new?template=documentation-correction.yml)**

Include the section (for example 19. Tyre), the field ID when relevant, the current texte, your proposed correction, and the evidence behind it (asset values, game version, telemetry, or comparative checks). Maintainers will review reports and update the reference accordingly. If you already have a ready-made edit, a Pull Request is equally welcome.

| 1. | Brake | System<br>[<br>.brakesystem<br>]                                                | 17 |
|----|-------|---------------------------------------------------------------------------------|----|
|    | A.    | Description                                                                     | 17 |
|    |       | I.<br>Role<br>in<br>the<br>stack                                                | 17 |
|    |       | II.<br>What<br>you<br>are<br>really<br>tuning                                   | 17 |
|    |       | III.<br>Architecture                                                            | 17 |
|    |       | 1 - Mechanical Baseline                                                         | 17 |
|    |       | 2 - Controllers (Share stage pattern)                                           | 18 |
|    |       | 3- EBB Mode Switch                                                              | 18 |
|    |       | IV.<br>How<br>to<br>read<br>the<br>examples                                     | 18 |
|    |       | 1 - Alfa Giulia GTAm / Lancia Delta                                             | 18 |
|    |       | 2 - Ferrari 296 GT3                                                             | 19 |
|    |       | 3 - Ferrari 296 GT3                                                             | 19 |
|    |       | V.<br>Practical<br>notes                                                        | 19 |
|    |       | VI.<br>Related<br>assets                                                        | 19 |
|    | B.    | Schema                                                                          | 19 |
|    | C.    | Measurement Units & Descriptions                                                | 21 |
|    | D.    | Example data                                                                    | 22 |
|    |       | I.<br>Chosen<br>Cars<br>for<br>Example                                          | 22 |
|    |       | II.<br>Example                                                                  | 22 |
|    |       | Alfa Romeo Giulia GTAm                                                          | 22 |
|    |       | Lancia Delta HF Integrale EVO II ( slug : ks_lancia_delta_hf_integrale_evo_ii ) | 23 |
|    |       | Ferrari 296 GT3                                                                 | 24 |
|    |       | Ferrari SF25                                                                    | 24 |
| 2. |       | Brakes<br>[<br>.brakes<br>]                                                     | 28 |
|    | A.    | Description                                                                     | 28 |
|    |       | I.<br>Role<br>in<br>the<br>stack                                                | 28 |
|    |       | II.<br>What<br>you<br>are<br>really<br>tuning                                   | 28 |
|    |       | III.<br>Architecture                                                            | 29 |
|    |       | 1 - Thermal modelling (schema 1-10)                                             | 29 |
|    |       | 2 - Dimensions and wear (schema 11-19)                                          | 29 |
|    |       | 3 - Performance curve (Schema 20)                                               | 29 |
|    |       | IV.<br>How<br>to<br>read<br>the<br>examples                                     | 29 |
|    |       | 1 - Vintage Road Front / Rear (split axle)                                      | 29 |
|    |       | 2 - Racing GT3 Pad 2 (shared compound)                                          | 29 |
|    |       | V.<br>Practical<br>notes                                                        | 30 |

|    |     | VI.  | Related<br>assets                                              | 30 |
|----|-----|------|----------------------------------------------------------------|----|
|    | B.  |      | Schema                                                         | 30 |
|    | C.  |      | Measurement Units & Descriptions                               | 30 |
|    | D.  |      | Example data                                                   | 32 |
|    |     | I.   | Chosen<br>Brakes<br>for<br>Example                             | 32 |
|    |     | II.  | Example                                                        | 32 |
|    |     |      | Vintage Road [ Front ]                                         | 32 |
|    |     |      | Vintage Road [ Rear ]                                          | 33 |
|    |     |      | Racing GT3 [ Pad 2 ]                                           | 34 |
| 3. | Car | Data | [<br>.car<br>]                                                 | 36 |
|    | A.  |      | Description                                                    | 36 |
|    |     | I.   | Role<br>in<br>the<br>stack                                     | 36 |
|    |     | II.  | What<br>you<br>are<br>really<br>tuning                         | 36 |
|    |     | III. | Architecture                                                   | 37 |
|    |     |      | 1 - Identity and General (schema 1-3)                          | 37 |
|    |     |      | 2 - Suspensions hub (schema 4)                                 | 37 |
|    |     |      | 3 - Powertrain and brake paths (schema 5-9)                    | 37 |
|    |     |      | 4 - Driver, collision, tires (schema 10-16)                    | 37 |
|    |     |      | 5 - Aero and hybrid (schema 17-19)                             | 37 |
|    |     |      | 6 - Setups, mesh, AI, modes (schema 20-28)                     | 37 |
|    |     | IV.  | How<br>to<br>read<br>the<br>examples                           | 37 |
|    |     |      | 1 - Ferrari 296 GTB (road mid-engine)                          | 37 |
|    |     |      | 2 - Audi R8 LMS GT3 Evo II (race GT3)                          | 38 |
|    |     |      | 3 - Renault 5 GT Turbo (light FWD hot hatch)                   | 38 |
|    |     | V.   | Practical<br>notes                                             | 38 |
|    |     | VI.  | Related<br>assets                                              | 38 |
|    | B.  |      | Dependency map                                                 | 38 |
|    |     | I.   | Direct<br>loads<br>from<br>Car<br>Data                         | 39 |
|    |     | II.  | Second<br>hop<br>—<br>what<br>loaded<br>assets<br>open<br>next | 39 |
|    |     | III. | Overlay<br>and<br>select<br>layers<br>(not<br>path<br>owners)  | 40 |
|    |     | IV.  | By<br>concern                                                  | 41 |
|    |     |      | 1 - Stop                                                       | 41 |
|    |     |      | 2 - Go                                                         | 41 |
|    |     |      | 3 - Platform                                                   | 41 |
|    |     |      | 4 - Aero                                                       | 42 |

|    |     | V.<br>Shared<br>libraries<br>(common_phsx)      | 42 |
|----|-----|-------------------------------------------------|----|
|    |     | VI.<br>Start<br>here                            | 42 |
|    |     | VII.<br>Pratical<br>notes                       | 43 |
|    | C.  | Schema                                          | 43 |
|    | D.  | Measurement Units & Descriptions                | 52 |
|    | E.  | Example data                                    | 67 |
|    |     | I.<br>Chosen<br>Car<br>Data<br>for<br>Example   | 67 |
|    |     | II.<br>Example                                  | 67 |
|    |     | Ferrari 296 GTB                                 | 67 |
|    |     | Audi R8 LMS GT3 Evo II                          | 77 |
|    |     | Renault 5 GT Turbo                              | 84 |
| 4. | Car | Engine<br>[<br>.carengine<br>]                  | 88 |
|    | A.  | Description                                     | 88 |
|    |     | I.<br>Role<br>in<br>the<br>stack                | 88 |
|    |     | II.<br>What<br>you<br>are<br>really<br>tuning   | 88 |
|    |     | III.<br>Architecture                            | 89 |
|    |     | 1 - Core propulsion (schema 1-4)                | 89 |
|    |     | 2 - Maps and rev limits (schema 5-8)            | 89 |
|    |     | 3 - GLobal throttle and start (schema 9-15)     | 89 |
|    |     | 4 - Forced induction (schema 16-20)             | 89 |
|    |     | 5 - Battery (schema 21)                         | 89 |
|    |     | IV.<br>How<br>to<br>read<br>the<br>examples     | 89 |
|    |     | 1 - Alpine A290 b (electric motor)              | 89 |
|    |     | 2 - Ferrari SF-25 (race ICE + strategy maps)    | 89 |
|    |     | 3 - Chevrolet Camaro ZL1 (boosted muscle)       | 89 |
|    |     | 4 - Datsun 240z Fairlady (classic NA)           | 89 |
|    |     | V.<br>Practical<br>notes                        | 90 |
|    |     | VI.<br>Related<br>assets                        | 90 |
|    | B.  | Schema                                          | 90 |
|    | C.  | Measurement Units & Descriptions                | 92 |
|    | D.  | Example data                                    | 96 |
|    |     | I.<br>Chosen<br>Car<br>Engine<br>for<br>Example | 96 |
|    |     | II.<br>Example                                  | 96 |
|    |     | Alpine A290 b                                   | 96 |
|    |     | Ferrari SF 25                                   | 97 |

|    |     |      | Chevrolet Camaro ZL1                           | 100 |
|----|-----|------|------------------------------------------------|-----|
|    |     |      | Datsun 240z Fairlady                           | 101 |
| 7. | Car |      | Setup<br>[<br>.carsetup<br>]                   | 103 |
|    | A.  |      | Description                                    | 103 |
|    |     | I.   | Role<br>in<br>the<br>stack                     | 103 |
|    |     | II.  | What<br>you<br>are<br>really<br>tuning         | 103 |
|    |     | III. | Architecture                                   | 104 |
|    |     |      | 1 - Import and mechanical balance (schema 1-2) | 104 |
|    |     |      | 2 - Per-corner structure (schema 3-5)          | 104 |
|    |     |      | 3 - Electronics (schema 6)                     | 104 |
|    |     |      | 4 - Aero and fuel (schema 7-8)                 | 104 |
|    |     |      | 5 - Preset identity (schema 9-11)              | 104 |
|    |     | IV.  | How<br>to<br>read<br>the<br>examples           | 104 |
|    |     |      | 1 - Audi Sport Quattro                         | 104 |
|    |     |      | 2 - Alfa ROmeo Junior                          | 104 |
|    |     |      | 3 - Ferrari 488 Challenge Eco (preset safe_1)  | 104 |
|    |     | V.   | Practical<br>notes                             | 105 |
|    |     | VI.  | Related<br>assets                              | 105 |
|    | B.  |      | Schema                                         | 105 |
|    | C.  |      | Measurement Units & Descriptions               | 106 |
|    | D.  |      | Example data                                   | 111 |
|    |     | I.   | Chosen<br>Car<br>Engine<br>for<br>Example      | 111 |
|    |     | II.  | Example                                        | 111 |
|    |     |      | Audi Sport Quattro                             | 111 |
|    |     |      | Alfa Romeo Junior                              | 113 |
|    |     |      | Ferrari 488 Challenge Evo [ preset : safe_1 ]  | 116 |
| 6. | Car |      | Setup<br>Limits<br>[<br>.carsetuplimits<br>]   | 119 |
|    | A.  |      | Description                                    | 119 |
|    |     | I.   | Role<br>in<br>the<br>stack                     | 119 |
|    |     | II.  | What<br>you<br>are<br>really<br>tuning         | 119 |
|    |     | III. | Architecture                                   | 120 |
|    |     |      | 1 - Binding (schema 1)                         | 120 |
|    |     |      | 2 - Mechanical Balance (schema 2)              | 120 |
|    |     |      | 3 - Per-corner and electronics (schema 3-6)    | 120 |
|    |     |      | 4 - Aero, fuel, compound mode (schema 7-9)     | 120 |

|    |     | IV.  | How<br>to<br>read<br>the<br>examples                | 120 |
|----|-----|------|-----------------------------------------------------|-----|
|    |     |      | 1 - BMW M4 CSL (locked production-style envelope)   | 120 |
|    |     |      | 2 - Lamborghini Countach (open adjustable envelope) | 120 |
|    |     | V.   | Practical<br>notes                                  | 121 |
|    |     | VI.  | Related<br>assets                                   | 121 |
|    | B.  |      | Schema                                              | 121 |
|    | C.  |      | Measurement Units & Descriptions                    | 130 |
|    | D.  |      | Example data                                        | 134 |
|    |     | I.   | Chosen<br>Car<br>Engine<br>for<br>Example           | 134 |
|    |     | II.  | Example                                             | 134 |
|    |     |      | BMW M4 CSL                                          | 134 |
|    |     |      | Lamborghini Countach                                | 154 |
| 7. | Car |      | Setup<br>Units<br>[<br>.carsetupunits<br>]          | 175 |
|    | A.  |      | Description                                         | 175 |
|    |     | I.   | Role<br>in<br>the<br>stack                          | 175 |
|    |     | II.  | What<br>you<br>are<br>really<br>tuning              | 175 |
|    |     | III. | Architecture                                        | 176 |
|    |     |      | 1 - Mechanical Balance (schema 1)                   | 176 |
|    |     |      | 2 - Suspensions and dampers (schema 2-3)            | 176 |
|    |     |      | 3 - Alignments (schema 4)                           | 176 |
|    |     |      | 4 - Electronics (schema 5)                          | 176 |
|    |     |      | 5 - Aero, fuel, compound mode (schema 6-8)          | 176 |
|    |     | IV.  | How<br>to<br>read<br>the<br>examples                | 176 |
|    |     |      | 1 - Shared Setup Units (common_phsx)                | 176 |
|    |     | V.   | Practical<br>notes                                  | 177 |
|    |     | VI.  | Related<br>assets                                   | 177 |
|    | B.  |      | Schema                                              | 177 |
|    | C.  |      | Measurement Units & Descriptions                    | 178 |
|    | D.  |      | Example data                                        | 181 |
|    |     | I.   | Chosen<br>Car<br>Engine<br>for<br>Example           | 181 |
|    |     | II.  | Example                                             | 181 |
|    |     |      | Setup Units                                         | 181 |
| 8. | Car |      | Tuning<br>Parts<br>[<br>.tuningpart<br>]            | 185 |
|    | A.  |      | Description                                         | 185 |

|    |                                                        | I.   | Role<br>in<br>the<br>stack                        | 185 |  |
|----|--------------------------------------------------------|------|---------------------------------------------------|-----|--|
|    |                                                        | II.  | What<br>you<br>are<br>really<br>tuning            | 185 |  |
|    |                                                        | III. | Architecture                                      | 186 |  |
|    |                                                        |      | 1 - Header (schema 1 and 3)                       | 186 |  |
|    |                                                        |      | 2 - Conditional payload (schema 2)                | 186 |  |
|    |                                                        |      | 3 - Nested controllers                            | 186 |  |
|    |                                                        | IV.  | How<br>to<br>read<br>the<br>examples              | 186 |  |
|    |                                                        |      | 1 - Toyota Supra MK IV (drift package set)        | 186 |  |
|    |                                                        |      | 2 - Datsun 240z Fairlady (catalogue upgrades)     | 187 |  |
|    |                                                        |      | 3 - Porsche 992 GT3 Cup (electronics / BOP style) | 187 |  |
|    |                                                        | V.   | Practical<br>notes                                | 187 |  |
|    |                                                        | VI.  | Related<br>assets                                 | 187 |  |
|    | B.                                                     |      | Schema                                            | 187 |  |
|    | C.                                                     |      | Measurement Units & Descriptions                  | 193 |  |
|    | D.                                                     |      | Example data                                      | 202 |  |
|    |                                                        | I.   | Chosen<br>Cars<br>for<br>Example                  | 202 |  |
|    |                                                        | II.  | Example                                           | 202 |  |
|    |                                                        |      | Toyota Supra MK IV                                | 202 |  |
|    |                                                        |      | Datsun 240z Fairlady                              | 203 |  |
|    |                                                        |      | Porsche 992 GT3 Cup                               | 205 |  |
| 9. | Car<br>Electronics<br>[<br>.carelectronics<br>]<br>206 |      |                                                   |     |  |
|    | A.                                                     |      | Description                                       | 206 |  |
|    |                                                        | I.   | Role<br>in<br>the<br>stack                        | 206 |  |
|    |                                                        | II.  | What<br>you<br>are<br>really<br>tuning            | 206 |  |
|    |                                                        | III. | Architecture                                      | 207 |  |
|    |                                                        |      | 1 - Traction Control (schema 1)                   | 207 |  |
|    |                                                        |      | 2 - Anti-lock Braking (schema 2)                  | 207 |  |
|    |                                                        |      | 3 - EDL (schema 3)                                | 207 |  |
|    |                                                        |      | 4 - ESP (schema 4)                                | 207 |  |
|    |                                                        | IV.  | How<br>to<br>read<br>the<br>examples              | 207 |  |
|    |                                                        |      | 1 - Lamborghini Huracan ST Evo 2                  | 207 |  |
|    |                                                        |      | 2 - Maserati MC20 GT2                             | 207 |  |
|    |                                                        |      | 3 - Porsche 992 GT3 Cup (two files)               | 207 |  |
|    |                                                        | V.   | Practical<br>notes                                | 208 |  |
|    |                                                        | VI.  | Related<br>assets                                 | 208 |  |

|     | B. | Schema                                        |     |  |
|-----|----|-----------------------------------------------|-----|--|
|     | C. | Measurement Units & Descriptions              | 209 |  |
|     | D. | Example data                                  |     |  |
|     |    | I.<br>Chosen<br>Cars<br>for<br>Example        | 212 |  |
|     |    | II.<br>Example                                | 212 |  |
|     |    | Lamborghini Huracan ST Evo 2                  | 212 |  |
|     |    | Maserati MC20 GT2                             | 216 |  |
|     |    | Porsche 992 GT3 Cup                           | 219 |  |
| 10. |    | Clutch<br>[<br>.clutch<br>]                   | 222 |  |
|     | A. | Description                                   | 222 |  |
|     |    | I.<br>Role<br>in<br>the<br>stack              | 222 |  |
|     |    | II.<br>What<br>you<br>are<br>really<br>tuning | 222 |  |
|     |    | III.<br>Architecture                          | 223 |  |
|     |    | 1 - Mechanical constants (schema 1-2)         | 223 |  |
|     |    | 2 - Autoclutch object (schema 3)              | 223 |  |
|     |    | 3 - Engagement map (schema 4)                 | 223 |  |
|     |    | IV.<br>How<br>to<br>read<br>the<br>examples   | 223 |  |
|     |    | 1 - Caterham 485 CSR — analog / historic      | 223 |  |
|     |    | 2 - Ferrari F2004 — race sequential style     | 223 |  |
|     |    | 3 - Volkswagen Golf GTI mk8 — road / assisted | 223 |  |
|     |    | V.<br>Practical<br>notes                      | 223 |  |
|     |    | VI.<br>Related<br>assets                      | 224 |  |
|     | B. | Schema                                        | 224 |  |
|     | C. | Measurement Units & Descriptions              | 224 |  |
|     | D. | Example data                                  | 225 |  |
|     |    | I.<br>Chosen<br>Cars<br>for<br>Example        | 225 |  |
|     |    | II.<br>Example                                | 225 |  |
|     |    | Caterham 485 CSR                              | 225 |  |
|     |    | Ferrari F2004                                 | 226 |  |
|     |    | Volkswagen Golf GTI mk8                       | 226 |  |
| 11. |    | Coilover<br>[<br>.coilover<br>]               | 227 |  |
|     | A. | Description                                   | 227 |  |
|     |    | I.<br>Role<br>in<br>the<br>stack              | 227 |  |
|     |    | II.<br>What<br>you<br>are<br>really<br>tuning | 227 |  |

|     |    | III.<br>Architecture                             | 228 |
|-----|----|--------------------------------------------------|-----|
|     |    | 1 - Springs and stops (schema 1-5)               | 228 |
|     |    | 2 - Damper block (schema 6)                      | 228 |
|     |    | 3 - Helper and controllers (schema 7-9)          | 228 |
|     |    | IV.<br>How<br>to<br>read<br>the<br>examples      | 228 |
|     |    | 1 - Caterham 485 CSR — compliant road / historic | 228 |
|     |    | 2 - Alpine A110s — stiff road / track sport      | 228 |
|     |    | 3 - Dallara EXP — high-downforce race            | 228 |
|     |    | V.<br>Practical<br>notes                         | 229 |
|     |    | VI.<br>Related<br>assets                         | 229 |
|     | B. | Schema                                           | 229 |
|     | C. | Measurement Units & Descriptions                 | 230 |
|     | D. | Example data                                     | 233 |
|     |    | I.<br>Chosen<br>Cars<br>for<br>Example           | 233 |
|     |    | II.<br>Example                                   | 234 |
|     |    | Caterham 485 CSR                                 | 234 |
|     |    | Alpine A110s                                     | 235 |
|     |    | Dallara EXP                                      | 237 |
| 12. |    | Damper<br>Curves<br>[<br>.dampercurves<br>]      | 239 |
|     | A. | Description                                      | 239 |
|     |    | I.<br>Role<br>in<br>the<br>stack                 | 239 |
|     |    | II.<br>What<br>you<br>are<br>really<br>tuning    | 239 |
|     |    | III.<br>Architecture                             | 240 |
|     |    | 1 - Damper Curves List Edit (schema 1)           | 240 |
|     |    | 2 - Reference payload                            | 240 |
|     |    | IV.<br>How<br>to<br>read<br>the<br>examples      | 240 |
|     |    | 1 - Ford GT3 dampers                             | 240 |
|     |    | 2 - Penske (common_phsx)                         | 240 |
|     |    | 3 - Porsche Cayman GT4 dampers                   | 240 |
|     |    | V.<br>Practical<br>notes                         | 240 |
|     |    | VI.<br>Related<br>assets                         | 241 |
|     | B. | Schema                                           | 241 |
|     | C. | Measurement Units & Descriptions                 | 241 |
|     | D. | Example data                                     | 241 |
|     |    |                                                  |     |

|     | I.<br>Chosen<br>Cars<br>for<br>Example        | 241 |
|-----|-----------------------------------------------|-----|
|     | II.<br>Example                                | 241 |
|     | Ford - GT3 Dampers                            | 241 |
|     | Penske                                        | 242 |
|     | Porsche Cayman Dampers                        | 244 |
| 13. | Drivetrain<br>[<br>.drivetrain<br>]           | 246 |
| A.  | Description                                   | 246 |
|     | I.<br>Role<br>in<br>the<br>stack              | 246 |
|     | II.<br>What<br>you<br>are<br>really<br>tuning | 246 |
|     | III.<br>Architecture                          | 247 |
|     | 1 - Layout and primary diff (schema 1-2)      | 247 |
|     | 2 - AWD differentials (schema 3)              | 247 |
|     | 3 - Torsion and flags (schema 4-10)           | 247 |
|     | 4 - Controllers and clutches (schema 11-16)   | 247 |
|     | IV.<br>How<br>to<br>read<br>the<br>examples   | 247 |
|     | 1 - Audi RS3 Sportback — controlled AWD       | 247 |
|     | 2 - Ferrari F40 LM — RWD with shaft torsion   | 247 |
|     | 3 - Abarth 695 Biposto — simple FWD LSD       | 247 |
|     | V.<br>Practical<br>notes                      | 248 |
|     | VI.<br>Related<br>assets                      | 248 |
| B.  | Schema                                        | 248 |
| C.  | Measurement Units & Descriptions              | 251 |
| D.  | Example data                                  | 254 |
|     | I.<br>Chosen<br>Cars<br>for<br>Example        | 254 |
|     | II.<br>Example                                | 254 |
|     | Audi RS3 Sportback                            | 254 |
|     | Ferrari F40 LM                                | 258 |
|     | Abarth 695 Biposto                            | 259 |
| 14. | Gearbox<br>[<br>.gearbox<br>]                 | 262 |
| A.  | Description                                   | 262 |
|     | I.<br>Role<br>in<br>the<br>stack              | 262 |
|     | II.<br>What<br>you<br>are<br>really<br>tuning | 262 |
|     | III.<br>Architecture                          | 263 |
|     | 1 - Ratios (schema 1-3)                       | 263 |
|     | 2 - Shift actuators and flags (schema 4-9)    | 263 |

|     |    | 3 - Protection and windows (schema 10-14)         | 263 |
|-----|----|---------------------------------------------------|-----|
|     |    | 4 - Assists and fatigue (schema 15–20)            | 263 |
|     |    | IV.<br>How<br>to<br>read<br>the<br>examples       | 263 |
|     |    | 1 - Porsche 718 Cayman GT4 CS MR — race DCT style | 263 |
|     |    | 2 - Alpine A290b — single-speed / EV layout       | 263 |
|     |    | 3 - Renault 5 GT Turbo — analog manual            | 263 |
|     |    | V.<br>Practical<br>notes                          | 264 |
|     |    | VI.<br>Related<br>assets                          | 264 |
|     | B. | Schema                                            | 264 |
|     | C. | Measurement Units & Descriptions                  | 265 |
|     | D. | Example data                                      | 267 |
|     |    | I.<br>Chosen<br>Cars<br>for<br>Example            | 267 |
|     |    | II.<br>Example                                    | 267 |
|     |    | Porsche 718 Cayman GT4 CS MR                      | 267 |
|     |    | Alpine A290 b                                     | 268 |
|     |    | Renault 5 GT Turbo                                | 269 |
| 15. |    | General<br>[<br>.generalcar<br>]                  | 271 |
|     | A. | Description                                       | 271 |
|     |    | I.<br>Role<br>in<br>the<br>stack                  | 271 |
|     |    | II.<br>What<br>you<br>are<br>really<br>tuning     | 271 |
|     |    | III.<br>Architecture                              | 272 |
|     |    | 1 - Core scalars (schema 1-14)                    | 272 |
|     |    | 2 - Mesh offset (schema 15)                       | 272 |
|     |    | IV.<br>How<br>to<br>read<br>the<br>examples       | 272 |
|     |    | 1 - Source statement                              | 272 |
|     |    | 2 - Practical reading via Car Data                | 272 |
|     |    | V.<br>Practical<br>notes                          | 272 |
|     |    | VI.<br>Related<br>assets                          | 273 |
|     | B. | Schema                                            | 273 |
|     | C. | Measurement Units & Descriptions                  | 273 |
|     | D. | Example data                                      | 275 |
|     |    | I.<br>Chosen<br>Cars<br>for<br>Example            | 275 |
| 16. |    | Surface<br>3D<br>[<br>.surface3d<br>]             | 276 |
|     | A. | Description                                       | 276 |
|     |    |                                                   |     |

|     | I.<br>Role<br>in<br>the<br>stack                                 | 276 |
|-----|------------------------------------------------------------------|-----|
|     | II.<br>What<br>you<br>are<br>really<br>tuning                    | 276 |
|     | III.<br>Architecture                                             | 277 |
|     | 1 - Optional linked curves (schema 1-2)                          | 277 |
|     | 2 - Grid definition (schema 3-8)                                 | 277 |
|     | 3 - Table and interp (schema 9-11)                               | 277 |
|     | 4 - CSV / import (schema 12-15)                                  | 277 |
|     | IV.<br>How<br>to<br>read<br>the<br>examples                      | 277 |
|     | 1 - Mercedes AMG GT2 — symmetric 8x8 pack                        | 277 |
|     | 2 - Audi R8 LMS GT3 Evo 2 — CX / CZ race maps                    | 277 |
|     | 3 - Dallara Stradale Coupe — coarser road/track pack             | 277 |
|     | V.<br>Practical<br>notes                                         | 278 |
|     | VI.<br>Related<br>assets                                         | 278 |
| B.  | Schema                                                           | 278 |
| C.  | Measurement Units & Descriptions                                 | 279 |
| D.  | Example data                                                     | 280 |
|     | I.<br>Chosen<br>Cars<br>for<br>Example                           | 280 |
|     | II.<br>Example                                                   | 280 |
|     | Mercedes AMG GT2                                                 | 280 |
|     | Audi R8 LMS GT3 Evo 2                                            | 282 |
|     | Dallara Stradale Coupe                                           | 284 |
| 17. | Suspension<br>[<br>.suspension<br>]                              | 287 |
| A.  | Description                                                      | 287 |
|     | I.<br>Role<br>in<br>the<br>stack                                 | 287 |
|     | II.<br>What<br>you<br>are<br>really<br>tuning                    | 287 |
|     | III.<br>Architecture                                             | 288 |
|     | 1 - Basic Data (schema 1)                                        | 288 |
|     | 2 - Legacy / classic topologies (schema 2-7)                     | 288 |
|     | 3 - Modern multilink and DW+coil (schema 8-9)                    | 288 |
|     | IV.<br>How<br>to<br>read<br>the<br>examples                      | 288 |
|     | 1 - Volkswagen Golf GTI Mk1 — strut front / trailing rear        | 288 |
|     | 2 - Honda S2000 AP1 — double wishbone + drift front              | 288 |
|     | 3 - Porsche 992 GT3 R Rennsport — DW coil front / multilink rear | 289 |
|     | V.<br>Practical<br>notes                                         | 289 |
|     | VI.<br>Related<br>assets                                         | 289 |

|     | B.    |              | Schema                                      | 289 |
|-----|-------|--------------|---------------------------------------------|-----|
|     | C.    |              | Measurement Units & Descriptions            |     |
|     | D.    | Example data | 297                                         |     |
|     |       | I.           | Chosen<br>Cars<br>for<br>Example            | 297 |
|     |       | II.          | Example                                     | 297 |
|     |       |              | Volkswagen Golf GTI Mk1                     | 297 |
|     |       |              | Honda S2000 AP1                             | 298 |
|     |       |              | Porsche 992 GT3 R Rennport                  | 300 |
| 18. | Turbo | [            | .turbo<br>]                                 | 302 |
|     | A.    |              | Description                                 | 302 |
|     |       | I.           | Role<br>in<br>the<br>stack                  | 302 |
|     |       | II.          | What<br>you<br>are<br>really<br>tuning      | 302 |
|     |       | III.         | Architecture                                | 303 |
|     |       | IV.          | How<br>to<br>read<br>the<br>examples        | 303 |
|     |       |              | 1 - Peugeot 205 T16 — two turbo stages      | 303 |
|     |       |              | 2 - Chevrolet Camaro ZL1 — compressor       | 303 |
|     |       |              | 3 - Toyota Supra MkIV — stock vs drift wins | 303 |
|     |       | V.           | Practical<br>notes                          | 303 |
|     |       | VI.          | Related<br>assets                           | 304 |
|     | B.    |              | Schema                                      | 304 |
|     | C.    |              | Measurement Units & Descriptions            | 304 |
|     | D.    |              | Example data                                | 305 |
|     |       | I.           | Chosen<br>Cars<br>for<br>Example            | 305 |
|     |       | II.          | Example                                     | 306 |
|     |       |              | Peugeot 205 T16                             | 306 |
|     |       |              | Chevrolet Camaro ZL1                        | 306 |
|     |       |              | Toyota Supra MKIV                           | 306 |
| 19. | Tyre  | [            | .tyre<br>]                                  | 308 |
|     | A.    |              | Description                                 | 308 |
|     |       | I.           | Role<br>in<br>the<br>stack                  | 308 |
|     |       | II.          | What<br>you<br>are<br>really<br>tuning      | 308 |
|     |       | III.         | Architecture                                | 309 |
|     |       |              | 1 - Header (schema 1-3)                     | 309 |
|     |       |              | 2 - Structure and model (schema 4-5)        | 309 |

| 309<br>309<br>309<br>309<br>310<br>310<br>310<br>310<br>313<br>321<br>321<br>321<br>321<br>323<br>325<br>329 |
|--------------------------------------------------------------------------------------------------------------|
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
|                                                                                                              |
| 329                                                                                                          |
| 329                                                                                                          |
| 329                                                                                                          |
| 330                                                                                                          |
| 330                                                                                                          |
| 330                                                                                                          |
| 330                                                                                                          |
|                                                                                                              |
| 330                                                                                                          |
| 330                                                                                                          |
| 330                                                                                                          |
| 330                                                                                                          |
| 330                                                                                                          |
| 331                                                                                                          |
| 331                                                                                                          |
| 332                                                                                                          |
| 334                                                                                                          |
|                                                                                                              |

| II. | Example        | 334 |
|-----|----------------|-----|
|     | Audi RS6 Avant | 334 |
|     | Lotus Emira    | 336 |
|     | Ferrari SF-25  | 338 |

# <span id="page-16-0"></span>**1. Brake System [ .brakesystem ]**

### <span id="page-16-1"></span>**A. Description**

Vehicle-wide braking authority: how hard the car can stop, how that force is split front/rear, and how electronic helpers (EBB, steer-brake, hybrid brake blending) reshape that split in real time.

Per-corner pad/disc thermal and friction behaviour lives in linked .brakes compounds — this asset points at them and sets the global hydraulic picture.

### <span id="page-16-2"></span>**I. Role in the stack**

| Concern                                         | Handled here        | Handled elsewhere  |
|-------------------------------------------------|---------------------|--------------------|
| Peak stopping torque, static bias,<br>handbrake | .brakesystem        | —                  |
| Pad/disc heat, fade, wear μ(T)                  | Paths → .brakes     | Asset 2. Brakes    |
| ABS / TC slip maps                              | —                   | .carelectronics    |
| Setup bias overrides                            | Cockpit bias fields | .carsetup / limits |

Car Data (or equivalent) load one .brakesystem per vehicle. Without it, the sim has no global brake torque or bias baseline.

### <span id="page-16-3"></span>**II. What you are really tuning**

- 1. **Raw decelerating power** *Total Torque* is the ceiling when the pedal is fully down (examples: Delta ~2800 Nm, GTAm ~4100 Nm, 296 GT3 ~4300 Nm, SF-25 ~5500 Nm). Raise it and the car stops harder *if* the tyres and compounds can take it; otherwise you just lock earlier.
- 2. **Static platform** *Front Bias* is the default axle split before electronics. Street/GT cars often sit around 0.65–0.78 (or 65–78 depending on authoring scale — check whether the car stores a 0–1 ratio or a percent-like float). Too far forward → early front lock / understeer on turn-in; too far rear → snap oversteer under heavy braking.
- 3. **Driver authority** *Has Cockpit Bias* + *Bias Step* expose in-car balance clicks (true on 296 GT3 / SF-25; false on GTAm / Delta). Step is the increment per press.
- 4. **Handbrake** *Hand Brake Torque* is a separate channel (often rear-biased). Rally/AWD cars may use a large value (Delta 1300 Nm); pure race cars may leave it near zero (SF-25).
- 5. **Compound links** *Front/Rear Compound Path* attach .brakes assets. GT3 examples point at shared racing pads; many road cars leave them None until compounds are wired.
- 6. **Live redistribution** Controllers rewrite bias (or torque) from telemetry through staged LUT pipelines. That is where modern "smart" braking and hybrid brake-by-wire live.

### <span id="page-16-4"></span>**III. Architecture**

### <span id="page-16-5"></span>**1 - MECHANICAL BASELINE**

Fields 1-7: torque, bias, handbrake, cockpit adjusters, compound paths. This is enough for a simple car with EBB off.

### <span id="page-17-0"></span>**2 - CONTROLLERS (SHARE STAGE PATTERN)**

Four controller slots reuse the same stage recipe (*Name* + *Stages[]*):

| Block                  | Typical job                                                               |
|------------------------|---------------------------------------------------------------------------|
| Controller EBB         | Single EBB pipeline (legacy / simpler cars)                               |
| Controllers EBB [x]    | Multiple named EBB pipelines (e.g. SF-25 migration<br>maps Mig0, Mig2 … ) |
| Steer Brake Controller | Micro brake / yaw assist from steer or yaw-delta<br>inputs                |
| Torque Controller EBB  | Scales total brake torque (lockup protection, region<br>blending)         |

#### Each **stage** is one closed loop :

- 1. Read an *Input Var* (Brake, LatG, LoadSpreadLF, SlipAngleRearMAX, ErsCoastTorque, …).
- 2. Map it through a *LUT* (.curve).
- 3. Combine with previous stages via *Add* or *Multiply*.
- 4. Smooth with *Filter Gain*, camp with *Up/Down Limit*.
- 5. *Current Value* is runtime; *Const Value* is a static fallback when input is **Const** or unused.

### <span id="page-17-1"></span>**3- EBB MODE SWITCH**

| Mode                         | Meaning                                                                           |
|------------------------------|-----------------------------------------------------------------------------------|
| ebbDisabled                  | Static bias only (common in simpler examples even<br>when controller trees exist) |
| ebbInternal                  | Engine built-in distribution logic                                                |
| ebbDynamicControllerAbsolute | Custom stages drive absolute balance                                              |
| ebbDynamicControllerRelative | Custom stages offset the base bias                                                |

**EBB Front Multiplier** scales how aggressively EBB can push front authority. **EBB Min Speed** gates the system below a speed threshold (0 = always eligible).

### <span id="page-17-2"></span>**IV. How to read the examples**

### <span id="page-17-3"></span>**1 - ALFA GIULIA GTAM / LANCIA DELTA**

Mechanical baseline filled; a Controller EBB tree exists (load transfer, slip angle, pedal), but **EBB Mode = ebbDisabled**, so those stages are dormant unless mode is switched. Useful as templates for enabling dynamic bias later.

### <span id="page-18-0"></span>**2 - FERRARI 296 GT3**

Strong total torque, cockpit bias on, shared GT3 .brakes pads front/rear, controllers empty, EBB disabled. Classic "race car with adjustable static bias + proper compounds."

### <span id="page-18-1"></span>**3 - FERRARI 296 GT3**

Highest torque, fine cockpit steps, no handbrake. Several **Controllers EBB** named migration maps combine **Brake** with **ErsCoastTorque** LUTs under kers/ebb/ — hybrid brake blending between hydraulic and regen drag. This is the reference pattern for ERS-aware brake systems.

### <span id="page-18-2"></span>**V. Practical notes**

- Controllers present ≠ controllers active. Always check **EBB Mode**.
- Bias units are not always written the same way across cars (ratio vs percent-like). Compare against known good cars of the same authoring style before copying values blindly.
- Compound paths (*None*) mean thermal/fade behaviour is incomplete even if torque numbers look raceready.
- Steer-brake and torque-EBB blocks are powerful; leave them *None* until you have LUTs and a clear stability goal.
- Schema typo: **Troque Controller EBB** = Torque Controller EBB.

### <span id="page-18-3"></span>**VI. Related assets**

- **2. Brakes [\[.brakes\]](#page-27-0)** pad/disc thermal & friction curves referenced by compound paths
- **9. Car Electronics [\[.carelectronics\]](#page-205-0)** ABS/TC (wheel slip intervention, not bias)
- **5-7. Car [Setup](#page-102-0) / [Limits](#page-118-0) / [Units](#page-174-0)** garage bias and display mapping when cockpit adjust is enabled

### <span id="page-18-4"></span>**B. Schema**

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
```

```
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
├ 11. Torque Controller EBB : object with an array of stages within 
│ ├ 8a. Name : string
│ ├ 8b. Stages [x] : object | Torque Controller EBB can have multiple 
stages 
│ │ ├ 8b1. Input Var : enum 
│ │ ├ 8b2. Combinator Mode : enum 
│ │ ├ 8b3. Lut : string - path 
│ │ ├ 8b4. Filter Gain : float 
│ │ ├ 8b5. Up Limit : float 
│ │ ├ 8b6. Down Limit : float 
│ │ ├ 8b7. Current Value : float 
│ └ └ 8b8. Const Value : float
├ 12. EBB Mode : enum
├ 13. EBB Front Multiplier : float
└ 14. EBB Min Speed : float
```

### **Enum List - Brake System**

| Enum           | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input Var      | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear,<br>SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX,<br>SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG,<br>SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor,<br>RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG,<br>LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR,<br>SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight,<br>ErsChargeLevel, ErsCoastTorque |
| CombinatorMode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                                               |
| EBB Mode       | ebbDisabled, ebbInternal, ebbDynamicControllerAbsolute,<br>ebbDynamicControllerRelative                                                                                                                                                                                                                                                                                                                                                                |

### <span id="page-20-0"></span>**C. Measurement Units & Descriptions**

| ID   | Name                | Unit of Measurement                      | Description                                                                                                       |
|------|---------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 1.   | Total Torque        | Nm ( Newton-meters )                     | Defines the maximum total braking<br>torque available for the entire<br>vehicle.                                  |
| 2.   | Front Bias          | % ( Percentage / Distribution<br>ratio ) | Sets the percentage of total<br>braking torque allocated to the<br>front axle (e.g., 0.60 = 60%).                 |
| 3.   | Hand Brake Torque   | Nm ( Newton-meters )                     | Specifies the maximum braking<br>torque applied by pulling the<br>mechanical handbrake.                           |
| 4.   | Has Cockpit Bias    | None ( Boolean : True /<br>False )       | Toggles whether the driver can<br>adjust the brake balance manually<br>from inside the cockpit while<br>driving.  |
| 5.   | Bias Step           | % ( Percentage increment )               | The step size by which the brake<br>bias changes per click when<br>adjusted (e.g., 0.005 for 0.5%<br>increments). |
| 6.   | Front Compound Path | None ( File path )                       | Points to the physics/lookup file<br>defining the friction and thermal<br>properties of the front brake pads.     |
| 7.   | Rear Compound Path  | None ( File path )                       | Points to the physics/lookup file<br>defining the friction and thermal<br>properties of the rear brake pads.      |
| 8a.  | Name                | None ( String )                          | An internal label or identifier for<br>the specific brake controller or<br>modifier stage.                        |
| 8b1. | Input Var           | None ( Telemetry enum )                  | The telemetry variable used as the<br>trigger input for this controller<br>(e.g., SteerDEG, Brake, Speed).        |

| ID   | Name                 | Unit of Measurement                  | Description                                                                                                        |
|------|----------------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| 8b2. | Combinator Mode      | None ( Math enum : Add / Mult )      | Determines how this stage's output combines with the baseline value (Addition or Multiplication).                  |
| 8b3. | Lut                  | None ( .curve file path )            | References a Look-Up Table curve file that maps the raw input value to a specific output factor.                   |
| 8b4. | Filter Gain          | Coefficient ( Smoothing multiplier ) | Controls the input signal smoothing filter; acts as a dampener to prevent sudden spikes in controller application. |
| 8b5. | Up Limit             | Depends on the input variable        | The upper bounding limit for the input signal, clamping values that exceed this threshold.                         |
| 8b6. | Down Limit           | Depends on the input variable        | The lower bounding limit for the input signal, clamping values that fall below this threshold.                     |
| 8b7. | Current Value        | Depends on the input variable        | The current, real-time value processed by the controller during simulation.                                        |
| 8b8. | Const Value          | Depends on the input variable        | A fallback fallback constant value used if no dynamic input curve or telemetry is active.                          |
| 12.  | EBB Mode             | None ( Mode enum )                   | Selects the operational logic profile for the Electronic Brake Balance system.                                     |
| 13.  | EBB Front Multiplier | Coefficient ( Scaling factor )       | Scaling factor that dynamically adjusts the front brake bias authority under EBB intervention.                     |
| 14.  | EBB Min Speed        | Km/h or m/s * ( Spped threshold )    | The minimum vehicle speed below which the Electronic Brake Balance system deactivates.                             |

### <span id="page-21-0"></span>D. Example data

## <span id="page-21-1"></span>I. Chosen Cars for Example

- Alfa Romeo Giulia GTAm (slug : ks\_alfa\_romeo\_giulia\_gtam)Lancia Delta HF Integrale EVO II (slug : ks\_lancia\_delta\_hf\_integrale\_evo\_ii)
- Ferrari 296 GT3 ( slug : ks\_ferrari\_296\_gt3 )
- Ferrari SF25 (slug: ks ferrari sf 25)

### <span id="page-21-2"></span>II. Example

### <span id="page-21-3"></span>Alfa Romeo Giulia GTAm

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
├ 11. Torque Controller EBB : None 
├ 12. EBB Mode : ebbDisabled 
├ 13. EBB Front Multiplier 1.10000 
└ 14. EBB Min Speed : 0.00000
   Lancia Delta HF Integrale EVO II ( slug : ks_lancia_delta_hf_integrale_evo_ii )
├ 1. Total Torque : 2800.00000
├ 2. Front Bias : 0.78000 
├ 3. Hand Brake Torque : 1300.00000 
├ 4. Has Cockpit Bias : false
```

<span id="page-22-0"></span>├ 5. Bias Step : 0.00000

├ 6. Front Compound Path : None

```
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
├ 11. Torque Controller EBB : None 
├ 12. EBB Mode : ebbDisabled 
├ 13. EBB Front Multiplier 1.20000 
└ 14. EBB Min Speed : 0.00000
```

### <span id="page-23-1"></span><span id="page-23-0"></span>**Ferrari 296 GT3**

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
├ 10. Steer Brake Controller : None 
├ 11. Torque Controller EBB : None 
├ 12. EBB Mode : ebbDisabled 
├ 13. EBB Front Multiplier 0.00000 
└ 14. EBB Min Speed : 0.00000
```

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
```

```
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
```

```
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
├ 11. Torque Controller EBB : None 
├ 12. EBB Mode : ebbDynamicControllerRelative 
├ 13. EBB Front Multiplier 0.00000 
└ 14. EBB Min Speed : 0.00000
```

# <span id="page-27-0"></span>**2. Brakes [ .brakes ]**

### <span id="page-27-1"></span>**A. Description**

Hardware-level brake physics for pads and discs: how friction builds with temperature, how heat enters and leaves the assembly, and how material wears away over a stint.

The .brakesystem asset commands *how much* brake torque to ask for and how to split it. This asset decides whether that torque is still available after heat, fade, rain, and wear have done their work.

### <span id="page-27-2"></span>**I. Role in the stack**

| Concern                                 | Handled here          | Handled elsewhere      |
|-----------------------------------------|-----------------------|------------------------|
| Pad/disc thermal mass, cooling,<br>fade | .brakes               | —                      |
| Wear thickness and μ loss per<br>mm     | .brakes               | —                      |
| Friction vs temperature curve           | .brakes → Perf Curve  |                        |
| Peak torque, bias, EBB,<br>handbrake    | —                     | 1. Brake System        |
| ABS / TC                                | —                     | .carelectronics        |
| Brake duct / cooling setup clicks       | Cooling responds here | .carsetup aero / ducts |

Referenced from Brake System via **Front / Rear Compound Path**. One file can serve a single axle (vintage front/rear split) or the whole car (shared GT3 pad compound).

### <span id="page-27-3"></span>**II. What you are really tuning**

- 1. **Cooling balance** *Cool Transfer* is the stationary ambient cooling rate. *Cool Speed Factor* scales cooling with vehicle speed (air through ducts). *Rain Cool Factor* boosts dissipation when wet. Together they set whether brakes stabilise or cook over a lap.
- 2. **Torque conversion** *Torque K* scales how efficiently commanded hydraulic effort becomes stopping torque at the disc. Same Brake System torque with a lower *Torque K* feels weaker or softer at the pedal.
- 3. **Thermal mass and conduction** *Thermal Capacity* (surface) and *Core Thermal Capacity* (bulk disc) set how fast temperature rises. *Thermal Conductivity* + *Conduction Thickness* move heat from the hot friction face into the core. *Emissivity* and *Surface* add radiation and exposed area for high-temp cooling.
- 4. **Wear life** *Disk / Pad Thickness* are brand-new thicknesses (mm). *Disk / Pad Consumption Rate* burn material under load/heat. *T Reference Wear* is the temperature above which wear accelerates. Endurance compounds (GT3 pad2) show much lower consumption than vintage road pads.

- 5. **Wear → performance loss** As thickness drops, *Perf Decrease M M*, *Mu Reduction M M*, *Area Reduction M M*, and *Gamma Correction M M* degrade bite, friction, contact area, and pedal feel. These are the endurance "brakes get longer" knobs.
- 6. **Temperature window** *Perf Curve* maps disc temperature (°C) → friction efficiency (1.0 = full target μ). Shape of that curve is the compound's personality: cold bite, sweet spot, and fade cliff.

### <span id="page-28-0"></span>**III. Architecture**

### <span id="page-28-1"></span>**1 - THERMAL MODELLING (SCHEMA 1-10)**

Cooling coefficients, emissivity, exposed surface, surface/core heat capacity, conductivity, and conduction depth. This block decides lap-to-lap temperature stability.

### <span id="page-28-2"></span>**2 - DIMENSIONS AND WEAR (SCHEMA 11-19)**

Consumption rates, initial thicknesses, per-millimetre performance penalties, and the wear temperature reference. Fields labelled **M M** mean "per millimetre of material lost."

### <span id="page-28-3"></span>**3 - PERFORMANCE CURVE (SCHEMA 20)**

External .curve LUT: X = temperature (°C), Y = friction efficiency modifier. The Brake System asks for torque; this curve says how much of the pad's potential is actually online at the current temperature.

### <span id="page-28-4"></span>**IV. How to read the examples**

### <span id="page-28-5"></span>**1 - VINTAGE ROAD FRONT / REAR (SPLIT AXLE)**

Two separate .brakes files: one for the front axle, one for the rear.

The thermal and wear numbers are almost the same on both (capacity, thickness, consumption). What differs is the **Perf Curve** path: front uses tcurve\_vintage\_front.curve, rear uses tcurve\_vintage\_rear.curve. That is the split-axle pattern: each axle can have its own temperature-to-friction behaviour, even when the hardware specs match.

On the vintage curve, cold bite is already high (about 0.90 at 0 °C), so the brakes work with little warm-up. Peak efficiency (about 1.0) sits around 600 °C, then fades gently toward about 0.80 at 1200 °C. Wear rates are relatively high (about 0.18 disc / 0.20 pad) compared with race endurance pads.

### <span id="page-28-6"></span>**2 - RACING GT3 PAD 2 (SHARED COMPOUND)**

One master .brakes file reused front and rear from Brake System compound paths. Larger *Surface* (0.40 vs 0.20), much lower consumption (about 0.0105 disc / 0.021 pad), earlier *T Reference Wear* (500 °C). Perf Curve is denser and stays high through a wide mid band, then drops harder past about 900-1000 °C: a race pad that wants heat but lasts longer in a stint. Cars often swap compounds by pointing both axles at another shared file (for example pad1 vs pad2), rather than authoring separate front/rear hardware.

### <span id="page-29-0"></span>**V. Practical notes**

- Brake System torque without a real .brakes path (*None*) means incomplete fade/wear: stopping power will not behave like a race car under heat.
- Split front/rear files when hardware or thermal load differs; share one compound file when the car swaps pads as a package (GT3).
- Read the Perf Curve before chasing *Total Torque*: a cold-weak race pad needs warm-up; a street curve that is already at 0.9 cold will feel strong immediately.
- High Cool Speed Factor couples strongly to duct / ride-height aero setup: brake temps are not only a .brakes problem.
- Wear fields are slow variables: they matter for endurance and long sessions more than a single qualifying lap.

### <span id="page-29-1"></span>**VI. Related assets**

- **1. Brake System [\[.brakesystem\]](#page-16-0)** torque, bias, compound paths that load this file
- **5. Car Setup [\[.carsetup\]](#page-102-0)** ducts / cooling-related setup that change effective cooling
- **19. Tyre [\[.tyre\]](#page-307-0)** separate thermal world; brake heat can couple via tyre thermal transfer factors when modelled

### <span id="page-29-2"></span>**B. Schema**

```
├ 1. Cool Transfer : float
├ 2. Torque K : float
├ 3. Cool Speed Factor : float
├ 4. Rain Cool Factor : float
├ 5. Emissivity : float
├ 6. Surface : float
├ 7. Thermal Capacity : float
├ 8. Core Thermal Capacity : float
├ 9. Thermal Conductivity : float
├ 10. Conduction Thickness : float
├ 11. Disk Consumption Rate : float
├ 12. Pad Consumption Rate : float
├ 13. Disk Thickness : float
├ 14. Pad Thickness : float
├ 15. Perf Decrease M M : float
├ 16. Gamma Correction M M : float
├ 17. Mu Reduction M M : float
├ 18. Area Reduction M M : float
├ 19. T Reference Wear : float
└ 20. Perf Curve : string - path
```

### <span id="page-29-3"></span>**C. Measurement Units & Descriptions**

| ID  | Name                  | Unit of Measurement         | Description                                                                                                                                                                             |
|-----|-----------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2.  | Torque Conversion / K | Dimensionless Factor        | Mechanical torque conversion<br>multiplier; scales how effi<br>ciently<br>hydraulic line pressure translates<br>into raw stopping torque.                                               |
| 3.  | Cool Speed Factor     | Coeffi<br>cient             | Airflow cooling multiplier; dictates<br>the linear or non-linear scaling of<br>heat dissipation as the vehicle<br>speed increases.                                                      |
| 4.  | Rain Cool Factor      | Dimensionless Ratio         | Wet-weather cooling modifier;<br>amplifies the global heat<br>dissipation rate to simulate rain<br>and track water spray striking the<br>brake assembly.                                |
| 5.  | Emissivity            | Dimensionless ( 0.0 - 1.0 ) | ε<br>Thermal radiation effi<br>ciency ( );<br>defines how effectively the brake<br>material radiates infrared heat,<br>becoming highly critical at<br>glowing, high-temperature states. |
| 6.  | Surface               | 2<br>m ( Square meters )    | Total physical exposed surface<br>area of the brake disc/assembly;<br>larger surfaces naturally facilitate<br>faster convective cooling.                                                |
| 7.  | Thermal Capacity      | J/K or J/°C                 | Heat storage capacity of the thin<br>outer friction surface layer;<br>determines how quickly the<br>contact zone heats up under<br>friction.                                            |
| 8.  | Core Thermal Capacity | J/K or J/°C                 | Heat storage capacity of the<br>internal "core" mass of the brake<br>disc; serves as the main thermal<br>reservoir absorbing energy from<br>the surface.                                |
| 9.  | Thermal Conductivity  | W/(m-K) or Coeffi<br>cient  | Internal heat transfer rate; controls<br>how fast heat energy moves from<br>the hot outer friction surface into<br>the cooler internal core.                                            |
| 10. | Conduction Thickness  | m (Meters) or mm            | Physical distance/depth<br>representing the boundary layer<br>for internal heat transfer between<br>the surface friction node and the<br>core mass.                                     |
| 11. | Disk Consumption Rate | Wear Coeffi<br>cient        | Material wear rate of the brake<br>disc/rotor, tracking physical<br>thickness reduction relative to<br>temperature and kinetic energy<br>absorption cycles.                             |
| 12. | Pad Consumption Rate  | Wear Coeffi<br>cient        | Material wear rate of the brake<br>pads, tracking friction compound<br>depletion relative to temperature<br>and kinetic energy absorption<br>cycles.                                    |

| ID  | Name                    | Unit of Measurement       | Description                                                                                                                                                                 |
|-----|-------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 13. | Disk Thickness          | mm ( Millimeters )        | The initial, brand-new physical<br>structural thickness of the brake<br>disc/rotor.                                                                                         |
| 14. | Pad Thickness           | mm ( Millimeters )        | The initial, brand-new physical<br>thickness of the wearable friction<br>material layer on the brake pad.                                                                   |
| 15. | Perf Decrease M M       | ) −1<br>% / mm ( mm       | Global percentage drop in overall<br>braking effi<br>ciency and biting<br>performance for every single<br>millimeter of total pad/disk<br>material lost to wear.            |
| 16. | Gamma Correction M<br>M | Dimensionless Exponent    | Non-linear scaling factor;<br>progressively adjusts how material<br>wear non-linearly alters pedal<br>feedback, compliance, and friction<br>behavior over time.             |
| 17. | Mu Reduction M M        | Δμ<br>/mm                 | The literal linear reduction of the<br>raw friction coeffi<br>cient (\$\mu\$)<br>applied as the pads and discs<br>become thinner.                                           |
| 18. | Area Reduction M M      | or 2 /mm<br>m<br>%<br>/mm | The progressive reduction of the<br>effective pad-to-disc contact<br>surface area as the pad material<br>shaves down.                                                       |
| 19. | T Reference Wear        | °C ( Degress Celsius )    | Threshold reference temperature;<br>defines the thermal boundary<br>above which component wear<br>rates begin to spike exponentially.                                       |
| 20. | Perf Curve              | None ( File path )        | File path pointing to an<br>external .curve look-up table<br>mapping raw operating<br>temperature (X-axis in °C) to<br>friction coeffi<br>cient effi<br>ciency (Y<br>axis). |

### <span id="page-31-0"></span>**D. Example data**

### <span id="page-31-1"></span>**I. Chosen Brakes for Example**

- Vintage Road Front ( slug : vintage\_road\_front ) / Vintage Road Rear ( vintage\_road\_rear )
- Racing GT3 [ Pad 2 ] ( slug : racing\_gt3\_pad2 )

### <span id="page-31-2"></span>**II. Example**

### <span id="page-31-3"></span>**Vintage Road [ Front ]**

├ 1. Cool Transfer : 1.30000

├ 2. Torque K : 0.70000

- ├ 3. Cool Speed Factor : 1.50000 ├ 4. Rain Cool Factor : 0.80000
- ├ 5. Emissivity : 0.70000 ├ 6. Surface : 0.20000
- ├ 7. Thermal Capacity : 100.00000
- ├ 8. Core Thermal Capacity : 1600.00000 ├ 9. Thermal Conductivity : 250.00000 ├ 10. Conduction Thickness : 0.00500 ├ 11. Disk Consumption Rate : 0.18000 ├ 12. Pad Consumption Rate : 0.19800
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
| P2 | 500.000              | 0.980                                   |
| P3 | 600.000              | 1.000                                   |
| P4 | 800.000              | 0.980                                   |
| P5 | 900.000              | 0.950                                   |
| P6 | 1000.000             | 0.850                                   |
| P7 | 1200.000             | 0.800                                   |

*Friction Coefficient Modifier = Performance Efficiency where 1.000 = 100%*

### <span id="page-32-0"></span>**Vintage Road [ Rear ]**

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

├ 15. Perf Decrease M M : 15.00000 ├ 16. Gamma Correction M M : 1.50000 ├ 17. Mu Reduction M M : 0.01000 ├ 18. Area Reduction M M : 0.16000

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
| P7 | 1200.000             | 0.800                                   |

*Friction Coefficient Modifier = Performance Efficiency where 1.000 = 100%*

### <span id="page-33-0"></span>**Racing GT3 [ Pad 2 ]**

├ 1. Cool Transfer : 0.90000

├ 2. Torque K : 0.70000

├ 3. Cool Speed Factor : 1.60000 ├ 4. Rain Cool Factor : 0.80000

├ 5. Emissivity : 0.70000

├ 6. Surface : 0.40000

├ 7. Thermal Capacity : 100.00000

├ 8. Core Thermal Capacity : 1600.00000 ├ 9. Thermal Conductivity : 250.00000 ├ 10. Conduction Thickness : 0.00500 ├ 11. Disk Consumption Rate : 0.01050

├ 12. Pad Consumption Rate : 0.02100

├ 13. Disk Thickness : 32.00000 ├ 14. Pad Thickness : 29.00000

├ 15. Perf Decrease M M : 13.00000

├ 16. Gamma Correction M M : 1.00000

├ 17. Mu Reduction M M : 0.01000

├ 18. Area Reduction M M : 0.08000 ├ 19. T Reference Wear : 500.00000

└ 20. Perf Curve :

content\cars\common\_phsx\brakes\racing\tcurve\_racing\_GT3\_pad2

|     | °C Temperature ( X ) | Friction Coeffi<br>cient Modifier ( Y ) |
|-----|----------------------|-----------------------------------------|
| P1  | -0.905               | 0.839                                   |
| P2  | 39.477               | 0.914                                   |
| P3  | 88.596               | 0.952                                   |
| P4  | 121.867              | 0.967                                   |
| P5  | 156.821              | 0.974                                   |
| P6  | 203.872              | 0.978                                   |
| P7  | 252.036              | 0.980                                   |
| P8  | 303.284              | 0.980                                   |
| P9  | 365.345              | 0.980                                   |
| P10 | 380.803              | 0.979                                   |
| P11 | 443.598              | 0.977                                   |
| P12 | 526.801              | 0.973                                   |
| P13 | 599.594              | 0.966                                   |
| P14 | 722.684              | 0.945                                   |
| P15 | 781.584              | 0.936                                   |
| P16 | 849.036              | 0.923                                   |
| P17 | 908.993              | 0.898                                   |
| P18 | 972.698              | 0.854                                   |
| P19 | 1047.645             | 0.734                                   |
| P20 | 1245.218             | 0.567                                   |

*Friction Coefficient Modifier = Performance Efficiency where 1.000 = 100%*

# <span id="page-35-0"></span>**3. Car Data [ .car ]**

### <span id="page-35-1"></span>**A. Description**

The vehicle master file: mass, inertia footprint, chassis geometry, fuel payload, and the path list that wires every other physics asset into one car.

If Brake System / Brakes are the stopping hardware, Car Data is the carcass and the bill of materials. Without it, the sim has nowhere to hang engine, gearbox, suspension, tyres, or aero.

### <span id="page-35-2"></span>**I. Role in the stack**

| Concern                                                 | Handled here                       | Handled elsewhere                      |
|---------------------------------------------------------|------------------------------------|----------------------------------------|
| Total mass, fuel mass, tank<br>position                 | .car General                       | —                                      |
| Wheelbase, track, CG location,<br>ride refs             | .car Suspensions                   | Kinematics detail in .suspension       |
| Chassis torsion / damping                               | .car General                       | —                                      |
| Paths to engine, gearbox, clutch,<br>drivetrain, brakes | .car path fields                   | Individual assets 4, 13, 14, 10,<br>1… |
| Tyre compound lists                                     | Front / Rear Tyre Compounds        | Grip/thermal in .tyre                  |
| Aero maps, DRS, ERS hooks                               | Aero / Drs / Ers blocks            | .wing, .surface3d, electronics         |
| Garage presets and limits                               | Setup / Performance Modes<br>paths | .carsetup, limits, units               |

One Car Data file per vehicle configuration. Other assets are modules this file references.

### <span id="page-35-3"></span>**II. What you are really tuning**

- 1. **Mass and fuel** *Total Mass* is the baseline vehicle mass used for F=ma (examples: Renault 5 about 910 kg, R8 GT3 about 1355 kg, 296 GTB about 1750 kg). *Fuel* / *Max Fuel* plus *Kg Per Liter* and *Tank Position* make mass and CG move as the tank empties — endurance balance drift lives here, not in the tyre file.
- 2. **Plan footprint** *Wheel Base*, *Track Front* / *Track Rear,* and *Longitudinal Cg Location* set the geometric DNA. Long wheelbase + mid CG (296 about 0.40 from the front reference) feels planted; short wheelbase + forward CG (R5 about 0.64) feels darty and nose-heavy. Narrow track (R5 about 1.34 m) rolls and rotates differently from a GT3 track (about 1.67 m).
- 3. **Vertical references** *Base Y Front* / *Base Y Rear*, pickup heights, and *Minimum Height* / *Check Rules* anchor ride height and regulatory floors (R8 enables rule checks with a minimum height value; road cars often leave checks off).
- 4. **Chassis stiffness**—*Torsional Stiffness* and *Torsional Damping* model the body as a flexible beam between axles. Soft shells (R5 about 11000) twist and muddy platform control; race tubs (R8 about 40000) stay flatter so ARBs and springs do the real work.

- 5. **Module wiring** Path fields (*Engine Path*, *Gearbox Path*, *Clutch Path*, *Drivetrain Path*, *Brakes Path*, coilover / suspension paths, electronics, setup presets) decide which concrete assets this car loads. Wrong path = silent fallback or broken car, even if the numbers in General look fine.
- 6. **Driver controls and aids hooks** *Steering System* (steer lock, rack behaviour), *Electronics* / *Electronics Path*, *Controls*, tyre compound arrays, *Aero* / *Drs* / *Ers*, and *Performance Modes* expose how the car is driven and which packages can be swapped.

### <span id="page-36-0"></span>**III. Architecture**

### <span id="page-36-1"></span>**1 - IDENTITY AND GENERAL (SCHEMA 1-3)**

Screen names, mass, fuel economy block, body box, pickup heights, rule flags, torsional pair, optional body mesh offset. *General Path* can point at a shared .general override when used.

### <span id="page-36-2"></span>**2 - SUSPENSIONS HUB (SCHEMA 4)**

Not the full kinematic hardpoints — those live in .suspension / .coilover. Here you get axle geometry (wheelbase, tracks, CG, base Y), damage thresholds, paths to front/rear coilover and suspension, optional heavy springs, ARB / flex-bar stiffness (and their dynamic controllers), and damper cockpit flags.

### <span id="page-36-3"></span>**3 - POWERTRAIN AND BRAKE PATHS (SCHEMA 5-9)**

Pointers to .drivetrain, .gearbox, .clutch, .carengine, and the brake system asset. This is the assembly list for longitudinal physics.

### <span id="page-36-4"></span>**4 - DRIVER, COLLISION, TIRES (SCHEMA 10-16)**

Steering system, electronics (inline and/or path), controls, box colliders, front/rear tyre compound lists.

### <span id="page-36-5"></span>**5 - AERO AND HYBRID (SCHEMA 17-19)**

Aero package (downforce elements, surface3d maps, wings path), DRS connections, ERS / hybrid hooks when present.

### <span id="page-36-6"></span>**6 - SETUPS, MESH, AI, MODES (SCHEMA 20-28)**

Setup limits path, collider/body mesh, stock / AI / wet setups, performance mode packages, AI car data, and residual fields (including *mm* in the schema tree).

### <span id="page-36-7"></span>**IV. How to read the examples**

### <span id="page-36-8"></span>**1 - FERRARI 296 GTB (ROAD MID-ENGINE)**

Heavy total mass (1750 kg), 2.60 m wheelbase, wide tracks (about 1.72 m), longitudinal CG about 0.40 (mass biased rearward of geometric mid). Torsional stiffness 30000. Large tank (max 120 L) with a defined tank position — fuel burn will move balance. Full path set to its own coilover, suspension, drivetrain, gearbox, clutch, engine, brakes. Road-car style: rules check off.

### <span id="page-37-0"></span>**2 - AUDI R8 LMS GT3 EVO II (RACE GT3)**

Lighter race mass (1355 kg), longer wheelbase (2.70 m), CG about 0.42, tracks about 1.67 m. Stiffer tub (40000) and much stiffer ARBs (front about 56800, rear about 39900). *Check Rules* true with a minimum height set — BoP / regulatory awareness. Efficiency non-zero. Same modular path pattern, aimed at shared race compounds and setups.

### <span id="page-37-1"></span>**3 - RENAULT 5 GT TURBO (LIGHT FWD HOT HATCH)**

Light (910 kg), short wheelbase (2.41 m), narrow tracks (about 1.34 / 1.32 m), longitudinal CG about 0.64 (nose-heavy). Soft torsional stiffness (11000) and soft ARBs; flex bar rear present. Small tank (max 50 L). High steer lock (630 in the example) versus GT cars. Shows how Car Data alone already predicts a nervous, front-driven road car before you open the suspension files.

### <span id="page-37-2"></span>**V. Practical notes**

- Fix mass, CG, wheelbase, and tracks before chasing setup springs: wrong Car Data geometry cannot be "tuned away" in the garage.
- Longitudinal CG location is a fraction along the wheelbase compare cars from the same authoring style before copying.
- Fuel tank position matters for stint balance; a rear tank that empties forward is a different car at the end of a race.
- Path fields are load-bearing: a typo in *Engine Path* or suspension path breaks the car even if General looks perfect.
- *Check Rules* / *Minimum Height* are easy to miss on race cars and can fight your ride-height setup.
- Schema label in the source TOC is .car; on disk the asset is still the Car Data package that references the other extensions.

### <span id="page-37-3"></span>**VI. Related assets**

- **15. General [\[.generalcar\]](#page-270-0)** optional shared general block via *General Path*
- **11 / 17. [Coilover](#page-226-0) / [Suspension](#page-286-0)** loaded from Suspensions paths
- **4 / 13 / 14 / 10. [Engine](#page-87-0) / [Drivetrain](#page-245-0) / [Gearbox](#page-261-0) / [Clutch](#page-221-0)** powertrain paths
- **1. Brake System [\[.brakesystem\]](#page-16-0)** *Brakes Path*
- **19 / 16 / 20. [Tyre](#page-307-0) / [Surface](#page-275-0) 3D / [Wing](#page-328-0)** compounds and aero hooks
- **5-7. Car [Setup](#page-102-0) / [Limits](#page-118-0) / [Units](#page-174-0)** garage presets and limits paths

### <span id="page-37-4"></span>**B. Dependency map**

Wiring chart for what .car **(Car Data)** loads, what those assets load next, and what only *overlays* or *selects* without owning a path.

#### **Legend**

| Link type     | Meaning                                                         |
|---------------|-----------------------------------------------------------------|
| Load          | Path string (or path list) — A opens B                          |
| Optional load | Path often None; when set, A opens B                            |
| Overlay       | Session / UI values on top of hardware already<br>loaded        |
| Select        | Index or enum into maps / lists defined elsewhere               |
| Override      | Tuning part (or similar) redirects paths that .car<br>would use |

### <span id="page-38-0"></span>**I. Direct loads from Car Data**

| Car Data field / block (typical) | Loads               | Description                                                          |
|----------------------------------|---------------------|----------------------------------------------------------------------|
| General (inline)                 | —                   | Mass, fuel, torsion, etc. live here<br>when no external general file |
| General Path                     | 15. General         | Optional shared general block —<br>usually None in shipped cars      |
| Coilover Front / Rear Path       | 11. Coilover        | Spring-damper units                                                  |
| Front / Rear Suspension Path     | 17. Suspension      | Kinematic hardpoints                                                 |
| Drivetrain Path                  | 13. Drivetrain      | Drive layout + diffs / AWD                                           |
| Gearbox Path                     | 14. Gearbox         | Ratios + shift behaviour                                             |
| Clutch Path                      | 10. Clutch          | Clamp + autoclutch                                                   |
| Engine Path                      | 4. Car Engine       | Torque maps, controllers, turbo<br>list                              |
| Brakes Path                      | 1. Brake System     | Global brake torque / bias                                           |
| Electronics / Electronics Path   | 9. Car Electronics  | TC / ABS / EDL / ESP maps                                            |
| Front / Rear Type Compounds [x]  | 19. Tyre            | Compound list per axle                                               |
| Aero → Front / Rear Lift, Drag   | 16. Surface 3D      | CX / CZ platform maps                                                |
| Aero → Wings Path [x]            | 20. Wing            | Discrete aero elements                                               |
| Setup / AI / wet setup paths     | 5. Car Setup        | Garage presets                                                       |
| Setup Limits path                | 6. Car Setup Limits | Min / Max / step                                                     |
| (Via shared / car tooling)       | 7. Car Setup Units  | Display units (often<br>common_phsx)                                 |

### <span id="page-38-1"></span>**II. Second hop — what loaded assets open next**

| From               | Link          | To                    | Notes                                                     |
|--------------------|---------------|-----------------------|-----------------------------------------------------------|
| 1. Brake System    | Load          | 2. Brakes             | Front / rear compound<br>paths                            |
| 4. Car Engine      | Load          | 18. Turbo             | Turbos To Load (0…n)                                      |
| 4. Car Engine      | Load          | .curve                | Power / coast / throttle /<br>controller LUTs             |
| 11. Coilover       | Optional load | 12. Damper Curves     | Damper.Lut List                                           |
| 12. Damper Curves  | Load          | .curve                | Each Damper Lut[x]                                        |
| 10. Clutch         | Optional load | .curve                | Autoclutch up/down<br>profiles, clutch curve              |
| 14. Gearbox        | Optional load | .curve                | Autoblip profile                                          |
| 13. Drivetrain     | Optional load | .curve                | Lock / AWD clutch<br>controller LUTs                      |
| 9. Car Electronics | —             | —                     | Maps are inline; no child<br>physics asset                |
| 19. Tyre           | Load          | .curve                | Wear + thermal<br>performance curves                      |
| 20. Wing           | Load          | .curve                | AOA CL/CD; optional<br>ground-height multi                |
| 16. Surface 3D     | Optional load | paths / CSV           | Downforce h/dh, import<br>tooling — often None            |
| 1. Brake System    | Load          | .curve                | EBB / controller stages<br>when present                   |
| 8. Tuning Parts    | Override      | Any domain path above | Swap engine, drivetrain,<br>setup limits, coilovers,<br>… |

### <span id="page-39-0"></span>**III. Overlay and select layers (not path owners)**

| Asset        | Link type | Acts on                       | What it does                                 |
|--------------|-----------|-------------------------------|----------------------------------------------|
| 5. Car Setup | Overlay   | Coilover / suspension<br>feel | Wheel rates, dampers,<br>bump stops, helpers |
| 5. Car Setup | Overlay   | Tyre                          | Pressures, camber, toe,<br>caster            |
| 5. Car Setup | Select    | 9. Electronics                | TC / ABS / ESC map<br>indices                |
| 5. Car Setup | Select    | 4. Engine / 18. Turbo         | Engine map, boost level<br>when adjustable   |
| 5. Car Setup | Overlay   | 13. Drivetrain                | Diff power / coast /<br>preload              |

| Asset           | Link type | Acts on                                       | What it does                               |
|-----------------|-----------|-----------------------------------------------|--------------------------------------------|
| 5. Car Setup    | Overlay   | 20. Wing + ride height<br>→<br>16. Surface 3D | Wing angles, target<br>heights             |
| 5. Car Setup    | Select    | 19. Tyre lists on .car                        | Compound index                             |
| 6. Setup Limits | Overlay   | Setup UI                                      | Legal min / max / step<br>only             |
| 7. Setup Units  | Overlay   | Setup UI                                      | Labels (bar, °, Ns/m, …)<br>— not SI truth |
| 9. Electronics  | Override  | Paths that .car uses                          | Variant packs (drift, Cup<br>aids, LSD, …) |

### <span id="page-40-0"></span>**IV. By concern**

### <span id="page-40-1"></span>**1 - STOP**

| Step | Asset                  | Role                                          |
|------|------------------------|-----------------------------------------------|
| 1    | .car → 1. Brake System | Peak torque, bias, controllers                |
| 2    | → 2. Brakes            | Pad / disc thermal & friction                 |
| 3    | .car → 9. Electronics  | ABS maps                                      |
| 4    | Setup                  | Bias / ducts overlays; ABS index              |
| 5    | 19. Tyre               | Longitudinal grip that can take<br>the torque |

### <span id="page-40-2"></span>**2 - GO**

| Step | Asset                 | Role                              |
|------|-----------------------|-----------------------------------|
| 1    | .car → 4. Engine      | Torque source                     |
| 2    | 18. Turbo             | Boost / lag when listed           |
| 3    | .car → 10. Clutch     | Couple to gearbox                 |
| 4    | .car → 14. Gearbox    | Ratios / shifts                   |
| 5    | .car → 13. Drivetrain | Diffs / AWD to wheels             |
| 6    | Setup / electronics   | Diff locks, TC index, boost level |

### <span id="page-40-3"></span>**3 - PLATFORM**

| Step | Asset                         | Role                         |
|------|-------------------------------|------------------------------|
| 1    | .car geometry (WB, track, CG) | Axle layout                  |
| 2    | → 17. Suspension              | Hardpoints / motion          |
| 3    | → 11. Coilover                | Springs / dampers            |
| 4    | → 12. Damper Curves           | Optional LUT bank            |
| 5    | Setup / limits / units        | Garage rates, clicks, labels |

### <span id="page-41-0"></span>**4 - AERO**

| Step | Asset                      | Role                                                        |
|------|----------------------------|-------------------------------------------------------------|
| 1    | .car Aero → 16. Surface 3D | Platform CX / CZ vs height                                  |
| 2    | .car Aero → 20. Wing       | BODY / FRONT / REAR / diffuser<br>elements                  |
| 3    | Setup                      | Ride heights feed Surface 3D<br>axes; wing angles feed Wing |
| 4    | Tuning part aero package   | Optional path / embedded aero<br>swap                       |

### <span id="page-41-1"></span>**V. Shared libraries (common\_phsx)**

| Kind         | Typical home                          | Referenced by               | Risk                                        |
|--------------|---------------------------------------|-----------------------------|---------------------------------------------|
| Tyres        | common_phsx\tyres\…                   | Many .car compound<br>lists | One edit hits many cars                     |
| Damper packs | common_phsx\dampers<br>\…             | Coilover Lut List           | One edit hits many cars                     |
| Setup units  | Shared setup_units                    | Many cars                   | UI label drift if forked<br>carelessly      |
| Curves       | Next to tyre / wing /<br>damper packs | Parent asset LUT fields     | Broken path = silent<br>wrong click / polar |

### <span id="page-41-2"></span>**VI. Start here**

| Intent                   | Open first     | Then                             |
|--------------------------|----------------|----------------------------------|
| Change peak power / maps | 4. Engine      | 18. Turbo if FI                  |
| Change gearing           | 14. Gearbox    | Matching 10. Clutch if swap pack |
| Change LSD / AWD         | 13. Drivetrain | Setup diff locks / limits        |

| Intent                            | Open first                                           | Then                                          |
|-----------------------------------|------------------------------------------------------|-----------------------------------------------|
| Change springs / dampers          | 11. Coilover                                         | 12. Damper Curves if LUT; setup<br>overlays   |
| Change roll centres / camber gain | 17. Suspension                                       | Setup alignment only overlays                 |
| Change ABS / TC personality       | 9. Electronics                                       | Setup index + 6. Limits                       |
| Strip aids (Cup style)            | 8. Tuning Parts + electronics /<br>limits            | Do not only zero setup indices                |
| Change grip / heat / wear         | 19. Tyre                                             | Setup pressure / camber                       |
| Change aero balance               | 16. Surface 3D + 20. Wing                            | Setup heights / wing angles                   |
| Change stopping power             | 1. Brake System                                      | 2. Brakes compounds                           |
| Ship a variant (drift, upgrade)   | 8. Tuning Parts                                      | Retarget paths; keep setup/limits<br>coherent |
| Change dry mass / fuel / torsion  | 3. Car Data General (or 15.<br>General if Path used) | —                                             |

### <span id="page-42-0"></span>**VII. Pratical notes**

- Always start from .car **paths** before editing a leaf asset wrong file in *common\_phsx* is a common footgun.
- Setup cannot invent hardware: no wing path → wing angle does nothing useful ; empty tyre list → compound index is empty.
- *General Path* / damper Lut / clutch curves / AWD controller curves are **optional** *None* is normal, not always a bug.
- Tuning parts **override** the graph; read the active part set before trusting stock .car paths.
- See also per-asset §1 tables in *01*…*20* for finer "handled here / elsewhere" splits.

### <span id="page-42-1"></span>**C. Schema**

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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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

### **Enum list - Car Engine**

| Id    | Enum           | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4l9b1 | Input Var      | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear,<br>SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX,<br>SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG,<br>SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor,<br>RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG,<br>LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR,<br>SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight,<br>ErsChargeLevel, ErsCoastTorque |
| 4l9b2 | CombinatorMode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 4q5a1 | Type           | <none>, Poly3, Poly5, Piece Wise, Damper Lut Data</none>                                                                                                                                                                                                                                                                                                                                                                                               |
| 18c1  | Mode           | UseEffect, UseAngle                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 26e1  | Type           | LSD, Spool, Torsen, EpicyclicTorsen, EpicyclicLSD,<br>TorqueVectoring                                                                                                                                                                                                                                                                                                                                                                                  |

### <span id="page-51-0"></span>**D. Measurement Units & Descriptions**

| ID  | Name                | Unit of Measurement                        | Description                                                                                                                                       |
|-----|---------------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 2a. | Screen Name         | None ( String )                            | Human-readable name shown for<br>the General block (mass, fuel,<br>body envelope) in tooling<br>interfaces.                                       |
| 2b. | Total Mass          | kg ( Kilograms )                           | Baseline vehicle mass including<br>driver and fluids as configured;<br>fundamental input for F=ma<br>weight transfer and inertia<br>calculations. |
| 2c. | Tank Position       | m ( Meters, X / Y / Z )                    | 3D coordinates of the fuel tank<br>centroid relative to the vehicle<br>reference frame; governs how CG<br>and weight bias shift as fuel burns.    |
| 2d. | Fuel                | L ( Liters )                               | Current fuel volume at session<br>start; dynamically reduces mass<br>and alters balance during the stint.                                         |
| 2e. | Max Fuel            | L ( Liters )                               | Maximum fuel tank capacity;<br>defines the upper bound for fuel<br>load and endurance strategy<br>calculations.                                   |
| 2f. | Effi<br>ciency      | Dimensionless ratio                        | Fuel consumption effi<br>ciency<br>modifier applied to engine fuel<br>burn calculations.                                                          |
| 2g. | Kg Per Liter        | kg/L ( Kilograms per Liter )               | Fuel density conversion factor;<br>translates volumetric fuel (liters)<br>into mass (kg) for physics weight<br>updates.                           |
| 2h. | Body Box Sizes      | m ( Meters, X / Y / Z )                    | Axis-aligned bounding box<br>dimensions of the chassis body<br>envelope; used for regulatory<br>checks and collision<br>approximation.            |
| 2i. | Pickup Front Height | m ( Meters )                               | Vertical pickup/reference height at<br>the front axle; aligns suspension<br>hardpoints and ground contact<br>geometry.                            |
| 2j. | Pickup Rear Height  | m ( Meters )                               | Vertical pickup/reference height at<br>the rear axle; aligns suspension<br>hardpoints and ground contact<br>geometry.                             |
| 2k. | Check Rules         | None ( Boolean : True /<br>False )         | Enables automated regulatory rule<br>validation (e.g., minimum ride<br>height) against series constraints.                                        |
| 2l. | Minimum Height      | m ( Meters )                               | Regulatory minimum ride-height<br>threshold enforced when Check<br>Rules is active.                                                               |
| 2m. | Torsional Stiffness | Nm/rad or N/m ( Torsional<br>spring rate ) | Chassis torsional spring rate;<br>resists twist between front and<br>rear axles under asymmetric<br>loading.                                      |

| ID   | Name                        | Unit of Measurement                | Description                                                                                                                              |
|------|-----------------------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 2n.  | Torsional Damping           | Nm·s/rad ( Torsional damping<br>)  | Chassis torsional damping<br>coeffi<br>cient; dissipates oscillatory<br>twist energy in the body structure.                              |
| 2o1. | Position                    | m ( Meters, X / Y / Z )            | Translation offset applied to the<br>visual/collision body mesh relative<br>to the physics origin (General ><br>Body Mesh Offset).       |
| 2o2. | Rotation                    | deg or rad ( X / Y / Z )           | Euler rotation offset applied to the<br>body mesh for visual/collision<br>alignment (General > Body Mesh<br>Offset).                     |
| 2o3. | Scale                       | Dimensionless ( X / Y / Z )        | Non-uniform scale factor applied<br>to the body mesh offset block for<br>model alignment.                                                |
| 3.   | General Path                | None ( File path )                 | External reference to a .generalcar<br>asset overriding or extending<br>global mass/inertia parameters.                                  |
| 4a.  | Wheel Base                  | m ( Meters )                       | Longitudinal distance between<br>front and rear axle centerlines;<br>stabilizes high-speed behavior and<br>affects rotation agility.     |
| 4b.  | Longitudinal Cg<br>Location | Ratio ( 0.0 - 1.0 )                | Longitudinal center-of-gravity<br>position along the wheelbase as a<br>fraction from front axle (e.g., 0.45<br>= slightly front-biased). |
| 4c.  | Base Y Front                | m ( Meters )                       | Reference vertical suspension hub<br>height at the front axle in the<br>chassis coordinate system.                                       |
| 4d.  | Base Y Rear                 | m ( Meters )                       | Reference vertical suspension hub<br>height at the rear axle in the<br>chassis coordinate system.                                        |
| 4e.  | Track Front                 | m ( Meters )                       | Lateral distance between left and<br>right front tire centerlines; wider<br>track increases roll stability.                              |
| 4f.  | Track Rear                  | m ( Meters )                       | Lateral distance between left and<br>right rear tire centerlines.                                                                        |
| 4g1. | Min Velocity                | m/s or km/h ( Speed<br>threshold ) | Minimum impact velocity required<br>before suspension/chassis<br>damage accumulation begins.                                             |
| 4g2. | Gain                        | Dimensionless coeffi<br>cient      | Damage accumulation rate<br>multiplier per unit of impact energy<br>above the minimum velocity<br>threshold.                             |
| 4g3. | Max Damage                  | Ratio ( 0.0 - 1.0 )                | Upper cap on cumulative<br>suspension/chassis damage<br>before performance degradation<br>saturates.                                     |

| ID    | Name                       | Unit of Measurement                 | Description                                                                                                                  |
|-------|----------------------------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 4g4.  | Debug Log                  | None ( Boolean : True /<br>False )  | Enables verbose logging of<br>suspension damage events for<br>development and tuning<br>diagnostics.                         |
| 4h.   | Coilover Front Path        | None ( File path )                  | Path to the front axle .coilover<br>asset defining spring rates,<br>damper curves, and bump-stop<br>geometry.                |
| 4i.   | Coilover Rear Path         | None ( File path )                  | Path to the rear axle .coilover<br>asset.                                                                                    |
| 4j.   | Front Suspension Path      | None ( File path )                  | Path to the front .suspension asset<br>defining kinematics, wishbone<br>geometry, and camber curves.                         |
| 4k.   | Rear Suspension path       | None ( File path )                  | Path to the rear .suspension asset.                                                                                          |
| 4l1.  | Spring Rate                | N/m ( Newtons per meter )           | Linear spring stiffness of the<br>heavy-duty auxiliary spring<br>element (used on trucks, off-road,<br>or dual-rate setups). |
| 4l2.  | Progressive Spring<br>Rate | N/m² or N/m ( Progressive<br>rate ) | Secondary progressive spring rate;<br>stiffness rises non-linearly as<br>compression increases.                              |
| 4l3a. | Range                      | m ( Meters )                        | Operational travel range of the<br>upper bump-stop before full<br>engagement (Heavy Springs ><br>Bump Stop Up).              |
| 4l3b  | Reference                  | m ( Meters )                        | Reference suspension position at<br>which the upper bump-stop force<br>model begins scaling.                                 |
| 4l3c. | Force                      | N ( Newtons )                       | Peak resistive force delivered by<br>the upper bump-stop at maximum<br>compression.                                          |
| 4l3d. | Gamma                      | Dimensionless exponent              | Non-linear shaping exponent for<br>upper bump-stop force vs.<br>compression curve.                                           |
| 4l3e. | Length                     | m ( Meters )                        | Physical contact length of the<br>upper bump-stop element.                                                                   |
| 4l3f. | Damping                    | N·s/m ( Damping coeffi<br>cient )   | Hydraulic or rubber damping<br>applied during upper bump-stop<br>engagement.                                                 |
| 4l4a. | Range                      | m ( Meters )                        | Operational travel range of the<br>lower (rebound) bump-stop (Heavy<br>Springs > Bump Stop Down).                            |
| 4l4b. | Reference                  | m ( Meters )                        | Reference position at which the<br>lower bump-stop force model<br>activates.                                                 |

| ID     | Name                      | Unit of Measurement               | Description                                                                                                         |
|--------|---------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 4l4c.  | Force                     | N ( Newtons )                     | Peak resistive force delivered by<br>the lower bump-stop at maximum<br>extension.                                   |
| 4l4d.  | Gamma                     | Dimensionless exponent            | Non-linear shaping exponent for<br>lower bump-stop force curve.                                                     |
| 4l4e.  | Length                    | m ( Meters )                      | Physical contact length of the<br>lower bump-stop element.                                                          |
| 4l4f.  | Damping                   | N·s/m ( Damping coeffi<br>cient ) | Damping applied during lower<br>bump-stop engagement on<br>rebound.                                                 |
| 4l5.   | Collar Position           | m ( Meters )                      | Adjustable spring perch/collar<br>position controlling static ride<br>height and preload on the heavy<br>spring.    |
| 4l6a1. | Bump                      | N·s/m ( Damping rate )            | Fast damper channel bump<br>(compression) damping rate within<br>the Heavy Springs embedded<br>damper model.        |
| 4l6a2. | Rebound                   | N·s/m ( Damping rate )            | Fast damper channel rebound<br>(extension) damping rate.                                                            |
| 4l6b1. | Bump                      | N·s/m ( Damping rate )            | Slow damper channel bump<br>damping rate for low-velocity<br>suspension movements.                                  |
| 4l6b2. | Rebound                   | N·s/m ( Damping rate )            | Slow damper channel rebound<br>damping rate.                                                                        |
| 4l6c.  | Fast Threshold Bump       | m/s ( Velocity threshold )        | Suspension compression velocity<br>above which the fast bump<br>damper circuit engages.                             |
| 4l6d.  | Fast Threshold<br>Rebound | m/s ( Velocity threshold )        | Suspension extension velocity<br>above which the fast rebound<br>damper circuit engages.                            |
| 4l6e.  | Cooling Surface           | m² ( Square meters )              | Exposed damper body surface<br>area used for thermal dissipation<br>modeling.                                       |
| 4l6f.  | Nominal Force             | N ( Newtons )                     | Reference force level for damper<br>nominal operating point and<br>fatigue calculations.                            |
| 4l6g.  | Min Stress Fatigue        | Pa or N ( Stress threshold )      | Lower bound stress level below<br>which damper fatigue<br>accumulation is negligible.                               |
| 4l6h.  | Mas Stress Fatigue        | Pa or N ( Stress threshold )      | Upper bound stress level at which<br>damper fatigue reaches maximum<br>degradation rate.                            |
| 4l6i.  | Thermal Capacity          | J/K or J/°C                       | Heat storage capacity of the<br>damper assembly; controls<br>temperature rise under repeated<br>high-energy cycles. |

| ID     | Name                             | Unit of Measurement                         | Description                                                                                                                                                               |
|--------|----------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4l6j.  | Heat Transfer<br>Coeffi<br>cient | W/(m²·K) ( Coeffi<br>cient )                | Convective heat transfer rate from<br>the damper body to ambient<br>airflow.                                                                                              |
| 4l6k.  | Lut List                         | None ( File path )                          | Path to a damper force-velocity<br>look-up table list defining non<br>linear damping behavior.                                                                            |
| 4l6l.  | Damper Lut Scale                 | None ( File path )                          | Scaling curve applied to the<br>damper LUT output for fine-tuning<br>peak forces.                                                                                         |
| 4l7.   | Helper K                         | N/m ( Spring rate )                         | Stiffness of the helper/tender<br>spring assisting the main spring at<br>low compression.                                                                                 |
| 4l8.   | Helper Range                     | m ( Meters )                                | Travel range over which the helper<br>spring is active before the main<br>spring fully engages.                                                                           |
| 4l9a.  | Name                             | None ( String )                             | Internal identifier for a dynamic<br>controller block. Reused across<br>Rod Controllers, ARB/Flex Bar<br>controllers, Steering, ERS, diff<br>lock, and turbo controllers. |
| 4l9b1. | Input Var                        | None ( Telemetry enum )                     | Live telemetry channel used as<br>controller input (e.g., Brake, Gas,<br>Speed, SlipRatio, SteerDEG,<br>ErsChargeLevel).                                                  |
| 4l9b2. | Combinator Mode                  | None ( Math enum : Add /<br>Mult )          | How this stage output combines<br>with prior stages: additive offset or<br>multiplicative scaling.                                                                        |
| 4l9b3. | Lut                              | None ( .curve file path )                   | Look-up table mapping the input<br>variable to an output modifier<br>factor.                                                                                              |
| 4l9b4. | Filter Gain                      | Coeffi<br>cient ( Smoothing<br>multiplier ) | Low-pass filter coeffi<br>cient<br>dampening rapid telemetry spikes<br>for smooth controller response.                                                                    |
| 4l9b5. | Up Limit                         | Depends on input variable                   | Upper clamp on the processed<br>input signal before LUT evaluation.                                                                                                       |
| 4l9b6. | Down Limit                       | Depends on input variable                   | Lower clamp on the processed<br>input signal before LUT evaluation.                                                                                                       |
| 4l9b7. | Current Value                    | Depends on input variable                   | Runtime value of the controller<br>stage output during simulation<br>(debug/telemetry).                                                                                   |
| 4l9b8. | Const Value                      | Depends on input variable                   | Fallback constant output when no<br>dynamic input or LUT is active.                                                                                                       |
| 4m1.   | Stiffness                        | Nm/deg or N/m ( Anti-roll bar<br>rate )     | Torsional stiffness of the front anti<br>roll bar resisting body roll in<br>cornering.                                                                                    |
| 4n1.   | Stiffness                        | Nm/deg or N/m ( Anti-roll bar<br>rate )     | Torsional stiffness of the rear anti<br>roll bar.                                                                                                                         |

| ID     | Name                            | Unit of Measurement                                                    | Description                                                                                                                         |
|--------|---------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| 4o1.   | Stiffness                       | Nm/deg or N/m ( Flex bar<br>rate )                                     | Stiffness of the front flex/<br>secondary torsion bar (compliance<br>element in complex suspension<br>layouts).                     |
| 4p1.   | Stiffness                       | Nm/deg or N/m ( Flex bar<br>rate )                                     | Stiffness of the rear flex/secondary<br>torsion bar.                                                                                |
| 4q1.   | Wheel Gain                      | Dimensionless coeffi<br>cient                                          | Global scaling gain for per-wheel<br>damper authority in the active<br>damper controller.                                           |
| 4q2.   | Heave Gain                      | Dimensionless coeffi<br>cient                                          | Gain applied to heave-mode<br>(vertical chassis) damper control<br>signals.                                                         |
| 4q3.   | Pitch Gain                      | Dimensionless coeffi<br>cient                                          | Gain applied to pitch-mode<br>damper control (nose dive / squat<br>compensation).                                                   |
| 4q4.   | Roll Gain                       | Dimensionless coeffi<br>cient                                          | Gain applied to roll-mode damper<br>control (lateral weight transfer<br>management).                                                |
| 4q5a1. | Type                            | None ( Enum : none / Poly3 /<br>Poly5 / PieceWise /<br>DamperLutData ) | Damper control curve type for<br>each motion mode (Base, Heave,<br>Roll, Pitch, Max, Min) on front/rear<br>axles.                   |
| 4r.    | Has Dampers Cockpit<br>Settings | None ( Boolean : True /<br>False )                                     | Allows the driver to adjust damper<br>settings from cockpit controls<br>during a session.                                           |
| 5.     | Drivetrain Path                 | None ( File path )                                                     | Path to the .drivetrain asset<br>defining differential type, gear<br>ratios, and torque split logic.                                |
| 6.     | Gearbox Path                    | None ( File path )                                                     | Path to the .gearbox asset defining<br>gear ratios, shift times, and auto<br>blip behavior.                                         |
| 7.     | Clutch Path                     | None ( File path )                                                     | Path to the .clutch asset defining<br>clutch friction, inertia, and<br>autoclutch engagement.                                       |
| 8.     | Engine Path                     | None ( File path )                                                     | Path to the .carengine asset<br>defining torque curves, turbo, and<br>engine braking.                                               |
| 9.     | Brakes Path                     | None ( File path )                                                     | Path to the .brakesystem asset<br>defining total braking torque, bias,<br>and EBB controllers.                                      |
| 10a.   | Four W S Controllers            | None ( Controller object )                                             | Four-wheel steering dynamic<br>controller array; modulates rear<br>steer angle via staged LUT<br>pipelines (uses 4l9 stage fields). |
| 11a1.  | Has T C2                        | None ( Boolean : True /<br>False )                                     | Enables a secondary traction<br>control map (TC2) for dual-stage<br>intervention logic.                                             |

| ID     | Name                         | Unit of Measurement          | Description                                                                                         |
|--------|------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------|
| 11a2.  | Frequency Hz                 | Hz ( Hertz )                 | Control loop update frequency of<br>the traction-control system.                                    |
| 11a3.  | Min Speed Kmh                | km/h ( Kilometers per hour ) | Minimum vehicle speed below<br>which traction control deactivates.                                  |
| 11a4.  | Gear Change Time             | s ( Seconds )                | Temporary TC suppression<br>window duration during gear<br>changes to avoid false<br>interventions. |
| 11a5.  | Min Cut Level                | Ratio ( 0.0 - 1.0 )          | Minimum engine torque cut level<br>applied at the lowest TC<br>intervention step.                   |
| 11a6.  | Max Cut Level                | Ratio ( 0.0 - 1.0 )          | Maximum engine torque cut level<br>at the most aggressive TC step.                                  |
| 11a7a. | Min Slip Ratio               | Dimensionless ratio          | Lower slip-ratio threshold at which<br>TC begins monitoring wheel spin<br>for this settings map.    |
| 11a7b. | Max Slip Ratio               | Dimensionless ratio          | Upper slip-ratio threshold<br>triggering full TC intervention for<br>this settings map.             |
| 11a7c. | Ref Slip Angle Deg           | deg ( Degrees )              | Reference rear slip angle used to<br>scale TC aggression relative to<br>yaw behavior.               |
| 11a7d. | Engine Cut Level             | Ratio ( 0.0 - 1.0 )          | Engine torque reduction factor<br>applied when slip thresholds are<br>exceeded.                     |
| 11a7e. | Angular A C Cgain            | Dimensionless gain           | Yaw-rate / angular acceleration<br>gain for TC correction authority.                                |
| 11a7f. | Oversteer Gain               | Dimensionless gain           | Additional TC sensitivity multiplier<br>when oversteer is detected.                                 |
| 11a7g. | Slip Angle Activation<br>Deg | deg ( Degrees )              | Minimum slip angle required<br>before this TC map becomes<br>active.                                |
| 11b1a. | Min Slip Ratio               | Dimensionless ratio          | Lower wheel slip threshold for<br>ABS monitoring on this settings<br>map.                           |
| 11b1b. | Max Slip Ratio               | Dimensionless ratio          | Upper slip threshold triggering<br>maximum ABS pressure<br>modulation.                              |
| 11b1c. | Ref Slip Angle Deg           | deg ( Degrees )              | Reference slip angle for ABS yaw<br>stability cross-correlation.                                    |
| 11b1d. | Cut Level                    | Ratio ( 0.0 - 1.0 )          | Brake pressure reduction factor<br>applied during ABS pulsing.                                      |
| 11b1f. | Max Torque Variation         | Nm or ratio                  | Maximum allowed brake torque<br>fluctuation per ABS cycle on this<br>map.                           |

| ID     | Name                 | Unit of Measurement                | Description                                                                                           |
|--------|----------------------|------------------------------------|-------------------------------------------------------------------------------------------------------|
| 11b2.  | Frequency            | Hz ( Hertz )                       | ABS control loop pulsing<br>frequency.                                                                |
| 11b3.  | Channels             | None ( Integer )                   | Number of independent ABS<br>control channels (typically one per<br>wheel or per axle).               |
| 11b4.  | Min Speed Kmh        | km/h ( Kilometers per hour )       | Minimum speed below which ABS<br>intervention is disabled.                                            |
| 11c1.  | Active               | None ( Boolean : True /<br>False ) | Master enable for Electronic<br>Differential Lock (EDL) brake<br>based torque transfer.               |
| 11c2.  | Brake Torque Power   | Nm ( Newton-meters )               | Brake torque applied to the<br>spinning wheel under power (on<br>throttle) to emulate a locking diff. |
| 11c3.  | Brake Torque Coast   | Nm ( Newton-meters )               | Brake torque applied during<br>coasting to synchronize wheel<br>speeds.                               |
| 11c4.  | Dead Zone Coast      | Ratio or rad/s                     | Speed-difference deadband below<br>which coast EDL does not<br>intervene.                             |
| 11c5.  | Dead Zone Power      | Ratio or rad/s                     | Speed-difference deadband below<br>which power EDL does not<br>intervene.                             |
| 11c6.  | Max Spin Power       | rad/s or ratio                     | Maximum allowed wheel spin<br>differential under power before<br>EDL fully engages.                   |
| 11c7.  | Max Spin Coaster     | rad/s or ratio                     | Maximum allowed wheel spin<br>differential on coast before EDL<br>engages.                            |
| 11c8.  | Min Speed            | m/s or km/h ( Speed<br>threshold ) | Minimum vehicle speed required<br>for EDL operation.                                                  |
| 11d1.  | Frequency Hz         | Hz ( Hertz )                       | Electronic Stability Program<br>control loop update frequency.                                        |
| 11d2.  | Min Speed Kmh        | km/h ( Kilometers per hour )       | Minimum speed below which ESP<br>deactivates.                                                         |
| 11d3a. | Gain                 | Dimensionless gain                 | Global ESP intervention authority<br>multiplier for this settings map.                                |
| 11d3b. | Steer Gain           | Dimensionless gain                 | Steering-angle sensitivity gain for<br>ESP yaw correction.                                            |
| 11d3c. | Min Steer Gain       | Dimensionless gain                 | Minimum steering gain applied at<br>low speeds within ESP logic.                                      |
| 11d3d. | Steer Gain Max Speed | km/h ( Kilometers per hour )       | Speed at which steering gain<br>reaches its maximum ESP<br>authority.                                 |
| 11d3e. | Oversteer Gain       | Dimensionless gain                 | Corrective gain when rear slip<br>(oversteer) is detected.                                            |

| ID     | Name                   | Unit of Measurement                         | Description                                                                                                 |
|--------|------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 11d3f. | Understeer Gain        | Dimensionless gain                          | Corrective gain when front slip<br>(understeer) is detected.                                                |
| 11d3g. | Max Slip Ratio         | Dimensionless gain                          | Maximum wheel slip ratio before<br>ESP applies full brake/engine<br>intervention.                           |
| 11d3h. | Dead Zone              | deg or ratio                                | Yaw/steer error deadband where<br>ESP remains passive.                                                      |
| 11d3i. | Filter Gain            | Coeffi<br>cient ( Smoothing<br>multiplier ) | Low-pass filter on ESP sensor<br>inputs to prevent oscillatory<br>corrections.                              |
| 11d3j. | Brake Perc             | Ratio ( 0.0 - 1.0 )                         | Percentage of available brake<br>pressure ESP may apply for<br>stability correction.                        |
| 11d3k. | Brake Perc Activation  | Ratio ( 0.0 - 1.0 )                         | Slip/yaw threshold fraction at<br>which ESP begins applying brake<br>intervention.                          |
| 12.    | Electronics Path       | None ( File path )                          | External reference to a<br>standalone .carelectronics asset<br>overriding inline TC/ABS/ESP<br>definitions. |
| 13a.   | Ff Mult                | Dimensionless multiplier                    | Force-feedback strength multiplier<br>scaling steering wheel torque<br>output to the driver.                |
| 13b.   | Steer Lock             | deg ( Degrees )                             | Maximum steering wheel rotation<br>angle from lock to lock.                                                 |
| 13c.   | Steer Ratio            | Ratio ( :1 )                                | Steering rack ratio converting<br>steering wheel angle to front wheel<br>angle.                             |
| 13d.   | Linear Steer Rod Ratio | M/rad or dimensionless                      | Linear rack displacement per unit<br>steering input; fine-tunes low<br>speed steering response.             |
| 13e.   | Steer Assist           | Dimensionless multiplier                    | Power-steering assist strength<br>scaling self-aligning torque<br>feedback.                                 |
| 14a.   | Center                 | m ( Meters, X / Y / Z )                     | Center position of an axis-aligned<br>box collider used for simplified<br>body collision detection.         |
| 14b.   | Size                   | m ( Meters, X / Y / Z )                     | Full dimensions (width, height,<br>length) of the box collider.                                             |
| 14c.   | Pitch Rotation Deg     | deg ( Degrees )                             | Pitch-axis rotation applied to<br>orient the box collider relative to<br>the chassis.                       |
| 15.    | Front Tyre Compounds   | None ( File path )                          | Path(s) to front axle .tyre<br>compound assets; multiple entries<br>allow compound selection.               |
| 16.    | Rear Type Compounds    | None ( File path )                          | Path(s) to rear axle .tyre<br>compound assets.                                                              |

| ID     | Name                   | Unit of Measurement                         | Description                                                                                         |
|--------|------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------|
| 17a.   | Slip Gain Multiple     | Dimensionless multiplier                    | Global scaling factor for<br>aerodynamic slip-stream and yaw<br>sensitivity effects.                |
| 17b.   | Speed Factor Mult      | Dimensionless multiplier                    | Multiplier applied to speed<br>dependent aero force calculations<br>(downforce/drag scaling).       |
| 17c1.  | Position               | m ( Meters, X / Y / Z )                     | Application point of an<br>aerodynamic downforce/lift<br>element on the chassis.                    |
| 17c2.  | Cl Gain                | Dimensionless coeffi<br>cient               | Lift coeffi<br>cient gain multiplier for<br>this downforce element.                                 |
| 17c3.  | Cd Gain                | Dimensionless coeffi<br>cient               | Drag coeffi<br>cient gain multiplier for<br>this downforce element.                                 |
| 17c4.  | Yaw Gain               | Dimensionless coeffi<br>cient               | Sensitivity of aero forces to vehicle<br>yaw angle (side-force generation).                         |
| 17c5.  | Drag Per Cool Transfer | Coeffi<br>cient                             | Drag penalty factor linked to<br>coolant or brake-duct thermal<br>transfer (aero-thermal coupling). |
| 17c6.  | Damage C L             | None ( String / curve<br>reference )        | Damage-state modifier curve for<br>lift coeffi<br>cient degradation on this<br>aero element.        |
| 17c7.  | Damage C D             | None ( String / curve<br>reference )        | Damage-state modifier curve for<br>drag coeffi<br>cient degradation.                                |
| 17c8a. | Combinator Mode        | None ( Math enum : Add /<br>Mult )          | How downforce controller stage<br>output combines with baseline<br>aero coeffi<br>cients.           |
| 17c8b. | Input                  | None ( Telemetry enum )                     | Telemetry input driving dynamic<br>downforce modulation (speed, ride<br>height, DRS state, etc.).   |
| 17c8c. | Filter                 | Coeffi<br>cient ( Smoothing<br>multiplier ) | Input smoothing filter for<br>downforce controller stages.                                          |
| 17c8d. | Up Limit               | Depends on input variable                   | Upper clamp on downforce<br>controller input.                                                       |
| 17c8e. | Down Limit             | Depends on input variable                   | Lower clamp on downforce<br>controller input.                                                       |
| 17c8f. | Lut                    | None ( .curve file path )                   | Look-up table mapping controller<br>input to aero coeffi<br>cient modifier.                         |
| 17c9.  | Lift Per Front Angle   | Coeffi<br>cient per deg                     | Rate of lift change per degree of<br>front ride-height / pitch angle.                               |
| 17c10. | Lift Per Rear Angle    | Coeffi<br>cient per deg                     | Rate of lift change per degree of<br>rear ride-height / pitch angle.                                |
| 17c11. | Drag Per Front Angle   | Coeffi<br>cient per deg                     | Rate of drag change per degree of<br>front body angle.                                              |
| 17c12. | Drag Per Rear Angle    | Coeffi<br>cient per deg                     | Rate of drag change per degree of<br>rear body angle.                                               |

| ID     | Name                | Unit of Measurement                     | Description                                                                                          |
|--------|---------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------|
| 17c13. | Default Front Angle | deg ( Degrees )                         | Baseline front body angle<br>reference for aero angle<br>dependent calculations.                     |
| 17c14. | Default Rear Angle  | deg ( Degrees )                         | Baseline rear body angle reference<br>for aero angle-dependent<br>calculations.                      |
| 17d.   | Front Lift          | None ( File path )                      | Path to a .surface3d front lift aero<br>map defining Cl vs. ride height /<br>speed.                  |
| 17e.   | Rear Lift           | None ( File path )                      | Path to a .surface3d rear lift aero<br>map.                                                          |
| 17f.   | Drag                | None ( File path )                      | Path to a .surface3d drag map<br>defining Cd vs. speed and<br>configuration.                         |
| 17g.   | Wings Path          | None ( File path )                      | Path(s) to .wing assets defining<br>adjustable aerodynamic devices<br>(splitters, wings, diffusers). |
| 18a.   | Ignore Zones        | None ( Boolean : True /<br>False )      | When true, DRS activation ignores<br>track zone restrictions<br>(development override).              |
| 18b.   | Limit G             | G ( Lateral G-force )                   | Maximum lateral G beyond which<br>DRS automatically deactivates for<br>safety.                       |
| 18c1.  | Mode                | None ( Enum : UseEffect /<br>UseAngle ) | DRS wing connection mode: apply<br>a coeffi<br>cient effect or a physical<br>angle offset.           |
| 18c2.  | Connected Wing      | None ( Integer index )                  | Index of the wing element in the<br>Wings Path array controlled by this<br>DRS connection.           |
| 18c3.  | Effect              | Dimensionless coeffi<br>cient<br>delta  | Aerodynamic coeffi<br>cient change<br>applied when DRS is open (Mode<br>= UseEffect).                |
| 18c4.  | Angle               | deg ( Degrees )                         | Physical wing angle offset applied<br>when DRS is open (Mode =<br>UseAngle).                         |
| 19a.   | Torque Lut          | None ( .curve file path )               | Look-up table mapping<br>deployment input to electric motor<br>assist torque (kW/Nm).                |
| 19b.   | Coast Lut           | None ( .curve file path )               | Look-up table defining<br>regenerative braking / coast<br>recovery torque.                           |
| 19c.   | Battery Charge Kj   | kJ ( Kilojoules )                       | Total energy storage capacity of<br>the hybrid battery pack.                                         |
| 19d.   | Has Button Override | None ( Boolean : True /<br>False )      | Allows driver button override of<br>automatic ERS deployment<br>strategy.                            |

| ID    | Name                              | Unit of Measurement                | Description                                                                                                           |
|-------|-----------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 19e.  | Max Kj Per Lap                    | kJ/lap ( Kilojoules per lap )      | Regulatory or strategic cap on<br>ERS energy deployment per lap.                                                      |
| 19f.  | Max Charge Kj Per Lap             | kJ/lap ( Kilojoules per lap )      | Maximum energy that can be<br>recovered into the battery per lap.                                                     |
| 19g.  | Heat Charge Perc                  | Ratio ( 0.0 - 1.0 )                | Fraction of waste heat energy<br>convertible into battery charge<br>(MGU-H simulation).                               |
| 19h.  | Heat Power Kw                     | kW ( Kilowatts )                   | Thermal energy recovery power<br>ceiling from exhaust/heat sources.                                                   |
| 19i.  | Default Power<br>Controller Index | None ( Integer )                   | Index of the default ERS<br>deployment map selected at<br>session start.                                              |
| 19j.  | Power Controllers Front           | None ( Controller array )          | Array of front-axle ERS<br>deployment controllers; each entry<br>uses the shared 4l9 stage fields<br>(Name + Stages). |
| 19k.  | Power Controllers Rear            | None ( Controller array )          | Array of rear-axle ERS deployment<br>controllers; each entry uses the<br>shared 4l9 stage fields.                     |
| 19l.  | Brake Rear Correction             | Ratio or Nm                        | Rear brake torque correction<br>factor when ERS regenerative<br>braking is active.                                    |
| 19m.  | Has Cockpit Controls              | None ( Boolean : True /<br>False ) | Exposes ERS deployment/<br>recovery controls to the driver in<br>the cockpit UI.                                      |
| 19n1. | Delivery Profile                  | None ( Boolean )                   | Cockpit toggle for ERS power<br>delivery profile selection.                                                           |
| 19n2. | Mgu H Mode                        | None ( Boolean )                   | Cockpit toggle for MGU-H<br>harvesting mode.                                                                          |
| 19n3. | Recovery                          | None ( Boolean )                   | Cockpit toggle for regenerative<br>recovery aggressiveness.                                                           |
| 19o.  | Has Front Motors                  | None ( Boolean : True /<br>False ) | Enables front-axle electric motor(s)<br>for hybrid or torque-vectoring<br>applications.                               |
| 19p1. | Torque Lut                        | None ( .curve file path )          | Torque delivery curve for front-axle<br>electric motor(s).                                                            |
| 19p2. | Discharge Time                    | s ( Seconds )                      | Time constant governing front<br>motor energy discharge rate from<br>the battery.                                     |
| 19p3. | Torque Vectoring Bias             | Ratio ( -1.0 - 1.0 )               | Left/right torque distribution bias<br>for front-axle electric torque<br>vectoring.                                   |
| 20.   | Setup Limits                      | None ( File path )                 | Path to .carsetuplimits asset<br>defining min/max/step bounds for<br>garage setup sliders.                            |

| ID     | Name                        | Unit of Measurement           | Description                                                                             |
|--------|-----------------------------|-------------------------------|-----------------------------------------------------------------------------------------|
| 21.    | Collider Mesh               | None ( File path )            | Path to the detailed collision mesh<br>used for body contact and<br>scraping detection. |
| 22a.   | Position                    | m ( Meters, X / Y / Z )       | Root-level body mesh translation<br>offset (distinct from General 2o<br>block).         |
| 22b.   | Rotation                    | deg or rad ( X / Y / Z )      | Root-level body mesh rotation<br>offset.                                                |
| 22c.   | Scale                       | Dimensionless ( X / Y / Z )   | Root-level body mesh scale factor.                                                      |
| 23.    | Stock Setup                 | None ( File path )            | Path to the default .carsetup preset<br>loaded for new sessions.                        |
| 24.    | Ai Setup                    | None ( File path )            | Path to the AI-specific .carsetup<br>preset used by computer<br>controlled opponents.   |
| 25.    | Wet Setup                   | None ( File path )            | Path to the wet-weather .carsetup<br>preset (tyre pressures, wing<br>angles, etc.).     |
| 26a.   | Performance Mode<br>Name    | None ( String )               | Label for a performance mode<br>preset (e.g., Qualifying, Race, Wet,<br>Safe).          |
| 26b1.  | Tc1                         | None ( Map index / level )    | Traction Control map level stored<br>in this performance mode.                          |
| 26b2.  | Tc2                         | None ( Map index / level )    | Secondary TC map level for dual<br>TC systems.                                          |
| 26b3.  | Abs                         | None ( Map index / level )    | ABS intervention map level for this<br>performance mode.                                |
| 26b4.  | Esc                         | None ( Map index / level )    | ESP/stability control map level for<br>this performance mode.                           |
| 26b5.  | Ebb                         | None ( Map index / level )    | Electronic Brake Balance mode/<br>level for this performance mode.                      |
| 26b6.  | Engine Map                  | None ( Map index )            | Engine power map selection (fuel/<br>power trade-off).                                  |
| 26b7.  | Telemetry Laps To<br>Record | None ( integer / lap number ) | Number of laps of telemetry data<br>to retain when this mode is active.                 |
| 26b8.  | Turbo Boost Lv              | bar or level index            | Turbo boost level preset for this<br>performance mode.                                  |
| 26b9.  | Ers Deployment Map          | None ( Map index )            | Turbo boost level preset for this<br>performance mode.                                  |
| 26b10. | Ers Recharge Lv             | None ( Level index )          | ERS energy recovery<br>aggressiveness level.                                            |
| 26b11. | Ers Heat Charging           | None ( Level index )          | MGU-H heat-to-battery charging<br>level.                                                |
| 26c1.  | Front Bias                  | Ratio ( 0.0 - 1.0 )           | Brake balance front percentage<br>stored in this performance mode.                      |

| ID     | Name                         | Unit of Measurement                                                                              | Description                                                                            |
|--------|------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| 26c2.  | Torque Multiplier            | Dimensionless multiplier                                                                         | Global braking torque scaling<br>factor for this mode.                                 |
| 26c3.  | Brake Ducts                  | Ratio ( 0.0 - 1.0 )                                                                              | Brake cooling duct opening<br>level(s); multiple entries for front/<br>rear ducts.     |
| 26d1.  | Slow Bump                    | Clicks or N·s/m                                                                                  | Slow-speed compression damper<br>setting for this performance mode.                    |
| 26d2.  | Fast Bump                    | Clicks or N·s/m                                                                                  | Fast-speed compression damper<br>setting.                                              |
| 26d3.  | Slow Rebound                 | Clicks or N·s/m                                                                                  | Slow-speed rebound damper<br>setting.                                                  |
| 26d4.  | Fast Rebound                 | Clicks or N·s/m                                                                                  | Fast-speed rebound damper<br>setting.                                                  |
| 26e1.  | Type                         | None ( Enum : LSD / Spool /<br>Torsen / EpicyclicTorsen /<br>EpicyclicLSD /<br>TorqueVectoring ) | Differential mechanism type<br>governing torque split behavior.                        |
| 26e2.  | Power                        | Nm or ratio                                                                                      | Differential lock/acceleration<br>sensitivity under power (on<br>throttle).            |
| 26e3.  | Coast                        | Nm or ratio                                                                                      | Differential lock sensitivity on<br>coast (off-throttle).                              |
| 26e4.  | Preload                      | Nm ( Newton-meters )                                                                             | Static preload torque required<br>before differential plates begin<br>slipping.        |
| 26e5.  | Front Share                  | Ratio ( 0.0 - 1.0 )                                                                              | Fraction of total driveline torque<br>directed to the front axle (AWD/<br>4WD).        |
| 26e6.  | Torque Bias Ratio<br>Power   | Ratio ( e.g., 2.0:1 )                                                                            | Torque bias ratio between axles or<br>sides under power.                               |
| 26e7.  | Torque Bias Ratio<br>Coast   | Ratio                                                                                            | Torque bias ratio between axles or<br>sides on coast.                                  |
| 26e8.  | Thermal Capacity             | J/K or J/°C                                                                                      | Heat storage capacity of<br>differential components for<br>thermal wear modeling.      |
| 26e9.  | Surface                      | m² ( Square meters )                                                                             | Exposed surface area of<br>differential housing for cooling<br>calculations.           |
| 26e10. | Heat Transfer Coef           | W/(m²·K) ( Coeffi<br>cient )                                                                     | Heat dissipation rate from<br>differential to ambient airflow.                         |
| 26e11. | Wear Factor                  | Dimensionless coeffi<br>cient                                                                    | Rate at which differential friction<br>surfaces degrade under load and<br>temperature. |
| 26e12. | Friction Reduction With<br>T | Ratio/°C                                                                                         | Linear friction reduction per<br>degree of temperature rise in the<br>differential.    |

| ID            | Name                    | Unit of Measurement          | Description                                                                                         |
|---------------|-------------------------|------------------------------|-----------------------------------------------------------------------------------------------------|
| 26e13.        | Friction Ref T          | °C ( Degrees Celsius )       | Reference temperature at which nominal differential friction is defined.                            |
| 26f1.         | Front Diff              | None ( Differential object ) | Front axle differential block; contains 26e1–26e13 fields for AWD/4WD layouts.                      |
| 26f2.         | Center Diff             | None ( Differential object ) | Center differential block for torque split between front and rear axles.                            |
| 26f3.         | Rear Diff               | None ( Differential object ) | Rear axle differential block.                                                                       |
| 26g.          | Front Lock Controllers  | None ( Controller object )   | Dynamic controller modulating front differential lock under telemetry conditions.                   |
| 26h.          | Center Lock Controllers | None ( Controller object )   | Dynamic controller modulating center differential lock.                                             |
| <b>26i.</b>   | Rear Lock Controllers   | None ( Controller object )   | Dynamic controller modulating rear differential lock.                                               |
| 26j1.         | Position                | None (Integer index)         | Index position of an AWD clutch pack in the driveline layout.                                       |
| <b>26j2</b> . | Preload                 | Nm ( Newton-meters )         | Static preload torque on this AWD clutch before slip occurs.                                        |
| 26k.          | Turbo Controllers       | None ( Controller object )   | Dynamic controller array modulating turbo boost via staged LUT pipelines (uses 4l9 stage fields).   |
| 2611.         | Boost Lv                | bar or level index           | Turbo boost level preset within this performance mode.                                              |
| 27.           | Ai Car Data             | None (File path)             | Path to an Al-specific .car data override tuning opponent behavior without altering player physics. |
| 28.           | mm                      | None (Integer)               | Internal unit-scaling or precision flag used by the editor toolchain (millimeter reference mode).   |

### <span id="page-66-0"></span>E. Example data

### <span id="page-66-1"></span>I. Chosen Car Data for Example

- Ferrari 296 GTB ( slug : ks\_ferrari\_286\_gtb )Audi R8 LMS GT3 Evo II ( slug : ks\_audi\_r8\_lms\_gt3\_evo\_2 )
- Renault 5 GT Turbo (slug: ks\_renault\_5\_gt\_turbo)

### <span id="page-66-3"></span><span id="page-66-2"></span>II. Example

```
├ 1. Screen Name : None 
├ 2. General 
│ ├ 2a. Screen Name : Ferrari 296 GTB 
│ ├ 2b. Total Mass : 1750.00000 
│ ├ 2c. Tank Position : 0.00000, -0.16715, -032949 
│ ├ 2d. Fuel : 60.00000 
│ ├ 2e. Max Fuel : 120.00000 
│ ├ 2f. Efficiency : 0.00000 
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
```

```
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
```

```
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
```

```
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
```

```
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
│ ├ 19k. Power Controllers Rear 2
│ │ ├ 4l9a. Name : MAP P 
│ │ ├ 4l9b. Stages 1
```

```
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
```

```
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
```

```
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
```

```
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
```

```
│ ├ 26i. Rear Lock Controllers : None
│ ├ 26j. Awd Clutches : None 
│ ├ 26k. Turbo Controllers : None 
│ ├ 26l. Turbo Settings : None
├ 27. Ai Car Data : 
content\cars\ks_ferrari_296_gtb\data\ks_ferrari_296_gtb.aicardata
└ 28. mm : 1
```

### <span id="page-76-0"></span>**Audi R8 LMS GT3 Evo II**

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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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

### <span id="page-83-0"></span>**Renault 5 GT Turbo**

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
```

```
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
```

```
│ └ 4r. Has Dampers Cockpit Settings : false 
├ 5. Drivetrain Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.drivetrain
├ 6. Gearbox Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.gearbox
├ 7. Clutch Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.clutch
├ 8. Engine Path : 
content\cars\ks_renault_5_gt_turbo\data\ks_renault_5_turbo.carengine
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
```

```
│ ├ 11d. E S P 
│ │ ├ 11d1. Frequency Hz : 0.00000 
│ │ ├ 11d2. Min Speed Kmh : 0.00000 
│ │ ├ 11d3. Settings : None 
├ 12. Electronics Path : None
├ 13. Controls 
│ ├ 13a. Ff Mult : 2.90000 
│ ├ 13b. Steer Lock : 630.00000 
│ ├ 13c. Steer Ratio : -19.60000 
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

# <span id="page-87-0"></span>**4. Car Engine [ .carengine ]**

### <span id="page-87-1"></span>**A. Description**

Propulsion core: how the power unit makes torque, how fast it revs, how the throttle feels, and how boost or hybrid overlays reshape that delivery.

Car Data only points here via *Engine Path*. This file owns the energy side of longitudinal dynamics acceleration, engine braking, map strategy, and forced-induction hooks.

### <span id="page-87-2"></span>**I. Role in the stack**

| Concern                                          | Handled here               | Handled elsewhere             |
|--------------------------------------------------|----------------------------|-------------------------------|
| Torque vs RPM, coast/engine<br>brake curve       | .carengine                 | —                             |
| Idle / limiter, inertia, throttle<br>shaping     | .carengine                 | —                             |
| Engine maps (power / fuel /<br>throttle / feel ) | .carengine Maps            | Setup map index               |
| Turbo / compressor load and<br>boost control     | Controllers + .turbo paths | 18. Turbo                     |
| Battery pack for motor / hybrid<br>assist        | Battery Data block         | Car Data ERS hooks            |
| Gear ratios, clutch, final drive                 | —                          | Gearbox / clutch / drivetrain |

Referenced from Car Data **Engine Path**. Without a valid .carengine, the car has no torque source.

### <span id="page-87-3"></span>**II. What you are really tuning**

- 1. **Power identity** *Engine Type* selects *combustion* or *motor*. *Power Curve* is the RPM to torque LUT (the shape everyone feels out of corners). *Coast Curve* is negative torque on a closed throttle — engine braking and entry stability for driven axles.
- 2. **Rotational character** *Inertia* is flywheel / rotating assembly mass. Low values (Alpine motor about 0.06) snap RPM up and down; high values (Camaro about 0.45) feel heavy and slow to build revs. SF-25 may leave inertia unset when handled elsewhere.
- 3. **Rev window** *Minimum* is idle (0 on the EV Alpine; about 600-900 on classic ICE). *Limiter* is the hard ceiling (Alpine about 15200, Camaro about 6600, Datsun about 7000). *Limiter Cycles* softens how the cut feels before a hard stop.
- 4. **Throttle feel** Global and per-map throttle response curves map pedal to effective opening. *Throttle Lag Up* / *Dn* smooth tip-in and lift. Camaro uses noticeable lag (about 0.8 up / 0.9 down); race maps often leave lag at 0 and swap **linear** vs **aggressive** curves instead.
- 5. **Maps** *Maps[]* are selectable power modes: *Power Mult*, *Consumption Mult*, optional throttle curve, lag, and map type (*gamma* / *cervone*). SF-25 stacks many maps (full power down to about 0.72 power with matching fuel cuts) — strategy and drivability live here more than in the raw power curve.

6. **Boost and hybrid extras** — Turbo / wastegate controller stages (same LUT pipeline pattern as brakes EBB), *Max Turbo Boost*, *Bov Threshold*, and *Turbos To Load* point at .turbo assets (Camaro loads a compressor turbo). *Battery Data* holds pack capacity and thermal limits for motor / hybrid use. *Start ECU Assist* is launch / anti-stall logic (RPM window, clutch slip target, gains).

### <span id="page-88-0"></span>**III. Architecture**

### <span id="page-88-1"></span>**1 - CORE PROPULSION (SCHEMA 1-4)**

Engine type, inertia, power curve path, coast curve path.

### <span id="page-88-2"></span>**2 - MAPS AND REV LIMITS (SCHEMA 5-8)**

Map array with per-map throttle behaviour; idle, limiter, limiter cycles.

### <span id="page-88-3"></span>**3 - GLOBAL THROTTLE AND START (SCHEMA 9-15)**

Fallback throttle curve and lag, rev choking, ignition time, starter torque, Start ECU Assist (launch control style fields).

### <span id="page-88-4"></span>**4 - FORCED INDUCTION (SCHEMA 16-20)**

Turbo Controllers and Waste Gate Controllers (shared stage fields: Input Var, Combinator, Lut, Filter, limits), max boost, BOV threshold, turbos-to-load paths.

### <span id="page-88-5"></span>**5 - BATTERY (SCHEMA 21)**

Capacity, charge/discharge efficiency, temperature loss, convection, thermal capacity, temp clamps relevant when Engine Type is motor or hybrid assist is active.

### <span id="page-88-6"></span>**IV. How to read the examples**

### <span id="page-88-7"></span>**1 - ALPINE A290 B (ELECTRIC MOTOR)**

Engine Type : motor, very low inertia, idle at 0, high limiter (about 15200). No maps, no turbos, no boost. Power + coast + throttle curves only. Clean EV template: instant response, no spool, no multi-map strategy.

### <span id="page-88-8"></span>**2 - FERRARI SF-25 (RACE ICE + STRATEGY MAPS)**

*combustion*, rich map list mixing power multipliers (1.00 down to about 0.72) with consumption multipliers and linear/aggressive throttle curves. Coast uses a smooth curve. Shows how modern race engines separate **peak curve** from **selectable maps** for fuel and drivability.

### <span id="page-88-9"></span>**3 - CHEVROLET CAMARO ZL1 (BOOSTED MUSCLE)**

High inertia (0.45), idle 900, limiter 6600, strong throttle lag, Start ECU Assist with clutch enabled. Turbo controller driven by *RPMS* into a boost LUT; *Turbos To Load* points at a compressor .turbo; *Max Turbo Boost* about 0.6. Battery block present but zeroed. Forced-induction ICE with launch assist.

### <span id="page-88-10"></span>**4 - DATSUN 240Z FAIRLADY (CLASSIC NA)**

Combustion, moderate inertia (0.18), idle 600, limiter 7000, map type *cervone*, no turbo load. Straightforward naturally aspirated road/race engine without boost plumbing.

### <span id="page-89-0"></span>**V. Practical notes**

- Shape the **Power Curve** before stacking maps: maps only scale and re-throttle what the curve already is.
- Coast curve is half of entry balance on driven wheels do not leave a placeholder if engine braking matters.
- Controllers present does not mean boost is active: check *Turbos To Load* and *Max Turbo Boost*, and read the linked .turbo lag/gamma fields.
- *motor* vs *combustion* changes which blocks matter (battery / zero idle vs turbo / idle RPM).
- Throttle lag and aggressive maps can mask or exaggerate turbo kick tune them together with the .turbo asset.
- Schema spellings to expect: *Throttle Rev Chocking*, *Dischage Efficiency*, *Start E C U Assist*, *Speed Range K H M*.

### <span id="page-89-1"></span>**VI. Related assets**

- **3. Car Data [\[.car\]](#page-35-0)** *Engine Path* loads this file
- **• 18. Turbo [\[.turbo\]](#page-301-0)** spool / wastegate assets listed in Turbos To Load
- **• 14 / 10 / 13. [Gearbox](#page-261-0) / [Clutch](#page-221-0) / [Drivetrain](#page-245-0)** consume engine torque downstream
- **5. Car Setup [\[.carsetup\]](#page-102-0)** engine map / turbo boost level selection in the garage

### <span id="page-89-2"></span>**B. Schema**

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
```

```
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
│ │ ├ 16b4. Filter Gain : float
│ │ ├ 16b5. Up Limit : float
│ │ ├ 16b6. Down Limit : float
│ │ ├ 16b7. Current Value : float
│ └ └ 16b8. Const Value : float
├ 18. Max Turbo Boost : float
├ 19. Bov Threshold : float
├ 20. Turbos To Load [x] : string - path | can have multiple Turbos To 
Load 
├ 21. Battery Data : object
│ ├ 21a. Capacity Kwh : float
│ ├ 21b. Dischage Efficiency : float
│ ├ 21c. Charge Efficiency : float
│ ├ 21d. Temp Eff Loss Per Deg : float
│ ├ 21e. Convection K : float
│ ├ 21f. Convection Forced K : float
│ ├ 21g. Thermal Capacity : float
│ ├ 21h. Max Temp : float
└ └ 21i. Min Temp : float
```

### **Enum - Car Engine**

| 5a   | Type           | gamma, cervone                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16b1 | Input Var      | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear,<br>SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX,<br>SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG,<br>SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor,<br>RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG,<br>LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR,<br>SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight,<br>ErsChargeLevel, ErsCoastTorque |
| 16b2 | CombinatorMode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                                               |

### <span id="page-91-0"></span>**C. Measurement Units & Descriptions**

| ID  | Name                       | Unit of Measurement                   | Description                                                                                                                                                                    |
|-----|----------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Engine Type                | None ( Enum : motor /<br>combustion ) | Selects the propulsion model:<br>motor for electric-only<br>powertrains, combustion for<br>internal-combustion (ICE) or<br>hybrid ICE behavior.                                |
| 2.  | Inertia                    | kg·m² ( Kilogram square<br>meters )   | Rotational inertia of the engine<br>assembly (crankshaft, flywheel,<br>pistons). Low values yield fast<br>revving (F1); high values create<br>sluggish RPM changes (heavy V8). |
| 3.  | Power Curve                | None ( .curve file path )             | Primary look-up table mapping<br>engine RPM (X-axis) to torque<br>output in Nm (Y-axis); the<br>foundation of all acceleration and<br>top-speed calculations.                  |
| 4.  | Coast Curve                | None ( .curve file path )             | Look-up table defining negative<br>engine torque (engine braking) as<br>a function of RPM when throttle is<br>fully released (0%).                                             |
| 5.  | Maps                       | None ( Object array )                 | Array of selectable engine maps<br>(power modes); each entry defines<br>power/consumption multipliers<br>and per-map throttle behavior.                                        |
| 5a. | Type                       | None ( Enum : gamma /<br>cervone )    | Engine map blending/interpolation<br>profile type governing how map<br>parameters transition between<br>operating points.                                                      |
| 5b. | Power Mult                 | Dimensionless multiplier              | Scalar applied to the base power/<br>torque curve output for this engine<br>map (e.g., 0.82 = 82% power for<br>economy mode).                                                  |
| 5d. | Throttle Response<br>Curve | None ( .curve file path )             | Per-map look-up table mapping<br>pedal position to effective throttle<br>plate opening (linear, aggressive,<br>progressive, wet).                                              |

| ID  | Name                       | Unit of Measurement               | Description                                                                                                                                 |
|-----|----------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 5e. | Throttle Gain K RPM        | Dimensionless gain                | RPM-dependent gain scaling<br>throttle response sensitivity;<br>modulates how aggressively the<br>engine reacts at different rev<br>ranges. |
| 5f. | Throttle Ref RPM Move      | RPM ( Revolutions per minute<br>) | Reference RPM delta threshold<br>triggering throttle gain adjustments<br>during rapid RPM changes.                                          |
| 5g. | Throttle Lap Up            | S ( Seconds ) or ratio            | Time constant or smoothing factor<br>for throttle opening response;<br>higher values soften pedal tip-in.                                   |
| 5h. | Throttle Lag Dn            | S ( Seconds ) or ratio            | Time constant or smoothing factor<br>for throttle closing response;<br>higher values delay lift-off engine<br>braking onset.                |
| 5i. | Throttling Factor          | Dimensionless coeffi<br>cient     | Global throttle shaping factor<br>applied within this engine map for<br>fine-tuning drivability.                                            |
| 6.  | Minimum                    | RPM ( Revolutions per minute<br>) | Idle RPM — the baseline engine<br>speed maintained at zero throttle<br>input.                                                               |
| 7.  | Limiter                    | RPM ( Revolutions per minute<br>) | Maximum engine RPM before the<br>rev limiter cuts fuel/ignition to<br>protect the engine.                                                   |
| 8.  | Limiter Cycles             | None ( Integer )                  | Number of soft-cut cycles the rev<br>limiter performs before hard<br>limiting; affects limiter feel and<br>sound.                           |
| 9.  | Throttle Response<br>Curve | None ( .curve file path )         | Global (non-map-specific) throttle<br>pedal-to-plate response curve<br>used when no per-map override is<br>active.                          |
| 10. | Throttle Lag Up            | s ( Seconds ) or ratio            | Global throttle opening lag/<br>smoothing applied across all maps<br>unless overridden per map.                                             |
| 11. | Throttle Lag Dn            | s ( Seconds ) or ratio            | Global throttle closing lag/<br>smoothing applied across all maps<br>unless overridden per map.                                             |
| 12. | Throttle Rev Chocking      | Dimensionless coeffi<br>cient     | Rev-choking factor limiting RPM<br>rise under partial throttle;<br>simulates intake restriction or anti<br>lag behavior.                    |
| 13. | Ignition Time S            | s ( Seconds ) or ratio            | Ignition timing delay or startup<br>ignition sequence duration; affects<br>initial fire-up and low-RPM<br>response.                         |
| 14. | Starter Engine Torque      | Nm ( Newton-meters )              | Cranking torque delivered by the<br>starter motor to bring the engine<br>from rest to idle RPM.                                             |

| ID    | Name              | Unit of Measurement                         | Description                                                                                                                |
|-------|-------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| 15a.  | Rpm Range         | RPM ( Revolutions per minute<br>)           | RPM window within which the<br>start/launch assist system actively<br>modulates torque and clutch slip.                    |
| 15b.  | Gain              | Dimensionless gain                          | Authority multiplier of the start<br>ECU assist torque and slip control<br>loop.                                           |
| 15c.  | Speed Range KMH   | km/h ( Kilometers per hour )                | Vehicle speed range over which<br>launch assist remains active<br>before disengaging.                                      |
| 15d.  | Rpm Limiter       | RPM ( Revolutions per minute<br>)           | Temporary RPM ceiling enforced<br>during launch assist to prevent<br>over-rev on clutch dump.                              |
| 15e.  | Limiter Cycles    | None ( Integer )                            | Number of rev-limiter cycles<br>permitted during launch assist<br>before hard cut.                                         |
| 15f.  | Use Clutch        | None ( Boolean : True /<br>False )          | Enables clutch-slip-based launch<br>control logic instead of pure<br>throttle modulation.                                  |
| 15g.  | Slip Ratio Target | Dimensionless ratio                         | Target wheel slip ratio maintained<br>by launch assist for optimal<br>traction off the line.                               |
| 15h.  | Clutch Gain       | Dimensionless gain                          | Clutch engagement modulation<br>gain within the launch assist<br>controller.                                               |
| 15i.  | Gas Gain          | Dimensionless gain                          | Throttle input scaling gain applied<br>during launch assist for traction<br>management.                                    |
| 16.   | Turbo Controllers | None ( Controller array )                   | Array of dynamic turbo boost<br>controllers; each entry contains a<br>Name and Stages pipeline (fields<br>16a, 16b1–16b8). |
| 16a.  | Name              | None ( String )                             | Internal identifier for a turbo or<br>wastegate controller block.                                                          |
| 16b1. | Input Var         | None ( Telemetry enum )                     | Telemetry channel driving the<br>controller stage (commonly RPMS,<br>Gas, or Boost pressure).                              |
| 16b2. | Combinator Mode   | None ( Math enum : Add /<br>Mult )          | How this stage output combines<br>with prior stages: additive offset or<br>multiplicative scaling.                         |
| 16b3. | Lut               | None ( .curve file path )                   | Look-up table mapping the input<br>variable to a turbo boost or<br>wastegate modifier.                                     |
| 16b4. | Filter Gain       | Coeffi<br>cient ( Smoothing<br>multiplier ) | Low-pass filter coeffi<br>cient<br>smoothing rapid input spikes for<br>stable boost control.                               |
| 16b5. | Up Limit          | Depends on input variable                   | Upper clamp on the processed<br>controller input signal.                                                                   |

| ID    | Name                     | Unit of Measurement                | Description                                                                                                                         |
|-------|--------------------------|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| 16b6. | Down Limit               | Depends on input variable          | Lower clamp on the processed<br>controller input signal.                                                                            |
| 16b7. | Current Value            | Depends on input variable          | Runtime output value of the<br>controller stage during simulation.                                                                  |
| 16b8. | Const Value              | Depends on input variable          | Fallback constant output when no<br>dynamic input or LUT is active.                                                                 |
| 17.   | Waste Gate Controllers   | None ( Controller array )          | Array of wastegate dynamic<br>controllers; reuses the same 16a<br>Name and 16b1–16b8 stage field<br>structure as Turbo Controllers. |
| 18.   | Max Turbo Boost          | bar ( bar gauge pressure )         | Maximum allowable turbocharger<br>boost pressure ceiling; hard limit<br>for forced-induction output.                                |
| 19.   | Bov Threshold            | bar or ratio                       | Blow-off valve (BOV) activation<br>threshold; pressure differential at<br>which excess boost is vented.                             |
| 20.   | Turbos To Load           | None ( .turbo file path )          | Path(s) to .turbo assets defining<br>turbocharger spool dynamics,<br>compressor maps, and wastegate<br>physics.                     |
| 21a.  | Capacity Kwh             | kWh ( Kilowatt-hours )             | Total electrical energy storage<br>capacity of the traction battery<br>pack.                                                        |
| 21b.  | Discharge Effi<br>ciency | Ratio ( 0.0 - 1.0 )                | Energy conversion effi<br>ciency from<br>battery to motor during discharge<br>(e.g., 0.80 = 80%).                                   |
| 21c.  | Charge Effi<br>ciency    | Ratio ( 0.0 - 1.0 )                | Energy conversion effi<br>ciency from<br>regenerative braking or charging<br>back into the battery.                                 |
| 21d.  | Temp Eff Loss Per Deg    | Ratio/°C ( Per degree<br>Celsius ) | Effi<br>ciency loss per degree of<br>battery temperature deviation from<br>optimal operating point.                                 |
| 21e.  | Convection K             | W/(m²·K) or coeffi<br>cient        | Natural convection heat transfer<br>coeffi<br>cient for passive battery<br>cooling.                                                 |
| 21f.  | Convection Forced K      | W/(m²·K) or coeffi<br>cient        | Forced convection coeffi<br>cient<br>when active cooling (airflow or<br>liquid) is applied.                                         |
| 21g.  | Thermal Capacity         | J/K or J/°C                        | Heat storage capacity of the<br>battery pack; controls temperature<br>rise rate under sustained load.                               |
| 21h.  | Max Temp                 | °C ( Degrees Celsius )             | Maximum safe operating<br>temperature before power derating<br>or thermal shutdown.                                                 |

| ID          | Name     | Unit of Measurement    | Description                                                                             |
|-------------|----------|------------------------|-----------------------------------------------------------------------------------------|
| <b>21</b> i | Min Temp | °C ( Degrees Celsius ) | Minimum operating temperature; below this, efficiency loss or power limiting may apply. |

#### <span id="page-95-0"></span>D. Example data

#### <span id="page-95-1"></span>I. Chosen Car Engine for Example

- Alpine A290 b (slug: ks\_alpine\_a290\_b)
- Ferrari SF 25 (slug: ks\_ferrari\_sf\_25)
- Chevrolet Camaro ZL1 (slug: ks\_renault\_5\_gt\_turbo)
- Datsun 240z Fairlady (slug : ks\_datsun\_240z\_fairlady)

#### <span id="page-95-2"></span>II. Example

#### <span id="page-95-3"></span>Alpine A290 b

```
1. Engine Type : motor
- 2. Inertia : 0.06000
 3. Power Curve : content\cars\ks alpine a290 b\data\HEADER POWER.curve
 4. Coast Curve : content\cars\ks_alpine_a290_b\data\coast.curve
 5. Maps : None
 6. Minimum: 0
 7. Limiter : 15200
- 8. Limiter Cycles : 20
9. Throttle Response Curve :
content\cars\ks alpine a290 b\data\throttle.curve
 10. Throttle Lag Up : 0.00000
 11. Throttle Lag Dn : 0.00000
 12. Throttle Rev Chocking: 0.00000
 13. Ignition Time S: 0.00000
 14. Starter Engine Torque: 0.00000
 15. Start E C U Assist
  - 15a. Rpm Range : 0.00000
   15b. Gain: 0.00000
   15c. Speed Range K H M : 0.00000
   15d. Rpm Limiter: 0.00000
  - 15e. Limiter Cycles : 0
   15f. Use Clutch: false
  - 15g. Slip Ratio Target : 0.00000
  - 15h. Clutch Gain : 0.00000
  L 15i. Gas Gain : 0.00000
 16. Turbo Controllers : None
 17. Waste Gate Controllers: None
 18. Max Turbo Boost : 0.00000
 19. Bov Threshold: 0.00000
 20. Turbos To Load : None
 21. Battery Data
 - 21a. Capacity Kwh : 52.000
```

```
│ ├ 21b. Dischage Efficiency : 0.800 
│ ├ 21c. Charge Efficiency : 0.600 
│ ├ 21d. Temp Eff Loss Per Deg : 0.01000 
│ ├ 21e. Convection K : 0.00100 
│ ├ 21f. Convection Forced K : 0.00050 
│ ├ 21g. Thermal Capacity : 100.000 
│ ├ 21h. Max Temp : 35.000 
└ └ 21i. Min Temp : 15.000
```

### <span id="page-96-0"></span>**Ferrari SF 25**

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
```

```
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
```

```
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
```

```
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
│ ├ 21h. Max Temp : 0.000 
└ └ 21i. Min Temp : 0.000
```

### <span id="page-99-0"></span>**Chevrolet Camaro ZL1**

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
```

```
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
```

<span id="page-100-0"></span>│ ├ 5b. Power Mult : 1.00000

│ ├ 5c. Consumption Mult : 1.00000

```
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
│ ├ 15h. Clutch Gain : 0.00000 
│ └ 15i. Gas Gain : 0.00000 
├ 16. Turbo Controllers : None 
├ 17. Waste Gate Controllers : None 
├ 18. Max Turbo Boost : 0.00000 
├ 19. Bov Threshold : 0.00000 
├ 20. Turbos To Load : None
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
```

# <span id="page-102-0"></span>**7. Car Setup [ .carsetup ]**

### <span id="page-102-1"></span>**A. Description**

Pit-garage snapshot: the adjustable values layered on top of fixed Car Data geometry and asset paths springs, dampers, alignment, aero targets, diff, electronics maps, and fuel load for a given session or preset.

Car Data defines what the car *is*. Car Setup defines how it is *configured today*. Limits and units (assets 6–7) decide what the UI will allow and how numbers are displayed.

### <span id="page-102-2"></span>**I. Role in the stack**

| Concern                                            | Handled here          | Handled elsewhere                        |
|----------------------------------------------------|-----------------------|------------------------------------------|
| ARB, bias, ducts, diff locks for<br>this preset    | .carsetup             | Hardware ceilings in other assets        |
| Per-corner wheel rate, bump<br>stops, helpers      | .carsetup Suspensions | Base coilover / suspension<br>kinematics |
| Damper clicks / rates                              | .carsetup Dampers     | Damper curves asset when used            |
| Pressures, camber, toe, caser,<br>compound index   | .carsetup Alignements | Tyre compound physics in .tyre           |
| TC / ABS / ESC / EBB / engine<br>map / ERS / boost | .carsetup Electronics | Maps defined in electronics /<br>engine  |
| Ride height targets, wing angles,<br>collars       | .carsetup Aero        | Wing / surface3d aero maps               |
| Legal min/max / steps                              | —                     | 6. Car Setup Limits                      |
| Display units (bar, clicks, deg)                   | —                     | 7. Car Setup Units                       |

Loaded from Car Data stock / AI / wet setup paths, or from tuning-part / performance-mode packages. *Import Setup* can inherit another .carsetup as a base.

### <span id="page-102-3"></span>**II. What you are really tuning**

- 1. **Mechanical balance** *Arbs* (typically index 1 front, 2 rear) shift roll stiffness front/rear primary understeer/oversteer lever without touching springs. *Steer Ratio* changes rack feel. Brakes block sets *Front Bias*, optional *Torque Multiplier*, and *Brake Ducts*. Differential *Power* / *Coast* / *Preload* shape exit drive and entry stability (often zeroed on open or non-adjustable diffs; race cars fill them in — 488 uses coast and preload).
- 2. **Springs and stops** Per-corner *Suspensions[]*: *Wheel Rate* is the main spring (or wheel-rate) number. Bump stops up/down (*Range* + *Rate*) catch end travel. Helper springs (*Helper Rate* / *Range*) fill gaps when used. Quattro / Junior sit around mid road-race rates; 488 Challenge jumps to much higher wheel rates (about 150000-160000 in the example).
- 3. **Dampers** Per-corner slow/fast bump and rebound. Schema skips *4d* and goes to *4e. Fast Rebound*. Values may be authored as physical coefficients or as click-like numbers depending on the car (Quattro slow bump thousands; 488 slow bump single digits) — always read Limits/Units for that vehicle.

- 4. **Alignment and tyres** Per-corner pressure, camber, toe, caster, plus derived *Static Camber* / *Toe Out Linear*, and *Compound* index into Car Data tyre lists. Race presets push more negative camber (488 about -3.5 deg) than road examples (about -1.0 to -1.3).
- 5. **Electronics package** TC1/TC2, ABS, ESC, EBB, engine map, turbo boost level, ERS maps/levels, telemetry laps. Safe race presets often raise TC/ABS (488 safe\_1 uses 3/3); older or mechanical presets may leave aids at 0.
- 6. **Aero and fuel** Collar positions, front/rear target ride heights, front/rear wing angles (488 rear wing 12 deg in the example; Quattro/Junior wings at 0). *Fuel Strategy* is session fuel load. Metadata: *Final State Name*, *Version*, *Is Setup Shared*.

### <span id="page-103-0"></span>**III. Architecture**

### <span id="page-103-1"></span>**1 - IMPORT AND MECHANICAL BALANCE (SCHEMA 1-2)**

Optional import path; ARBs, steer ratio, brakes sub-block, differential sub-block.

### <span id="page-103-2"></span>**2 - PER-CORNER STRUCTURE (SCHEMA 3-5)**

Indexed suspensions, dampers, and alignements (usually 1-4 = LF, RF, LR, RR). This is where left/right and front/rear asymmetry lives.

### <span id="page-103-3"></span>**3 - ELECTRONICS (SCHEMA 6)**

Driver-aid and powertrain map selectors for this preset.

### <span id="page-103-4"></span>**4 - AERO AND FUEL (SCHEMA 7-8)**

Platform and wing targets; fuel quantity for the run.

### <span id="page-103-5"></span>**5 - PRESET IDENTITY (SCHEMA 9-11)**

Final state name/path, version integer, shared flag for multiplayer or garage sharing.

### <span id="page-103-6"></span>**IV. How to read the examples**

### <span id="page-103-7"></span>**1 - AUDI SPORT QUATTRO**

Mechanical road/rally style: ARBs 25000 / 20000, brake bias 72, diff locks at 0. Wheel rates about 50000 front / lower rear in the dump, cold pressures 28, mild camber (-1.0). ABS on, TC off. Wings at 0, fuel 30. A balanced base preset without heavy race aero.

### <span id="page-103-8"></span>**2 - ALFA ROMEO JUNIOR**

*Stiffer ARBs (about 40000 / 38000), bias 80, pressures 26-27, camber about -1.3. TC and ABS both 1. Very low fuel in the dump (3) — short-run or display preset. Still road-car aero angles at 0.*

### <span id="page-103-9"></span>**3 - FERRARI 488 CHALLENGE ECO (PRESET SAFE\_1)**

Race Challenge setup: ARB split 34000 / 17000, bias 64, coast lock 0.3 and preload 10. High wheel rates, aggressive camber (-3.5), lower pressures (about 23.5-24), rear wing 12 deg. TC 3 / ABS 3 — clearly a safer electronics package on a stiff aero platform. Named mech/visual preset pair in *Final State Name*.

### <span id="page-104-0"></span>**V. Practical notes**

- Setup cannot invent hardware: if Car Data has no wing path or the tyre list is empty, wing angle and compound indices do nothing useful.
- Always pair with **Setup Limits** before copying numbers between cars min/max/step and click scales differ.
- Damper and spring magnitudes are not universal SI across all examples; treat them as car-local until Units/Limits say otherwise.
- Schema spelling: **Alignements** (not Alignments); damper ID jumps **4c to 4e** (no 4d).
- Import Setup plus performance-mode packages can stack overrides check what actually loaded insession.
- Electronics indices must match maps defined in engine / electronics assets, or the garage selection is an empty switch.

### <span id="page-104-1"></span>**VI. Related assets**

- **3. Car Data [\[.car\]](#page-35-0)** stock / AI / wet setup paths that load this file
- **• 6 / 7. Car Setup [Limits](#page-118-0) / [Units](#page-174-0)** legal range and display mapping
- **• 11 / 17 / 19 / 20. [Coilover](#page-226-0) / [Suspension](#page-286-0) / [Tyre](#page-307-0) / [Wing](#page-328-0)** physics underneath the garage numbers
- **8. Car Tuning Parts [\[.tuningpart\]](#page-184-0)** can embed or swap full setup packages
- **9 / 4 / 18. [Electronics](#page-205-0) / [Engine](#page-87-0) / [Turbo](#page-301-0)** maps selected by Electronics fields

### <span id="page-104-2"></span>**B. Schema**

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
```

```
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
│ ├ 5f. Toe Out Linear : float
│ └ 5g. Compound : float
├ 6. Electronics : object
│ ├ 6a. Tc1 : float
│ ├ 6b. Tc2 : float
│ ├ 6c. Abs : float
│ ├ 6d. Esc : float
│ ├ 6e. Ebb : float
│ ├ 6f. Engine Map : float
│ ├ 6g. Telemetry Laps to Record : float
│ ├ 6h. Turbo Boost Lv : float
│ ├ 6i. Ers Deployment Map : float
│ ├ 6j. Ers Recharge Lv : float
│ └ 6k. Ers Heat Charging : float
├ 7. Aero : object
│ ├ 7a. Collar Positions Mm [x] : float | can have multiple Collar 
Positions Mm 
│ ├ 7b. Front Target Height : float
│ ├ 7c. Rear Target Height : float
│ ├ 7d. Front Wing Angle : float
│ └ 7e. Rear Wing Angle : float
├ 8. Fuel Strategy : object
│ └ 8a. Fuel : float
├ 9. Final State Name : string - path
├ 10. Version : integer
├ 11. Is Setup Shared : boolean
```

### <span id="page-105-0"></span>**C. Measurement Units & Descriptions**

| ID | Name               | Unit of Measurement | Description                                                                                                           |
|----|--------------------|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1. | Import Setup       | None ( File path )  | Optional path to a base .carsetup<br>preset from which this setup<br>inherits or overlays values.                     |
| 2. | Mechanical Balance | None ( Object )     | Parent block grouping chassis<br>balance adjustments: anti-roll<br>bars, steering ratio, brakes, and<br>differential. |

| ID   | Name              | Unit of Measurement                          | Description                                                                                                                           |
|------|-------------------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 2a.  | Arbs              | Nm/deg or N/m ( Anti-roll bar<br>stiffness ) | Anti-roll bar stiffness values; index<br>1 = front axle, index 2 = rear axle.<br>Primary tool for shifting roll<br>stiffness balance. |
| 2b.  | Steer Ratio       | Ratio ( :1 ) or clicks                       | Adjustable steering rack ratio<br>override applied at setup level;<br>modifies low-speed agility and<br>steering wheel sensitivity.   |
| 2c.  | Brakes            | None ( Object )                              | Brake setup sub-block within<br>Mechanical Balance; contains<br>bias, torque scaling, and duct<br>settings.                           |
| 2c1. | Front Bias        | % ( Percentage )                             | Brake balance percentage sent to<br>the front axle (e.g., 72 = 72%<br>front / 28% rear).                                              |
| 2c2. | Torque Multiplier | % or dimensionless multiplier                | Global braking torque scaling<br>factor for this setup (100 = 100%<br>of base brake system torque).                                   |
| 2c3. | Brake Ducts       | Ratio ( 0.0 - 1.0 ) or clicks                | Brake cooling duct opening<br>level(s); multiple entries typically<br>map to front/rear duct positions.                               |
| 2d.  | Differential      | None ( Object )                              | Differential setup sub-block within<br>Mechanical Balance; governs<br>power, coast, and preload lock.                                 |
| 2d1. | Power             | % or Nm ( Differential lock )                | Differential locking intensity under<br>acceleration (on-throttle); higher<br>values increase drive-wheel<br>coupling on corner exit. |
| 2d2. | Coast             | % or Nm ( Differential lock )                | Differential locking intensity on<br>coast/deceleration; stabilizes the<br>rear under braking and lift-off.                           |
| 2d3. | Preload           | Nm ( Newton-meters )                         | Static preload torque locking the<br>differential plates at zero throttle;<br>resists free differential action mid<br>corner.         |
| 3.   | Suspensions       | None ( Object array, per<br>wheel )          | Per-corner suspension block;<br>indices 1–4 map to LF, RF, LR, RR<br>wheels respectively.                                             |
| 3a.  | Wheel Rate        | N/m ( Newtons per meter )                    | Effective wheel-rate spring<br>stiffness at this corner; controls<br>ride frequency, body roll, and aero<br>platform stability.       |
| 3b.  | Bump Stop Up      | None ( Object )                              | Upper bump-stop definition within<br>each Suspensions entry; limits<br>compression travel beyond spring<br>range.                     |
| 3b1. | Range             | m ( Meters )                                 | Travel range before the upper<br>bump-stop engages (Suspensions<br>> Bump Stop Up).                                                   |

| ID   | Name           | Unit of Measurement                  | Description                                                                                                                              |
|------|----------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 3b2. | Rate           | N/m or N ( Bump-stop<br>stiffness )  | Stiffness/force rate of the upper<br>bump-stop resisting compression<br>beyond the range threshold.                                      |
| 3c.  | Bump Stop Down | None ( Object )                      | Lower bump-stop definition within<br>each Suspensions entry; limits<br>droop/extension travel.                                           |
| 3c1. | Range          | m ( Meters )                         | Travel range before the lower<br>(rebound) bump-stop engages<br>(Suspensions > Bump Stop<br>Down).                                       |
| 3c2. | Rate           | N/m or N ( Bump-stop<br>stiffness )  | Stiffness/force rate of the lower<br>bump-stop resisting droop/<br>extension.                                                            |
| 3d.  | Helper Rate    | N/m ( Spring rate )                  | Stiffness of the helper/tender<br>spring assisting the main coil at<br>low compression.                                                  |
| 3e.  | Helper Range   | m ( Meters )                         | Travel range over which the helper<br>spring is active before the main<br>spring fully carries load.                                     |
| 4.   | Dampers        | None ( Object array, per<br>wheel )  | Per-corner damper settings;<br>indices 1–4 map to LF, RF, LR, RR.<br>Values may be raw N·s/m or UI<br>clicks depending on carsetupunits. |
| 4a.  | Slow Bump      | N·s/m or clicks                      | Slow-shaft-speed compression<br>damping; controls body roll and<br>pitch from driver inputs (braking,<br>cornering).                     |
| 4b.  | Fast Bump      | N·s/m or clicks                      | Fast-shaft-speed compression<br>damping; absorbs kerb strikes,<br>bumps, and high-frequency track<br>irregularities.                     |
| 4c.  | Slow Rebound   | N·s/m or clicks                      | Slow-shaft-speed extension<br>damping; regulates how the<br>chassis settles after weight<br>transfer releases.                           |
| 4e.  | Fast Rebound   | N·s/m or clicks                      | Fast-shaft-speed extension<br>damping; controls how quickly the<br>tyre returns to the track surface<br>after a kerb hit.                |
| 5.   | Alignements    | None ( Object array, per<br>wheel )  | Per-corner tyre pressure and<br>alignment geometry; indices 1–4<br>map to LF, RF, LR, RR.                                                |
| 5a.  | Pressure       | PSI or bar ( Cold tyre<br>pressure ) | Cold inflation pressure before<br>leaving the pits; determines hot<br>operating pressure and tyre<br>carcass temperature window.         |

| ID  | Name                        | Unit of Measurement          | Description                                                                                                                         |
|-----|-----------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| 5b. | Camber                      | deg ( Degrees )              | Adjustable camber angle (negative<br>= top of wheel leans inward);<br>maximizes contact patch during<br>body roll in corners.       |
| 5c. | Toe                         | deg ( Degrees )              | Toe angle relative to vehicle<br>centerline; toe-out front increases<br>turn-in, toe-in rear stabilizes<br>straight-line stability. |
| 5d. | Caster                      | deg ( Degrees )              | Steering axis caster angle;<br>influences straight-line stability,<br>self-centering torque, and camber<br>gain during steering.    |
| 5e. | Static Camber               | deg ( Degrees )              | Computed/static camber at ride<br>height including kinematic offset;<br>read-only or derived alignment<br>reference.                |
| 5f. | Toe Out Linear              | deg/m or rad/m ( Toe curve ) | Linear toe change rate as a<br>function of suspension travel or<br>steering; models compliance and<br>kinematic toe curve.          |
| 5g. | Compound                    | None ( Compound index )      | Tyre compound selection index<br>referencing the available front/rear<br>tyre compound paths in Car Data.                           |
| 6.  | Electronics                 | None ( Object )              | Driver-aid and powertrain map<br>presets stored in this setup (TC,<br>ABS, ESC, engine map, ERS,<br>turbo).                         |
| 6a. | Tc1                         | None ( Map level / index )   | Traction Control map level (primary<br>TC); references TC settings<br>defined in Car Data electronics.                              |
| 6b. | Tc2                         | None ( Map level / index )   | Secondary Traction Control map<br>level for dual-TC systems.                                                                        |
| 6c. | Abs                         | None ( Map level / index )   | ABS intervention map level;<br>controls slip thresholds and<br>pulsing aggressiveness.                                              |
| 6d. | Esc                         | None ( Map level / index )   | Electronic Stability Program map<br>level; governs yaw/brake<br>intervention authority.                                             |
| 6e. | Ebb                         | None ( Map level / index )   | Electronic Brake Balance mode or<br>level for dynamic bias adjustment.                                                              |
| 6f. | Engine Map                  | None ( Map index )           | Engine power map selection<br>referencing engine map entries in<br>the .carengine asset.                                            |
| 6g. | Telemetry Laps To<br>Record | None ( Integer )             | Number of laps of onboard<br>telemetry to retain when this setup<br>is active.                                                      |
| 6h. | Turbo Boost Lv              | bar or level index           | Turbo boost level preset for<br>forced-induction engines.                                                                           |

| ID  | Name                | Unit of Measurement                    | Description                                                                                                                   |
|-----|---------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| 6i. | Ers Deployment Map  | None ( Map index )                     | Hybrid ERS power deployment<br>map selection.                                                                                 |
| 6j. | Ers Recharge Lv     | None ( Level index )                   | ERS regenerative recovery<br>aggressiveness level.                                                                            |
| 6k. | Ers Heat Charging   | None ( Level index )                   | MGU-H heat-to-battery charging<br>level for hybrid systems.                                                                   |
| 7.  | Aero                | None ( Object )                        | Aerodynamic setup block: ride<br>heights, spring collar positions,<br>and adjustable wing angles.                             |
| 7a. | Collar Positions Mm | mm ( millimeters )                     | Spring perch/collar position per<br>corner controlling static ride<br>height; indices 1–4 = LF, RF, LR,<br>RR.                |
| 7b. | Front Target Height | mm ( millimeters )                     | Target front ride height reference<br>for aero platform setup and<br>regulatory ride-height checks.                           |
| 7c. | Rear Target Height  | mm ( millimeters )                     | Target rear ride height; combined<br>with front height defines rake<br>(nose-up/nose-down aero<br>attitude).                  |
| 7d. | Front Wing Angle    | deg ( Degrees )                        | Mechanical angle of the front aero<br>device (splitter/wing); increases<br>downforce and drag when raised.                    |
| 7e. | Rear Wing Angle     | deg ( Degrees )                        | Mechanical angle of the rear wing<br>element; primary high-speed<br>cornering stability vs. straight-line<br>speed trade-off. |
| 8.  | Fuel Strategy       | None ( Object )                        | Fuel load planning block for this<br>setup preset.                                                                            |
| 8a. | Fuel                | L ( Liters )                           | Fuel load strategy for this setup<br>preset; affects weight, CG<br>position, and stint length planning.                       |
| 9.  | Final State Name    | None ( String / preset<br>identifier ) | Composite preset identifier linking<br>mechanical and visual setup<br>states (e.g., mech + visual preset<br>names).           |
| 10. | Version             | None ( Integer )                       | Setup file format version for<br>backward compatibility with the<br>editor and simulation loader.                             |
| 11. | Is Setup Shared     | None ( Boolean : True /<br>False )     | Indicates whether this setup<br>preset is shared/exportable across<br>sessions or locked to a single<br>vehicle profile.      |

#### <span id="page-110-0"></span>D. Example data

#### <span id="page-110-1"></span>I. Chosen Car Engine for Example

```
- Audi Sport Quattro ( slug : ks_audi_sport_quattro )
```

- Alfa Romeo Junior (slug: ks\_alfa\_romeo\_junior)
- Ferrari 488 Challenge Evo (slug: ks ferrari 488 challenge evo [preset: safe 1]

#### <span id="page-110-2"></span>II. Example

#### <span id="page-110-3"></span>**Audi Sport Quattro**

```
1. Import Setup: None
2. Mechanical Balance
 - 2a. Arbs 1 : 25000.00000
 - 2a. Arbs 2 : 20000.00000
 - 2b. Steer Ratio : 18.00000
  2c. Brakes
   - 2c1. Front Bias : 72.00000
   2c2. Torque Multiplier : 100.00000
   L 2c3. Brake Ducts : None
  2d. Differential
   - 2d1. Power : 0.00000
    2d2. Coast: 0.00000
  2d3. Preload : 0.00000
3. Suspensions 1
 - 3a. Wheel Rate : 50000.00000
  3b. Bump Stop Up
   - 3b1. Range : 0.02645
  3b2. Rate: 650.00000
  3c. Bump Stop Down
   - 3c1. Range : 0.11855
3c2. Rate : 650.00000
  3d. Helper Rate : 0.00000
L 3e. Helper Range: 0.00000
3. Suspensions 2
 - 3a. Wheel Rate : 50000.00000
  3b. Bump Stop Up
   - 3b1. Range : 0.02645
3b2. Rate : 650.00000
  3c. Bump Stop Down
   - 3c1. Range : 0.11855
  3c2. Rate: 650.00000
  3d. Helper Rate: 0.00000
3e. Helper Range : 0.00000
3. Suspensions 3
 - 3a. Wheel Rate : 42750.00000
  3b. Bump Stop Up
   - 3b1. Range : 0.04487
  3b2. Rate: 400.00000
  3c. Bump Stop Down
   - 3c1. Range : 0.04513
   L 3c2. Rate : 400.00000
```

```
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
```

```
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
│ └ 8a. Fuel : 30.00000 
├ 9. Final State Name : 
ks_audi_sport_quattro_preset_sq_mech_1_preset_sq_visual_1 
├ 10. Version : None 
├ 11. Is Setup Shared : false
```

### <span id="page-112-0"></span>**Alfa Romeo Junior**

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
```

```
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
```

```
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
```

```
├ 10. Version : 0 
├ 11. Is Setup Shared : false
```

### <span id="page-115-0"></span>**Ferrari 488 Challenge Evo [ preset : safe\_1 ]**

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
```

```
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
```

```
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

# <span id="page-118-0"></span>**6. Car Setup Limits [ .carsetuplimits ]**

### <span id="page-118-1"></span>**A. Description**

Garage rulebook for .carsetup: which parameters exist as sliders, how far they can move, in what steps, and how the UI should treat them.

Car Setup stores the *current* values. Setup Limits define the *allowed envelope* and interface behaviour. Without limits, the garage has no legal min/max/step model for that car.

### <span id="page-118-2"></span>**I. Role in the stack**

| Concern                                      | Handled here    | Handled elsewhere                         |
|----------------------------------------------|-----------------|-------------------------------------------|
| Min / max / step per setup field             | .carsetuplimits | —                                         |
| Locked vs adjustable ( Is<br>Modifiable )    | .carsetuplimits | —                                         |
| Hide raw value, sign, boolean<br>treatment   | .carsetuplimits | —                                         |
| Optional LUT for non-linear click<br>mapping | .carsetuplimits | Curves on disk                            |
| Display unit string on a limit<br>object     | Often here      | Canonical labels in 7. Car Setup<br>Units |
| Actual spring/damper/aero<br>numbers in use  | —               | 5. Car Setup                              |
| Physics hardware underneath                  | —               | Coilover, tyre, wing, etc.                |

Usually referenced from Car Data *Setup Limits* path. Tree layout mirrors Car Setup (mechanical balance, suspensions, dampers, alignments, electronics, aero, fuel).

### <span id="page-118-3"></span>**II. What you are really tuning**

1. **The limit object (shared anatomy)** —Almost every tunable reuses the same nested fields (schema IDs reused as *2a1*…*2a10* under each parent):

| Field         | Role                                       |
|---------------|--------------------------------------------|
| Step          | Garage increment per click                 |
| Min / Max     | Absolute allowed range                     |
| Lut           | Optional curve remapping clicks to physics |
| Is Modifiable | false = locked / greyed out                |
| Hide Value    | Hide numeric readout                       |
| Is Negative   | Sign / direction convention for UI         |

| Field             | Role                                              |
|-------------------|---------------------------------------------------|
| Unit              | Label string (may be None if Units asset owns it) |
| Fractional Digits | Decimal precision on screen                       |
| Treat As Boolean  | Present as on/off instead of a continuous slider  |

When *Min == Max* and *Is Modifiable* is false, the parameter is frozen at a factory value.

- 2. **What you lock vs open** Road cars often freeze ARBs, springs, dampers, wings, and diff only pressures or mild alignment stay open. Motorsport cars open most flags but keep **narrow** min/max windows so the platform stays in its aero/kinematic sweet spot. BOP can tighten windows (raise minimum wing, clamp ride height) without rewriting core Car Data mass or engine curves.
- 3. **Categories (same map as setup)** Mechanical balance (ARBs, steer ratio, brake bias/ducts, diff), per-corner suspensions and dampers, alignments (pressures, camber, toe…), electronics map indices, aero (collars, heights, wing angles), fuel strategy, plus *Use Single Compound* for tyre UI behaviour.

### <span id="page-119-0"></span>**III. Architecture**

### <span id="page-119-1"></span>**1 - BINDING (SCHEMA 1)**

*Car Data* path (often None when the limits file is already paired by Car Data's own Setup Limits field).

### <span id="page-119-2"></span>**2 - MECHANICAL BALANCE (SCHEMA 2)**

Limit objects for ARBs *[x]*, steer ratio, brakes (bias, torque multiplier, ducts), differential (power, coast, preload). Same subtree shape as setup, but each leaf is a limit object, not a float.

### <span id="page-119-3"></span>**3 - PER-CORNER AND ELECTRONICS (SCHEMA 3-6)**

Suspensions, dampers, alignments arrays; electronics selectors (TC, ABS, maps…). Indexing matches setup corners (typically 1-4).

### <span id="page-119-4"></span>**4 - AERO, FUEL, COMPOUND MODE (SCHEMA 7-9)**

Aero limit blocks, fuel limit, *Use Single Compound* flag for whether front/rear compounds are forced to stay linked in the UI.

### <span id="page-119-5"></span>**IV. How to read the examples**

### <span id="page-119-6"></span>**1 - BMW M4 CSL (LOCKED PRODUCTION-STYLE ENVELOPE)**

ARBs show Is Modifiable : false with Min equal to Max (front stuck at 30000, rear at 11000 in the dump). That is the stock profile: the garage exposes little or no ARB travel because the car is not meant to be a full race adjuster. Read other false flags the same way — frozen factory identity.

### <span id="page-119-7"></span>**2 - LAMBORGHINI COUNTACH (OPEN ADJUSTABLE ENVELOPE)**

ARBs *Is Modifiable : true* with real windows (front about 28000-68000 step 4000; rear about 5000-50000 step 5000). The car can be explored across a wide mechanical range. Compare min/max width and step size to judge how "race engineer" vs "coarse kit" the garage feels.

### <span id="page-120-0"></span>**V. Practical notes**

- A setup value outside min/max should be treated as illegal or clamped fix the setup or the limits, do not assume the sim will honour out-of-range garage numbers.
- Copying setup numbers between cars without copying limits is how you get greyed sliders or impossible clicks.
- *Step* and LUT together define the feel of the menu: linear physics steps vs non-linear click tables.
- Schema reuses limit-field IDs (*2a1…2a10*) under many parents that is intentional templating, not a documentation error.
- Setup file spelling is **Alignements**; limits schema may say **Alignments** same corner block.
- Fuel under Fuel Strategy is **8a** in the corrected schema tree (paired with setup's fuel field).
- For display unit policy, still check **7. Car Setup Units**; limit *Unit* strings can be None.

### <span id="page-120-1"></span>**VI. Related assets**

- **5. Car Setup [\[.carsetup\]](#page-102-0)** values constrained by these limits
- **• 7. Car Setup Units [\[.carsetupunits\]](#page-174-0)** unit labels / localisation for the same tree
- **• 3. Car Data [\[.car\]](#page-35-0)** *Setup Limits* path that loads this file
- **8. Car Tuning Parts [\[.tuningparts\]](#page-184-0)** performance modes may ship with their own setup/limit packages

### <span id="page-120-2"></span>**B. Schema**

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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

```
│ │ ├ 2a3. Max : float
│ │ ├ 2a4. Lut : string - path
│ │ ├ 2a5. Is Modifiable : boolean
│ │ ├ 2a6. Hide Value : boolean
│ │ ├ 2a7. Is Negative : boolean
│ │ ├ 2a8. Unit : string
│ │ ├ 2a9. Fractional Digits : integer
│ └ └ 2a10. Treat As Boolean : boolean
├ 8. Fuel Strategy : object
│ ├ 8a. Fuel : object
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
└ 9. Use Single Compound : boolean
```

### <span id="page-129-0"></span>**C. Measurement Units & Descriptions**

| ID   | Name               | Unit of Measurement                                | Description                                                                                                          |
|------|--------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 1.   | Car Data           | None ( File path )                                 | Path to the parent .car asset this<br>limits file is bound to; links<br>regulatory bounds to the correct<br>vehicle. |
| 2.   | Mechanical Balance | None ( Object )                                    | Parent block for chassis balance<br>limit definitions: ARBs, steering,<br>brakes, and differential.                  |
| 2a.  | Arbs               | None ( Limit object array )                        | Per-axle anti-roll bar limit blocks;<br>index 1 = front, 2 = rear. Each<br>entry contains fields 2a1–2a10.           |
| 2a1. | Step               | Depends on parameter<br>( physics unit or clicks ) | Garage increment applied per<br>adjustment click; defines the<br>resolution of slider/stepper<br>controls.           |
| 2a2. | Min                | Depends on parameter                               | Absolute minimum allowable<br>physics value for the linked setup<br>parameter.                                       |
| 2a3. | Max                | Depends on parameter                               | Absolute maximum allowable<br>physics value for the linked setup<br>parameter.                                       |
| 2a4. | Lut                | None ( .curve file path )                          | Optional look-up table mapping<br>linear UI steps to non-linear<br>physical output values.                           |
| 2a5. | Is Modifiable      | None ( Boolean : True /<br>False )                 | When false, the garage slider is<br>locked/greyed out; parameter<br>cannot be changed by the user.                   |

| ID    | Name              | Unit of Measurement                 | Description                                                                                         |
|-------|-------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| 2a6.  | Hide Value        | None ( Boolean : True /<br>False )  | When true, obscures the raw<br>numeric value in the UI<br>(proprietary team data simulation).       |
| 2a7.  | Is Negative       | None ( Boolean : True /<br>False )  | UI sign convention flag; allows<br>negative values to display/be<br>edited correctly (camber, toe). |
| 2a8.  | Unit              | None ( String )                     | Display unit label rendered in the<br>garage UI (e.g., mm, deg, PSI, bar,<br>Nm, clicks).           |
| 2a9.  | Fractional Digits | None ( Integer )                    | Number of decimal places shown<br>in the garage UI for this parameter.                              |
| 2a10. | Treat As Boolean  | None ( Boolean : True /<br>False )  | Renders the parameter as an on/<br>off toggle instead of a numeric<br>slider when true.             |
| 2b.   | Steer Ratio       | None ( Limit object )               | Limit definition for the adjustable<br>steering ratio parameter in Car<br>Setup.                    |
| 2c.   | Brakes            | None ( Object )                     | Brake setup limits sub-block<br>within Mechanical Balance.                                          |
| 2c1.  | Front Bias        | None ( Limit object )               | Limit definition for brake balance<br>front percentage.                                             |
| 2c2.  | Torque Multiplier | None ( Limit object )               | Limit definition for global braking<br>torque scaling.                                              |
| 2c3.  | Brake Ducts       | None ( Limit object array )         | Per-duct brake cooling limit<br>blocks; multiple entries for front/<br>rear duct positions.         |
| 2d.   | Differential      | None ( Object )                     | Differential setup limits sub-block<br>within Mechanical Balance.                                   |
| 2d1.  | Power             | None ( Limit object )               | Limit definition for on-throttle<br>differential lock intensity.                                    |
| 2d2.  | Coast             | None ( Limit object )               | Limit definition for coast/off<br>throttle differential lock intensity.                             |
| 2d3.  | Preload           | None ( Limit object )               | Limit definition for static<br>differential preload torque.                                         |
| 3.    | Suspensions       | None ( Object array, per<br>wheel ) | Per-corner suspension limit<br>blocks; indices 1–4 = LF, RF, LR,<br>RR.                             |
| 3a.   | Wheel Rate        | None ( Limit object )               | Limit definition for per-corner<br>wheel-rate spring stiffness.                                     |
| 3b.   | Bump Stop Up      | None ( Object )                     | Upper bump-stop limit sub-block<br>within each Suspensions entry.                                   |
| 3b1.  | Range             | None ( Limit object )               | Bump-stop travel range limit.<br>Under 3b Bump Stop Up; ID<br>reused under 3c Bump Stop<br>Down.    |

| ID   | Name           | Unit of Measurement                 | Description                                                                                              |
|------|----------------|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| 3b2. | Rate           | None ( Limit object )               | Bump-stop stiffness/force rate<br>limit. Under 3b Bump Stop Up; ID<br>reused under 3c Bump Stop<br>Down. |
| 3c.  | Bump Stop Down | None ( Object )                     | Lower bump-stop limit sub-block;<br>contains 3b1 (Range) and 3b2<br>(Rate) limit objects per schema.     |
| 3d.  | Helper Rate    | None ( Limit object )               | Limit definition for helper/tender<br>spring stiffness.                                                  |
| 3e.  | Helper Range   | None ( Limit object )               | Limit definition for helper spring<br>active travel range.                                               |
| 4.   | Dampers        | None ( Object array, per<br>wheel ) | Per-corner damper limit blocks;<br>indices 1–4 = LF, RF, LR, RR.                                         |
| 4a.  | Slow Bump      | None ( Limit object )               | Limit definition for slow-speed<br>compression damper clicks/<br>values.                                 |
| 4b.  | Fast Bump      | None ( Limit object )               | Limit definition for fast-speed<br>compression damper clicks/<br>values.                                 |
| 4c.  | Slow Rebound   | None ( Limit object )               | Limit definition for slow-speed<br>rebound damper clicks/values.                                         |
| 4d.  | Fast Rebound   | None ( Limit object )               | Limit definition for fast-speed<br>rebound damper clicks/values (4d<br>here; Car Setup uses 4e).         |
| 5.   | Alignments     | None ( Object array, per<br>wheel ) | Per-corner alignment and tyre limit<br>blocks; indices 1–4 = LF, RF, LR,<br>RR.                          |
| 5a.  | Pressure       | None ( Limit object )               | Limit definition for cold tyre<br>inflation pressure.                                                    |
| 5b.  | Camber         | None ( Limit object )               | Limit definition for adjustable<br>camber angle.                                                         |
| 5c.  | Toe            | None ( Limit object )               | Limit definition for toe angle.                                                                          |
| 5d.  | Caster         | None ( Limit object )               | Limit definition for caster angle.                                                                       |
| 5e.  | Static Camber  | None ( Limit object )               | Limit definition for computed/<br>static camber display or override<br>bounds.                           |
| 5f.  | Toe Out Linear | None ( Limit object )               | Limit definition for linear toe<br>compliance curve coeffi<br>cient.                                     |
| 5g.  | Compound       | None ( Limit object )               | Limit definition for tyre compound<br>selection index bounds.                                            |
| 6.   | Electronics    | None ( Object )                     | Driver-aid and powertrain map<br>limit definitions stored in the<br>garage UI.                           |
| 6a.  | Tc1            | None ( Limit object )               | Limit definition for primary Traction<br>Control map level selection.                                    |

| ID  | Name                        | Unit of Measurement                | Description                                                                                          |
|-----|-----------------------------|------------------------------------|------------------------------------------------------------------------------------------------------|
| 6b. | Tc2                         | None ( Limit object )              | Limit definition for secondary TC<br>map level.                                                      |
| 6c. | Abs                         | None ( Limit object )              | Limit definition for ABS map level<br>selection.                                                     |
| 6d. | Esc                         | None ( Limit object )              | Limit definition for ESP/stability<br>control map level.                                             |
| 6e. | Ebb                         | None ( Limit object )              | Limit definition for Electronic<br>Brake Balance level.                                              |
| 6f. | Engine Map                  | None ( Limit object )              | Limit definition for engine power<br>map index selection.                                            |
| 6g. | Telemetry Laps To<br>Record | None ( Limit object )              | Limit definition for onboard<br>telemetry lap recording count.                                       |
| 6h. | Turbo Boost Lv              | None ( Limit object )              | Limit definition for turbo boost<br>level preset.                                                    |
| 6i. | Ers Deployment Map          | None ( Limit object )              | Limit definition for ERS<br>deployment map index.                                                    |
| 6j. | Ers Recharge Lv             | None ( Limit object )              | Limit definition for ERS recharge<br>aggressiveness level.                                           |
| 6k. | Ers Heat Charging           | None ( Limit object )              | Limit definition for MGU-H heat<br>charging level.                                                   |
| 7.  | Aero                        | None ( Object )                    | Aerodynamic setup limit block:<br>ride heights, collar positions, and<br>wing angles.                |
| 7a. | Collar Positions            | None ( Limit object array )        | Per-corner spring collar/ride<br>height limit blocks under 7. Aero;<br>indices 1–4 = LF, RF, LR, RR. |
| 7b. | Front Target Height         | None ( Limit object )              | Limit definition for front target ride<br>height.                                                    |
| 7c. | Rear Target Height          | None ( Limit object )              | Limit definition for rear target ride<br>height.                                                     |
| 7d. | Front Wing Angle            | None ( Limit object )              | Limit definition for front aero<br>device angle adjustment range.                                    |
| 7e. | Rear Wing Angle             | None ( Limit object )              | Limit definition for rear wing angle<br>adjustment range.                                            |
| 8.  | Fuel Strategy               | None ( Object )                    | Fuel load planning limit block.                                                                      |
| 8a. | Fuel                        | None ( Limit object )              | Fuel load volume limit under 8.<br>Fuel Strategy.                                                    |
| 9.  | Use Single Compound         | None ( Boolean : True /<br>False ) | Forces all four corners to share a<br>single tyre compound selection<br>when true.                   |

### <span id="page-133-0"></span>**D. Example data**

### <span id="page-133-1"></span>**I. Chosen Car Engine for Example**

- BMW M4 CSL ( slug : ks\_bmw\_m4\_csl )
- Lamborghini Countach ( slug : ks\_lamborghini\_countach )

### <span id="page-133-2"></span>**II. Example**

### <span id="page-133-3"></span>**BMW M4 CSL**

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
│ │ │ ├ 2a2. Min : 0.00000 
│ │ │ ├ 2a3. Max : 100.00000 
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false
```

```
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
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 47000.00000 
│ │ ├ 2a3. Max : 47000.00000 
│ │ ├ 2a4. Lut : None
```

```
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
│ ├ 3d. Helper Rate 
│ │ ├ 2a1. Step : 1.00000 
│ │ ├ 2a2. Min : 5000.00000 
│ │ ├ 2a3. Max : 5000.00000
```

```
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
│ │ └ └ 2a10. Treat As Boolean : false 
│ ├ 3c. Bump Stop Down 
│ │ ├ 3b1. Range 
│ │ │ ├ 2a1. Step : 1.00000
```

```
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
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3b. Bump Stop Up 
│ │ ├ 3b1. Range
```

```
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
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 3e. Helper Range
```

```
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
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0
```

```
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
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0
```

```
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
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0
```

```
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
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0
```

```
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
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None
```

```
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
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0
```

```
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
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0
```

```
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
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0
```

```
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
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ └ └ 2a10. Treat As Boolean : false
```

```
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
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false
```

```
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
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false
```

```
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
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 6i. Ers Deployment Map
```

```
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
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7a. Collar Positions 3
```

```
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
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false 
│ ├ 7e. Rear Wing Angle 
│ │ ├ 2a1. Step : 0.00000
```

```
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
│ ├ 8a. Fuel 
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

### <span id="page-153-0"></span>**Lamborghini Countach**

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
│ ├ 2b. Steer Ratio 
│ │ ├ 2a1. Step : 1.45000 
│ │ ├ 2a2. Min : -14.50000 
│ │ ├ 2a3. Max : -14.50000
```

```
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
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 2d3. Preload 
│ │ │ ├ 2a1. Step : 1.00000 
│ │ │ ├ 2a2. Min : 10.00000
```

```
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
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false 
│ │ ├ 3b2. Rate
```

```
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
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None 
│ │ │ ├ 2a9. Fractional Digits : 0 
│ │ │ └ 2a10. Treat As Boolean : false
```

```
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
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0 
│ │ └ 2a10. Treat As Boolean : false
```

```
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
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false 
│ │ │ ├ 2a8. Unit : None
```

```
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
│ │ │ ├ 2a4. Lut : None 
│ │ │ ├ 2a5. Is Modifiable : false 
│ │ │ ├ 2a6. Hide Value : false 
│ │ │ ├ 2a7. Is Negative : false
```

```
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
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false
```

```
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
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false
```

```
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
│ │ ├ 2a3. Max : 10000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false
```

```
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
│ │ ├ 2a3. Max : 2000.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false
```

```
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
│ │ ├ 2a3. Max : -1.80000 
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
│ │ ├ 2a3. Max : 0.20000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false
```

```
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
│ │ ├ 2a3. Max : 35.00000 
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false
```

```
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
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false
```

```
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
│ │ ├ 2a4. Lut : None
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false
```

```
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
│ │ ├ 2a4. Lut : None 
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false
```

```
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
│ │ ├ 2a5. Is Modifiable : true 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None
```

```
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
│ │ ├ 2a5. Is Modifiable : false 
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None
```

```
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
│ │ ├ 2a6. Hide Value : false 
│ │ ├ 2a7. Is Negative : false 
│ │ ├ 2a8. Unit : None 
│ │ ├ 2a9. Fractional Digits : 0
```

```
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
│ ├ 8a. Fuel 
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

# <span id="page-174-0"></span>**7. Car Setup Units [ .carsetupunits ]**

### <span id="page-174-1"></span>**A. Description**

UI label map for the garage: which display string sits next to each setup field (N/m, PSI, degrees, litres, or None).

This asset does **not** change physics. Car Setup holds values; Setup Limits hold min/max/step; Setup Units hold how those numbers are *named on screen*. Wrong units mislead telemetry and modding even when the sim maths stay correct.

### <span id="page-174-2"></span>**I. Role in the stack**

| Concern                              | Handled here   | Handled elsewhere                                     |
|--------------------------------------|----------------|-------------------------------------------------------|
| Display unit strings per setup field | .carsetupunits | —                                                     |
| Current numeric values               | —              | 5. Car Setup                                          |
| Legal range / step / lock flags      | —              | 6. Car Setup Limits (may also<br>carry a Unit string) |
| Real Sl physics inside assets        | —              | Coilover, tyre, wing, engine…                         |

Tree layout mirrors Setup / Limits (mechanical balance, suspensions, dampers, alignments, electronics, aero, fuel). Often shipped as a shared *common\_phsx* asset (*setup\_units*) reused across many cars.

### <span id="page-174-3"></span>**II. What you are really tuning**

1. **Readability profile**— Each leaf is a *string* (or None). Typical tokens :

| Field            | Role                                                              |
|------------------|-------------------------------------------------------------------|
| N/m, Ns/m, N, Nm | Force / rate / damper / preload style Sl                          |
| %                | Ratios (bias, torque multiplier)                                  |
| PSI              | Tyre pressure presentation                                        |
| °                | Angles (camber, toe, wing)                                        |
| m, mm            | Lenghts (bump-stop range vs ride height)                          |
| L                | Fuel volume                                                       |
| None             | No unit label (indices, ratios without a symbol,<br>unused fields |

Choosing *Ns/m* vs a click-style label (when used) is the difference between an engineering garage and a driver "count the clicks" garage.

2. **Consistency with Limits**— If Limits say a damper steps in clicks but Units still print *Ns/m*, the UI lies. Keep Units, Limits steps, and the magnitude of Setup values in the same authoring language for that car.

3. **None is intentional**— Electronics maps, compound index, steer ratio, and many diff locks often show None — they are indices or dimensionless selectors, not physical quantities with a unit glyph.

### <span id="page-175-0"></span>**III. Architecture**

### <span id="page-175-1"></span>**1 - MECHANICAL BALANCE (SCHEMA 1)**

*Unit strings for ARBs, steer ratio, brake bias / torque multiplier / ducts, diff power / coast / preload.*

### <span id="page-175-2"></span>**2 - SUSPENSIONS AND DAMPERS (SCHEMA 2-3)**

Per-corner (or multi-index) wheel rate, bump-stop range/rate, helpers; slow/fast bump and rebound. Schema reuses 2b1/2b2 under both bump-stop up and down — same pattern as Limits ID reuse.

### <span id="page-175-3"></span>**3 - ALIGNMENTS (SCHEMA 4)**

Pressure, camber, toe, caster, static camber, toe-out related field, compound. Schema name here is **Alignments** (Setup file often spells **Alignements**).

### <span id="page-175-4"></span>**4 - ELECTRONICS (SCHEMA 5)**

TC, ABS, ESC, EBB, engine map, telemetry laps, turbo boost level, ERS fields — almost always None in the shared example.

### <span id="page-175-5"></span>**5 - AERO, FUEL, COMPOUND MODE (SCHEMA 6-8)**

Collar positions, ride heights, wing angles (schema jumps *6c* to *6e*, no *6d*), fuel string, *Use Single Compound* label.

### <span id="page-175-6"></span>**IV. How to read the examples**

### <span id="page-175-7"></span>**1 - SHARED SETUP UNITS (COMMON\_PHSX)**

Single shared file, not per-car. Engineering-facing defaults:

• ARBs and wheel rates : *N/m*

• Dampers : *Ns/m* 

• Bump-stop range : *m*, rate : *N*

• Helpers : *N/m* and *m*

• Brake bias / torque multiplier : *%*

• Diff preload : *Nm* (power/coast None)

• Pressures : *PSI*; camber/toe/static/toe-out : °

• Collar positions: *m*; target height : *mm*; wings : °

• Fuel : *L*

• Electronics and many unused labels : *None*

That is the scientific profile: garage text matches SI-style authoring. A click-profile car would swap damper (and sometimes spring) strings toward dimensionless click labels while Limits steps match detent counts.

### <span id="page-176-0"></span>**V. Practical notes**

- Changing a Units string does not convert the stored Setup float it only changes the caption. To change system (PSI vs bar) you need consistent values, limits, and labels together.
- *None* means "no unit glyph," not "field missing."
- Schema quirks: missing aero *6d*; bump-stop down reuses *2b1/2b2*; fuel is **7a** here (Setup/Limits fuel lives under strategy **8a** — parallel trees, different numbering).
- Field name drift: Units may say *Toe Out Camber* while Setup says *Toe Out Linear* treat as the toerelated alignment label for that slot.
- Shared *common\_phsx* units are a baseline; car-specific overrides only appear if that car ships its own .carsetupunits.

### <span id="page-176-1"></span>**VI. Related assets**

- **5. Car Setup [\[.carsetup\]](#page-102-0)** values shown beside these labels
- **• 6. Car Setup Limits [\[.carsetuplimits\]](#page-118-0)** range/step; may duplicate Unit strings
- **• 3. Car Data [\[.car\]](#page-35-0)** wire which setup/limits/units package the car uses
- Telemetry / HUD consumers should agree with these strings for driver-facing consistency

### <span id="page-176-2"></span>**B. Schema**

```
├ 1. Mechanical Balance : object
│ ├ 1a. Arbs [x] : string | can have multiple Arbs
│ ├ 1b Steer Ratio : string
│ ├ 1c. Brakes : object
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
```

```
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

### <span id="page-177-0"></span>**C. Measurement Units & Descriptions**

| ID   | Name               | Unit of Measurement | Description                                                                                  |
|------|--------------------|---------------------|----------------------------------------------------------------------------------------------|
| 1.   | Mechanical Balance | None ( Object )     | Parent block defining UI unit<br>strings for chassis balance<br>parameters.                  |
| 1a.  | Arbs               | None ( String )     | Display unit label for anti-roll bar<br>stiffness; index 1 = front, 2 = rear<br>(e.g., N/m). |
| 1b.  | Steer Ratio        | None ( String )     | Display unit label for steering ratio<br>(e.g., ratio value or None if<br>dimensionless).    |
| 1c.  | Brakes             | None ( Object )     | Brake setup unit sub-block within<br>Mechanical Balance.                                     |
| 1c1. | Front Bias         | None ( String )     | Display unit label for brake<br>balance front percentage (e.g., %).                          |
| 1c2. | Torque Multiplier  | None ( String )     | Display unit label for global<br>braking torque multiplier (e.g., %).                        |

| ID   | Name           | Unit of Measurement                 | Description                                                                                |
|------|----------------|-------------------------------------|--------------------------------------------------------------------------------------------|
| 1c3. | Brake Ducts    | None ( String )                     | Display unit label for brake duct<br>opening level(s); multiple entries<br>for front/rear. |
| 1d.  | Differential   | None ( Object )                     | Differential setup unit sub-block<br>within Mechanical Balance.                            |
| 1d1. | Power          | None ( String )                     | Display unit label for on-throttle<br>differential lock (e.g., %, Nm, or<br>None).         |
| 1d2. | Coast          | None ( String )                     | Display unit label for coast<br>differential lock (e.g., %, Nm, or<br>None).               |
| 1d3. | Preload        | None ( String )                     | Display unit label for differential<br>preload torque (e.g., Nm).                          |
| 2.   | Suspensions    | None ( Object array, per<br>wheel ) | Per-corner suspension unit block;<br>indices 1–4 (or more) map to<br>wheel positions.      |
| 2a.  | Wheel Rate     | None ( String )                     | Display unit label for wheel-rate<br>spring stiffness (e.g., N/m, N/mm,<br>kg/mm, Hz).     |
| 2b.  | Bump Stop Up   | None ( Object )                     | Upper bump-stop unit sub-block<br>within each Suspensions entry.                           |
| 2b1. | Range          | None ( String )                     | Display unit label for upper bump<br>stop travel range under 2b Bump<br>Stop Up (e.g., m). |
| 2b2. | Rate           | None ( String )                     | Display unit label for upper bump<br>stop force rate under 2b Bump<br>Stop Up (e.g., N).   |
| 2c.  | Bump Stop Down | None ( Object )                     | Lower bump-stop unit sub-block;<br>child fields reuse IDs 2b1 and 2b2<br>per schema.       |
| 2d.  | Helper Rate    | None ( String )                     | Display unit label for helper/tender<br>spring stiffness (e.g., N/m).                      |
| 2e.  | Helper Range   | None ( String )                     | Display unit label for helper spring<br>travel range (e.g., m).                            |
| 3.   | Dampers        | None ( Object array, per<br>wheel ) | Per-corner damper unit block;<br>indices 1–4 (or more) map to<br>wheel positions.          |
| 3a.  | Slow Bump      | None ( String )                     | Display unit label for slow-speed<br>compression damping (e.g., Ns/m<br>or clicks).        |
| 3b.  | Fast Bump      | None ( String )                     | Display unit label for fast-speed<br>compression damping (e.g., Ns/m<br>or clicks).        |
| 3c.  | Slow Rebound   | None ( String )                     | Display unit label for slow-speed<br>rebound damping (e.g., Ns/m or<br>clicks).            |

| ID  | Name                        | Unit of Measurement                 | Description                                                                         |
|-----|-----------------------------|-------------------------------------|-------------------------------------------------------------------------------------|
| 3d. | Fast Rebound                | None ( String )                     | Display unit label for fast-speed<br>rebound damping (e.g., Ns/m or<br>clicks).     |
| 4.  | Alignments                  | None ( Object array, per<br>wheel ) | Per-corner alignment and tyre unit<br>block; indices 1–4 map to wheel<br>positions. |
| 4a. | Pressure                    | None ( String )                     | Display unit label for cold tyre<br>pressure (e.g., PSI, bar).                      |
| 4b. | Camber                      | None ( String )                     | Display unit label for camber angle<br>(e.g., °).                                   |
| 4c. | Toe                         | None ( String )                     | Display unit label for toe angle<br>(e.g., °).                                      |
| 4d. | Caster                      | None ( String )                     | Display unit label for caster angle<br>(e.g., ° or None).                           |
| 4e. | Static Camber               | None ( String )                     | Display unit label for computed/<br>static camber (e.g., °).                        |
| 4f. | Toe Out Camber              | None ( String )                     | Display unit label for toe-out<br>linear/camber curve coeffi<br>cient<br>(e.g., °). |
| 4g. | Compound                    | None ( String )                     | Display unit label for tyre<br>compound index (often None /<br>dimensionless).      |
| 5.  | Electronics                 | None ( Object )                     | Driver-aid and powertrain map unit<br>labels for garage UI.                         |
| 5a. | Tc1                         | None ( String )                     | Display unit label for primary<br>Traction Control map level.                       |
| 5b. | Tc2                         | None ( String )                     | Display unit label for secondary TC<br>map level.                                   |
| 5c. | Abs                         | None ( String )                     | Display unit label for ABS map<br>level.                                            |
| 5d. | Esc                         | None ( String )                     | Display unit label for ESP/stability<br>control map level.                          |
| 5e. | Ebb                         | None ( String )                     | Display unit label for Electronic<br>Brake Balance level.                           |
| 5f. | Engine Map                  | None ( String )                     | Display unit label for engine power<br>map index.                                   |
| 5g. | Telemetry Laps To<br>Record | None ( String )                     | Display unit label for telemetry lap<br>recording count.                            |
| 5h. | Turbo Boost Lv              | None ( String )                     | Display unit label for turbo boost<br>level (e.g., bar).                            |
| 5i. | Ers Deployment Map          | None ( String )                     | Display unit label for ERS<br>deployment map index.                                 |
| 5j. | Ers Recharge Lv             | None ( String )                     | Display unit label for ERS recharge<br>level.                                       |

| ID  | Name                | Unit of Measurement | Description                                                                                                 |
|-----|---------------------|---------------------|-------------------------------------------------------------------------------------------------------------|
| 5k. | Ers Heat Charging   | None ( String )     | Display unit label for MGU-H heat<br>charging level.                                                        |
| 6.  | Aero                | None ( Object )     | Aerodynamic setup unit block: ride<br>heights, collar positions, and wing<br>angles.                        |
| 6a. | Collar Positions    | None ( String )     | Display unit label for per-corner<br>spring collar position (e.g., m,<br>mm); indices 1–4 = LF, RF, LR, RR. |
| 6b. | Front Target Height | None ( String )     | Display unit label for front target<br>ride height (e.g., mm).                                              |
| 6c. | Rear Target Height  | None ( String )     | Display unit label for rear target<br>ride height (e.g., mm).                                               |
| 6e. | Front Wing Angle    | None ( String )     | Display unit label for front aero<br>device angle (e.g., °). Schema<br>skips 6d.                            |
| 6f. | Rear Wing Angle     | None ( String )     | Display unit label for rear wing<br>angle (e.g., °).                                                        |
| 7.  | Fuel Strategy       | None ( Object )     | Fuel load planning unit block.                                                                              |
| 7a. | Fuel                | None ( String )     | Display unit label for fuel load<br>volume (e.g., L).                                                       |
| 8.  | Use Single Compound | None ( String )     | Display unit label for the single<br>compound toggle (often None /<br>boolean).                             |

### <span id="page-180-0"></span>**D. Example data**

### <span id="page-180-1"></span>**I. Chosen Car Engine for Example**

- Setup Units ( slug : setup\_units ) [ common\_phsx ]

### <span id="page-180-2"></span>**II. Example**

### <span id="page-180-3"></span>**Setup Units**

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
```

```
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
```

```
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
```

```
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
│ └ 6f. Rear Wing Angle : ° 
├ 7. Fuel Strategy 
│ └ 7a. Fuel : L 
└ 8. Use Single Compound : None
```

# <span id="page-184-0"></span>**8. Car Tuning Parts [ .tuningpart ]**

### <span id="page-184-1"></span>**A. Description**

Modular switchboard for vehicle variants: each part picks a physics domain and either redirects asset paths or embeds override data (engine tune maths, aero package, full performance-mode setups).

Baseline Car Data still defines the stock car. Activating a tuning part hot-swaps or overlays pieces of that stack — drift drivetrain, alternate gearbox, "No ABS / No TC" limits — without duplicating the whole vehicle folder.

### <span id="page-184-2"></span>**I. Role in the stack**

| Concern                               | Handled here               | Handled elsewhere                  |
|---------------------------------------|----------------------------|------------------------------------|
| Which domain this part overrides      | Physics Tuning enum        | —                                  |
| Path redirects to alternate assets    | [physics_tuning] object    | Target .carengine, .drivetrain, …  |
| Engine multiplier / waveform tune     | Engine Tube fields         | Base curve still in .carengine     |
| Embedded aero package / wing<br>index | Aero Package / Wing fields | .wing, .surface3d                  |
| Embedded garage packages              | Performance Modes block    | Also exist as standalone .carsetup |
| UI category label                     | Car Part Type              | Showroom / upgrade menus           |
| Stock wiring of the car               | —                          | 3. Car Data                        |

One car can ship many .tuningpart files (Supra drift set, Datsun upgrade catalogue, Cup electronics packs). Selection is combinatorial: engine part + gearbox part + setup limits part, etc.

### <span id="page-184-3"></span>**II. What you are really tuning**

1. **Domain selector** — *Physics Tuning* chooses the override family: Engine, Engine Tune, Gearbox, Drivetrain, Clutch, Brakes / Brake System, Electronics, Suspensions, Suspensions Geometry, Wing, Aero Package, Setup, Setup Limits, Performance Modes Tuning, or None.

The object under field **2** is keyed by that choice — Engine parts expose an Engine path block; Setup Limits parts expose a Setup Limits path block. Wrong enum + wrong nested keys = part that does nothing.

- 2. **Path redirects** Most mechanical parts are thin wrappers: Path (or front/rear coilover / geometry paths) pointing at an alternate asset. Examples: Supra drift .carengine / .drivetrain / .gearbox / .carsetup / .carsetuplimits; Datsun 5-speed gearbox, L28 engine, LSD drivetrain, G-nose coilovers.
- 3. **Engine Tune scalars** When tuning type is Engine Tune (not a full Engine path swap): multiplier, add, and cosine amplitude / period / phase reshape the existing power delivery without replacing the whole .carengine file.
- 4. **Brakes and suspension packages** Brake System / Brakes paths (front/rear compounds), coilover front/rear, suspension geometry front/rear. Lets a single menu item restyle the undercarriage or calipers.

- 5. **Aero and performance modes** Wing index override; full Aero Package Data (downforce elements, surface3d paths, controllers). Performance Modes Tuning can embed named modes with electronics, brakes, dampers, diffs, lock controllers, AWD clutches, turbo settings — a setup package living inside the tuning part.
- 6. **Electronics restrictors** *Physics Tuning : None* plus *Car Part Type : Mechanics\_Electronics* (Porsche Cup "No ABS No TC" / "Only ABS") tags an electronics policy. Companion parts often retarget **Setup Limits** so the garage cannot re-enable stripped aids.

### <span id="page-185-0"></span>**III. Architecture**

### <span id="page-185-1"></span>**1 - HEADER (SCHEMA 1 AND 3)**

*Physics Tuning* enum; *Car Part Type* enum/string for UI taxonomy (*Mechanics\_Engine*, *Mechanics\_Drivetrain*, *Mechanics\_Electronics*, exterior categories, or None for pure setup/limits packs).

### <span id="page-185-2"></span>**2 - CONDITIONAL PAYLOAD (SCHEMA 2)**

*[physics\_tuning]* object whose fields depend on enum 1:

| Family                   | Typical contents                                                                     |
|--------------------------|--------------------------------------------------------------------------------------|
| Path-baed modules        | Engine / Gearbox / Drivetrain / Clutch / Brake<br>System / Setup / Setup Limits Path |
| Engine Tune              | Multiplier, Add, Cos Ampl / Period / Phase                                           |
| Brakes                   | Front / Rear compound paths                                                          |
| Suspensions              | Coilover front/rear paths                                                            |
| Suspensions Geometry     | Geometry path front/rear                                                             |
| Wing                     | Wing index override                                                                  |
| Aero Package             | Slip/speed multi, downforces array, lift/drag maps,<br>wings paths                   |
| Performance Modes Tuning | Named modes with nested electronics / chassis /<br>driveline / turbo settings        |

### <span id="page-185-3"></span>**3 - NESTED CONTROLLERS**

Inside aero downforces and performance-mode diffs/locks, the familiar stage pipeline reappears (Input, Combinator, Lut, Filter, limits) — same pattern as brake EBB / turbo controllers.

### <span id="page-185-4"></span>**IV. How to read the examples**

### <span id="page-185-5"></span>**1 - TOYOTA SUPRA MK IV (DRIFT PACKAGE SET)**

Seven parts that rebuild the car for drift: suspensions geometry, drivetrain, engine, coilovers, gearbox, setup, setup limits — each with Physics Tuning matching the domain and a path into *…\_drift…* assets. Shows the "variant pack" pattern: many small redirects, one coherent alternate identity.

### <span id="page-186-0"></span>**2 - DATSUN 240Z FAIRLADY (CATALOGUE UPGRADES)**

Eight parts as optional upgrades: 5-speed gearbox, brake system, clutch, G-nose coilovers, matching setup + limits, L28 engine, LSD drivetrain. Classic aftermarket tree — pick gearbox and LSD independently of engine.

### <span id="page-186-1"></span>**3 - PORSCHE 992 GT3 CUP (ELECTRONICS / BOP STYLE)**

"No ABS No TC" and "Only ABS" use *Physics Tuning : None* with *Mechanics\_Electronics*. Paired Setup Limits parts force garage rules for those electronics states. Regulation by menu item + limits file, not by rewriting Car Electronics maps in place.

### <span id="page-186-2"></span>**V. Practical notes**

- Always read **field 1 first**: it tells you which subtree under field 2 is meaningful.
- A path redirect must point at a real asset of the right type; a gearbox part pointing at a .brakesystem (OCR noise in some dumps) is a content bug.
- Setup / Setup Limits parts often set *Car Part Type : None* they are garage packages, not showroom body parts.
- Electronics "None" tuning still needs companion limits if you want the UI locked to the intended aid set.
- Performance Modes inside a tuning part can duplicate what Car Data performance modes already do check which layer actually loads in-session.
- Schema typos to expect: Front Brias, Brakes rear path typed oddly in the tree dump; enum table OCR wrapping around Physics Tuning values.

### <span id="page-186-3"></span>**VI. Related assets**

- **4. Car Data [\[.car\]](#page-35-0)** baseline paths that parts override
- **• 4 / 13 / 14 / 10 / 1. [Engine](#page-87-0) / [Drivetrain](#page-245-0) / [Gearbox](#page-261-0) / [Clutch](#page-221-0) / Brake [System](#page-16-0)** —common redirect targets
- **• 5 / 6. Car [Setup](#page-102-0) / Setup [Limits](#page-118-0)** drift and Cup companion packs
- **11 / 17 / 20. [Coilover](#page-226-0) / [Suspension](#page-286-0) / [Wing](#page-328-0)** suspension and aero redirects
- **9. Car [Electronics](#page-205-0)** maps still live here; tuning parts often only gate them via limits / None tags

### <span id="page-186-4"></span>**B. Schema**

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
```

```
│ ├ 2f. (Engine Tune) Cos Phase : float
│ ├ 2g. (Brakes) Front Path : string - path
│ ├ 2h. (Brakes) Rear Path : float
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
│ │ │ ├ 2o3a. Front Bias : float
│ │ │ ├ 2o3b. Torque Multiplier : float
│ │ │ └ 2o3c. Brake Ducts [x] : float | can have multiple Brake Ducts
```

```
│ │ ├ 2o4. Damper Settings [x] : object | can have multiple Damper 
Settings
│ │ │ ├ 2o4a. Slow Bump : float
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
```

```
│ │ │ ├ 2o6c7. Torque Bias Ratio Coast : float
│ │ │ ├ 2o6c8. Thermal Capacity : float
│ │ │ ├ 2o6c9. Surface : float
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
```

```
│ │ │ └ 2o11b. Stages [x] : object
│ │ │ ├ 2o11b1. Input Var : enum
│ │ │ ├ 2o11b2. Combinator Mode : enum
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

### **Enum - Car Tuning Pars**

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

### <span id="page-192-0"></span>**C. Measurement Units & Descriptions**

| ID  | Name                | Unit of Measurement               | Description                                                                                                                                                                                    |
|-----|---------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Physics Tuning      | None ( Enum )                     | Primary enum selector declaring<br>which mechanical domain this<br>tuning part overrides (Engine,<br>Gearbox, Drivetrain, Setup Limits,<br>Aero Package, Performance<br>Modes Tuning, etc.).   |
| 2.  | [physics_tuning]    | None ( Object )                   | Dynamic object whose JSON key<br>equals the Physics Tuning enum<br>value; only the branch matching<br>field 1 is populated at runtime.                                                         |
| 2a. | Path                | None ( File path )                | File path redirect for component<br>swap tuning parts; active when<br>Physics Tuning is Engine,<br>Gearbox, Drivetrain, Clutch, Brake<br>System, Electronics, Wing, Setup,<br>or Setup Limits. |
| 2b. | Multiplier          | Dimensionless float               | Engine tune torque multiplier<br>scalar applied on top of the base<br>power curve when Physics Tuning<br>is Engine Tune.                                                                       |
| 2c. | Add                 | Nm ( Newton-meters )              | Flat torque offset added to the<br>engine output curve when Physics<br>Tuning is Engine Tune.                                                                                                  |
| 2d. | Cos Ampl            | Dimensionless coeffi<br>cient     | Cosine-wave torque modulation<br>amplitude for periodic engine tune<br>effects (Engine Tune mode).                                                                                             |
| 2e. | Cos Period          | s ( Seconds ) or rad              | Period of the cosine torque<br>modulation in Engine Tune mode.                                                                                                                                 |
| 2f. | Cos Phase           | rad ( Radians ) or deg            | Phase offset of the cosine torque<br>modulation in Engine Tune mode.                                                                                                                           |
| 2g. | Front Path          | None ( File path )                | Path to an alternative front brake<br>asset (.brakes or related) when<br>Physics Tuning is Brakes.                                                                                             |
| 2h. | Rear Path           | Depends on parameter<br>( float ) | Path or scalar reference for rear<br>brake configuration when Physics<br>Tuning is Brakes (schema types as<br>float; verify against asset).                                                    |
| 2i. | Coilover Path Front | None ( File path )                | Path to a replacement<br>front .coilover asset when Physics<br>Tuning is Suspensions.                                                                                                          |
| 2j. | Coilover Path Rear  | None ( File path )                | Path to a replacement<br>rear .coilover asset when Physics<br>Tuning is Suspensions.                                                                                                           |
| 2k. | Geometry Path Front | None ( File path )                | Path to a replacement<br>front .suspension geometry asset<br>when Physics Tuning is<br>Suspensions Geometry.                                                                                   |

| ID     | Name                         | Unit of Measurement           | Description                                                                                                                      |
|--------|------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 2l.    | Geometry Path Rear           | None ( File path )            | Path to a replacement<br>rear .suspension geometry asset<br>when Physics Tuning is<br>Suspensions Geometry.                      |
| 2m.    | Wing Index Override          | None ( Integer )              | Integer index selecting which wing<br>aero profile slot to override when<br>Physics Tuning is Wing.                              |
| 2n.    | Data                         | None ( Object )               | Root aero package data block<br>when Physics Tuning is Aero<br>Package; contains downforce<br>modifiers and wing path overrides. |
| 2n1.   | Slip Gain Mult               | Dimensionless multiplier      | Global multiplier applied to tyre<br>slip-driven aero gain within the<br>aero package.                                           |
| 2n2.   | Speed Factor Mult            | Dimensionless multiplier      | Multiplier scaling speed<br>dependent aero factor curves in<br>the package.                                                      |
| 2n3.   | Downforces [x]               | None ( Object array )         | Per-element downforce modifier<br>block; multiple entries for distinct<br>aero surfaces or zones.                                |
| 2n3a.  | Position                     | m ( Meters, X / Y / Z )       | 3D position offset (X/Y/Z) of this<br>downforce element relative to the<br>vehicle reference frame.                              |
| 2n3b.  | Cl Gain                      | Dimensionless coeffi<br>cient | Lift coeffi<br>cient (CL) gain multiplier<br>for this downforce element.                                                         |
| 2n3c.  | Cd Gain                      | Dimensionless coeffi<br>cient | Drag coeffi<br>cient (CD) gain<br>multiplier for this downforce<br>element.                                                      |
| 2n3d.  | Yaw Gain                     | Dimensionless coeffi<br>cient | Yaw-angle sensitivity gain for this<br>downforce element.                                                                        |
| 2n3e.  | Drag Per Cool Transfer       | Coeffi<br>cient               | Drag penalty per unit of cooling<br>airflow transfer through this<br>element.                                                    |
| 2n3f.  | Damage C L [x]               | Dimensionless coeffi<br>cient | Array of lift-damage coeffi<br>cients<br>reducing CL under aerodynamic<br>damage states.                                         |
| 2n3g.  | Damage C D [x]               | Dimensionless coeffi<br>cient | Array of drag-damage coeffi<br>cients<br>reducing CD effi<br>ciency under<br>damage.                                             |
| 2n3h.  | Downforce Controllers<br>[x] | None ( Object array )         | Dynamic downforce controller<br>block; multiple controllers can<br>combine inputs (brake, steer,<br>speed, etc.).                |
| 2n3h1. | Combinator Mode              | None ( Enum )                 | Enum selecting how this controller<br>combines with others (AddH,<br>MultH, AddClGain, MultClGain,<br>etc.).                     |

| ID     | Name                     | Unit of Measurement                         | Description                                                                                                                |
|--------|--------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| 2n3h2. | Input                    | None ( Enum )                               | Input signal source for the<br>controller (Brake, Gas, Yaw, LatG,<br>Speed, SusTravelLR, etc.).                            |
| 2n3h3. | Filter                   | Coeffi<br>cient ( Smoothing<br>multiplier ) | Low-pass filter time constant<br>smoothing the controller input<br>signal.                                                 |
| 2n3h4. | Up Limit                 | Depends on input variable                   | Upper clamp limit for controller<br>output contribution.                                                                   |
| 2n3h5. | Down Limit               | Depends on input variable                   | Lower clamp limit for controller<br>output contribution.                                                                   |
| 2n3h6. | Lut                      | None ( .curve file path )                   | Optional .curve LUT mapping<br>filtered input to aero output<br>modifier.                                                  |
| 2n3i.  | Lift Per Front Angle     | Coeffi<br>cient per deg                     | Lift sensitivity per degree of front<br>wing angle for this package.                                                       |
| 2n3j.  | Lift Per Rear Angle      | Coeffi<br>cient per deg                     | Lift sensitivity per degree of rear<br>wing angle.                                                                         |
| 2n3k.  | Drag Per Front Angle     | Coeffi<br>cient per deg                     | Drag sensitivity per degree of front<br>wing angle.                                                                        |
| 2n3l.  | Drag Per Rear Angle      | Coeffi<br>cient per deg                     | Drag sensitivity per degree of rear<br>wing angle.                                                                         |
| 2n3m.  | Default Front Angle      | deg ( Degrees )                             | Default front wing angle reference<br>used when no setup override is<br>active.                                            |
| 2n3n.  | Default Rear Angle       | deg ( Degrees )                             | Default rear wing angle reference<br>used when no setup override is<br>active.                                             |
| 2n4.   | Front Lift               | None ( File path )                          | Path to front lift aero curve/asset<br>override within the aero package.                                                   |
| 2n5.   | Rear Lift                | None ( File path )                          | Path to rear lift aero curve/asset<br>override within the aero package.                                                    |
| 2n6.   | Drag                     | None ( File path )                          | Path to drag aero curve/asset<br>override within the aero package.                                                         |
| 2n7.   | Wings Path [x]           | None ( File path )                          | Path(s) to alternative wing<br>definition assets; multiple entries<br>for multi-element wings.                             |
| 2o.    | Performance Modes [x]    | None ( Object array )                       | Performance mode preset block<br>when Physics Tuning is<br>Performance Modes Tuning;<br>multiple modes (Wet, Quali, etc.). |
| 2o1.   | Performance Mode<br>Name | None ( String )                             | Display name string for this<br>performance mode shown in UI<br>selection menus.                                           |
| 2o2.   | Electronics Settings     | None ( Object )                             | Electronics preset sub-block<br>bundled into this performance<br>mode.                                                     |

| ID    | Name                        | Unit of Measurement        | Description                                                                                |
|-------|-----------------------------|----------------------------|--------------------------------------------------------------------------------------------|
| 2o2a. | Tc1                         | None ( Map index / level ) | Traction Control map level preset<br>for this performance mode.                            |
| 2o2b. | Tc2                         | None ( Map index / level ) | Secondary TC map level preset.                                                             |
| 2o2c. | Abs                         | None ( Map index / level ) | ABS map level preset.                                                                      |
| 2o2d. | Esc                         | None ( Map index / level ) | ESC/ESP map level preset.                                                                  |
| 2o2e. | Ebb                         | None ( Map index / level ) | Electronic Brake Balance level<br>preset.                                                  |
| 2o2f. | Engine Map                  | None ( Map index )         | Engine power map index preset.                                                             |
| 2o2g. | Telemetry Laps To<br>Record | None ( Integer )           | Telemetry lap recording count<br>preset.                                                   |
| 2o2h. | Turbo Boost Lv              | bar or level index         | Turbo boost level preset.                                                                  |
| 2o2i. | Ers Deployment Map          | None ( Map index )         | ERS deployment map preset.                                                                 |
| 2o2j. | Ers Recharge Lv             | None ( Level index )       | ERS recharge level preset.                                                                 |
| 2o2k. | Ers Heat Charging           | None ( Level index )       | MGU-H heat charging level preset.                                                          |
| 2o3.  | Brake Settings              | None ( Object )            | Brake setup preset sub-block for<br>this performance mode.                                 |
| 2o3a. | Front Bias                  | Ratio ( 0.0 - 1.0 )        | Brake balance front percentage<br>preset                                                   |
| 2o3b. | Torque Multiplier           | Dimensionless multiplier   | Global braking torque multiplier<br>preset.                                                |
| 2o3c. | Brake Ducts [x]             | Ratio ( 0.0 - 1.0 )        | Brake duct opening level preset(s);<br>multiple entries for front/rear<br>ducts.           |
| 2o4.  | Damper Settings [x]         | None ( Object array )      | Per-corner damper preset block;<br>indices map to wheel positions.                         |
| 2o4a. | Slow Bump                   | Clicks or N·s/m            | Slow-speed compression damping<br>preset for this corner.                                  |
| 2o4b. | Fast Bump                   | Clicks or N·s/m            | Fast-speed compression damping<br>preset.                                                  |
| 2o4c. | Slow Rebound                | Clicks or N·s/m            | Slow-speed rebound damping<br>preset.                                                      |
| 2o4d. | Fast Rebound                | Clicks or N·s/m            | Fast-speed rebound damping<br>preset.                                                      |
| 2o5.  | Differential Data           | None ( Object )            | Single differential override block<br>within a performance mode.                           |
| 2o5a. | Type                        | None ( Enum )              | Differential type enum (LSD,<br>Spool, Torsen, EpicyclicTorsen,<br>TorqueVectoring, etc.). |
| 2o5b. | Power                       | Nm or ratio                | On-throttle differential lock<br>intensity preset.                                         |

| ID     | Name                         | Unit of Measurement           | Description                                                                |
|--------|------------------------------|-------------------------------|----------------------------------------------------------------------------|
| 2o5c.  | Coast                        | Nm or ratio                   | Coast/off-throttle differential lock<br>intensity preset.                  |
| 2o5d.  | Preload                      | Nm ( Newton-meters )          | Static differential preload torque<br>preset.                              |
| 2o5e.  | Front Share                  | Ratio ( 0.0 - 1.0 )           | Front torque share fraction for<br>torque-vectoring or active diffs.       |
| 2o5f.  | Torque Bias Ratio<br>Power   | Ratio ( e.g., 2.0:1 )         | Torque bias ratio under power.                                             |
| 2o5g.  | Torque Bias Ratio<br>Coast   | Ratio                         | Torque bias ratio on coast                                                 |
| 2o5h.  | Thermal Capacity             | J/K or J/°C                   | Thermal mass of differential<br>friction surfaces for heat model.          |
| 2o5i.  | Surface                      | m² ( Square meters )          | Effective friction surface area for<br>differential heat generation.       |
| 2o5j.  | Heat Transfer Coef           | W/(m²·K) ( Coeffi<br>cient )  | Heat transfer coeffi<br>cient to<br>ambient/oil for differential cooling.  |
| 2o5k.  | Wear Factor                  | Dimensionless coeffi<br>cient | Wear accumulation rate factor for<br>differential friction surfaces.       |
| 2o5l.  | Friction Reduction With<br>T | Ratio/°C                      | Friction reduction factor as a<br>function of differential<br>temperature. |
| 2o5m.  | Friction Ref T               | °C ( Degrees Celsius )        | Reference temperature for friction<br>reduction curve.                     |
| 2o6.   | Four W D Differentials       | None ( Object )               | AWD/4WD triple-differential preset<br>container (front, center, rear).     |
| 2o6a.  | Front Dif                    | None ( Object )               | Front axle differential preset sub<br>block.                               |
| 2o6a1. | Type                         | None ( Enum )                 | Differential type enum for the front<br>diff.                              |
| 2o6a2. | Power                        | Nm or ratio                   | On-throttle lock intensity for the<br>front diff.                          |
| 2o6a3. | Coast                        | Nm or ratio                   | Coast lock intensity for the front<br>diff.                                |
| 2o6a4. | Preload                      | Nm ( Newton-meters )          | Preload torque for the front diff.                                         |
| 2o6a5. | Front Share                  | Ratio ( 0.0 - 1.0 )           | Front torque share for the front<br>diff.                                  |
| 2o6a6. | Torque Bias Ratio<br>Power   | Ratio ( e.g., 2.0:1 )         | Power torque bias ratio for the<br>front diff.                             |
| 2o6a7. | Torque Bias Ratio<br>Coast   | Ratio                         | Coast torque bias ratio for the<br>front diff.                             |
| 2o6a8. | Thermal Capacity             | J/K or J/°C                   | Thermal capacity of the front diff<br>friction pack.                       |

| ID      | Name                         | Unit of Measurement           | Description                                                      |
|---------|------------------------------|-------------------------------|------------------------------------------------------------------|
| 2o6a9.  | Surface                      | m² ( Square meters )          | Friction surface area for the front<br>diff.                     |
| 2o6a10. | Heat Transfer Coef           | W/(m²·K) ( Coeffi<br>cient )  | Heat transfer coeffi<br>cient for the<br>front diff.             |
| 2o6a11. | Wear Factor                  | Dimensionless coeffi<br>cient | Wear rate factor for the front diff.                             |
| 2o6a12. | Friction Reduction With<br>T | Ratio/°C                      | Temperature-dependent friction<br>reduction for the front diff.  |
| 2o6a13. | Friction Ref T               | °C ( Degrees Celsius )        | Reference temperature for front<br>diff friction model.          |
| 2o6b.   | Center Dif                   | None ( Object )               | Center differential preset sub<br>block.                         |
| 2o6b1.  | Type                         | None ( Enum )                 | Differential type enum for the<br>center diff.                   |
| 2o6b2.  | Power                        | Nm or ratio                   | On-throttle lock intensity for the<br>center diff.               |
| 2o6b3.  | Coast                        | Nm or ratio                   | Coast lock intensity for the center<br>diff.                     |
| 2o6b4.  | Preload                      | Nm ( Newton-meters )          | Preload torque for the center diff.                              |
| 2o6b5.  | Front Share                  | Ratio ( 0.0 - 1.0 )           | Front torque share for the center<br>diff.                       |
| 2o6b6.  | Torque Bias Ratio<br>Power   | Ratio ( e.g., 2.0:1 )         | Power torque bias ratio for the<br>center diff.                  |
| 2o6b7.  | Torque Bias Ratio<br>Coast   | Ratio                         | Coast torque bias ratio for the<br>center diff.                  |
| 2o6b8.  | Thermal Capacity             | J/K or J/°C                   | Thermal capacity of the center diff<br>friction pack.            |
| 2o6b9.  | Surface                      | m² ( Square meters )          | Friction surface area for the center<br>diff.                    |
| 2o6b10. | Heat Transfer Coef           | W/(m²·K) ( Coeffi<br>cient )  | Heat transfer coeffi<br>cient for the<br>center diff.            |
| 2o6b11. | Wear Factor                  | Dimensionless coeffi<br>cient | Wear rate factor for the center diff.                            |
| 2o6b12. | Friction Reduction With<br>T | Ratio/°C                      | Temperature-dependent friction<br>reduction for the center diff. |
| 2o6b13. | Friction Ref T               | °C ( Degrees Celsius )        | Reference temperature for center<br>diff friction model.         |
| 2o6c.   | Rear Dif                     | None ( Object )               | Rear axle differential preset sub<br>block.                      |
| 2o6c1.  | Type                         | None ( Enum )                 | Differential type enum for the rear<br>diff.                     |
| 2o6c2.  | Power                        | Nm or ratio                   | On-throttle lock intensity for the<br>rear diff.                 |

| ID      | Name                         | Unit of Measurement                         | Description                                                                                    |
|---------|------------------------------|---------------------------------------------|------------------------------------------------------------------------------------------------|
| 2o6c3.  | Coast                        | Nm or ratio                                 | Coast lock intensity for the rear<br>diff.                                                     |
| 2o6c4.  | Preload                      | Nm ( Newton-meters )                        | Preload torque for the rear diff.                                                              |
| 2o6c5.  | Front Share                  | Ratio ( 0.0 - 1.0 )                         | Front torque share for the rear diff.                                                          |
| 2o6c6.  | Torque Bias Ratio<br>Power   | Ratio ( e.g., 2.0:1 )                       | Power torque bias ratio for the rear<br>diff.                                                  |
| 2o6c7.  | Torque Bias Ratio<br>Coast   | Ratio                                       | Coast torque bias ratio for the rear<br>diff.                                                  |
| 2o6c8.  | Thermal Capacity             | J/K or J/°C                                 | Thermal capacity of the rear diff<br>friction pack.                                            |
| 2o6c9.  | Surface                      | m² ( Square meters )                        | Friction surface area for the rear<br>diff.                                                    |
| 2o6c10. | Heat Transfer Coef           | W/(m²·K) ( Coeffi<br>cient )                | Heat transfer coeffi<br>cient for the<br>rear diff.                                            |
| 2o6c11. | Wear Factor                  | Dimensionless coeffi<br>cient               | Wear rate factor for the rear diff.                                                            |
| 2o6c12. | Friction Reduction With<br>T | Ratio/°C                                    | Temperature-dependent friction<br>reduction for the rear diff.                                 |
| 2o6c13. | Friction Ref T               | °C ( Degrees Celsius )                      | Reference temperature for rear diff<br>friction model.                                         |
| 2o7.    | Front Lock Controllers       | None ( Object )                             | Front axle lock controller definition<br>for active/vectoring diffs.                           |
| 2o7a.   | Name                         | None ( String )                             | Display/debug name for the front<br>lock controller.                                           |
| 2o7b.   | Stages [x]                   | None ( Object array )                       | Multi-stage controller pipeline;<br>each stage processes an input<br>through a LUT and limits. |
| 2o7b1.  | Input Var                    | None ( Telemetry enum )                     | Input variable enum for this stage<br>(SlipRatio, Steer, LatG,<br>ErsChargeLevel, etc.).       |
| 2o7b2.  | Combinator Mode              | None ( Math enum : Add /<br>Mult )          | Combinator mode for merging<br>stage output (Add or Mult).                                     |
| 2o7b3.  | Lut                          | None ( .curve file path )                   | Look-up table (.curve) mapping<br>filtered input to lock fraction.                             |
| 2o7b4.  | Filter Gain                  | Coeffi<br>cient ( Smoothing<br>multiplier ) | Filter gain smoothing the stage<br>input signal.                                               |
| 2o7b5.  | Up Limit                     | Depends on input variable                   | Upper output limit for this stage.                                                             |
| 2o7b6.  | Down Limit                   | Depends on input variable                   | Lower output limit for this stage.                                                             |
| 2o7b7.  | Current Value                | Depends on input variable                   | Runtime current value output of<br>this stage (telemetry/state).                               |
| 2o7b8.  | Const Value                  | Depends on input variable                   | Constant fallback input value<br>when Input Var is Const.                                      |

| ID     | Name                    | Unit of Measurement                         | Description                                              |
|--------|-------------------------|---------------------------------------------|----------------------------------------------------------|
| 2o8.   | Center Lock Controllers | None ( Object )                             | Center differential lock controller<br>definition.       |
| 2o8a.  | Name                    | None ( String )                             | Display/debug name for the center<br>lock controller.    |
| 2o8b.  | Stages [x]              | None ( Object array )                       | Multi-stage controller pipeline for<br>center diff lock. |
| 2o8b1. | Input Var               | None ( Telemetry enum )                     | Input variable enum for center lock<br>stage.            |
| 2o8b2. | Combinator Mode         | None ( Math enum : Add /<br>Mult )          | Combinator mode (Add/Mult) for<br>center lock stage.     |
| 2o8b3. | Lut                     | None ( .curve file path )                   | LUT path for center lock stage.                          |
| 2o8b4. | Filter Gain             | Coeffi<br>cient ( Smoothing<br>multiplier ) | Filter gain for center lock stage<br>input.              |
| 2o8b5. | Up Limit                | Depends on input variable                   | Upper output limit for center lock<br>stage.             |
| 2o8b6. | Down Limit              | Depends on input variable                   | Lower output limit for center lock<br>stage.             |
| 2o8b7. | Current Value           | Depends on input variable                   | Current runtime value for center<br>lock stage.          |
| 2o8b8. | Const Value             | Depends on input variable                   | Constant input value for center<br>lock stage.           |
| 2o9.   | Rear Lock Controllers   | None ( Object )                             | Rear axle lock controller definition.                    |
| 2o9a.  | Name                    | None ( String )                             | Display/debug name for the rear<br>lock controller.      |
| 2o9b.  | Stages [x]              | None ( Object array )                       | Multi-stage controller pipeline for<br>rear diff lock.   |
| 2o9b1. | Input Var               | None ( Telemetry enum )                     | Input variable enum for rear lock<br>stage.              |
| 2o9b2. | Combinator Mode         | None ( Math enum : Add /<br>Mult )          | Combinator mode for rear lock<br>stage.                  |
| 2o9b3. | Lut                     | None ( .curve file path )                   | LUT path for rear lock stage.                            |
| 2o9b4. | Filter Gain             | Coeffi<br>cient ( Smoothing<br>multiplier ) | Filter gain for rear lock stage.                         |
| 2o9b5. | Up Limit                | Depends on input variable                   | Upper output limit for rear lock<br>stage.               |
| 2o9b6. | Down Limit              | Depends on input variable                   | Lower output limit for rear lock<br>stage.               |
| 2o9b7. | Current Value           | Depends on input variable                   | Current runtime value for rear lock<br>stage.            |
| 2o9b8. | Const Value             | Depends on input variable                   | Constant input value for rear lock<br>stage.             |

| ID       | Name                  | Unit of Measurement                         | Description                                                                       |
|----------|-----------------------|---------------------------------------------|-----------------------------------------------------------------------------------|
| 2o10     | Awd Clutches [x]      | None ( Object array )                       | AWD clutch pack definition;<br>multiple clutches for front/rear axle<br>coupling. |
| 2o10a.   | Position              | None ( Integer )                            | Integer position/index of this<br>clutch in the AWD coupling matrix.              |
| 2o10b.   | Preload               | Nm ( Newton-meters )                        | Static preload torque on this AWD<br>clutch pack.                                 |
| 2o10c.   | Controllers           | None ( Object )                             | Nested lock controller for this<br>AWD clutch.                                    |
| 2o10c1.  | Name                  | None ( String )                             | Display name for the AWD clutch<br>controller.                                    |
| 2o10c2.  | Stages [x]            | None ( Object array )                       | Multi-stage pipeline controlling<br>AWD clutch lock.                              |
| 2o10c2a. | Input Var             | None ( Telemetry enum )                     | Input variable enum for AWD<br>clutch stage.                                      |
| 2o10c2b. | Combinator Mode       | None ( Math enum : Add /<br>Mult )          | Combinator mode for AWD clutch<br>stage.                                          |
| 2o10c2c. | Lut                   | None ( .curve file path )                   | LUT path for AWD clutch stage.                                                    |
| 2o10c2d. | Filter Gain           | Coeffi<br>cient ( Smoothing<br>multiplier ) | Filter gain for AWD clutch stage.                                                 |
| 2o10c2e. | Up Limit              | Depends on input variable                   | Upper output limit for AWD clutch<br>stage.                                       |
| 2o10c2f. | Down Limit            | Depends on input variable                   | Lower output limit for AWD clutch<br>stage.                                       |
| 2o10c2g. | Current Value         | Depends on input variable                   | Current runtime value for AWD<br>clutch stage.                                    |
| 2o10c2h. | Const Value           | Depends on input variable                   | Constant input for AWD clutch<br>stage.                                           |
| 2o11     | Turbo Controllers [x] | None ( Object array )                       | Turbo boost controller block within<br>performance mode tuning.                   |
| 2o11a.   | Name                  | None ( String )                             | Display name for turbo controller.                                                |
| 2o11b.   | Stages [x]            | None ( Object array )                       | Multi-stage turbo boost control<br>pipeline.                                      |
| 2o11b1.  | Input Var             | None ( Telemetry enum )                     | Input variable enum for turbo<br>stage.                                           |
| 2o11b2.  | Combinator Mode       | None ( Math enum : Add /<br>Mult )          | Combinator mode for turbo stage.                                                  |
| 2o11b3.  | Lut                   | None ( .curve file path )                   | LUT path mapping input to boost<br>modifier.                                      |
| 2o11b4.  | Filter Gain           | Coeffi<br>cient ( Smoothing<br>multiplier ) | Filter gain for turbo stage input.                                                |
| 2o11b5.  | Up Limit              | Depends on input variable                   | Upper boost limit for this stage.                                                 |

| ID      | Name           | Unit of Measurement       | Description                                                                                                                                                            |
|---------|----------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2o11b6. | Down Limit     | Depends on input variable | Lower boost limit for this stage.                                                                                                                                      |
| 2o11b7. | Current Value  | Depends on input variable | Current runtime boost modifier value.                                                                                                                                  |
| 2o11b8. | Const Value    | Depends on input variable | Constant input for turbo stage.                                                                                                                                        |
| 2012.   | Turbo Settings | None (Object)             | Turbo settings sub-block within performance mode.                                                                                                                      |
| 2o12a.  | Boost Lv       | bar or level index        | Target turbo boost level preset for this performance mode.                                                                                                             |
| 3.      | Car Part Type  | None ( Enum )             | Enum categorizing the visual/<br>mechanical part slot this tuning<br>part occupies in the parts menu<br>(Mechanics_Engine,<br>Mechanics_Gearbox, Exterior_*,<br>etc.). |

### <span id="page-201-0"></span>D. Example data

### <span id="page-201-1"></span>I. Chosen Cars for Example

- Toyota Supra MK IV (slug: ks toyota supra mkiv) [7 tuning parts]
- Datsun 240z Fairlady (slug: ks\_datsun\_240z\_fairlady) [8 tuning parts]
- Porsche 992 GT3 Cup (slug: ks porsche 992 gt3 cup) [4 tuning parts]

#### <span id="page-201-2"></span>II. Example

### <span id="page-201-3"></span>**Toyota Supra MK IV**

#### 1. Drift Front Geometry (file:

ks\_toyota\_supra\_geometry\_front\_drift\_geometry.tuningpart)

- 1. Physics Tuning : Suspensions Geometry
- 2 Suspensions Geometry
- |

content\cars\ks\_toyota\_supra\_mkiv\data\ks\_toyota\_supra\_mkiv\_front\_drift.
suspension

L 2b. Geometry Path Rear:

content\cars\ks\_toyota\_supra\_mkiv\data\ks\_toyota\_supra\_mkiv\_rear.suspens\nion

L 3. Car Part Type: Mechanics SuspensionGeometry Front

#### 2. Drift Drivetrain (file: ks toyota supra mkiv drivetrain drift.tuningpart)

- 1. Physics Tuning : Drivetrain
  - 2. Drivetrain
  - L 2a. Path:

content\cars\ks\_toyota\_supra\_mkiv\data\ks\_toyota\_supra\_mkiv\_drift.drivet
rain

```
3. Drift Engine ( file : ks_toyota_supra_mkiv_engine_drift.tuningpart )
├ 1. Physics Tuning : Engine 
├ 2. Engine 
│ └ 2a. Path : 
content\cars\ks_toyota_supra_mkiv\data\ks_toyota_supra_mkiv_drift.careng
ine 
└ 3. Car Part Type : Mechanics_Engine 
4. Drift Front Suspension ( file : ks_toyota_supra_mkiv_front_susp_drift.tuningpart ) 
├ 1. Physics Tuning : Suspensions 
├ 2. Suspensions 
│ ├ 2a. Coilover Path Front : 
content\cars\ks_toyota_supra_mkiv\data\ks_toyota_supra_mkiv_front.coilov
er
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
```

└ 3. Car Part Type : Mechanics\_Drivetrain

### <span id="page-202-0"></span>**Datsun 240z Fairlady**

*1. 5 Speed Gearbox ( file : ks\_datsun\_240z\_fairlady\_5speed.tuningpart )* 

```
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
```

```
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
                             Porsche 992 GT3 Cup 
1. No ABS No TC ( file : 992_gt3_no_abs_no_tc.tuningpart ) 
├ 1. Physics Tuning : <None> 
└ 2. Car Part Type : Mechanics_Electronics 
2. No ABS No TC Setup Limits ( file : 992_gt3_no_abs_no_tc_setuplimits.tuningpart ) 
├ 1. Physics Tuning : Setup Limits 
├ 2. Setup Limits 
│ └ 2a. Path : 
content\cars\ks_porsche_992_gt3_cup\data\Setup\limitsporsche992cup_no_ab
s_no_tc.carsetuplimits 
└ 3. Car Part Type : None 
3. Only ABS ( file : 992_gt3_only_abs.tuningpart ) 
├ 1. Physics Tuning : <None> 
└ 2. Car Part Type : Mechanics_Electronics 
4. Only ABS Setup Limits ( file : 992_gt3_only_abs_setuplimits.tuningpart ) 
├ 1. Physics Tuning : Setup Limits 
├ 2. Setup Limits 
│ └ 2a. Path : 
content\cars\ks_porsche_992_gt3_cup\data\Setup\limitsporsche992cup_only_
abs.carsetuplimits 
└ 3. Car Part Type : None
```

# <span id="page-205-0"></span>**9. Car Electronics [ .carelectronics ]**

### <span id="page-205-1"></span>**A. Description**

Software layer for driver aids: traction control, ABS, optional electronic differential lock (EDL), and ESP. It reads wheel slip, yaw, and steering telemetry and intervenes on engine torque or brake pressure — it does not replace mechanical brakes, drivetrain, or tyre physics.

Car Setup only stores which map index is selected (TC 3, ABS 5…). The actual slip windows and cut severity live here. Tuning parts / setup limits can swap or lock entire .carelectronics files (Cup "No ABS No TC" vs "Only ABS").

### <span id="page-205-2"></span>**I. Role in the stack**

| Concern                              | Handled here                 | Handled elsewhere             |
|--------------------------------------|------------------------------|-------------------------------|
| TC / ABS / EDL / ESP map<br>matrices | .carelectronics              | —                             |
| Which map is active in the garage    | —                            | .carsetup Electronics indices |
| Allowed TC/ABS range in UI           | —                            | .carsetuplimits               |
| Hydraulic brake torque and bias      | —                            | .brakesystem / .brakes        |
| Engine torque the TC can cut         | —                            | .carengine                    |
| Swap / strip aids per variant        | Path or None via .tuningpart | Companion setup limits        |

Car Data (or a tuning part) points at one electronics asset. Empty TC/ABS objects mean that aid is absent for that file — not "map 0 soft".

### <span id="page-205-3"></span>**II. What you are really tuning**

1. **Traction control envelope** — Per-setting slip window (*Min* / *Max Slip Ratio*), lateral tolerance (*Ref Slip Angle Deg*, *Slip Angle Activation Deg*), and how hard the ECU chops torque (*Engine Cut Level*). Gains on angular acceleration and oversteer decide how early the system reacts to yaw, not only pure wheelspin.

Higher map numbers in GT examples usually tighten the slip band and raise intervention gains — wet / worn / safer. Setting 1 is often a hard off slot (zeros, or slip ratios at -1 for ABS).

- 2. **TC global clocks** *Frequency Hz* (Huracan / MC20 at 333), *Min Speed Kmh* (often 40 no TC crawling in pit lane), *Gear Change Time* (brief mute around shifts: Huracan 0.045 s, MC20 0.025 s), and *Min* / *Max Cut Level* clamp how soft or brutal cuts can get. *Has TC2* flags a second TC channel when present.
- 3. **ABS envelope** Per-setting longitudinal slip targets, reference slip angle, *Cut Level* (how aggressively pressure is released), and *Max Torque Variation* (how fast brake torque may change — smoothing vs violent cycling). Setting 1 with min/max slip at -1 is the usual "ABS off" sentinel in race packs.
- 4. **ABS global clocks** *Frequency* (examples at 200 Hz), *Channels* (4 = four-wheel independent), *Min Speed Kmh* (often 20). Faster sample rate → smoother pedal pulse if the rest of the map allows it.

5. **EDL and ESP** — *EDL* can apply brake torque under power/coast spin with deadzones and max-spin thresholds — electronic locker behaviour. Race examples here leave it *None*. *ESP* settings (gain, steer gains, over/understeer gains, brake percent) are present in schema but often disabled in motorsport files (*Frequency Hz : 0*, empty settings).

### <span id="page-206-0"></span>**III. Architecture**

### <span id="page-206-1"></span>**1 - TRACTION CONTROL (SCHEMA 1)**

Object *TC*: globals (*Has TC2*, frequency, min speed, gear-change mute, cut clamps) plus *Settings[x]* rows of slip / angle / cut / gain fields.

### <span id="page-206-2"></span>**2 - ANTI-LOCK BRAKING (SCHEMA 2)**

Object *ABS*: *Settings[x]* rows, then frequency, channel count, min speed.

### <span id="page-206-3"></span>**3 - EDL (SCHEMA 3)**

Optional object: *Active*, brake torque power/coast, deadzones, max spin power/coast, min speed. Entire block may be *None*.

### <span id="page-206-4"></span>**4 - ESP (SCHEMA 4)**

Frequency, min speed, and *Settings[x]* with gain / steer / slip / brake-percent fields. Often stubbed off on GT / Cup cars.

### <span id="page-206-5"></span>**IV. How to read the examples**

### <span id="page-206-6"></span>**1 - LAMBORGHINI HURACAN ST EVO 2**

Full pro multi-map suite: 10 TC settings (1 = null/off; 2→10 tighten slip from about 0.18–0.45 down to 0.05– 0.15 and raise angular / oversteer gains). ABS has 12 settings (1 = off via -1 slips; live maps around 0.03– 0.12 slip with *Max Torque Variation* 0.7). EDL None; ESP frequency 0. Classic GT3-style adjustable aids.

### <span id="page-206-7"></span>**2 - MASERATI MC20 GT2**

Similar layout, 13 TC maps and 12 ABS maps. Mid maps push oversteer gain hard (up to about 14) while late maps drop engine cut toward 0.1 — different authoring curve than Huracan, same idea: map index = intervention personality. EDL None; ESP empty.

### <span id="page-206-8"></span>**3 - PORSCHE 992 GT3 CUP (TWO FILES)**

**No ABS No TC:** *TC* and *ABS* both *None* — pure mechanical driving, electronics file is a stub.

**Only ABS:** *TC : None*, ABS populated (12 settings, off slot + progressive slip windows). Paired with tuning parts + setup limits so the garage cannot re-enable stripped aids. Regulation by swapping the whole asset, not by zeroing every map in place.

### <span id="page-207-0"></span>**V. Practical notes**

- Setup index N must exist as *Settings N* here; pointing setup at map 8 when only 5 rows exist is a content bug.
- Treat Setting 1 zeros / -1 slips as intentional Off, not as "very soft intervention".
- Stripping aids for Cup / historic cars: prefer a dedicated .carelectronics with TC/ABS *None* (and matching limits) over leaving dead maps that the UI can still select.
- *Min Speed gates intervention* low-speed spins may be intentional if the threshold is high.
- OCR spacing in the dump (*T C*, *A B S*, *Ref Slip Angledeg*) is cosmetic; field meaning is the slip/cut/gain set above.
- ESP/EDL stubs with frequency 0 or *None* mean "not used on this car", not "map missing".

### <span id="page-207-1"></span>**VI. Related assets**

- **5 / 6. Car [Setup](#page-102-0) / Setup [Limits](#page-118-0)** select and clamp TC/ABS/ESC indices
- **• 8. Car [Tuning](#page-184-0) Parts** swap electronics files or tag Mechanics\_Electronics variants
- **• 1 / 2. Brake [System](#page-16-0) / [Brakes](#page-27-0)** hydraulic plant ABS modulates
- **4. Car [Engine](#page-87-0)** torque source TC cuts
- **3. Car [Data](#page-35-0)** default electronics path for the stock car

### <span id="page-207-2"></span>**B. Schema**

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
│ │ ├ 1g6. Oversteer Gain : float
│ └ └ 1g7. Slip Angle Activation Deg : float 
├ 2. A B S : object 
│ ├ 2a. Settings [x] : object | can have multiple Settings
│ │ ├ 2a1. Min Slip Ratio : float
│ │ ├ 2a2. Max Slip Ratio : float
│ │ ├ 2a3. Ref Slip Angledeg : float
│ │ ├ 2a4. Cut Level : float
│ │ └ 2a5. Max Torque Variation : float
│ ├ 2b. Frequency : float
│ ├ 2c. Channels : integer
│ └ 2d. Min Speed Kmh : float
```

```
├ 3. E D L : object 
│ ├ 3a. Active : boolean
│ ├ 3b. Braketorquepower : float
│ ├ 3c. Braketorquecoast : float
│ ├ 3d. Deadzonecoast : float
│ ├ 3e. Deadzonepower : float
│ ├ 3f. Maxspinpower : float
│ ├ 3g. Maxspincoast : float
│ └ 3h. Minspeed : float
├ 4. E S P : object 
│ ├ 4a. Frequency Hz : float
│ ├ 4b. Min Speed Kmh : float
│ ├ 4c. Settings [x] : object | can have multiple Settings
│ │ ├ 4c1. Gain : float
│ │ ├ 4c2. Steer Gain : float
│ │ ├ 4c3. Min Steer Gain : float
│ │ ├ 4c4. Steer Gain Max Speed : float
│ │ ├ 4c5. Oversteer Gain : float
│ │ ├ 4c6. Understeer Gain : float
│ │ ├ 4c7. Max Slip Ratio : float
│ │ ├ 4c8. Dead Zone : float
│ │ ├ 4c9. Filter Gain : float
│ │ ├ 4c10. Brake Perc : float
└ └ └ 4c11. Brake Perc Activation : float
```

### <span id="page-208-0"></span>**C. Measurement Units & Descriptions**

| ID  | Name             | Unit of Measurement                | Description                                                                                            |
|-----|------------------|------------------------------------|--------------------------------------------------------------------------------------------------------|
| 1.  | TC               | None ( Object )                    | Traction Control system block;<br>processes wheel slip and yaw to<br>modulate engine torque.           |
| 1a. | Has TC2          | None ( Boolean : True /<br>False ) | Enables a secondary traction<br>control map (TC2) for dual-stage<br>intervention logic.                |
| 1b. | Frequency Hz     | Hz ( Hertz )                       | Control loop update frequency of<br>the traction-control system (e.g.,<br>333 Hz in Huracán ST Evo 2). |
| 1c. | Min Speed Kmh    | km/h ( Kilometers per hour )       | Minimum vehicle speed below<br>which traction control deactivates<br>(e.g., 40 km/h).                  |
| 1d. | Gear Change Time | s ( Seconds )                      | Temporary TC suppression<br>window duration during gear<br>changes to avoid false<br>interventions.    |
| 1e. | Min Cut Level    | Ratio ( 0.0 - 1.0 )                | Minimum engine torque cut level<br>applied at the lowest TC<br>intervention step.                      |
| 1f. | Max Cut Level    | Ratio ( 0.0 - 1.0 )                | Maximum engine torque cut level<br>at the most aggressive TC step.                                     |

| ID   | Name                         | Unit of Measurement   | Description                                                                                         |
|------|------------------------------|-----------------------|-----------------------------------------------------------------------------------------------------|
| 1g.  | Settings                     | None ( Object array ) | Per-map TC settings block;<br>multiple entries (Settings 1–12+)<br>selectable from the cockpit.     |
| 1g1. | Min Slip Ratio               | Dimensionless ratio   | Lower slip-ratio threshold at which<br>TC begins monitoring wheel spin<br>for this settings map.    |
| 1g2. | Max Slip Ratio               | Dimensionless ratio   | Upper slip-ratio threshold<br>triggering full TC intervention for<br>this settings map.             |
| 1g3. | Ref Slip Angle Deg           | deg ( Degrees )       | Reference rear slip angle used to<br>scale TC aggression relative to<br>yaw behavior.               |
| 1g4. | Engine Cut Level             | Ratio ( 0.0 - 1.0 )   | Engine torque reduction factor<br>applied when slip thresholds are<br>exceeded.                     |
| 1g5. | Angular ACC Gain             | Dimensionless gain    | Yaw-rate / angular acceleration<br>gain for TC correction authority<br>(schema: Angular A C Cgain). |
| 1g6. | Oversteer Gain               | Dimensionless gain    | Additional TC sensitivity multiplier<br>when oversteer is detected.                                 |
| 1g7. | Slip Angle Activation<br>Deg | deg ( Degrees )       | Minimum slip angle required<br>before this TC map becomes<br>active.                                |
| 2.   | ABS                          | None ( Object )       | Anti-lock Braking System block;<br>modulates brake line pressure to<br>prevent wheel lockup.        |
| 2a.  | Settings                     | None ( Object array ) | Per-map ABS settings block;<br>multiple entries (Settings 1–12+)<br>for intervention intensity.     |
| 2a1. | Min Slip Ratio               | Dimensionless ratio   | Lower wheel slip threshold for<br>ABS monitoring on this settings<br>map.                           |
| 2a2. | Max Slip Ratio               | Dimensionless ratio   | Upper slip threshold triggering<br>maximum ABS pressure<br>modulation.                              |
| 2a3. | Ref Slip Angle Deg           | deg ( Degrees )       | Reference slip angle for ABS yaw<br>stability cross-correlation (schema:<br>Ref Slip Angledeg).     |
| 2a4. | Cut Level                    | Ratio ( 0.0 - 1.0 )   | Brake pressure reduction factor<br>applied during ABS pulsing.                                      |
| 2a5. | Max Torque Variation         | Nm or ratio           | Maximum allowed brake torque<br>fluctuation per ABS cycle on this<br>map.                           |
| 2b.  | Frequency                    | Hz ( Hertz )          | ABS control loop pulsing<br>frequency (e.g., 200 Hz in Huracán<br>ST Evo 2).                        |

| ID  | Name               | Unit of Measurement                | Description                                                                                                               |
|-----|--------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| 2c. | Channels           | None ( Integer )                   | Number of independent ABS<br>control channels (e.g., 4 = one per<br>wheel).                                               |
| 2d. | Min Speed Kmh      | km/h ( Kilometers per hour )       | Minimum speed below which ABS<br>intervention is disabled (e.g., 20<br>km/h).                                             |
| 3.  | EDL                | None ( Object )                    | Electronic Differential Lock block;<br>uses brake torque to emulate a<br>locking differential (may be None/<br>disabled). |
| 3a. | Active             | None ( Boolean : True /<br>False ) | Master enable for Electronic<br>Differential Lock brake-based<br>torque transfer.                                         |
| 3b. | Brake Torque Power | Nm ( Newton-meters )               | Brake torque applied to the<br>spinning wheel under power to<br>emulate diff lock (schema:<br>Braketorquepower).          |
| 3c. | Brake Torque Coast | Nm ( Newton-meters )               | Brake torque applied during<br>coasting to synchronize wheel<br>speeds (schema:<br>Braketorquecoast).                     |
| 3d. | Dead Zone Coast    | Ratio or rad/s                     | Speed-difference deadband below<br>which coast EDL does not<br>intervene (schema:<br>Deadzonecoast).                      |
| 3e. | Dead Zone Power    | Ratio or rad/s                     | Speed-difference deadband below<br>which power EDL does not<br>intervene (schema:<br>Deadzonepower).                      |
| 3f. | Max Spin Power     | rad/s or ratio                     | Maximum allowed wheel spin<br>differential under power before<br>EDL fully engages (schema:<br>Maxspinpower).             |
| 3g. | Max Spin Coast     | rad/s or ratio                     | Maximum allowed wheel spin<br>differential on coast before EDL<br>engages (schema: Maxspincoast).                         |
| 3h. | Min Speed          | M/s or km/h ( Speed<br>threshold   | Minimum vehicle speed required<br>for EDL operation (schema:<br>Minspeed).                                                |
| 4.  | ESP                | None ( Object )                    | Electronic Stability Program block;<br>applies selective braking and<br>torque reduction to control yaw.                  |
| 4a. | Frequency Hz       | Hz ( Hertz )                       | ESP control loop update<br>frequency (0 = disabled in some<br>example configs).                                           |
| 4b. | Min Speed Kmh      | km/h ( Kilometers per hour )       | Minimum speed below which ESP<br>deactivates.                                                                             |

| ID    | Name                  | Unit of Measurement                  | Description                                                                            |
|-------|-----------------------|--------------------------------------|----------------------------------------------------------------------------------------|
| 4c.   | Settings              | None (Object array)                  | Per-map ESP settings block;<br>multiple entries for intervention<br>authority presets. |
| 4c1.  | Gain                  | Dimensionless gain                   | Global ESP intervention authority multiplier for this settings map.                    |
| 4c2.  | Steer Gain            | Dimensionless gain                   | Steering-angle sensitivity gain for ESP yaw correction.                                |
| 4c3.  | Min Steer Gain        | Dimensionless gain                   | Minimum steering gain applied at low speeds within ESP logic.                          |
| 4c4.  | Steer Gain Max Speed  | km/h ( Kilometers per hour )         | Speed at which steering gain reaches its maximum ESP authority.                        |
| 4c5.  | Oversteer Gain        | Dimensionless gain                   | Corrective gain when rear slip (oversteer) is detected.                                |
| 4c6.  | Understeer Gain       | Dimensionless gain                   | Corrective gain when front slip (understeer) is detected.                              |
| 4c7.  | Max Slip Ratio        | Dimensionless ratio                  | Maximum wheel slip ratio before ESP applies full brake/engine intervention.            |
| 4c8.  | Dead Zone             | deg or ratio                         | Yaw/steer error deadband where ESP remains passive.                                    |
| 4c9.  | Filter Gain           | Coefficient ( Smoothing multiplier ) | Low-pass filter on ESP sensor inputs to prevent oscillatory corrections.               |
| 4c10. | Brake Perc            | Ratio ( 0.0 - 1.0 )                  | Percentage of available brake pressure ESP may apply for stability correction.         |
| 4c11. | Brake Perc Activation | Ratio ( 0.0 - 1.0 )                  | Slip/yaw threshold fraction at which ESP begins applying brake intervention.           |

### <span id="page-211-0"></span>D. Example data

### <span id="page-211-1"></span>I. Chosen Cars for Example

- Lamborghini Huracan ST Evo 2 (slug: ks\_lamborghini\_huracan\_st\_evo2)
- Maserati MC20 GT2 (slug: ks\_maserati\_mc20\_gt2)
- Porsche 992 GT3 Cup (slug: ks\_porsche\_992\_gt3\_cup) [ 2 variants ]

### <span id="page-211-2"></span>II. Example

### <span id="page-211-3"></span>Lamborghini Huracan ST Evo 2

```
│ ├ 1b. Frequency Hz : 333.00000 
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

### <span id="page-215-0"></span>**Maserati MC20 GT2**

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

### <span id="page-218-0"></span>**Porsche 992 GT3 Cup**

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

# <span id="page-221-0"></span>**10. Clutch [ .clutch ]**

### <span id="page-221-1"></span>**A. Description**

Mechanical bridge between crankshaft and gearbox input: how much torque the plates can hold, how much inertia they add when spinning, and how automated clutch logic (anti-stall, shift assist, forced engagement) behaves when the driver is not working a three-pedal clutch by hand.

Gear ratios and shift times live in the gearbox; engine torque lives in .carengine. This asset decides whether that torque couples cleanly, slips under load, or is handed off by an autoclutch during paddle / assisted shifts.

### <span id="page-221-2"></span>**I. Role in the stack**

| Concern                                    | Handled here        | Handled elsewhere       |
|--------------------------------------------|---------------------|-------------------------|
| Plate inertia and max clamp<br>torque      | .clutch             | —                       |
| Bite / engagement curve<br>(optional)      | Clutch Curve path   | External .curve         |
| Up/down shift actuator curves              | Autoclutch profiles | External .curve         |
| Gear ratios, shift timing hardware         | —                   | .gearbox                |
| Peak engine torque the clutch<br>must hold | —                   | .carengine              |
| Which clutch file loads                    | —                   | .car / .tuningpart path |

Loaded from Car Data *Clutch Path*, or swapped by a tuning part (e.g. Datsun 5-speed clutch pack).

### <span id="page-221-3"></span>**II. What you are really tuning**

- 1. **Holding capacity** *Clutch Max Torque* (Nm) is the fuse: above it, the plates slip even at full clamp. Caterham 500 Nm, Golf GTI 450 Nm, F2004 700 Nm. Engine upgrades that exceed this number waste power as heat and slip instead of acceleration.
- 2. **Rotational inertia** *Clutch Inertia* is the spinning mass of the assembly. Low values (F2004 0.005) let RPM rise and fall fast when decoupled — race response. Higher values (Caterham 0.017, Golf 0.010) store more kinetic energy and feel heavier / more road-car like on launch and blips.
- 3. **Autoclutch behaviour** Forced On true (Golf GTI) means the sim owns the clutch pedal binding is effectively obsolete. *false* (Caterham, F2004) leaves manual clutch feel available.

*Min Rpms* / *Max Rpms* bound anti-stall / launch assist windows (Caterham 1200–2000, Golf 1500–2400, F2004 a high 4300–4900 race idle band). Below min, the actuator can slip or open to save the engine.

*Use On Changes* true = autoclutch intervenes on gear changes (F2004, Golf). false (Caterham) = no automatic clutch work on shifts — pure driver friction zone.

- 4. **Shift profiles** *Upshift Profile* / *Down Shift Profile* point at .curve files that shape engagement timing and damping during automated or assisted shifts. Caterham wires both; F2004 only a downshift profile in the dump; Golf leaves both None and relies on Forced On + RPM window instead.
- 5. **Clutch curve** Optional path for a progressive bite map vs pedal / actuator travel. All three examples leave *Clutch Curve : None* — default linear or engine-side behaviour unless a curve is authored.

### <span id="page-222-0"></span>**III. Architecture**

### <span id="page-222-1"></span>**1 - MECHANICAL CONSTANTS (SCHEMA 1-2)**

*Clutch Inertia*, *Clutch Max Torque*

### <span id="page-222-2"></span>**2 - AUTOCLUTCH OBJECT (SCHEMA 3)**

Paths for up/down profiles; *Forced On*; *Min* / *Max Rpms*; *Use On Changes*.

### <span id="page-222-3"></span>**3 - ENGAGEMENT MAP (SCHEMA 4)**

*Clutch Curve* string path (or None).

### <span id="page-222-4"></span>**IV. How to read the examples**

### <span id="page-222-5"></span>**1 - CATERHAM 485 CSR — ANALOG / HISTORIC**

Inertia 0.017, max torque 500 Nm. Both shift profiles present, but *Forced On* and *Use On Changes* false. Manual three-pedal philosophy with curve blueprints available if assist paths are ever enabled; no forced electronic safety net against stalls.

### <span id="page-222-6"></span>**2 - FERRARI F2004 — RACE SEQUENTIAL STYLE**

Very low inertia (0.005), high clamp (700 Nm). Downshift profile only; *Use On Changes* true; high RPM autoclutch window (4300–4900). Built for fast engine response and assisted shifts without full Forced On automation.

### <span id="page-222-7"></span>**3 - VOLKSWAGEN GOLF GTI MK8 — ROAD / ASSISTED**

Mid inertia (0.010), 450 Nm. No up/down curve paths; *Forced On* true and *Use On Changes* true with a 1500–2400 RPM band. Everyday drivability: software owns the clutch, profiles optional.

### <span id="page-222-8"></span>**V. Practical notes**

- After an engine torque bump, re-check *Clutch Max Torque* or launches and WOT pulls will slip the plates.
- *Forced On : true* + empty profiles can still work if Min/Max RPM logic is enough; empty profiles + Forced On false usually means pure pedal.
- Tuning-part clutch swaps (alternate gearbox packages) should match the gearbox they ship with 5 speed clutch with a different ratio set is a common content pairing.

- *Clutch Curve : None* is normal in the sample cars; do not assume a missing curve is a bug unless bite feel is wrong in-session.
- Schema dump spacing (*Down Shift Profile*) is cosmetic.

### <span id="page-223-0"></span>**VI. Related assets**

- **3. Car [Data](#page-35-0)** Clutch Path
- **• 14. [Gearbox](#page-261-0)** ratios and shift events the clutch couples through
- **• 4. Car [Engine](#page-87-0)** torque the clutch must host
- **13. [Drivetrain](#page-245-0)** downstream of a closed clutch
- **8. Car [Tuning](#page-184-0) Parts** default electronics path for the stock car

### <span id="page-223-1"></span>**B. Schema**

```
├ 1. Clutch Inertia : float 
├ 2. Clutch Max Torque : float
├ 3. Autoclutch : object
│ ├ 3a. Upshift Profile : string - path
│ ├ 3b. Down Shift Profile : string - path 
│ ├ 3c. Forced On : boolean
│ ├ 3d. Min Rpms : float
│ ├ 3e. Max Rpms : float
│ └ 3f. Use On Changes : boolean
└ 4. Clutch Curve : string - path
```

### <span id="page-223-2"></span>**C. Measurement Units & Descriptions**

| ID  | Name              | Unit of Measurement                 | Description                                                                                                                                                                          |
|-----|-------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Clutch Intertia   | kg·m² ( Kilogram square<br>meters ) | Rotational inertia of the clutch<br>pressure plates and disc<br>assembly; lower values allow<br>faster RPM changes when<br>decoupled (e.g., 0.005 F2004,<br>0.017 Caterham 485 CSR). |
| 2.  | Clutch Max Torque | Nm ( Newton-meters )                | Maximum torque the friction plates<br>can transmit when fully clamped<br>before slip; acts as a powertrain<br>fuse (e.g., 500 Nm Caterham, 700<br>Nm F2004).                         |
| 3.  | Autoclutch        | None ( Object )                     | Automated clutch assist profile<br>block for shift timing, anti-stall,<br>and launch logic.                                                                                          |
| 3a. | Upshift Profile   | None ( .curve file path )           | Engagement/disengagement<br>curve applied during upshifts (e.g.,<br>upShiftProfile.curve); may be None<br>if unused.                                                                 |

| ID  | Name               | Unit of Measurement            | Description                                                                                                                                     |
|-----|--------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 3b. | Down Shift Profile | None ( .curve file path )      | Engagement curve applied during downshifts (e.g., downShiftProfile.curve); may be None if unused.                                               |
| 3c. | Forced On          | None (Boolean : True / False)  | When true, fully automates clutch operation (no manual pedal required; e.g., Golf GTI mk8).                                                     |
| 3d. | Min Rpms           | RPM ( Revolutions per minute ) | Lower RPM threshold for<br>automated anti-stall logic; clutch<br>slips or disengages below this<br>speed (e.g., 1200 Caterham, 4300<br>F2004).  |
| 3e. | Max Rpms           | RPM ( Revolutions per minute ) | Upper RPM window bound for automated clutch/launch assist logic (e.g., 2000 Caterham, 4900 F2004).                                              |
| 3f. | Use On Changes     | None (Boolean : True / False)  | When true, autoclutch intervenes during gear changes; when false, driver controls friction zone manually (Caterham: false).                     |
| 4.  | Clutch Curve       | None ( .curve file path )      | Look-up table mapping pedal travel or actuator position to clamping force / friction coefficient; often None when autoclutch profiles are used. |

#### <span id="page-224-0"></span>D. Example data

#### <span id="page-224-1"></span>I. Chosen Cars for Example

- Caterham 485 CSR (slug: ks\_caterham\_485\_csr)
- Ferrari F2004 (slug: ks\_ferrari\_f2004)
- Volkswagen Golf GTI mk8 ( slug : ks\_volkswagen\_golf\_gti\_mk8 )

#### <span id="page-224-2"></span>II. Example

### <span id="page-224-3"></span>Caterham 485 CSR

- 1. Clutch Inertia : 0.01700 - 2. Clutch Max Torque : 500.00000
- 3. Autoclutch
- 3a. Upshift Profile:

content\cars\ks\_caterham\_485\_csr\data\upShiftProfile.curve

- | 3b. Down Shift Profile :
- content\cars\ks\_caterham\_485\_csr\data\downShiftProfile.curve
  - 3c. Forced On : false - 3d. Min Rpms : 1200.00000 - 3e. Max Rpms : 2000.00000

│ └ 3f. Use On Changes : false └ 4. Clutch Curve : None

### <span id="page-225-0"></span>**Ferrari F2004**

├ 1. Clutch Inertia : 0.00500

├ 2. Clutch Max Torque : 700.00000

├ 3. Autoclutch

│ ├ 3a. Upshift Profile : None │ ├ 3b. Down Shift Profile :

content\cars\ks\_ferrari\_f2004\data\downShiftProfile.curve

│ ├ 3c. Forced On : false │ ├ 3d. Min Rpms : 4300.00000 │ ├ 3e. Max Rpms : 4900.00000 │ └ 3f. Use On Changes : true └ 4. Clutch Curve : None

### <span id="page-225-1"></span>**Volkswagen Golf GTI mk8**

├ 1. Clutch Inertia : 0.01000

├ 2. Clutch Max Torque : 450.00000

├ 3. Autoclutch

│ ├ 3a. Upshift Profile : None │ ├ 3b. Down Shift Profile : None

│ ├ 3c. Forced On : true

│ ├ 3d. Min Rpms : 1500.00000 │ ├ 3e. Max Rpms : 2400.00000 │ └ 3f. Use On Changes : true

└ 4. Clutch Curve : None

# <span id="page-226-0"></span>**11. Coilover [ .coilover ]**

### <span id="page-226-1"></span>**A. Description**

Per-axle (usually front and rear files) spring–damper unit: base spring rate, progressive rate, bump/rebound stops, collar position, slow/fast damper valves, optional damper LUT pack, helper spring, and optional rod controllers.

Car Setup overlays garage wheel rates, damper clicks, and ride-height collars on top of this hardware. Suspension kinematics (pickups, arms) live in .suspension. Alignment (camber, toe, pressure) is a setup concern — not fields in this schema, despite older prose that mixes the topics.

### <span id="page-226-2"></span>**I. Role in the stack**

| Concern                                           | Handled here             | Handled elsewhere                                  |
|---------------------------------------------------|--------------------------|----------------------------------------------------|
| Base spring / progressive rate                    | .coilover                | Garage override in .carsetup                       |
| Bump stop up/down shape                           | .coilover                | Setup may retarget ranges/rates                    |
| Slow/fast damper coeffi<br>cients +<br>thresholds | .coilover Damper         | Click overlay in setup; curves<br>in .dampercurves |
| Damper force LUT pack                             | Lut List → .dampercurves | Shared common_phsx packs                           |
| Helper spring K / range                           | .coilover                | Setup helpers when exposed                         |
| Active rod / heave logic                          | Rod Controllers stages   | Same stage pattern as other<br>controllers         |
| Hardpoints / motion ratio<br>geometry             | —                        | .suspension                                        |
| Which front/rear files load                       | —                        | .car / .tuningpart paths                           |

One coilover asset ≈ one corner family (front file + rear file in examples). Tuning parts can swap both (Datsun G-nose pack).

### <span id="page-226-3"></span>**II. What you are really tuning**

1. **Spring platform** — *Sprint Rate* in the dump is **Spring Rate** (OCR). Effective stiffness at the unit — Caterham about 14000 front / 16000 rear; Alpine 31000 / 40000; Dallara EXP 50000 / 80000. Higher = flatter platform, less mechanical compliance.

*Progressive Spring Rate* adds rate with travel when non-zero (Alpine front 30000, rear 40000). Zero (Caterham, Dallara) = linear main spring.

2. **Bump stops** — *Bump Stop Up* / *Down*: *Range*, *Reference*, *Force*, *Gamma*, *Length*, *Damping*. Up = compression packer behaviour; Down = extension / droop stop. Short ranges and high gamma (Dallara front Up range negative / tight reference 0.08) engage early under load — race aero platform. Caterham keeps longer ranges (about 0.04–0.07) for travel.

- 3. **Collar / ride reference** *Collar Position* sets the threaded perch baseline that setup ride-height / collar adjustments build on (Caterham front about 0.05, rear about 0.07; Alpine and Dallara vary per axle).
- 4. **Damper valves** *Damper.Slow* / *Fast* bump and rebound, plus *Fast Threshold* bump/rebound (velocity where "fast" map takes over). Caterham thresholds 0.15; Alpine 0.5 / 0.8; Dallara 0.8 / 0.8 race packs separate chassis control from kerb hits more explicitly.

Thermal / fatigue fields (*Cooling Surface*, *Nominal Force*, stress, *Thermal Capacity*, *Heat Transfer Coef*) are present but zeroed in these examples.

- 5. **Damper LUT** *Lut List* can point at a .dampercurves asset (Dallara → Penske pack in *common\_phsx*) with *Damper Lut Scale* (1.0). Caterham / Alpine leave Lut *None* and rely on the scalar slow/fast values alone.
- 6. **Helpers and rods** *Helper K* / *Helper Range* for tender springs unused (0) in all three samples. *Rod Controllers* stages (Input Var × Combinator × Lut × limits) enable active or linked rod behaviour; examples leave Name/Stages empty.

### <span id="page-227-0"></span>**III. Architecture**

### <span id="page-227-1"></span>**1 - SPRINGS AND STOPS (SCHEMA 1-5)**

*Spring rate, progressive rate, bump stop Up/Down objects, collar position.*

### <span id="page-227-2"></span>**2 - DAMPER BLOCK (SCHEMA 6)**

Fast/Slow bump & rebound; thresholds; thermal/fatigue placeholders; optional Lut path + scale.

### <span id="page-227-3"></span>**3 - HELPER AND CONTROLLERS (SCHEMA 7-9)**

*Helper K/range; Rod Controllers with staged Input Var / Combinator Mode enums (Brake, Gas, LatG, LonG, Steer, Speed, slip/angle metrics, ERS…; Add / Mult).*

### <span id="page-227-4"></span>**IV. How to read the examples**

### <span id="page-227-5"></span>**1 - CATERHAM 485 CSR — COMPLIANT ROAD / HISTORIC**

Soft springs (14k / 16k), progressive 0, generous bump-stop ranges, low fast thresholds (0.15), no damper LUT, no helpers/rods. Same damper scalars front and rear in the dump — balance comes more from spring rates and geometry elsewhere.

### <span id="page-227-6"></span>**2 - ALPINE A110S — STIFF ROAD / TRACK SPORT**

Much higher rates (31k–40k) plus strong progressive springs. Shorter compression stop up front; denser slow rebound (7000–7500). Still no LUT — authored as scalar valves with higher fast thresholds than Caterham.

### <span id="page-227-7"></span>**3 - DALLARA EXP — HIGH-DOWNFORCE RACE**

50k / 80k linear springs, aggressive bump-stop packing, high slow damper numbers (rear rebound 12800), Penske .dampercurves LUT at scale 1.0. Classic race pattern: stiff platform + shared professional damper map.

### <span id="page-228-0"></span>**V. Practical notes**

- Schema label **Sprint Rate** = Spring Rate typo in the converted dump.
- Setup wheel rates / damper clicks must stay consistent with whether this car is SI (*Ns/m*) or click-profile — see Setup Units.
- Negative bump-stop *Range* values appear in Alpine rear Down and Dallara front Up treat as authored packer geometry, not necessarily a parse error, but verify in-game travel.
- Wiring a Lut List without a valid .dampercurves path breaks the valve model; scale 0 with a path is suspicious.
- Front/rear are separate files a tuning part that only swaps one axle will create an asymmetric package on purpose or by mistake.
- PDF "alignments inside coilover" prose does not match this schema; use Car Setup for camber/toe/ pressure.

### <span id="page-228-1"></span>**VI. Related assets**

- **5 / 6 / 7. Car [Setup](#page-102-0) / [Limits](#page-118-0) / [Units](#page-174-0)** garage overlays and display language
- **• 12. [Damper](#page-238-0) Curves** LUT packs referenced by Lut List
- **• 17. [Suspension](#page-286-0)** kinematic hardpoints and motion
- **3. Car [Data](#page-35-0)** front/rear coilover paths
- **8. Car [Tuning](#page-184-0) Parts** coilover path redirects (G-nose, drift packs)

### <span id="page-228-2"></span>**B. Schema**

```
├ 1. Spring Rate : float
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
```

```
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
│ ├ 6k. Lut List : string - path
│ └ 6l. Damper Lut Scale : float
├ 7. Helper K : float
├ 8. Helper Range : float
├ 9. Rod Controllers : object
│ ├ 9a. Name : string
│ ├ 9b. Stages [x] : object | can have multiple Stages
│ │ ├ 9b1. Input Var : enum
│ │ ├ 9b2. Combinator Mode : enum
│ │ ├ 9b3. Lut : string - path
│ │ ├ 9b4. Filter Gain : float
│ │ ├ 9b5. Up Limit : float
│ │ ├ 9b6. Down Limit : float
│ │ ├ 9b7. Current Value : float
└ └ └ 9b8. Const Value : float
```

### **Enum - Car Coilover**

| 9b2 | Input Var       | UndefinedInput, Brake, Gas, LatG, LonG, Steer, Speed, Gear,<br>SlipRatioFrontAVG, SlipRatioRearAVG, SlipRatioFrontMAX,<br>SlipRatioRearMAX, SlipAngleFrontAVG, SlipAngleRearAVG,<br>SlipAngleFrontMAX, SlipAngleRearMAX, OversteerFactor,<br>RearSpeedRatio, SteerDEG, Const, RPMS, WheelSteerDEG,<br>LoadSpreadLF, LoadSpreadRF, AvgTravelRear, SusTravelLR,<br>SusTravelRR, SteerYawDeltaLeft, SteerYawDeltaRight,<br>ErsChargeLevel, ErsCoastTorque |
|-----|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 9b2 | Combinator Mode | UndefinedMode, Add, Mult                                                                                                                                                                                                                                                                                                                                                                                                                               |

### <span id="page-229-0"></span>**C. Measurement Units & Descriptions**

| ID | Name        | Unit of Measurement       | Description                                                                                                                                                 |
|----|-------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. | Spring Rate | N/m ( Newtons per meter ) | Primary linear spring stiffness at<br>the wheel (schema label Sprint<br>Rate; likely Spring Rate).<br>Caterham front: 14000 N/m, Alpine<br>rear: 40000 N/m. |

| ID  | Name                       | Unit of Measurement                 | Description                                                                                                           |
|-----|----------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 2.  | Progressive Spring<br>Rate | N/m² or N/m ( Progressive<br>rate ) | Secondary progressive spring rate;<br>stiffness rises non-linearly with<br>compression (0 = disabled on<br>Caterham). |
| 3.  | Bump Stop Up               | None ( Object )                     | Upper bump-stop block limiting<br>compression travel beyond main<br>spring range.                                     |
| 3a. | Range                      | m ( Meters )                        | Travel range before upper bump<br>stop engages (Bump Stop Up).                                                        |
| 3b. | Reference                  | m ( Meters )                        | Reference suspension position<br>where upper bump-stop force<br>scaling begins.                                       |
| 3c. | Force                      | N ( Newtons )                       | Peak resistive force of the upper<br>bump-stop at maximum<br>compression.                                             |
| 3d. | Gamma                      | Dimensionless exponent              | Non-linear shaping exponent for<br>upper bump-stop force vs.<br>compression.                                          |
| 3e. | Length                     | m ( Meters )                        | Physical contact length of the<br>upper bump-stop element.                                                            |
| 3f. | Damping                    | N·s/m ( Damping coeffi<br>cient )   | Damping applied during upper<br>bump-stop engagement.                                                                 |
| 4.  | Bump Stop Down             | None ( Object )                     | Lower bump-stop block limiting<br>droop/rebound travel.                                                               |
| 4a. | Range                      | m ( Meters )                        | Travel range before lower bump<br>stop engages (Bump Stop Down).                                                      |
| 4b. | Reference                  | m ( Meters )                        | Reference position where lower<br>bump-stop force model activates.                                                    |
| 4c. | Force                      | N ( Newtons )                       | Peak resistive force of the lower<br>bump-stop at maximum<br>extension.                                               |
| 4d. | Gamma                      | Dimensionless exponent              | Non-linear shaping exponent for<br>lower bump-stop force curve.                                                       |
| 4e. | Length                     | m ( Meters )                        | Physical contact length of the<br>lower bump-stop element.                                                            |
| 4f. | Damping                    | N·s/m ( Damping coeffi<br>cient )   | Damping applied during lower<br>bump-stop engagement on<br>rebound.                                                   |
| 5.  | Collar Position            | m ( Meters )                        | Spring perch/collar position<br>controlling static ride height and<br>preload (e.g., 0.04961 m Caterham<br>front).    |
| 6.  | Damper                     | None ( Object )                     | Hydraulic damper block: fast/slow<br>circuits, thresholds, thermal<br>model, and optional LUT.                        |

| ID   | Name                      | Unit of Measurement          | Description                                                                                              |
|------|---------------------------|------------------------------|----------------------------------------------------------------------------------------------------------|
| 6a.  | Fast                      | None ( Object )              | Fast damper circuit sub-block for<br>high-velocity wheel movements<br>(kerbs, bumps).                    |
| 6a1. | Bump                      | N·s/m ( Damping rate )       | Fast-speed compression damping<br>under 6a Fast (e.g., 700 Caterham,<br>1500 Alpine).                    |
| 6a2. | Rebound                   | N·s/m ( Damping rate )       | Fast-speed extension damping<br>under 6a Fast (e.g., 1700<br>Caterham front).                            |
| 6b.  | Slow                      | None ( Object )              | Slow damper circuit sub-block for<br>body roll, pitch, and weight<br>transfer.                           |
| 6a1. | Bump                      | N·s/m ( Damping rate )       | Slow-speed compression damping<br>under 6b Slow; schema reuses ID<br>6a1 (examples may label 6b1).       |
| 6a2. | Rebound                   | N·s/m ( Damping rate )       | Slow-speed extension damping<br>under 6b Slow; schema reuses ID<br>6a2 (examples may label 6b2).         |
| 6c.  | Fast Threshold Bump       | m/s ( Velocity threshold )   | Compression velocity above which<br>the fast bump circuit engages<br>(e.g., 0.15 Caterham, 0.50 Alpine). |
| 6d.  | Fast Threshold<br>Rebound | m/s ( Velocity threshold )   | Extension velocity above which<br>the fast rebound circuit engages.                                      |
| 6e.  | Cooling Surface           | m² ( Square meters )         | Exposed damper body surface<br>area for thermal dissipation<br>modeling.                                 |
| 6f.  | Nominal Force             | N ( Newtons )                | Reference force level for damper<br>nominal operating point and<br>fatigue calculations.                 |
| 6g.  | Min Stress Fatigue        | Pa or N ( Stress threshold ) | Lower bound stress below which<br>damper fatigue accumulation is<br>negligible.                          |
| 6h.  | Max Stress Fatigue        | Pa or N ( Stress threshold ) | Upper bound stress at which<br>damper fatigue reaches maximum<br>degradation rate.                       |
| 6i.  | Thermal Capacity          | J/K or J/°C                  | Heat storage capacity of the<br>damper assembly under repeated<br>high-energy cycles.                    |
| 6j.  | Heat Transfer Coef        | W/(m²·K) ( Coeffi<br>cient ) | Convective heat transfer rate from<br>damper body to ambient airflow.                                    |
| 6k.  | Lut List                  | None ( File path )           | Path to damper force-velocity LUT<br>list; often None when using scalar<br>rates only.                   |
| 6i.  | Damper Lut Scale          | Dimensionless multiplier     | Scaling factor applied to LUT<br>damper output (0 = unused when<br>Lut List is None).                    |

| ID   | Name            | Unit of Measurement                  | Description                                                                                        |
|------|-----------------|--------------------------------------|----------------------------------------------------------------------------------------------------|
| 7.   | Helper K        | N/m (Spring Rate)                    | Stiffness of helper/tender spring assisting the main coil at low compression.                      |
| 8.   | Helper Range    | m ( Meters )                         | Travel range over which the helper spring is active before the main spring carries full load.      |
| 9.   | Rod Controllers | None (Object)                        | Dynamic suspension rod controller block; optional active/heave control pipelines.                  |
| 9a.  | Name            | None (String)                        | Internal identifier for the rod controller; often None when inactive.                              |
| 9b.  | Stages          | None (Object array)                  | Multi-stage controller pipeline;<br>each stage maps telemetry input<br>through a LUT (often None). |
| 9b1. | Input Var       | None ( Telemetry enum )              | Telemetry input channel (Speed, SusTravelLR, SteerDEG, SlipRatio, ErsChargeLevel, etc.).           |
| 9b2. | Combinator Mode | None ( Math enum : Add / Mult )      | How stage output combines with prior stages: additive or multiplicative.                           |
| 9b3. | Lut             | None ( .curve file path )            | Look-up table mapping filtered input to rod/damper modifier output.                                |
| 9b4. | Filter Gain     | Coefficient ( Smoothing multiplier ) | Low-pass filter coefficient smoothing controller input spikes.                                     |
| 9b5. | Up Limit        | Depends on input variable            | Upper clamp on processed input before LUT evaluation.                                              |
| 9b6. | Down Limit      | Depends on input variable            | Lower clamp on processed input before LUT evaluation.                                              |
| 9b7. | Current Value   | Depends on input variable            | Runtime controller stage output during simulation (telemetry/ debug).                              |
| 9b8. | Const Value     | Depends on input variable            | Constant fallback output when Input Var is Const or LUT is inactive.                               |

### <span id="page-232-0"></span>D. Example data

### <span id="page-232-1"></span>I. Chosen Cars for Example

Caterham 485 CSR (slug: ks\_caterham\_485\_csr)Alpine A110s (slug: ks\_alpine\_a110\_s)Dallara EXP (slug: ks\_dallara\_exp)

### <span id="page-233-0"></span>**II. Example**

### <span id="page-233-1"></span>**Caterham 485 CSR**

*1. Front Coilover ( file : caterham\_485\_csr\_fr\_coil.coilover )* 

```
├ 1. Spring Rate : 14000.00000 
├ 2. Progressive Spring Rate : 0.00000 
├ 3. Bump Stop Up : object 
│ ├ 3a. Range : 0.04539 
│ ├ 3b. Reference : 0.01000 
│ ├ 3c. Force : 100.00000 
│ ├ 3d. Gamma : 2.00000 
│ ├ 3e. Length : 0.02000 
│ └ 3f. Damping : 300.00000 
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
├ 1. Spring Rate : 16000.00000 
├ 2. Progressive Spring Rate : 0.00000 
├ 3. Bump Stop Up : object 
│ ├ 3a. Range : 0.04031
```

│ ├ 3b. Reference : 0.01000 │ ├ 3c. Force : 100.00000

```
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

### <span id="page-234-0"></span>**Alpine A110s**

### *1. Front Coilover ( file : ks\_alpine\_a110\_s\_front.coilover )*

```
├ 1. Spring Rate : 31000.00000 
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
```

```
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
│ └ 6l. Damper Lut Scale : 0.00000 
├ 7. Helper K : 0.00000 
├ 8. Helper Range : 0.00000 
│ 9. Rod Controllers : object 
│ ├ 9a. Name : None 
└ └ 9b. Stages [x] : None 
2. Rear Coilover ( file : ks_alpine_a110_s_rear.coilover ) 
├ 1. Spring Rate : 40000.00000 
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
```

│ └ 4f. Damping : 500.00000 ├ 5. Collar Position : 0.00913

│ │ ├ 6a1. Bump : 1500.00000 │ │ └ 6a2. Rebound : 2300.00000

│ │ ├ 6b1. Bump : 4200.00000 │ │ └ 6b2. Rebound : 7500.00000

│ ├ 6c. Fast Threshold Bump : 0.50000 │ ├ 6d. Fast Threshold Rebound : 0.80000

│ ├ 6g. Min Stress Fatigue : 0.00000 │ ├ 6h. Max Stress Fatigue : 0.00000

│ ├ 6e. Cooling Surface : 0.00000 │ ├ 6f. Nominal Force : 0.00000

├ 6. Damper : object │ ├ 6a. Fast : object

│ ├ 6b. Slow : object

```
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

### <span id="page-236-0"></span>**Dallara EXP**

*1. Front Coilover ( file : ks\_dallara\_exp\_front\_coil.coilover )* 

```
├─ 1. Spring Rate : 50000.00000 
├─ 2. Progressive Spring Rate : 0.00000 
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
```

### *2. Rear Coilover ( file : ks\_dallara\_exp\_rear\_coil.coilover )*

```
├ 1. Spring Rate : 80000.00000 
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

# <span id="page-238-0"></span>**12. Damper Curves [ .dampercurves ]**

### <span id="page-238-1"></span>**A. Description**

Indexable bank of damper force LUTs: an ordered list of paths to .curve files. Coilover assets reference one of these packs via *Damper.Lut List*, then scale or select into it with *Damper Lut Scale* and garage damper settings.

The official prose block in the source dump is unfinished placeholder text (copied spring/alignment headings). Behaviour below is inferred from the schema and from how coilovers actually wire these packs (e.g. Dallara EXP → Penske).

### <span id="page-238-2"></span>**I. Role in the stack**

| Concern                                | Handled here  | Handled elsewhere             |
|----------------------------------------|---------------|-------------------------------|
| Ordered list of damper LUT<br>curves   | .dampercurves | Each entry → .curve           |
| Which pack a corner uses               | —             | .coilover Lut List            |
| Scale / blend of that pack             | —             | .coilover Damper Lut Scale    |
| Slow/fast scalar valves when no<br>LUT | —             | .coilover Damper Fast/Slow    |
| Garage damper clicks / rates           | —             | .carsetup (+ limits / units ) |

Almost always shipped under *content\cars\common\_phsx\dampers\…* and shared across many cars — not duplicated per vehicle folder.

### <span id="page-238-3"></span>**II. What you are really tuning**

- 1. **LUT catalogue, not a single curve** The asset is only *Damper Lut [x]* paths. Index 1, 2, 3… are alternate valve maps (click positions, bump/rebound families, or manufacturer presets). The coilover / setup layer picks which entry matters in session.
- 2. **Front vs rear packs** Some brands ship separate .dampercurves files per axle (Ford GT3 front/rear, Cayman GT4 front/rear) so F and R can use different curve sets. Others ship one shared pack (Penske) referenced by both front and rear coilovers.
- 3. **Depth of the click rack** Catalogue size varies by hardware philosophy:

| Pack                            | Approx. LUT count | Pattern                         |
|---------------------------------|-------------------|---------------------------------|
| Ford GT3 front / rear           | 5 + 5             | Compact race click set per axle |
| Porsche Cayman GT4 front / rear | 12 + 12           | Wider per-axle rack             |
| Penske (shared)                 | 60                | Dense shared library            |

More entries = finer garage resolution **if** setup/limits expose that many steps and the coilover scale maps onto them cleanly.

4. **Relationship to scalar dampers** — Caterham / Alpine coilovers in the coilover examples leave *Lut List : None* and use Slow/Fast bump-rebound floats only. Dallara sets Lut List to Penske and *Damper Lut Scale : 1.0* — the curve bank becomes the real force shape; scalars and scale still matter as multipliers / baselines depending on authoring.

### <span id="page-239-0"></span>**III. Architecture**

### <span id="page-239-1"></span>**1 - DAMPER CURVES LIST EDIT (SCHEMA 1)**

Single repeating field: *Damper Lut [x] : string* (path). Can have many entries; no other fields in the dump.

### <span id="page-239-2"></span>**2 - REFERENCE PAYLOAD**

Each path points at a *.curve* (force vs velocity or equivalent LUT). Editing damper feel means editing those curves or swapping which *.dampercurves* pack the coilover points at — not adding sibling fields inside this asset.

### <span id="page-239-3"></span>**IV. How to read the examples**

### <span id="page-239-4"></span>**1 - FORD GT3 DAMPERS**

Two files: *ford\_gt3\_front\_damper.dampercurves* and rear counterpart. Each lists five LUTs (*ford\_damper\_front\_1…5.curve* / *rear\_1…5*). Axle-specific, short click banks — typical GT3 shared physics.

### <span id="page-239-5"></span>**2 - PENSKE (COMMON\_PHSX)**

One pack with sixty LUTs (*damper\_1.curve* … *damper\_60.curve*). Same file Dallara EXP coilovers reference. Broad manufacturer library reused by multiple race cars.

### <span id="page-239-6"></span>**3 - PORSCHE CAYMAN GT4 DAMPERS**

Front and rear packs under *…\porsche\cayman\*, twelve curves each (*front1…12, rear1…12*). Mid-size peraxle racks between Ford's five and Penske's sixty.

### <span id="page-239-7"></span>**V. Practical notes**

- Source Description section is placeholder (*Xxxxxxx*) do not trust its spring/alignment headings for this asset.
- Broken or missing .curve paths inside the list fail at the LUT the garage actually selects, which can look like "random click does nothing".
- Changing only the .dampercurves file while coilovers still point at another pack does nothing until *Lut List* is updated.
- *Damper Lut Scale : 0* with a non-None Lut List (or scale 1 with empty curves) is a content smell.

- Prefer editing shared common phsx packs carefully one change hits every car that references them.
- Setup damper indices must not exceed the LUT count in the referenced pack.

#### <span id="page-240-0"></span>VI. Related assets

- 11. Coilover Lut List / Damper Lut Scale consumers
- 5 / 6 / 7. Car Setup / Limits / Units which click/rate the driver selects and how it is labelled
- External .curve files actual force-velocity (or equivalent) maps listed here
- 3. Car Data does not hold dampercurvews directly; reaches them through coilover paths

#### <span id="page-240-1"></span>B. Schema

[ Data in a "Damper Curves List Edit" object ]

Lack 1. Damper Lut [x]: string - path | can have multiple Damper Lut

#### <span id="page-240-2"></span>C. Measurement Units & Descriptions

| ID | Name       | Unit of Measurement       | Description                                                                                                                                                                                                                                                                                                     |
|----|------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. | Damper Lut | None ( .curve file path ) | Indexed list of damper forcevelocity LUT curves (.curve); each entry defines non-linear bump/rebound damping for a discrete damper click or valve map.  Referenced from Coilover <b>6k Lut List</b> (.DAMPERCURVES asset). Ford GT3: 5 curves per axle; Penske kit: 60 curves; Porsche Cayman GT4: 12 per axle. |

#### <span id="page-240-3"></span>D. Example data

#### <span id="page-240-4"></span>I. Chosen Cars for Example

- Ford GT3 Dampers (common phsx) [2 dampers]
- Penske Dampers (common\_phsx)
- Porsche Cayman Dampers (common phsx) [2 dampers]

#### <span id="page-240-5"></span>II. Example

#### <span id="page-240-6"></span>Ford - GT3 Dampers

Front Damper (file: ford\_gt3\_front\_damper.dampercurves)

```
├ 1. Damper Lut 1 : 
content\cars\common_phsx\dampers\ford\ford_damper_front_1.curve 
├ 1. Damper Lut 2 : 
content\cars\common_phsx\dampers\ford\ford_damper_front_2.curve 
├ 1. Damper Lut 3 : 
content\cars\common_phsx\dampers\ford\ford_damper_front_3.curve 
├ 1. Damper Lut 4 : 
content\cars\common_phsx\dampers\ford\ford_damper_front_4.curve 
├ 1. Damper Lut 5 : 
content\cars\common_phsx\dampers\ford\ford_damper_front_5.curve
```

### *2. Rear Damper ( file : ford\_gt3\_rear\_damper.dampercurves )*

```
├ 1. Damper Lut 1 : 
content\cars\common_phsx\dampers\ford\ford_damper_rear_1.curve 
├ 1. Damper Lut 2 : 
content\cars\common_phsx\dampers\ford\ford_damper_rear_2.curve 
├ 1. Damper Lut 3 : 
content\cars\common_phsx\dampers\ford\ford_damper_rear_3.curve 
├ 1. Damper Lut 4 : 
content\cars\common_phsx\dampers\ford\ford_damper_rear_4.curve 
└ 1. Damper Lut 5 : 
content\cars\common_phsx\dampers\ford\ford_damper_rear_5.curve
```

### <span id="page-241-0"></span>**Penske**

```
├ 1. Damper Lut 1 : 
content\cars\common_phsx\dampers\penske\damper_1.curve 
├ 1. Damper Lut 2 : 
content\cars\common_phsx\dampers\penske\damper_2.curve 
├ 1. Damper Lut 3 : 
content\cars\common_phsx\dampers\penske\damper_3.curve 
├ 1. Damper Lut 4 : 
content\cars\common_phsx\dampers\penske\damper_4.curve 
├ 1. Damper Lut 5 : 
content\cars\common_phsx\dampers\penske\damper_5.curve 
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
```

```
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
```

```
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

### <span id="page-243-0"></span>**Porsche Cayman Dampers**

### *1. Front Damper ( file : cayman\_gt4\_front.dampercurves )*

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
```

```
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

### *2. Rear Damper ( file : cayman\_gt4\_rear.dampercurves )*

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
└ 1. Damper Lut 12 : 
content\cars\common_phsx\dampers\porsche\cayman\rear12.curve
```

# <span id="page-245-0"></span>**13. Drivetrain [ .drivetrain ]**

### <span id="page-245-1"></span>**A. Description**

How engine torque reaches the wheels: driven-axle layout, differential type and lock (power / coast / preload), optional multi-diff AWD tree, halfshaft / driveline torsion, and staged lock or AWD-clutch controllers.

Gear ratios live in .gearbox. Garage power/coast/preload clicks live in .carsetup. This asset is the mechanical baseline those layers sit on — and where full AWD clutch logic is authored.

Official Description prose in the source dump is unfinished placeholder text (spring/damper headings). Content below follows the schema and examples.

### <span id="page-245-2"></span>**I. Role in the stack**

| Concern                           | Handled here            | Handled elsewhere        |
|-----------------------------------|-------------------------|--------------------------|
| FWD / RWD / AWD layout            | Traction Type           | —                        |
| Primary diff type & locks         | Differential Data       | Setup may override locks |
| Front / center / rear diffs (AWD) | Four WD Differentials   | —                        |
| Driveline stiffness / torsion     | Stiffness fields        | —                        |
| Dynamic lock / eLSD maps          | Lock Controllers stages | .curve LUTs              |
| AWD clutch packs                  | Awd Clutches [x]        | Controllers + curves     |
| Ratios / shift                    | —                       | .gearbox                 |
| Which file loads                  | —                       | .car / .tuningpart path  |

### <span id="page-245-3"></span>**II. What you are really tuning**

- 1. **Traction layout** *Traction Type* selects the driven scheme. Examples: *AWDF* (Audi RS3 AWD with front-biased architecture), *RWD* (F40 LM), *FWD* (Abarth 695). Wrong type with filled AWD blocks is a content bug.
- 2. **Primary differential** *Differential Data*: *Type* (LSD, Spool, Torsen, EpicyclicTorsen, EpicyclicLSD, TorqueVectoring — same family as Car Data performance-mode enums), plus *Power* / *Coast* / *Preload*, optional *Front Share*, torque-bias ratios, and thermal / wear / friction-vs-temperature fields.

On simple FWD/RWD cars this block is the real diff (Abarth: LSD, power/coast 0.25, preload 20). On the RS3 AWD example the primary block is zeroed — locks live under Four WD Differentials instead.

3. **Four-wheel-drive tree** — *Four WD Differentials* → Front / Center / Rear, each with the same lock/ thermal shape as Differential Data. RS3: front LSD (0.5 / 0.1 / preload 30), center EpicyclicLSD with *Front Share* 0.40, rear Spool with torque-bias ratios (power 2.5 / coast 2.0). RWD/FWD cars still show the tree in the dump but with zeroed stubs.

- 4. **Driveline torsion** *Stiffness*, *Stiffness Mult*, *Damping Ratio*, *Max Torsion Deg*, *Non Linear Model* model shaft wind-up between gearbox and wheels. F40 LM fills these in (stiffness 4500, mult 2, damping 0.05, max torsion 40°, nonlinear true). RS3 / Abarth leave them at 0 / false — rigid coupling assumption.
- 5. **Flags and lock controllers** *Max Between Lsd And Elsd*, *Has Cockpit Controls*. Front / Center / Rear / Left / Right **Lock Controllers** reuse the staged Input × Combinator × Lut pipeline (Gas, LatG, slip, oversteer…). Empty in these three samples.
- 6. **AWD clutches** *Awd Clutches[x]*: *Position*, *Preload*, nested Controllers. RS3 ships two clutches (positions 2 and 3) with five stages each — Gas and front slip (Add), then LatG, OversteerFactor, and Speed (Mult) — classic Haldex-style transfer logic. F40 / Abarth: None.

### <span id="page-246-0"></span>**III. Architecture**

### <span id="page-246-1"></span>**1 - LAYOUT AND PRIMARY DIFF (SCHEMA 1-2)**

*Traction Type*; *Differential Data* object.

### <span id="page-246-2"></span>**2 - AWD DIFFERENTIALS (SCHEMA 3)**

Front / Center / Rear diff objects (same leaf fields as 2).

### <span id="page-246-3"></span>**3 - TORSION AND FLAGS (SCHEMA 4-10)**

Stiffness stack; nonlinear flag; LSD/eLSD max flag; cockpit controls flag.

### <span id="page-246-4"></span>**4 - CONTROLLERS AND CLUTCHES (SCHEMA 11-16)**

Five lock-controller slots; repeating AWD clutch entries with their own stage lists.

### <span id="page-246-5"></span>**IV. How to read the examples**

### <span id="page-246-6"></span>**1 - AUDI RS3 SPORTBACK — CONTROLLED AWD**

*AWDF*. Real behaviour in Four WD diffs + two AWD clutches driven by Gas / slip / LatG / oversteer / speed curves. Primary Differential Data empty. Shows where modern quattro-style logic lives: not a single power/ coast pair, but center share + clutch maps.

### <span id="page-246-7"></span>**2 - FERRARI F40 LM — RWD WITH SHAFT TORSION**

*RWD*, LSD type declared, lock numbers zero in the dump (expect setup overlays or open baseline until garage sets them). Four WD / AWD clutches unused. Driveline torsion fully authored — race RWD that can wind up and unload.

### <span id="page-246-8"></span>**3 - ABARTH 695 BIPOSTO — SIMPLE FWD LSD**

*FWD* with Differential Data LSD at 0.25 / 0.25 / preload 20. Four WD stubs and AWD clutches empty; torsion off. Compact hot-hatch pattern: one mechanical LSD, no transfer case.

### <span id="page-247-0"></span>**V. Practical notes**

- Source Description section is placeholder ignore its spring/alignment headings.
- For AWD, always read **Four WD Differentials** and **Awd Clutches** before trusting Differential Data (may be a zero stub).
- Setup power/coast/preload must stay consistent with the active diff node (primary vs front/rear).
- OCR quirks: duplicated *2i* labels, *LSF* on F40 front stub, nested controller IDs reused as *11a*/*11b* under clutch 16.
- Empty lock controllers + nonzero AWD clutch stages is normal clutch pack owns the dynamics.
- Tuning-part drivetrain swaps (Supra drift, Datsun LSD) replace this whole file; pair with matching setup/ limits.

### <span id="page-247-1"></span>**VI. Related assets**

- **3. Car [Data](#page-35-0)** Drivetrain Path
- **• 14 / 10 / 4. [Gearbox](#page-261-0) / [Clutch](#page-221-0) / [Engine](#page-87-0)** upstream torque path
- **• 5 / 6. Car [Setup](#page-102-0) / [Limits](#page-118-0)** garage diff locks
- **8. Car [Tuning](#page-184-0) Parts** alternate .drivetrain redirects
- **9. Car [Electronics](#page-205-0)** EDL / TC intervene on top of mechanical lock, they do not replace this asset

### <span id="page-247-2"></span>**B. Schema**

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
```

```
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
```

```
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
│ ├ 16b. Preload : float
│ ├ 16c. Controllers : object
│ │ ├ 11a. Name : string
│ │ ├ 11b. Stages [x] : object | can have multiple Stages 
│ │ │ ├ 11b1. Input Var : enum
│ │ │ ├ 11b2. Combinator Mode : enum
│ │ │ ├ 11b3. Lut : string - path
│ │ │ ├ 11b4. Filter Gain : float
│ │ │ ├ 11b5. Up Limit : float
│ │ │ ├ 11b6. Down Limit : float
│ │ │ ├ 11b7. Current Value : float
└ └ └ └ 11b8. Const Value : float
```

### <span id="page-250-0"></span>**C. Measurement Units & Descriptions**

| ID  | Name                         | Unit of Measurement                                                                              | Description                                                                                                                   |
|-----|------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Traction Type                | None ( Enum : FWD / RWD /<br>AWDF / … )                                                          | Global driveline layout enum (e.g.,<br>AWDF Audi RS3, RWD Ferrari F40<br>LM, FWD Abarth 695).                                 |
| 2.  | Differential Data            | None ( Object )                                                                                  | Primary differential parameter<br>block for single-diff or default axle<br>configuration.                                     |
| 2a. | Type                         | None ( Enum : LSD / Spool /<br>Torsen / EpicyclicTorsen /<br>EpicyclicLSD /<br>TorqueVectoring ) | Differential mechanism type<br>governing torque split and lock<br>behavior.                                                   |
| 2b. | Power                        | Nm or ratio                                                                                      | Lock/acceleration sensitivity under<br>power (on-throttle); higher values<br>increase drive-wheel coupling on<br>corner exit. |
| 2c. | Coast                        | Nm or ratio                                                                                      | Lock sensitivity on coast/off<br>throttle; stabilizes the axle under<br>braking and lift-off.                                 |
| 2d. | Preload                      | Nm ( Newton-meters )                                                                             | Static preload torque before<br>differential plates begin slipping.                                                           |
| 2e. | Front Share                  | Ratio ( 0.0 - 1.0 )                                                                              | Fraction of total driveline torque<br>directed to the front axle (AWD/<br>center diff).                                       |
| 2f. | Torque Bias Ratio<br>Power   | Ratio ( e.g., 2.0:1 )                                                                            | Torque bias ratio between sides or<br>axles under power.                                                                      |
| 2g. | Torque Bias Ratio<br>Coast   | Ratio                                                                                            | Torque bias ratio between sides or<br>axles on coast.                                                                         |
| 2h. | Thermal Capacity             | J/K or J/°C                                                                                      | Heat storage capacity of<br>differential friction components for<br>thermal wear modeling.                                    |
| 2i. | Surface                      | m² ( Square meters )                                                                             | Exposed friction surface area of<br>the differential housing for cooling<br>calculations.                                     |
| 2j. | Heat Transfer Coef           | W/(m²·K) ( Coeffi<br>cient )                                                                     | Convective heat dissipation rate<br>from differential to ambient/oil.                                                         |
| 2k. | Wear Factor                  | Dimensionless coeffi<br>cient                                                                    | Rate at which differential friction<br>surfaces degrade under load and<br>temperature.                                        |
| 2l. | Friction Reduction With<br>T | Ratio/°C                                                                                         | Linear friction reduction per<br>degree of differential temperature<br>rise.                                                  |
| 2m. | Friction Ref T               | °C ( Degrees Celsius )                                                                           | Reference temperature at which<br>nominal differential friction is<br>defined.                                                |

| ID   | Name                        | Unit of Measurement                    | Description                                                                                                                                                                               |
|------|-----------------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.   | Four W D Differentials      | None ( Object )                        | AWD/4WD triple-differential<br>container: front, center, and rear<br>axle blocks.                                                                                                         |
| 3a.  | Front Dif                   | None ( Object )                        | Front Diff sub-block within Four W<br>D Differentials (3).                                                                                                                                |
| 3b.  | Center Dif                  | None ( Object )                        | Center Diff sub-block within Four<br>W D Differentials (3).                                                                                                                               |
| 3c.  | Rear Dif                    | None ( Object )                        | Rear Diff sub-block within Four W<br>D Differentials (3).                                                                                                                                 |
| 4.   | Stiffness                   | Nm/deg ( Newton-meters per<br>degree ) | Torsional stiffness of the<br>differential coupling model (e.g.,<br>4500 Nm/deg Ferrari F40 LM).                                                                                          |
| 5.   | Stiffness Mult              | Dimensionless multiplier               | Scalar multiplier applied to base<br>stiffness for non-linear or epicyclic<br>models (e.g., 2.0 F40 LM).                                                                                  |
| 6.   | Damping Ratio               | Dimensionless ratio ( ζ )              | Torsional damping ratio of the<br>differential dynamics model (e.g.,<br>0.05 F40 LM).                                                                                                     |
| 7.   | Max Torsion Deg             | deg ( Degrees )                        | Maximum torsion angle before the<br>differential model saturates (e.g.,<br>40° F40 LM).                                                                                                   |
| 8.   | Non Linear Model            | None ( Boolean : True /<br>False )     | When true, enables non-linear<br>torsional differential physics (true<br>on F40 LM).                                                                                                      |
| 9.   | Max Between Lsd And<br>Elsa | None ( Boolean : True /<br>False )     | When true, caps combined LSD<br>and eLSD lock contribution to a<br>maximum blended value.                                                                                                 |
| 10.  | Has Cockpit Controls        | None ( Boolean : True /<br>False )     | When true, exposes in-cockpit<br>differential lock or bias adjustment<br>to the driver.                                                                                                   |
| 11.  | Front Lock Controllers      | None ( Object )                        | Dynamic controller modulating<br>front lock controllers under<br>telemetry conditions.                                                                                                    |
| 11a. | Name                        | None ( String )                        | Internal identifier for the lock<br>controller; often None when<br>inactive. Under Front Lock<br>Controllers; schema reuses IDs<br>11a/11b/11b1–11b8.                                     |
| 11b. | Stages                      | None ( Object array )                  | Multi-stage controller pipeline<br>mapping telemetry input through<br>LUTs (often None on simple LSD<br>setups). Under Front Lock<br>Controllers; schema reuses IDs<br>11a/11b/11b1–11b8. |

| ID    | Name                    | Unit of Measurement                         | Description                                                                                                                                                         |
|-------|-------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 11b1. | Input Var               | None ( Telemetry enum )                     | Telemetry input channel (Gas,<br>SlipRatioFrontAVG, LatG, Speed,<br>ErsChargeLevel, etc.). Under<br>Front Lock Controllers; schema<br>reuses IDs 11a/11b/11b1–11b8. |
| 11b2. | Combinator Mode         | None ( Math enum : Add /<br>Mult )          | How stage output combines with<br>prior stages: additive or<br>multiplicative. Under Front Lock<br>Controllers; schema reuses IDs<br>11a/11b/11b1–11b8.             |
| 11b3. | Lut                     | None ( .curve file path )                   | Look-up table mapping filtered<br>input to differential/clutch lock<br>modifier. Under Front Lock<br>Controllers; schema reuses IDs<br>11a/11b/11b1–11b8.           |
| 11b4. | Filter Gain             | Coeffi<br>cient ( Smoothing<br>multiplier ) | Low-pass filter coeffi<br>cient<br>smoothing controller input spikes.<br>Under Front Lock Controllers;<br>schema reuses IDs 11a/11b/11b1–<br>11b8.                  |
| 11b5. | Up Limit                | Depends on input variable                   | Upper clamp on processed input<br>before LUT evaluation. Under<br>Front Lock Controllers; schema<br>reuses IDs 11a/11b/11b1–11b8.                                   |
| 11b6. | Down Limit              | Depends on input variable                   | Lower clamp on processed input<br>before LUT evaluation. Under<br>Front Lock Controllers; schema<br>reuses IDs 11a/11b/11b1–11b8.                                   |
| 11b7. | Current Value           | Depends on input variable                   | Runtime controller stage output<br>during simulation (telemetry/<br>debug). Under Front Lock<br>Controllers; schema reuses IDs<br>11a/11b/11b1–11b8.                |
| 11b8. | Const Value             | Depends on input variable                   | Constant fallback output when<br>Input Var is Const or LUT is<br>inactive. Under Front Lock<br>Controllers; schema reuses IDs<br>11a/11b/11b1–11b8.                 |
| 12.   | Center Lock Controllers | None ( Object )                             | Dynamic controller modulating<br>center lock controllers under<br>telemetry conditions.                                                                             |
| 13.   | Rear Lock Controllers   | None ( Object )                             | Dynamic controller modulating<br>rear lock controllers under<br>telemetry conditions.                                                                               |
| 14.   | Left Lock Controllers   | None ( Object )                             | Dynamic controller modulating left<br>lock controllers under telemetry<br>conditions.                                                                               |
| 15.   | Right Lock Controllers  | None ( Object )                             | Dynamic controller modulating<br>right lock controllers under<br>telemetry conditions.                                                                              |

| ID   | Name         | Unit of Measurement  | Description                                                                                              |
|------|--------------|----------------------|----------------------------------------------------------------------------------------------------------|
| 16.  | Awd Clutches | None (Object array)  | AWD clutch pack array; each entry couples axles with preload and optional active controllers (Audi RS3). |
| 16a. | Position     | None (Integer index) | Clutch pack index/position in the AWD coupling matrix (e.g., 2 on Audi RS3).                             |
| 16b. | Preload      | Nm ( Newton-meters ) | Static preload torque on this AWD clutch before slip occurs.                                             |
| 16c. | Controllers  | None ( Object )      | Nested lock controller block for this AWD clutch pack.                                                   |

### <span id="page-253-0"></span>D. Example data

### <span id="page-253-1"></span>I. Chosen Cars for Example

- Audi RS3 Sportback (slug: ks\_audi\_rs\_3\_sportback)
- Ferrari F40 LM (slug: ks\_ferrari\_f40\_lm)
- Abarth 695 Biposto (slug: ks\_abarth\_695\_biposto)

### <span id="page-253-2"></span>II. Example

### <span id="page-253-3"></span>**Audi RS3 Sportback**

```
1. Traction Type : AWDF
2. Differential Data
 - 2a. Type : LSD
  2b. Power: 0.00000
  2c. Coast: 0.00000
  2d. Preload: 0.00000
  2e. Front Share: 0.00000
  2f. Torque Bias Ratio Power: 0.00000
  2g. Torque Bias Ratio Coast : 0.00000
  2h. Thermal Capacity: 0.00000
  2i. Surface: 0.00000
 - 2i. Heat Transfer Coeff : 0.00000
  2k. Wear Factor: 0.00000
  21. Friction Reduction With T: 0.00000
 L 2m. Friction Ref T: 0.00000
3. Four W D Differentials
 3a. Front Diff
   - 2a. Type : LSD
    2b. Power: 0.50000
   - 2c. Coast : 0.10000
   - 2d. Preload : 30.00000
    2e. Front Share: 0.00000
    2f. Torque Bias Ratio Power: 0.00000
    2g. Torque Bias Ratio Coast : 0.00000
```

```
│ │ ├ 2h. Thermal Capacity : 0.00000 
│ │ ├ 2i. Surface : 0.00000 
│ │ ├ 2j. Heat Transfer Coeff : 0.00000 
│ │ ├ 2k. Wear Factor : 0.00000 
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
```

```
├ 16. Awd Clutches 1 
│ ├ 16a. Position : 2 
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
│ └ └ └ 11b8. Const Value : 0.00000 
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
```

```
│ │ │ ├ 11b3. Lut : 
content\cars\ks_audi_rs_3_sportback\data\controller\new_awd\ks_audi_rs_3
_awd_clutch_speed_power.curve 
│ │ │ ├ 11b4. Filter Gain : 0.00000 
│ │ │ ├ 11b5. Up Limit : 3000.00000 
│ │ │ ├ 11b6. Down Limit : 0.00000 
│ │ │ ├ 11b7. Current Value : 0.00000 
└ └ └ └ 11b8. Const Value : 0.00000
```

```
Ferrari F40 LM 
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
```

│ │ └ 2m. Friction Ref T : 0.00000 │ ├ 3c. Rear Diff │ │ ├ 2a. Type : LSD │ │ ├ 2b. Power : 0.00000 │ │ ├ 2c. Coast : 0.00000 │ │ ├ 2d. Preload : 0.00000 │ │ ├ 2e. Front Share : 0.00000 │ │ ├ 2f. Torque Bias Ratio Power : 0.00000 │ │ ├ 2g. Torque Bias Ratio Coast : 0.00000 │ │ ├ 2h. Thermal Capacity : 0.00000 │ │ ├ 2i. Surface : 0.00000 │ │ ├ 2j. Heat Transfer Coeff : 0.00000 │ │ ├ 2k. Wear Factor : 0.00000 │ │ ├ 2l. Friction Reduction With T : 0.00000 │ └ └ 2m. Friction Ref T : 0.00000 ├ 4. Stiffness : 4500.00000 ├ 5. Stiffness Mult : 2.00000 ├ 6. Damping Ratio : 0.05000 ├ 7. Max Torsion Deg : 40.00000 ├ 8. Non Linear Model : true ├ 9. Max Between Lsd And Elsd : false ├ 10. Has Cockpit Controls : false ├ 11. Front Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None ├ 12. Center Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None ├ 13. Rear Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None ├ 14. Left Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None ├ 15. Right Lock Controllers │ ├ 11a. Name : None │ └ 11b. Stages : None └ 16. Awd Clutches : None

### <span id="page-258-0"></span>**Abarth 695 Biposto**

├ 1. Traction Type : FWD ├ 2. Differential Data │ ├ 2a. Type : LSD │ ├ 2b. Power : 0.25000 │ ├ 2c. Coast : 0.25000 │ ├ 2d. Preload : 20.00000 │ ├ 2e. Front Share : 0.00000 │ ├ 2f. Torque Bias Ratio Power : 0.00000 │ ├ 2g. Torque Bias Ratio Coast : 0.00000 │ ├ 2h. Thermal Capacity : 0.00000 │ ├ 2i. Surface : 0.00000 │ ├ 2j. Heat Transfer Coeff : 0.00000 │ ├ 2k. Wear Factor : 0.00000

```
│ ├ 2l. Friction Reduction With T : 0.00000 
│ └ 2m. Friction Ref T : 0.00000 
├ 3. Four W D Differentials 
│ ├ 3a. Front Diff 
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
```

│ ├ 11a. Name : None │ └ 11b. Stages : None

├ 13. Rear Lock Controllers

│ ├ 11a. Name : None │ └ 11b. Stages : None

├ 14. Left Lock Controllers

│ ├ 11a. Name : None │ └ 11b. Stages : None

├ 15. Right Lock Controllers

│ ├ 11a. Name : None │ └ 11b. Stages : None ├ 16. Awd Clutches : None

# <span id="page-261-0"></span>**14. Gearbox [ .gearbox ]**

### <span id="page-261-1"></span>**A. Description**

Transmission ratios and shift behaviour: gear list (including reverse and neutral), final drive, up/down shift times, throttle cut during shifts, dual-clutch / H-pattern flags, downshift protection, autoblip, autoshifter thresholds, gearbox inertia, and optional gear fatigue stress parameters.

Clutch engagement curves live in .clutch. Diff and driven axles live in .drivetrain. This asset decides what ratio sits between engine and final drive, and how long / how violently a gear change interrupts torque.

Official Description prose in the source dump is unfinished placeholder text. Content below follows the schema and examples.

### <span id="page-261-2"></span>**I. Role in the stack**

| Concern                                | Handled here                            | Handled elsewhere                 |
|----------------------------------------|-----------------------------------------|-----------------------------------|
| Pear-gear ratios (+ R / N)             | Gears[x]                                | —                                 |
| Final drive                            | Final Ratio                             | —                                 |
| Shift duration / throttle cut          | Up/Dn time, Auto Cut Off, Gas<br>Cut Of | Clutch autoclutch profiles        |
| Dual clutch / H-shifter support        | Flags                                   | Controls bindings                 |
| Overrev / neutral lock on<br>downshift | Downshift Protection                    | —                                 |
| Autoblip / auto shift assists          | Autoblip, Autoshifter                   | .curve profiles                   |
| Spinning gearbox inertia               | Gearbox Inertia                         | Engine / clutch inertia elsewhere |
| Which file loads                       | —                                       | .car / .tuningpart path           |

### <span id="page-261-3"></span>**II. What you are really tuning**

- 1. **Ratio stack** *Gear Count* is the number of forward gears. *Gears[x]* always lists named slots with ratios — examples include *R* (negative), N (0), then 1…n. Cayman GT4 CS MR: 6-speed with R −3.55 through 6th 0.881, final 3.72. Alpine A290 b: *Gear Count : 1* with only R / N / 1 and final 1.0 — singleratio / EV-style reduction. R5: classic 5-speed, final 3.73.
- 2. **Shift timing and cut** *Gear Up Time* / *Gear Dn Time* ( Cayman 30 / 80, Alpine 10 / 16, R5 250 / 270 — race DCT vs slow manual). *Auto Cut Of Time* and *Gas Cut Off Level* shape how much and how long throttle is pulled during automated cuts (Cayman cut level 0.7; Alpine/R5 level 0).
- 3. **Hardware personality** *Has Dual Clutch* (Cayman true; Alpine/R5 false). *Is Shifter Supported* (R5 true for H-pattern; paddle cars false). Together with shift times they separate sequential/DCT race boxes from three-pedal manuals.

- 4. **Downshift protection** *Is Active*, *Overrev* margin, *Lock N*. Cayman/Alpine active with overrev 300 / 100 and Lock N true — blocks suicidal downshifts. R5 inactive (0 / Lock N false) — period-correct "you can grenade it".
- 5. **Shift windows and inertia** *Damage Rpm Window*, *Valid Shift Rpm Window*, *Controls Window Gain* gate when a shift request is accepted vs damaging. *Gearbox Inertia* (Cayman 0.012, Alpine 0.008, R5 0.017) adds rotating mass in the box.
- 6. **Autoblip and auto shifter** Autoblip *Profile* path + *Is Electronic* (true on Cayman/Alpine, false on R5 — mechanical vs ECU blip). Autoshifter: *Up* RPM, down threshold, *Slip Threshold*, *Gas Cutoff Time* for assisted / AI-style shifting (Cayman up 7700, Alpine 6850, R5 6000).
- 7. **Fatigue (optional)** *Gears Fatigue Log10 A*, nominal torque, max/min stress present but zeroed in all three examples.

### <span id="page-262-0"></span>**III. Architecture**

### <span id="page-262-1"></span>**1 - RATIOS (SCHEMA 1-3)**

*Gear count; repeating Name/Ratio gears; final ratio.*

### <span id="page-262-2"></span>**2 - SHIFT ACTUATORS AND FLAGS (SCHEMA 4-9)**

Up/down times; auto cut-off time/level; dual clutch; shifter supported.

### <span id="page-262-3"></span>**3 - PROTECTION AND WINDOWS (SCHEMA 10-14)**

Downshift Protection object; damage / valid shift windows; controls gain; gearbox inertia.

### <span id="page-262-4"></span>**4 - ASSISTS AND FATIGUE (SCHEMA 15–20)**

Autoblip (profile + electronic flag — dump reuses 15a for both); Autoshifter; four fatigue floats.

### <span id="page-262-5"></span>**IV. How to read the examples**

### <span id="page-262-6"></span>**1 - PORSCHE 718 CAYMAN GT4 CS MR — RACE DCT STYLE**

6 forward gears, dual clutch, fast upshifts (30), slower downs (80), electronic autoblip, downshift protection on, shifter not supported. Autoshift up around 7700 RPM. Modern cup/GT transmission feel.

### <span id="page-262-7"></span>**2 - ALPINE A290B — SINGLE-SPEED / EV LAYOUT**

*Gear Count : 1*, tall ±9.0 R/1 ratios, final 1.0, very short shift times, no dual clutch, electronic autoblip still wired. Shows the schema working for non-H multi-gear ICE boxes.

### <span id="page-262-8"></span>**3 - RENAULT 5 GT TURBO — ANALOG MANUAL**

5-speed, long 250/270 shift times, dual clutch off, H-shifter supported, downshift protection off, nonelectronic autoblip curve, higher gearbox inertia (0.017). Classic hot-hatch: slow shifts, driver can overrev.

### <span id="page-263-0"></span>**V. Practical notes**

- Source Description section is placeholder ignore its spring/alignment headings.
- *Gear Count* counts forward gears; array length is larger because R and N are included.
- Shift time units look like milliseconds in race cars (30–80) vs hundreds for manuals keep consistency within a car, do not mix blindly across titles.
- Schema OCR duplicates Autoblip field id *15a* for both Profile path and *Is Electronic*.
- Tuning-part gearbox swaps (Datsun 5-speed, Supra drift) must stay paired with a compatible clutch file.
- Fatigue zeros mean "unused", not "indestructible by design" unless the rest of the damage model agrees.

### <span id="page-263-1"></span>**VI. Related assets**

- **3. Car [Data](#page-35-0)** *Gearbox Path*
- **• 10. [Clutch](#page-221-0)** couples/decouples during shifts; autoclutch profiles
- **• 4. Car [Engine](#page-87-0)** RPM band the ratios must match
- **13. [Drivetrain](#page-245-0)** after the final drive
- **8. Car [Tuning](#page-184-0) Parts** alternate .gearbox redirects

### <span id="page-263-2"></span>**B. Schema**

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
├ 9. Is Shifter Supported : boolean
├ 10. Downshift Protection : object
│ ├ 10a. Is Active : boolean
│ ├ 10b. Is Debug : boolean
│ ├ 10c. Overrev : integer
│ └ 10d. Lock N : boolean
├ 11. Damage Rpm Window : float
├ 12. Valid Shift Rpm Window : float
├ 13. Controls Window Gain : float
├ 14. Gearbox Inertia : float
├ 15. Autoblip : object
│ ├ 15a. Profile : float 
│ └ 15b. Is Electronic : boolean
├ 16. Autoshifter : object
│ ├ 16a. Up : integer
│ ├ 16b. Down Rpm Threshold : integer
```

│ ├ 16c. Slip Threshold : float │ └ 16d. Gas Cutoff Time : float ├ 17. Gears Fatigue Log10 A : float

├ 18. Gears Fatigue Nominal Torque : float

├ 19. Gears Fatigue Max Stress : float └ 20. Gears Fatigue Min Stress : float

### <span id="page-264-0"></span>**C. Measurement Units & Descriptions**

| ID  | Name                 | Unit of Measurement                | Description                                                                                                                      |
|-----|----------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Gear Count           | None ( Integer count )             | Number of forward/reverse gear<br>ratios configured (excludes R/N<br>slots in Gear Count; Porsche GT4:<br>6).                    |
| 2.  | Gears                | None ( Object array )              | Per-gear entries including reverse<br>(R), neutral (N), and numbered<br>forward ratios; each slot repeats<br>IDs 2a/2b.          |
| 2a. | Name                 | None ( String )                    | Gear label (R, N, 1, 2, …);<br>identifies reverse, neutral, and<br>forward gears in the ratio table.                             |
| 2b. | Ratio                | Ratio ( dimensionless )            | Internal gear ratio; negative for<br>reverse (e.g., -3.55 R), 0 for<br>neutral, positive for forward (3.909<br>1st Porsche GT4). |
| 3.  | Final Ratio          | Ratio ( dimensionless )            | Final-drive/differential ring-and<br>pinion multiplier applied after the<br>selected gear (e.g., 3.72461<br>Porsche GT4).        |
| 4.  | Gear Up Time         | ms ( Milliseconds )                | Upshift engagement duration;<br>lower values yield faster shifts (30<br>ms DCT Porsche, 250 ms Renault<br>5 manual).             |
| 5.  | Gear Dn Time         | ms ( Milliseconds )                | Downshift engagement duration;<br>often longer than upshift for rev<br>matching (80 ms Porsche, 16 ms<br>Alpine).                |
| 6.  | Auto Cut Off Time    | ms ( Milliseconds )                | Engine fuel/torque cut duration<br>during automated or semi<br>automated shifts.                                                 |
| 7.  | Gas Cut Off Level    | Ratio ( 0.0 - 1.0 )                | Fraction of throttle cut during shift<br>fuel interruption (0.7 Porsche DCT;<br>0 on single-speed Alpine).                       |
| 8.  | Has Dual Clutch      | None ( Boolean : True /<br>False ) | When true, gearbox uses a dual<br>clutch layout with overlapping shift<br>phases (Porsche GT4: true).                            |
| 9.  | Is Shifter Supported | None ( Boolean : True /<br>False ) | When true, H-pattern or sequential<br>shifter hardware input is supported<br>for manual shifts.                                  |

| ID   | Name                      | Unit of Measurement                 | Description                                                                                                         |
|------|---------------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 10.  | Downshift Protection      | None ( Object )                     | Anti-over-rev downshift protection<br>block preventing destructive<br>downshift RPM excursions.                     |
| 10a. | Is Active                 | None ( Boolean : True /<br>False )  | Master enable for downshift over<br>rev protection logic.                                                           |
| 10b. | Is Debug                  | None ( Boolean : True /<br>False )  | When true, exposes debug<br>telemetry for downshift protection<br>triggers.                                         |
| 10c. | Overrev                   | RPM ( Revolutions per minute<br>)   | Allowed RPM overshoot margin<br>before downshift is blocked (300<br>Porsche, 100 Alpine).                           |
| 10d. | Lock N                    | None ( Boolean : True /<br>False )  | When true, prevents accidental<br>departure from neutral without<br>clutch/shift validation.                        |
| 11.  | Damage Rpm Window         | RPM ( Revolutions per minute<br>)   | RPM band width used when<br>evaluating gearbox/drivetrain<br>damage from over-rev events (100<br>in examples).      |
| 12.  | Valid Shift Rpm<br>Window | RPM ( Revolutions per minute<br>)   | RPM tolerance window within<br>which a shift request is considered<br>valid (800 in examples).                      |
| 13.  | Controls Window Gain      | Dimensionless coeffi<br>cient       | Gain scaling driver shift-input<br>timing tolerance (0.4 across<br>example cars).                                   |
| 14.  | Gearbox Intertia          | kg·m² ( Kilogram square<br>meters ) | Rotational inertia of gears and<br>shafts; affects rev hang and shift<br>feel (0.012 Porsche, 0.017 Renault<br>5).  |
| 15.  | Autoblip                  | None ( Object )                     | Throttle-blip profile block for<br>downshift rev-matching on<br>manual/semi-auto setups.                            |
| 15a. | Profile                   | None ( .curve file path )           | Autoblip throttle envelope curve<br>(e.g., 718_gt4_autoblip.curve);<br>schema types float but examples<br>use path. |
| 15b. | Is Electronic             | None ( Boolean : True /<br>False )  | When true, autoblip is applied<br>electronically via ECU/throttle<br>actuation rather than pedal<br>coaching.       |
| 16.  | Autoshifter               | None ( Object )                     | Automated upshift/downshift<br>assist thresholds for sequential or<br>auto modes.                                   |
| 16a. | Up                        | RPM ( Revolutions per minute<br>)   | Engine RPM threshold triggering<br>upshift in autoshifter mode (7700<br>Porsche, 6850 Alpine).                      |
| 16b. | Down Rpm Threshold        | RPM ( Revolutions per minute<br>)   | RPM threshold below which<br>downshift is requested (0 =<br>disabled in examples).                                  |

| ID   | Name                            | Unit of Measurement                           | Description                                                                                      |
|------|---------------------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------------|
| 16c. | Slip Threshold                  | Ratio ( 0.0 - 1.0 )                           | Wheel-slip ratio threshold influencing autoshifter shift decisions (0.96 Porsche, 0.95 Alpine).  |
| 16d. | Gas Cutoff Time                 | s ( Seconds )                                 | Duration of throttle cut during autoshifter shifts (0.063 s Porsche, 0.15 s Alpine).             |
| 17.  | Gears Fatigue Log10 A           | Dimensionless coefficient (log10 coefficient) | Log10 fatigue curve coefficient A for gear tooth stress accumulation (0 = disabled in examples). |
| 18.  | Gears Fatigue Nominal<br>Torque | Nm ( Newton-meters )                          | Reference torque level for gear fatigue life calculations.                                       |
| 19.  | Gears Fatigue Max<br>Stress     | Pa or N (Stress threshold)                    | Upper stress bound for gear fatigue degradation modeling.                                        |
| 20.  | Gears Fatigue Min<br>Stress     | Pa or N (Stress threshold)                    | Lower stress bound below which gear fatigue accumulation is negligible.                          |

### <span id="page-266-0"></span>D. Example data

### <span id="page-266-1"></span>I. Chosen Cars for Example

- Porsche 718 Cayman GT4 CS MR ( slug : ks\_porsche\_718\_cayman\_gt4\_cs\_mr )
- Alpine A290 b (slug: ks\_alpine\_a290\_b)
- Renault 5 GT Turbo (slug: ks\_renault\_5\_gt\_turbo)

#### <span id="page-266-2"></span>II. Example

### <span id="page-266-3"></span>Porsche 718 Cayman GT4 CS MR

- 1. Gear Count : 6
- 2. Gears 1

2. Gears 6 |- 2a. Name : 4

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
│ └ 15b. Is Electronic : true 
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

### <span id="page-267-0"></span>**Alpine A290 b**

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
│ └ 15b. Is Electronic : true 
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

### <span id="page-268-0"></span>**Renault 5 GT Turbo**

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
│ └ 15b. Is Electronic : false 
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

# <span id="page-270-0"></span>**15. General [ .generalcar ]**

### <span id="page-270-1"></span>**A. Description**

Standalone "chassis identity" block: display name, total mass, fuel tank and fuel economy, body box, pickup heights, ride-height rule flags, torsional stiffness/damping, and optional body-mesh offset.

It is the same field set as the **General** object embedded inside **3. Car Data** (.car), exposed as its own asset type so a car can optionally load it via *General Path* instead of (or as an override for) the inline General object.

Official Description prose in the source dump is unfinished placeholder text. The example section states explicitly that **no shipped car or common asset currently uses a** .generalcar **file** — all practical values live inline in Car Data with *General Path : None*.

### <span id="page-270-2"></span>**I. Role in the stack**

| Concern                                | Handled here       | Handled elsewhere                |
|----------------------------------------|--------------------|----------------------------------|
| Screen name, mass, fuel, tank          | .generalcar fields | .car → General object            |
| Body box / pickup heights              | .generalcar        | Same inline General              |
| Check rules / minimum height           | .generalcar        | Same inline General              |
| Chassis torsion pair                   | .generalcar        | Same inline General              |
| Body mesh offset                       | .generalcar        | Same inline General              |
| Which general block loads              | —                  | .car General Path                |
| Wheelbase, tracks, CG, module<br>paths | —                  | Rest of .car (not in this asset) |

Think of .generalcar as an extractable shared fragment — useful for tooling or multi-car inheritance — not as a second physics domain.

### <span id="page-270-3"></span>**II. What you are really tuning**

- 1. **Identity and mass** *Screen Name* for UI. *Total Mass* is the F=ma baseline (in Car Data examples: R5 about 910 kg, R8 GT3 about 1355 kg, 296 GTB about 1750 kg).
- 2. **Fuel payload** *Tank Position* (x,y,z), *Fuel* / *Max Fuel*, *Efficiency*, *Kg Per Liter*. Changing fuel changes mass and CG over a stint — same behaviour whether authored inline or via this asset.
- 3. **Body envelope and pickups** *Body Box Sizes* (x,y,z), *Pickup Front Height* / *Pickup Rear Height* collision / jack / reference heights tied to the body, not suspension hardpoints.
- 4. **Regulatory floor** *Check Rules* + *Minimum Height* enable ride-height legality checks when true (race cars in Car Data examples); road cars often leave checks off.
- 5. **Chassis beam** *Torsional Stiffness* / *Torsional Damping* soft shells twist (R5 about 11000 stiffness in Car Data); stiff tubs stay flatter (R8 about 40000).

6. **Mesh alignment** — Body Mesh Offset → Position / Rotation / Scale — visual/collider mesh placement relative to the physics body.

### <span id="page-271-0"></span>**III. Architecture**

### <span id="page-271-1"></span>**1 - CORE SCALARS (SCHEMA 1-14)**

*Screen name; mass; tank and fuel block; body box; pickup heights; check rules; minimum height; torsional stiffness and damping.*

### <span id="page-271-2"></span>**2 - MESH OFFSET (SCHEMA 15)**

Nested Position / Rotation / Scale vectors.

Field order matches Car Data *General* leaves (*2a*…*2o*), flattened to top-level 1…15 in this asset type.

### <span id="page-271-3"></span>**IV. How to read the examples**

### <span id="page-271-4"></span>**1 - SOURCE STATEMENT**

No cars or common assets use an asset of the "generalcar" type.

There is no vehicle dump to walk through for this file. Treat the schema as the contract; treat **Car Data → General** dumps as the living examples of the same numbers.

### <span id="page-271-5"></span>**2 - PRACTICAL READING VIA CAR DATA**

| Car Data example       | What the General block shows                                             |
|------------------------|--------------------------------------------------------------------------|
| Ferrari 296 GTB        | Mass 1750, torsional stiffness 30000, large tank,<br>General Path : None |
| Audi R8 LMS GT3 Evo II | Mass 1355, stiffness 40000, rules/min height used,<br>path None          |
| Renault 5 GT Turbo     | Mass 910, soft shell about 11000, path None                              |

If a future car sets *General Path* to a .generalcar file, expect those fields to supply (or replace) the inline General object — verify in-session which layer wins.

### <span id="page-271-6"></span>**V. Practical notes**

- Source Description section is placeholder ignore spring/alignment headings.
- Do not invent a .generalcar dependency for current ACE cars; shipped content keeps everything in .car.
- Duplicating mass/fuel here **and** inline without a clear Path policy will confuse authors pick one source of truth per vehicle.

- Extension name in the doc title is .generalcar; Car Data only exposes *General Path* (string). Match whatever on-disk extension the toolchain actually writes.
- Editing torsion or mass for handling work still means editing Car Data General today.

### <span id="page-272-0"></span>**VI. Related assets**

- **3. Car [Data](#page-35-0)** owns inline General today; optional *General Path* consumer
- **• 5. Car [Setup](#page-102-0)** session fuel load overlays Max Fuel capacity defined here / in General
- **• 11 / 17. [Coilover](#page-226-0) / [Suspension](#page-286-0)** ride and kinematics; not substitutes for torsional stiffness

### <span id="page-272-1"></span>**B. Schema**

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
├ 11. Check Rules : boolean
├ 12. Minimum Height : float
├ 13. Torsional Stiffness : float
├ 14. Torsional Damping : float
├ 15. Body Mesh Offset : object
│ ├ 15a. Position : x, y, z float
│ ├ 15b. Rotation : x, y, z float
└ └ 15c. Scale : x, y, z float
```

### <span id="page-272-2"></span>**C. Measurement Units & Descriptions**

| ID | Name          | Unit of Measurement     | Description                                                                                                                  |
|----|---------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 1. | Screen Name   | None ( String )         | Human-readable label for<br>this .generalcar profile in editor or<br>UI tooling; does not affect physics.                    |
| 2. | Total Mass    | Kg ( Kilograms )        | Baseline vehicle mass including<br>driver and fluids; fundamental input<br>for weight transfer and inertia (Car<br>Data 2b). |
| 3. | Tank Position | m ( Meters, X / Y / Z ) | 3D coordinates of the fuel tank<br>centroid relative to the vehicle<br>reference frame (Car Data 2c).                        |
| 4. | Fuel          | L ( Liters )            | Starting fuel volume at session<br>load; reduces mass and shifts CG<br>as fuel burns (Car Data 2d).                          |

| ID   | Name                | Unit of Measurement                        | Description                                                                                                               |
|------|---------------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| 5.   | Max Fuel            | L ( Liters )                               | Maximum fuel tank capacity;<br>upper bound for fuel load and<br>endurance calculations (Car Data<br>2e).                  |
| 6.   | Effi<br>ciency      | Dimensionless ratio                        | Fuel consumption effi<br>ciency<br>modifier applied to engine burn<br>calculations (Car Data 2f).                         |
| 7.   | Kg Per Liter        | kg/L ( Kilograms per liter )               | Fuel density factor converting<br>volumetric fuel into mass for<br>physics updates (Car Data 2g).                         |
| 8.   | Body Box Sizes      | m ( Meters, X / Y / Z )                    | Axis-aligned bounding box<br>dimensions of the chassis body<br>envelope for regulatory/collision<br>checks (Car Data 2h). |
| 9.   | Pickup Front Height | m ( Meters )                               | Vertical pickup/reference height at<br>the front axle; aligns suspension<br>hardpoints (Car Data 2i).                     |
| 10.  | Pickup Rear Height  | m ( Meters )                               | Vertical pickup/reference height at<br>the rear axle (Car Data 2j).                                                       |
| 11.  | Check Rules         | None ( Boolean : True /<br>False )         | When true, enables automated<br>regulatory validation such as<br>minimum ride height (Car Data 2k).                       |
| 12.  | Minimum Height      | m ( Meters )                               | Regulatory minimum ride-height<br>threshold enforced when Check<br>Rules is active (Car Data 2l).                         |
| 13.  | Torsional Sitffness | Nm/rad or N/m ( Torsional<br>spring rate ) | Chassis torsional spring rate<br>resisting twist between front and<br>rear axles (Car Data 2m).                           |
| 14.  | Torsional Damping   | Nm·s/rad ( Torsional damping<br>)          | Chassis torsional damping<br>coeffi<br>cient dissipating body twist<br>oscillations (Car Data 2n).                        |
| 15.  | Body Mesh Offset    | None ( Object )                            | Visual/collision body mesh<br>alignment block relative to the<br>physics origin (Car Data 2o).                            |
| 15a. | Position            | m ( Meters, X / Y / Z )                    | Translation offset of the body<br>mesh from the physics origin (Car<br>Data 2o1).                                         |
| 15b. | Rotation            | deg or rad ( X / Y / Z )                   | Euler rotation offset applied to the<br>body mesh for model alignment<br>(Car Data 2o2).                                  |
| 15c. | Scale               | Dimensionless ( X / Y / Z )                | Non-uniform scale factor on the<br>body mesh offset block (Car Data<br>2o3).                                              |

### <span id="page-274-0"></span>**D. Example data**

### <span id="page-274-1"></span>**I. Chosen Cars for Example**

No cars or common assets use an asset of the "generalcar" type.

# <span id="page-275-0"></span>**16. Surface 3D [ .surface3d ]**

### <span id="page-275-1"></span>**A. Description**

Transmission ratios and shift behaviour: gear list (including reverse and neutral), final drive, up/down shift times, throttle cut during shifts, dual-clutch / H-pattern flags, downshift protection, autoblip, autoshifter thresholds, gearbox inertia, and optional gear fatigue stress parameters.

Clutch engagement curves live in .clutch. Diff and driven axles live in .drivetrain. This asset decides what ratio sits between engine and final drive, and how long / how violently a gear change interrupts torque.

Official Description prose in the source dump is unfinished placeholder text. Content below follows the schema and examples.

### <span id="page-275-2"></span>**I. Role in the stack**

| Concern                        | Handled here              | Handled elsewhere              |
|--------------------------------|---------------------------|--------------------------------|
| Cd / Cl (or CX / CZ)           | Interpolation table       | —                              |
| Axis span and grid density     | min/max + size front/rear | —                              |
| Optional secondary height LUTs | Downforce h/dh mm paths   | Usually None in samples        |
| Denser runtime interp cache    | Interp Map when done      | —                              |
| CSV authoring import/export    | Import/export paths       | Tooling only                   |
| Which maps the car uses        | —                         | .car Aero paths / tuning parts |
| Wing angles / element gains    | —                         | .wing, setup aero              |
| Session ride heights           | —                         | .carsetup Aero targets         |

Typical triplet per car: one drag (CX) map + front lift/downforce (CZ) + rear lift/downforce (CZ).

### <span id="page-275-3"></span>**II. What you are really tuning**

- 1. **The lookup axes** *min* / *max* front and rear plus *size front* / *size rear* define the grid. Table headers are the sampled axis values (Mercedes drag about 65–160 on both axes; R8 CX/CZ front 30–80 with 6 samples, rear 30–100 with 8). Outside the span the runtime must clamp or extrapolate — keep setup ride heights inside the map.
- 2. **Coefficient cells** Each cell is the aero coefficient at that front/rear pairing. Reading a row = fixed front state while rear varies (columns). R8 rear CZ rises strongly as front height drops (more front rake / lower nose → big rear load in that map). Drag maps often rise when both ends sit high (Mercedes highhigh corner about 0.67 vs diagonal mid about 0.46).
- 3. **Naming conventions** Same schema, different filenames/roles:

| Role                 | Example filenames                           |  |  |  |
|----------------------|---------------------------------------------|--|--|--|
| Front downforce / CZ | front_downforce, frontczmap, front_lift_map |  |  |  |
| Rear downforce / CZ  | rear_downforce, rearczmap, rear_lift_map    |  |  |  |

"Lift" vs "downforce" in the filename is authoring vocabulary — sign and magnitude live in the cell values.

- 4. **Interpolation bookkepping** *interpolation done* true + filled *Interp Map* (min/max val, resolution front/ rear) marks a denser baked interp (Mercedes front/rear DF and all R8 maps: resolution 18×18, val span −0.5…2.0). Raw grids with *interpolation done : false* and *Interp Map : None* (Mercedes drag, Dallara maps) rely on the coarse table alone.
- 5. **Tooling fields** *Downforce h mm* / *dh mm* paths, CSV import/export, *Import front* / *Import range x y* — authoring hooks. All examples leave paths *None* and import flags false.

### <span id="page-276-0"></span>**III. Architecture**

### <span id="page-276-1"></span>**1 - OPTIONAL LINKED CURVES (SCHEMA 1-2)**

Paths for height / delta-height downforce helpers (unused in samples).

### <span id="page-276-2"></span>**2 - GRID DEFINITION (SCHEMA 3-8)**

Integer sizes (0–30); float min/max per axis.

### <span id="page-276-3"></span>**3 - TABLE AND INTERP (SCHEMA 9-11)**

Interpolation table of size rear × size front; interpolation done; optional Interp Map object.

### <span id="page-276-4"></span>**4 - CSV / IMPORT (SCHEMA 12-15)**

Booleans and paths for bulk edit workflows.

### <span id="page-276-5"></span>**IV. How to read the examples**

### <span id="page-276-6"></span>**1 - MERCEDES AMG GT2 — SYMMETRIC 8X8 PACK**

Three files: drag, front downforce, rear downforce. Drag left at coarse interp; DF maps baked to 18×18. Drag diagonal soft mid values; high-high corner climbs. Rear DF axis spans much taller (about 2–288) than front (about 20–154) — rear map covers a wider operating window.

### <span id="page-276-7"></span>**2 - AUDI R8 LMS GT3 EVO 2 — CX / CZ RACE MAPS**

Wired from Car Data as *Drag* → *cxmap*, *Front Lift* → *frontczmap*, *Rear Lift* → *rearczmap*. Shared 6×8 rideheight window (F 30–80, R 30–100). CX stays about 1.04–1.16; front CZ collapses toward 0 as front height rises; rear CZ sits about 1.8–2.6. Classic GT3 platform sensitivity to ride height.

### <span id="page-276-8"></span>**3 - DALLARA STRADALE COUPE — COARSER ROAD/TRACK PACK**

7 rear × 4 front, axes 60–120. Drag and front lift tables are numerically identical in the dump (likely shared/ placeholder front map — verify before trusting). Rear lift is distinct and higher (about 1.4–2.1). All three leave interp undone.

### <span id="page-277-0"></span>**V. Practical notes**

- Source Description section is placeholder ignore spring/alignment headings.
- Table size must match *size front* × *size rear*; a mismatched CSV import is a silent footgun.
- Keep garage ride-height limits inside min/max or the car runs off-map.
- Editing one map without the sibling CX/CZ pair breaks aero balance even if numbers "look fine" in isolation.
- Filename "lift" does not imply positive lift read cell signs against how Car Data gains multiply them.
- OCR can corrupt edge cells (e.g. truncated decimals); prefer re-export from source assets when numbers look broken.

### <span id="page-277-1"></span>**VI. Related assets**

- **3. Car [Data](#page-35-0)** Aero Front Lift / Rear Lift / Drag paths
- **• 20. [Wing](#page-328-0)** discrete wing elements referenced beside these maps
- **• 5 / 6. Car [Setup](#page-102-0) / [Limits](#page-118-0)** ride height and wing angles that feed the axes
- **8. Car [Tuning](#page-184-0) Parts** aero package redirects that can swap these maps

### <span id="page-277-2"></span>**B. Schema**

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
├ 10. interpolation done : boolean
├ 11. Interp Map : object 
│ ├ 11a. min val : float
│ ├ 11b. max val : float
│ ├ 11c. resolution front : range integer ( 3 - 90 )
│ └ 11d. resolution rear : range integer ( 3 - 90 )
├ 12. Import front : boolean
├ 13. Import range x y : boolean
├ 14. CSV import path : string - path
└ 15. CSV export name : string - path
```

### <span id="page-278-0"></span>**C. Measurement Units & Descriptions**

| ID   | Name                | Unit of Measurement                            | Description                                                                                                                                   |  |  |
|------|---------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| 1.   | Downforce h mm      | None ( File path )                             | Optional source height map<br>defining absolute ride-height<br>reference for aero lookup (often<br>None; Mercedes drag map).                  |  |  |
| 2.   | Downforce dh mm     | None ( File path )                             | Optional delta ride-height map<br>layered on Downforce h mm for<br>dynamic aero offset (often None).                                          |  |  |
| 3.   | Size rear           | Integer count ( 0 - 30 )                       | Rear-axis grid resolution of the 2D<br>interpolation table (rows; e.g., 8 on<br>Mercedes/Audi GT3 maps).                                      |  |  |
| 4.   | Size front          | Integer count ( 0 - 30 )                       | Front-axis grid resolution of the<br>interpolation table (columns; e.g.,<br>6–8).                                                             |  |  |
| 5.   | Min rear            | mm ( Millimeters )                             | Minimum rear ride-height sample<br>bound for table axis (e.g., 65.338<br>mm Mercedes drag, 30 mm Audi<br>Cx).                                 |  |  |
| 6.   | Max rear            | mm ( Millimeters )                             | Maximum rear ride-height sample<br>bound for table axis (e.g., 160.227<br>mm Mercedes drag).                                                  |  |  |
| 7.   | Min front           | mm ( Millimeters )                             | Minimum front ride-height sample<br>bound for table axis.                                                                                     |  |  |
| 8.   | Max front           | mm ( Millimeters )                             | Maximum front ride-height sample<br>bound for table axis.                                                                                     |  |  |
| 9.   | Interpolation Table | Dimensionless coeffi<br>cient<br>( 2D matrix ) | size rear × size front lookup of<br>aero coeffi<br>cients (Cd, Cl, Cz) vs.<br>front/rear ride height; schema ID<br>shown as (9). in examples. |  |  |
| 10.  | Interpolation done  | None ( Boolean : True /<br>False )             | When true, raw table data has<br>been processed into the Interp<br>Map representation (true on<br>downforce maps).                            |  |  |
| 11.  | Interp Map          | None ( Object )                                | Baked interpolation map metadata<br>block derived from the table (None<br>when using raw matrix only).                                        |  |  |
| 11a. | Min val             | Dimensionless coeffi<br>cient                  | Lower clamp of interpolated aero<br>coeffi<br>cient output (e.g., -0.500).                                                                    |  |  |
| 11b. | Max val             | Dimensionless coeffi<br>cient                  | Upper clamp of interpolated aero<br>coeffi<br>cient output (e.g., 2.000).                                                                     |  |  |
| 11c. | Resolution front    | Integer count ( 3 - 90 )                       | Front-axis resolution of the baked<br>interpolation map (18 on<br>processed GT3/GT2 maps).                                                    |  |  |
| 11d. | Resolution rear     | Integer count ( 3 - 90 )                       | Rear-axis resolution of the baked<br>interpolation map (18 in<br>examples).                                                                   |  |  |

| ID  | Name             | Unit of Measurement           | Description                                                                                       |  |
|-----|------------------|-------------------------------|---------------------------------------------------------------------------------------------------|--|
| 12. | Import front     | None (Boolean : True / False) | When true, front-axis data is imported from an external source rather than edited inline.         |  |
| 13. | Import range x y | None (Boolean : True / False) | When true, imports axis range bounds from external CSV/tooling rather than manual min/max fields. |  |
| 14. | CSV Import path  | None (File path)              | Path to a CSV file for bulk table import; often None when table is authored in-editor.            |  |
| 15. | CSV export name  | None (File path or string)    | Target path or filename for CSV export of the interpolation table; often None.                    |  |

### <span id="page-279-0"></span>D. Example data

### <span id="page-279-1"></span>I. Chosen Cars for Example

- Mercedes AMG GT2 (slug: ks\_mercedes\_amg\_gt2) [3 surface 3d]
- Audi R8 LMS GT3 Evo 2 (slug: ks\_audi\_r8\_lms\_gt3\_evo\_2) [3 surface 3d]
- Dallara Stradale Coupe (slug: ks\_dallara\_stradale\_coupe) [3 surface 3d]

### <span id="page-279-2"></span>II. Example

#### <span id="page-279-3"></span>**Mercedes AMG GT2**

### 1. Drag map (file: drag\_map.surface3d)

- 1. Downforce h mm : None - 2. Downforce dh mm : None

- 3. size rear : 8 - 4. size front : 8 - 5. min rear : 65.338 - 6. max rear : 160.227 - 7. min front : 65.338 - 8. max front : 160.227 - (9). Interpolation Table

| Front v /<br>Rear | 65.3  | 78.9  | 92.4  | 106.0 | 119.6 | 133.1 | 146.7 | 160.2 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 65.3              | 0.454 | 0.475 | 0.487 | 0.498 | 0.509 | 0.539 | 0.579 | 0.671 |
| 78.9              | 0.487 | 0.456 | 0.476 | 0.489 | 0.506 | 0.522 | 0.545 | 0.582 |
| 92.4              | 0.515 | 0.489 | 0.457 | 0.478 | 0.497 | 0.519 | 0.528 | 0.548 |
| 106.0             | 0.540 | 0.516 | 0.490 | 0.459 | 0.486 | 0.510 | 0.525 | 0.531 |
| 119.6             | 0.556 | 0.541 | 0.518 | 0.492 | 0.467 | 0.499 | 0.516 | 0.528 |

| Front v /<br>Rear | 65.3  | 78.9  | 92.4  | 106.0 | 119.6 | 133.1 | 146.7 | 160.2 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 133.1             | 0.572 | 0.557 | 0.542 | 0.520 | 0.500 | 0.480 | 0.505 | 0.519 |
| 146.7             | 0.597 | 0.573 | 0.558 | 0.545 | 0.528 | 0.513 | 0.486 | 0.508 |
| 160.2             | 0.642 | 0.599 | 0.574 | 0.561 | 0.553 | 0.541 | 0.519 | 0.489 |

├ 10. interpolation done : false

├ 11. Interp Map : None ├ 12. Import front : false ├ 13. Import range x y : false

├ 14. CSV import path : None └ 15. CSV export name : None

### *2. Front downforce ( file : front\_downforce.surface3d )*

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

├ 14. CSV import path : None └ 15. CSV export name : None

### *3. Rear downforce ( file : rear\_downforce.surface3d )*

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

├ 13. Import range x y : false

├ 14. CSV import path : None

└ 15. CSV export name : None

### <span id="page-281-0"></span>**Audi R8 LMS GT3 Evo 2**

### *1. CX Map ( file : cxmap.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

├ 3. size rear : 8 ├ 4. size front : 6 ├ 5. min rear : 30.000 ├ 6. max rear : 100.000 ├ 7. min front : 30.000

| Front v /<br>Rear | 30.0  | 40.0  | 50.0  | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 30.0              | 1.041 | 1.049 | 1.051 | 1.054 | 1.057 | 1.061 | 1.065 | 1.068 |
| 40.0              | 1.076 | 1.080 | 1.080 | 1.078 | 1.080 | 1.085 | 1.089 | 1.092 |
| 50.0              | 1.092 | 1.104 | 1.108 | 1.113 | 1.121 | 1.119 | 1.123 | 1.127 |
| 60.0              | 1.098 | 1.110 | 1.119 | 1.127 | 1.129 | 1.137 | 1.141 | 1.145 |
| 70.0              | 1.110 | 1.123 | 1.131 | 1.140 | 1.141 | 1.145 | 1.152 | 1.153 |
| 80.0              | 1.120 | 1.134 | 1.141 | 1.146 | 1.149 | 1.152 | 1.158 | 1.164 |

├ 10. interpolation done : true

├ 11. Interp Map

│ ├ 11a. min val : -0.500 │ ├ 11b. max val : 2.000

│ ├ 11c. resolution front : 18 │ └ 11d. resolution rear : 18 ├ 12. Import front : false ├ 13. Import range x y : false

├ 14. CSV import path : None └ 15. CSV export name : None

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

├ 10. interpolation done : true ├ 11. Interp Map │ ├ 11a. min val : -0.500 │ ├ 11b. max val : 2.000 │ ├ 11c. resolution front : 18 │ └ 11d. resolution rear : 18 ├ 12. Import front : false ├ 13. Import range x y : false ├ 14. CSV import path : None └ 15. CSV export name : None

### *3. Rear CZ Map ( file : rearczmap.surface3d )*

├ 2. Downforce dh mm : None ├ 3. size rear : 8 ├ 4. size front : 6 ├ 5. min rear : 30.000 ├ 6. max rear : 100.000 ├ 7. min front : 30.000 ├ 8. max front : 80.000 ├ (9). Interpolation Table

├ 1. Downforce h mm : None

| Front v /<br>Rear | 30.0  | 40.0  | 50.0  | 60.0  | 70.0  | 80.0  | 90.0  | 100.0 |
|-------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 30.0              | 1.927 | 2.011 | 2.026 | 1.953 | 1.905 | 1.892 | 1.859 | 1.823 |
| 40.0              | 2.085 | 2.122 | 2.125 | 2.074 | 2.015 | 1.965 | 1.917 | 1.871 |
| 50.0              | 2.267 | 2.262 | 2.240 | 2.191 | 2.124 | 2.053 | 1.992 | 1.934 |
| 60.0              | 2.428 | 2.407 | 2.365 | 2.299 | 2.227 | 2.151 | 2.080 | 2.005 |
| 70.0              | 2.542 | 2.513 | 2.464 | 2.395 | 2.316 | 2.232 | 2.156 | 2.079 |
| 80.0              | 2.633 | 2.591 | 2.539 | 2.481 | 2.401 | 2.305 | 2.217 | 2.138 |

├ 10. interpolation done : true ├ 11. Interp Map │ ├ 11a. min val : -0.500 │ ├ 11b. max val : 2.000 │ ├ 11c. resolution front : 18 │ └ 11d. resolution rear : 18 ├ 12. Import front : false ├ 13. Import range x y : false ├ 14. CSV import path : None └ 15. CSV export name : None

### <span id="page-283-0"></span>**Dallara Stradale Coupe**

### *1. Drag map ( file : drag\_map.surface3d )*

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

### *2. Front lift map ( file : front\_lift\_map.surface3d )*

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

### *3. Rear lift map ( file : rear\_lift\_map.surface3d )*

├ 1. Downforce h mm : None ├ 2. Downforce dh mm : None

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

# <span id="page-286-0"></span>**17. Suspension [ .suspension ]**

### <span id="page-286-1"></span>**A. Description**

Kinematic hardpoint package for one axle (or corner family): hub mass, baseline camber/toe linear, rim offset, plus exactly one filled geometry topology (strut, double wishbone, trailing arm, multilink, axle, etc.).

Coilover rates and dampers live in .coilover. Garage camber/toe/pressure live in .carsetup. This file decides how the upright moves through travel and steer — motion ratios, camber gain, bump steer — via pickup coordinates.

Official Description prose in the source dump is unfinished placeholder text. Content below follows the schema and examples.

### <span id="page-286-2"></span>**I. Role in the stack**

| Concern                                              | Handled here             | Handled elsewhere         |  |
|------------------------------------------------------|--------------------------|---------------------------|--|
| Hub / upright mass                                   | Basic Data               | —                         |  |
| Baseline static camber / toe-out<br>linear           | Basic Data               | Setup alignment overlays  |  |
| Rim offset                                           | Basic Data               | —                         |  |
| Wishbone / strut / trailing /<br>multilink / pickups | Topology objects 2-9     | —                         |  |
| Coilover attach points (when in<br>geometry)         | Dw Coil / Multi Link New | Spring rates in .coilover |  |
| Wheelbase, track, CG                                 | —                        | .car Suspensons hub       |  |
| Which front/rear files load                          | —                        | .car / .tuningpart paths  |  |

One .suspension file per axle side of the architecture (front file + rear file; optional drift variants).

### <span id="page-286-3"></span>**II. What you are really tuning**

- 1. **Basic hub identity** Always filled: *Hub Mass*, *Toe Out Linear*, *Static Camber*, *Rim Offset*. Golf front hub 50 kg / camber −0.3°; S2000 front 37 kg / −0.4° with rim offset 0.045; Porsche GT3 R front 51 kg / camber −5.7° — race baseline geometry, not a mild road setup.
- 2. **One topology wins** Only one of the geometry blocks should be non-None. The schema lists every layout; authors fill the matching family:

| Block    | Typical layout                                |
|----------|-----------------------------------------------|
| D W Data | Double wishbone (top/bottom car+tyre + steer) |
| Strut    | MacPherson strut + lower wishbone + steer     |
| Strut Ml | Strut multilink (adds thrust balls/arm)       |

| Block               | Typical layout                                           |
|---------------------|----------------------------------------------------------|
| Axle                | Live/beam axle links, leak K, torque reaction            |
| Multi Link Data     | Older joint-car / joint-tyre arrays                      |
| Trailing Arm Data   | Trailing arm hinges + upright + steer                    |
| Multi Link New Data | Named links/arms, coilover flags, toe link               |
| Dw Coil Data        | Double wishbone + explicit car/bottom coilover<br>points |

- 3. **Coordinate pickups** All hardpoints are *x, y, z* in the car/tyre frames used by the toolchain (car-side vs tyre-side pairs). Moving a pickup changes instantaneous centre, roll centre, camber gain, and bump steer — more sensitive than tweaking a spring rate.
- 4. **Coilover attachment in geometry** *Dw Coil Data* and *Multi Link New* expose *Car Coilover* / *Bottom Coilover* (and per-link *Has Coilover Attached*). That is where the damper unit sits in space relative to the links — motion ratio comes from this geometry + coilover rates.
- 5. **Variant packs** Same Basic Data with relocated DW pickups = alternate kinematics without a new spring file (S2000 stock front vs front drift: top mounts lowered in Y, steer/tyre points shifted). Tuning parts can redirect geometry paths the same way.

### <span id="page-287-0"></span>**III. Architecture**

### <span id="page-287-1"></span>**1 - BASIC DATA (SCHEMA 1)**

Hub mass, toe-out linear, static camber, rim offset.

### <span id="page-287-2"></span>**2 - LEGACY / CLASSIC TOPOLOGIES (SCHEMA 2-7)**

DW Data; Strut; Strut Ml; Axle; Multi Link Data; Trailing Arm Data.

### <span id="page-287-3"></span>**3 - MODERN MULTILINK AND DW+COIL (SCHEMA 8-9)**

Multi Link New: Links (ball car/tyre, coilover flag, Is Toe) and Arms (two car balls + tyre ball); coilover car/ bottom points. Dw Coil Data: full DW set plus coilover pickups.

### <span id="page-287-4"></span>**IV. How to read the examples**

### <span id="page-287-5"></span>**1 - VOLKSWAGEN GOLF GTI MK1 — STRUT FRONT / TRAILING REAR**

Front fills **Strut** (classic Mk1 MacPherson). Rear fills **Trailing Arm Data** (Steer Link To Body : false). All other topology blocks None. Period road-car architecture, mild static cambers.

### <span id="page-287-6"></span>**2 - HONDA S2000 AP1 — DOUBLE WISHBONE + DRIFT FRONT**

Stock front and rear use **D W Data**. Extra *front\_drift* file keeps the same hub/camber/rim basics but relocates upper mounts and steer points — geometry-only drift package. OCR note: the rear dump header incorrectly reuses the drift front filename; treat content (hub 44.5, camber −1.6, DW points) as the rear axle.

### <span id="page-288-0"></span>**3 - PORSCHE 992 GT3 R RENNSPORT — DW COIL FRONT / MULTILINK REAR**

Front uses **Dw Coil Data** (wishbones + coilover car/bottom). Rear uses **Multi Link New Data** with five links (one named *steer* with *Is Toe : true*, one with coilover attached) and explicit coilover points. Aggressive static camber (−5.7 / −4.4). Modern GT race pattern.

### <span id="page-288-1"></span>**V. Practical notes**

- Source Description section is placeholder ignore spring/alignment headings.
- Filling two topology blocks in one file is a content bug; leave unused families *None*.
- Setup camber/toe adjust on top of *Static Camber* / *Toe Out Linear* do not double-count when comparing cars.
- Drift / geometry tuning parts must point at real .suspension files; swapping only coilovers will not change roll centres.
- OCR can garble coordinates (e.g. *-010540*); prefer re-reading source assets when a point looks impossible.
- Rim offset changes scrub/track feel without touching Car Data track width keep both consistent.

### <span id="page-288-2"></span>**VI. Related assets**

- **3. Car [Data](#page-35-0)** front/rear suspension paths, wheelbase/track/CG
- **• 11. [Coilover](#page-226-0)** spring/damper unit hanging on these pickups
- **• 5 / 6. Car [Setup](#page-102-0) / [Limits](#page-118-0)** alignment and ride overlays
- **8. Car [Tuning](#page-184-0) Parts** Suspensions Geometry path redirects
- **19. [Tyre](#page-307-0)** contact patch that kinematics aim at the ground

### <span id="page-288-3"></span>**B. Schema**

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
│ ├ 2e. Car Bottom Rear : x, y, z float
│ ├ 2f. Tyre Bottom : x, y, z float
│ ├ 2g. Car Steer : x, y, z float
│ └ 2h. Tyre Steer : x, y, z float
├ 3. Strut : object
│ ├ 3a. Car Strut : x, y, z float
```

```
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
│ └ 8d. Bottom Coilover : x, y, z float
├ 9. Dw Coil Data : object
│ ├ 9a. Car Top Front : x, y, z float
│ ├ 9b. Car Top Rear : x, y, z float
│ ├ 9c. Tyre Top : x, y, z float
│ ├ 9d. Car Bottom Front : x, y, z float
```

│ ├ 9e. Car Bottom Rear : x, y, z float │ ├ 9f. Tyre Bottom : x, y, z float │ ├ 9g. Car Steer : x, y, z float │ ├ 9h. Tyre Steer : x, y, z float │ ├ 9i. Car Coilover : x, y, z float └ └ 9j. Bottom Coilover : x, y, z float

### <span id="page-290-0"></span>**C. Measurement Units & Descriptions**

| ID  | Name           | Unit of Measurement         | Description                                                                                                                                                                                                                                                                              |
|-----|----------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Basic Data     | None ( Object )             | Per-corner suspension asset root;<br>holds unsprung mass, static<br>alignment, and exactly one<br>kinematic block (2–9). Referenced<br>from Car Data front/rear<br>suspension paths (.suspension).                                                                                       |
| 1a. | Hub Mass       | kg ( Kilograms )            | Unsprung mass at the hub: wheel,<br>tire, brake rotor/caliper, hub, and<br>upright share. Typical range ~37–<br>51 kg in examples (S2000 light<br>front 37 kg, Golf 50 kg, GT3 R 51<br>kg). Lower mass improves bump<br>compliance and tire contact<br>response.                         |
| 1b. | Toe Out Linear | rad/m ( Radians per meter ) | Linear kinematic toe gradient vs.<br>suspension displacement or stroke<br>(aligned with Car Setup 5f). Small<br>signed values (e.g. ±0.0002–<br>0.0011) model bump-steer /<br>compliance toe; positive often<br>means increasing toe-out with<br>travel depending on axis<br>convention. |
| 1c. | Static Camber  | deg ( Degrees )             | Fixed geometric camber at<br>reference ride height before live<br>setup offsets. Negative = top of<br>wheel leans inward (-0.3° street<br>Golf, -1.6° S2000 rear, -5.7° GT3 R<br>race front). Sets baseline contact<br>patch and camber gain reference.                                  |
| 1d. | Rim Offset     | m ( Meters )                | Wheel rim lateral offset (ET<br>equivalent) from hub mounting<br>face; shifts scrub radius and track<br>(e.g. 0.045 m S2000 front, 0.037 m<br>rear). Affects steering feel, kingpin<br>offset, and fender clearance.                                                                     |
| 2.  | D W Data       | None ( Object )             | Double-wishbone (DWB) kinematic<br>hardpoints; used when Strut / Axle<br>/ Trailing Arm / Multi Link blocks<br>are None (e.g. Honda S2000 front).<br>Defines upper/lower arm pivots<br>and steer tie-rod points in the car<br>body frame.                                                |

| ID  | Name             | Unit of Measurement     | Description                                                                                                                                                                                         |
|-----|------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2a. | Car Top Front    | m ( Meters, X / Y / Z ) | Chassis-side pivot of the upper<br>wishbone, forward inner bushing<br>(subframe / body mount). With 2b<br>defines upper arm axis and<br>camber / caster kinematics during<br>jounce and rebound.    |
| 2b. | Car Top Rear     | m ( Meters, X / Y / Z ) | Chassis-side pivot of the upper<br>wishbone, rear inner bushing. Pair<br>with 2a sets upper control arm<br>length, inclination, and roll-center<br>contribution.                                    |
| 2c. | Tyre Top         | m ( Meters, X / Y / Z ) | Upright-side ball joint for the<br>upper wishbone (outer upper<br>pivot). Primary camber-change link<br>as the wheel moves vertically and<br>steers.                                                |
| 2d. | Car Bottom Front | m ( Meters, X / Y / Z ) | Chassis-side pivot of the lower<br>wishbone, forward inner bushing.<br>Sets anti-dive geometry with 2e<br>and influences roll center height.                                                        |
| 2e. | Car Bottom Rear  | m ( Meters, X / Y / Z ) | Chassis-side pivot of the lower<br>wishbone, rear inner bushing. With<br>2d defines lower arm plane and<br>longitudinal compliance.                                                                 |
| 2f. | Tyre Bottom      | m ( Meters, X / Y / Z ) | Upright-side ball joint for the lower<br>wishbone (outer lower pivot).<br>Carries vertical load into the lower<br>arm; strongly affects scrub radius<br>and kingpin axis.                           |
| 2g. | Car Steer        | m ( Meters, X / Y / Z ) | Steering tie-rod inner attachment<br>on rack or steering arm (body<br>side). With 2h defines bump-steer<br>and Ackermann geometry for<br>DWB layouts.                                               |
| 2h. | Tyre Steer       | m ( Meters, X / Y / Z ) | Steering tie-rod outer ball joint on<br>the upright/knuckle. Motion<br>relative to 2g produces steer angle<br>change through travel.                                                                |
| 3.  | Strut            | None ( Object )         | McPherson strut kinematic set;<br>lower arm + telescopic strut define<br>wheel motion (e.g. Golf GTI Mk1<br>front). Mutually exclusive with<br>other geometry blocks when set to<br>None elsewhere. |
| 3a. | Car Strut        | m ( Meters, X / Y / Z ) | Strut top mount on the body<br>(shock tower / dome). Defines<br>primary vertical load path and strut<br>axis inclination (caster/camber<br>offset from strut angle).                                |

| ID  | Name             | Unit of Measurement     | Description                                                                                                                                                            |
|-----|------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3b. | Tyre Strut       | m ( Meters, X / Y / Z ) | Strut lower joint at the steering<br>knuckle (wheel-side strut pin).<br>Sliding joint along strut axis; sets<br>kingpin inclination with 3a.                           |
| 3c. | Car Bottom W B F | m ( Meters, X / Y / Z ) | Lower control arm (wishbone)<br>inner forward bushing on the<br>subframe. "W B" = wishbone; front<br>pivot of the LCA.                                                 |
| 3d. | Car Bottom W B R | m ( Meters, X / Y / Z ) | Lower control arm inner rear<br>bushing on the subframe. With 3c<br>sets LCA swing axis, anti-roll, and<br>longitudinal location.                                      |
| 3e. | Tyre Bottom W B  | m ( Meters, X / Y / Z ) | Lower control arm outer ball joint<br>at the knuckle. Vertical wheel<br>motion rotates about the LCA line<br>3c–3d–3e.                                                 |
| 3f. | Car Steer        | m ( Meters, X / Y / Z ) | Steering tie-rod inner point (rack<br>or steering arm on body) for<br>McPherson layout.                                                                                |
| 3g. | Tyre Steer       | m ( Meters, X / Y / Z ) | Tie-rod outer joint on the knuckle;<br>combined with 3f defines steer<br>angle and McPherson bump-steer.                                                               |
| 4.  | Strut Ml         | None ( Object )         | McPherson-strut variant with<br>additional locating links (multi-link<br>McPherson / strut-plus-links).<br>Adds thrust links and extra steer<br>points beyond block 3. |
| 4a. | Car Strut        | m ( Meters, X / Y / Z ) | Strut top mount on the body for<br>Strut Ml layout (same role as 3a).                                                                                                  |
| 4b. | Tyre Strut       | m ( Meters, X / Y / Z ) | Strut-to-knuckle lower joint for<br>Strut Ml (same role as 3b).                                                                                                        |
| 4c. | Car Bottom W B F | m ( Meters, X / Y / Z ) | Lower wishbone forward inner<br>pivot (Strut Ml).                                                                                                                      |
| 4d. | Car Bottom W B R | m ( Meters, X / Y / Z ) | Lower wishbone rear inner pivot<br>(Strut Ml).                                                                                                                         |
| 4e. | Tyre Bottom W B  | m ( Meters, X / Y / Z ) | Lower wishbone outer ball joint at<br>the upright (Strut Ml).                                                                                                          |
| 4f. | Car Thrust Ball1 | m ( Meters, X / Y / Z ) | First chassis-side pivot of a<br>thrust / radius rod limiting knuckle<br>rotation about the strut axis;<br>improves camber control under<br>lateral load.              |
| 4g. | Car Thrust Ball2 | m ( Meters, X / Y / Z ) | Second chassis-side pivot paired<br>with 4f (dual-link or split bush axis)<br>for the thrust linkage.                                                                  |

| ID  | Name                | Unit of Measurement                             | Description                                                                                                                                                                                                             |
|-----|---------------------|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4h. | Tyre Thrust Arm     | m ( Meters, X / Y / Z )                         | Upright-side joint for the thrust /<br>radius arm connecting to 4f/4g;<br>resists fore-aft knuckle rotation<br>and brake steer.                                                                                         |
| 4i. | Car Steer           | m ( Meters, X / Y / Z )                         | Steering tie-rod inner attachment<br>(Strut Ml geometry).                                                                                                                                                               |
| 4j. | Tyre Steer          | m ( Meters, X / Y / Z )                         | Steering tie-rod outer joint on the<br>upright (Strut Ml).                                                                                                                                                              |
| 5.  | Axle                | None ( Object )                                 | Live / solid axle kinematic block<br>for dependent rear (or front)<br>suspension: locating links, leaf<br>spring, and torque reaction. Used<br>on trucks and classic live-axle<br>cars when DW/Strut blocks are<br>None |
| 5a. | Attach Relative Pos | m ( Meters ) or dimensionless<br>ratio ( 0 -1 ) | Longitudinal or normalized<br>position along the axle/leaf where<br>the spring or link attaches relative<br>to axle center; sets load transfer<br>and wrap-up geometry.                                                 |
| 5b. | Link Count          | Integer count                                   | Number of axle locating links<br>modeled (Panhard rod, trailing<br>links, Watt's link, etc.); pairs with<br>indexed 5c/5d entries.                                                                                      |
| 5c. | Car Side            | m ( Meters, X / Y / Z )                         | Chassis-side attachment point for<br>an axle locating link (indexed [x]<br>per link). Defines roll center and<br>lateral axle location.                                                                                 |
| 5d. | Axle Side           | m ( Meters, X / Y / Z )                         | Axle-side attachment for the<br>corresponding locating link [x].<br>With 5c sets link length and lateral<br>constraint stiffness.                                                                                       |
| 5e. | Hub Mass            | kg ( Kilograms )                                | Unsprung mass per corner for the<br>axle layout (same physical<br>meaning as 1a but authored inside<br>the Axle block for live-axle assets).                                                                            |
| 5f. | Leaf Spring Lat K   | N/m ( Newtons per meter )                       | Lateral stiffness of the leaf spring<br>stack resisting sideways axle shift<br>(leaf-as-lateral-locator). Higher<br>values reduce axle walk under<br>cornering and braking.                                             |
| 5g. | Torquereaction      | Nm/rad ( Newton-meters per<br>radian )          | Axle torque-reaction stiffness<br>against driveline/brake wrap-up<br>(rotation of axle about its lateral<br>axis). Models anti-squat / anti-lift<br>from link geometry and compliant<br>mounts.                         |

| ID  | Name                | Unit of Measurement                | Description                                                                                                                                                                                                                 |
|-----|---------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 6.  | Multi Link Data     | None ( Object )                    | Legacy multi-link hardpoint list<br>(indexed joints) predating Multi<br>Link New Data; simpler joint-car<br>enumeration for older ACE<br>suspension templates.                                                              |
| 6a. | Joint Car           | m ( Meters, X / Y / Z )            | Chassis-side pivot for link index [x]<br>in the legacy multi-link solver (one<br>point per link).                                                                                                                           |
| 6b. | Joint Type          | m ( Meters, X / Y / Z )            | Per-link constraint data for index<br>[x]; schema types as x,y,z float<br>(likely encoded joint class / axis<br>flags rather than a literal position—<br>treat as solver metadata vector in<br>meters or normalized codes). |
| 7.  | Trailing Arm Data   | None ( Object )                    | Semi-trailing or trailing-arm rear<br>geometry (e.g. Golf GTI Mk1 rear).<br>Arm hinges on body and carries<br>hub at outer end.                                                                                             |
| 7a. | Car Hinge Int       | m ( Meters, X / Y / Z )            | Inner trailing-arm bushing on the<br>body (inboard pivot). Defines<br>primary arm axis with 7b.                                                                                                                             |
| 7b. | Car Hinge Ext       | m ( Meters, X / Y / Z )            | Secondary inner hinge point on<br>the body (outboard bushing of the<br>arm inner pair). Two-point inner<br>mount sets bushing compliance<br>axis and toe change under load.                                                 |
| 7c. | Tyre Top            | m ( Meters, X / Y / Z )            | Hub/upright attachment at the<br>upper outer end of the trailing arm.                                                                                                                                                       |
| 7d. | Tyre Bottom         | m ( Meters, X / Y / Z )            | Hub/upright attachment at the<br>lower outer end; with 7c fixes<br>wheel plane orientation on the<br>arm.                                                                                                                   |
| 7e. | Car Steer           | m ( Meters, X / Y / Z )            | Steering or toe-link inner point on<br>body (often inactive on driven rear<br>arms).                                                                                                                                        |
| 7f. | Tyre Steer          | m ( Meters, X / Y / Z )            | Steering / toe-link outer point on<br>the hub for rear steer or toe<br>compliance.                                                                                                                                          |
| 7g. | Steer Link To Body  | None ( Boolean : True /<br>False ) | When true, the steer/toe link inner<br>mount is fixed to the body; when<br>false, it may attach to the arm,<br>changing toe compliance under<br>traction/braking.                                                           |
| 8.  | Multi Link New Data | None ( Object )                    | Explicit graph-based multi-link:<br>indexed Links (two-point struts)<br>and Arms (three-point control<br>arms) plus optional coilover<br>mounts (e.g. Porsche 992 GT3 R<br>rear).                                           |

| ID   | Name                  | Unit of Measurement                | Description                                                                                                                                                      |
|------|-----------------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 8a.  | Links                 | None ( Object array [x] )          | Repeatable link elements (tie rods,<br>toe links, strut rods); each index<br>defines a rigid link between Ball<br>Car and Ball Tyre.                             |
| 8a1. | Name                  | None ( String )                    | Optional label for the link (e.g.<br>"steer" on GT3 R toe link); aids<br>authoring/debug, not used in<br>physics directly.                                       |
| 8a2. | Ball Car              | m ( Meters, X / Y / Z )            | Chassis-side spherical joint for link<br>[x].                                                                                                                    |
| 8a3. | Ball Tyre             | m ( Meters, X / Y / Z )            | Upright-side spherical joint for link<br>[x]; distance to 8a2 sets link length<br>and constraint direction.                                                      |
| 8a4. | Has Coilover Attached | None ( Boolean : True /<br>False ) | When true, the coilover damper<br>unit (.coilover asset) acts on this<br>link (force along link or at pickup<br>on link geometry).                               |
| 8a5. | Is Toe                | None ( Boolean : True /<br>False ) | When true, this link is flagged as<br>the primary toe-control member<br>(toe link / steering compliance<br>arm); GT3 R example sets true on<br>link named steer. |
| 8b.  | Arms                  | None ( Object array [x] )          | Repeatable control arms with two<br>body pivots and one upright pivot<br>(classic multi-link arm).                                                               |
| 8b1. | Name                  | None ( String )                    | Optional arm identifier for<br>authoring (camper arm, upper<br>lateral, etc.).                                                                                   |
| 8b2. | Ball Car 1            | m ( Meters, X / Y / Z )            | First chassis-side pivot of arm [x]<br>(inner bushing pair or front link<br>point).                                                                              |
| 8b3. | Ball Car 2            | m ( Meters, X / Y / Z )            | Second chassis-side pivot of arm<br>[x]; with 8b2 defines arm plane<br>and bush axis.                                                                            |
| 8b4. | Ball Tyre             | m ( Meters, X / Y / Z )            | Upright-side ball joint for arm [x];<br>primary load path from wheel into<br>the arm.                                                                            |
| 8b5. | Has Coilover Attached | None ( Boolean : True /<br>False ) | When true, coilover spring/damper<br>attaches to this arm (common on<br>lower or virtual swing arm).                                                             |
| 8c.  | Car Coilover          | m ( Meters, X / Y / Z )            | Coilover upper mount on the body<br>when not carried by a flagged link/<br>arm (shock tower pickup).                                                             |
| 8d.  | Bottom Coilover       | m ( Meters, X / Y / Z )            | Coilover lower mount on the<br>upright or link; with 8c defines<br>damper line and motion ratio.                                                                 |

| ID  | Name             | Unit of Measurement     | Description                                                                                                                                                |
|-----|------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 9.  | Dw Coil Data     | None ( Object )         | Double wishbone geometry with integrated coilover pick-ups (e.g. Porsche 992 GT3 R front). Combines DW hardpoints with explicit damper mount points 9i/9j. |
| 9a. | Car Top Front    | m ( Meters, X / Y / Z ) | Upper wishbone forward inner pivot (Dw Coil layout; same role as 2a).                                                                                      |
| 9b. | Car Top Rear     | m ( Meters, X / Y / Z ) | Upper wishbone rear inner pivot (Dw Coil; same role as 2b).                                                                                                |
| 9c. | Tyre Top         | m ( Meters, X / Y / Z ) | Upper wishbone outer ball joint on upright (Dw Coil; same role as 2c).                                                                                     |
| 9d. | Car Bottom Front | m ( Meters, X / Y / Z ) | Lower wishbone forward inner pivot (Dw Coil; same role as 2d).                                                                                             |
| 9e. | Car Bottom Rear  | m ( Meters, X / Y / Z ) | Lower wishbone rear inner pivot (Dw Coil; same role as 2e).                                                                                                |
| 9f. | Tyre Bottom      | m ( Meters, X / Y / Z ) | Lower wishbone outer ball joint (Dw Coil; same role as 2f).                                                                                                |
| 9g. | Car Steer        | m ( Meters, X / Y / Z ) | Steering tie-rod inner point for Dw Coil geometry.                                                                                                         |
| 9h. | Tyre Steer       | m ( Meters, X / Y / Z ) | Steering tie-rod outer joint for Dw Coil geometry.                                                                                                         |
| 9i. | Car Coilover     | m ( Meters, X / Y / Z ) | Coilover upper mount on chassis/<br>subframe; defines damper axis<br>relative to DW kinematics.                                                            |
| 9j. | Bottom Coilover  | m ( Meters, X / Y / Z ) | Coilover lower mount on upright or lower arm; with 9i sets spring motion ratio and anti-dive line.                                                         |

### <span id="page-296-0"></span>D. Example data

#### <span id="page-296-1"></span>I. Chosen Cars for Example

- Volkswagen Golf GTI Mk1 ( slug : ks\_volkswagen\_golf\_gti\_mk1 ) [ 2 suspensions ]
- Honda S2000 AP1 (slug: ks\_honda\_s2000\_ap1) [3 suspensions]
- Porsche 992 GT3 R Rennsport (slug: ks\_porsche\_992\_gt3\_r\_rennsport) [2 suspensions]

### <span id="page-296-2"></span>II. Example

### <span id="page-296-3"></span>Volkswagen Golf GTI Mk1

1. Front Suspension (file: ks\_volkswagen\_golf\_gti\_mk1\_front.suspension)

Basic Data

- 1a. Hub Mass : 50.00000

```
│ ├ 1b. Toe Out Linear : 0.00030 
│ ├ 1c. Static Camber : -0.30000 
│ └ 1d. Rim Offset : 0.00000 
├ 2. D W Data : None 
├ 3. Strut 
│ ├ 3a. Car Strut : 0.13200, 0.38800, -0.01050 
│ ├ 3b. Tyre Strut : 0.05200, -0.05000, 0.01500 
│ ├ 3c. Car Bottom W B F : 0.41000, -0.05700, 0.32500 
│ ├ 3d. Car Bottom W B R : 0.39000, -0.05000, -0.04000 
│ ├ 3e. Tyre Bottom W B : 0.05200, -0.05000, 0.01500 
│ ├ 3f. Car Steer : 0.39000, -0.05250, 0.06000 
│ └ 3g. Tyre Steer : 0.05200, -0.05000, 0.15000 
├ 4. Strut Ml : None 
├ 5. Axle : None 
├ 6. Multi Link Data : None 
├ 7. Trailing Arm Data : None 
├ 8. Multi Link New Data : None 
├ 9. Dw Coil Data : None
```

*2. Rear Suspension ( file : ks\_volkswagen\_golf\_gti\_mk1\_rear.suspension )* 

```
├ 1. Basic Data
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
```

### <span id="page-297-0"></span>**Honda S2000 AP1**

*1. Front Suspension ( file : ks\_honda\_s2000\_ap1\_front.suspension )* 

```
├ 1. Basic Data
│ ├ 1a. Hub Mass : 37.00000 
│ ├ 1b. Toe Out Linear : -0.00020 
│ ├ 1c. Static Camber : -0.40000 
│ └ 1d. Rim Offset : 0.04500 
├ 2. D W Data 
│ ├ 2a. Car Top Front : 0.34203, 0.12311, 0.08000
│ ├ 2b. Car Top Rear : 0.34302, 0.12451, -0.08000
```

```
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
├ 2. D W Data 
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
```

│ └ 2h. Tyre Steer : 0.09130, -0.05342, 0.14988

├ 3. Strut : None

```
├ 4. Strut Ml : None 
├ 5. Axle : None 
├ 6. Multi Link Data : None 
├ 7. Trailing Arm Data : None 
├ 8. Multi Link New Data : None 
├ 9. Dw Coil Data : None
```

### <span id="page-299-0"></span>**Porsche 992 GT3 R Rennport**

*1. Front Suspension ( file : ks\_porsche\_992\_gt3\_r\_rennsport\_front.suspension )* 

```
├ 1. Basic Data
│ ├ 1a. Hub Mass : 51.00000 
│ ├ 1b. Toe Out Linear : 0.00044 
│ ├ 1c. Static Camber : -5.70000 
│ └ 1d. Rim Offset : 0.00000 
├ 2. D W Data : None 
├ 3. Strut : None 
├ 4. Strut Ml : None 
├ 5. Axle : None 
├ 6. Multi Link Data : None 
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
```

*2. Rear Suspension ( file : ks\_porsche\_992\_gt3\_r\_rennsport\_rear.suspension )* 

```
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
```

```
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
│ │ ├ 8a2. Ball Car : 0.32123, -0.00156, -0.12150 
│ │ ├ 8a3. Ball Tyre : 0.05699, 0.10790, -0.12715 
│ │ ├ 8a4. Has Coilover Attached : false 
│ │ └ 8a5. Is Toe : true 
│ ├ 8b. Arms : None 
│ ├ 8c. Car Coilover : 0.32123, -0.00156, -0.12150 
│ └ 8d. Bottom Coilover : 0.05699, 0.10790, -0.12715 
├ 9. Dw Coil Data : None
```

# <span id="page-301-0"></span>**18. Turbo [ .turbo ]**

### <span id="page-301-1"></span>**A. Description**

Per-charger boost behaviour: peak boost, spool lag up/down, RPM reference, RPM/throttle gamma shaping, wastegate ceiling, whether boost is garage-adjustable, and an index into the engine's turbo list.

Loaded from Car Engine Turbos To Load (and related controller / max-boost logic). Controllers and maps on the engine decide *when* boost is requested; this asset decides *how* the charger builds and caps pressure.

Official Description prose in the source dump is unfinished placeholder text. Content below follows the schema and examples.

### <span id="page-301-2"></span>**I. Role in the stack**

| Concern                       | Handled here         | Handled elsewhere                       |
|-------------------------------|----------------------|-----------------------------------------|
| Max boost / wastegate         | Max Boost, Watergate | Engine Max Turbo Boost /<br>controllers |
| Spool / decay lag             | Lag UP / Lag DN      | Throttle lag on .carengine              |
| RPM / throttle response shape | Rpm Ref, gammas      | Engine turbo controllers LUTs           |
| Garage-adjustable boost       | Is Adjustable        | Setup turbo boost level                 |
| Which turbo file loads        | —                    | Engine Turbos To Load paths             |
| Base torque curve             | —                    | .carengine power maps                   |

One engine can load several .turbo files (205 T16 pair, Supra twin / drift twins).

### <span id="page-301-3"></span>**II. What you are really tuning**

- 1. **Boost ceiling** *Max Boost* is the pressure target/cap for this charger (205 soft stage 0.7, hard 1.2; Camaro 1.0; Supra drift secondary 2.0). Stock Supra examples sit at 0.0 here — boost may be driven entirely from engine controllers / maps with this file only supplying lag shape.
- 2. **Wastegate** Watergate in the dump is **wastegate** (OCR). Often mirrors or sits just under max boost (205 0.7 / 1.2; Camaro 0.9 vs max 1.0; drift Supra 0.3 / 1.5 vs max 0.3 / 2.0). Caps how much pressure the gate will hold.
- 3. **Lag factors** *Lag UP* / *Lag DN* near 1.0 (0.99x) = slow exponential spool/bleed typical of exhaust turbos. Camaro compressor uses **0.0 / 0.0** — effectively no turbo lag (supercharger-style instant response). Drift Supra stages tweak lag slightly (0.9975 / 0.988 vs stock 0.995 / 0.990).
- 4. **RPM and gamma shaping** *Rpm Ref* anchors where the charger "comes alive" (205 2300 vs 4100 for the two stages; Camaro 6000; Supra stock 3500 / 4000). *Gamma Rpm* / *Gamma Gas* steepen or soften build vs RPM and throttle (205 both 2.5; Camaro gamma gas 0; drift hard stage gamma RPM 3.0).

5. **Adjustability and wiring** — *Is Adjustable* true (Supra drift) exposes boost to garage / cockpit control; false locks the stage. *CarData* path is optional linkage (None in samples). *Turbo no* indexes the unit in the engine's turbo list (0 in all dumps here — filename / load order still distinguishes twins).

### <span id="page-302-0"></span>**III. Architecture**

Flat schema (1–10):

- 1. *Max Boost*
- 2-3. *Lag UP* / *Lag DN*
- 4. *Rpm Re*f
- 5-6. *Gamma Rpm* / *Gamma Gas*
- 7. *Watergate* ( wastegate )
- 8. *Is Adjustable*
- 9. *CarData* path
- 10. *Turbo no*

No nested controllers inside this asset — those live on .carengine.

### <span id="page-302-1"></span>**IV. How to read the examples**

### <span id="page-302-2"></span>**1 - PEUGEOT 205 T16 — TWO TURBO STAGES**

Turbo 0: max 0.7, Rpm Ref 2300, wastegate 0.7. Turbo 1: max 1.2, Rpm Ref 4100, wastegate 1.2. Same lag (0.995 / 0.990) and gammas (2.5). Classic sequential / staged Group B style: low-RPM soft charger + high-RPM hard charger. Not adjustable.

### <span id="page-302-3"></span>**2 - CHEVROLET CAMARO ZL1 — COMPRESSOR**

Max 1.0, wastegate 0.9, **zero lag**, Gamma Gas 0, Rpm Ref 6000. Labelled compressor in the source list behaviour matches a blower: pressure without exhaust spool delay. Engine example loads this via *Turbos To Load*.

### <span id="page-302-4"></span>**3 - TOYOTA SUPRA MKIV — STOCK VS DRIFT WINS**

Stock turbo 0/1: Max Boost and wastegate 0, lag present, soft gammas 0.5 — lag skeleton with boost authored elsewhere. Drift turbo 0/1: real boost 0.3 then 2.0, wastegates 0.3 / 1.5, *Is Adjustable : true*, stronger gammas on the big stage. Tuning-part drift package swaps the charger personality with the rest of the car.

### <span id="page-302-5"></span>**V. Practical notes**

- Source Description section is placeholder ignore spring/alignment headings.
- Always read **engine** turbo controllers + *Max Turbo Boost* together with this file; zeros here do not always mean NA.
- *Watergate* = wastegate typo in the converted dump.
- Lag 0/0 is a feature (compressor), not a missing value do not "fix" it to 0.99 unless you want turbo lag.

- Multi-turbo engines: match *Turbo no* / load order to the stage you intend; duplicate *Turbo no : 0* on every file in the dump means identity is path-based.
- Filename OCR (*t15* vs *t16*) appears in the Peugeot examples trust the car slug, not the mistyped stem.

### <span id="page-303-0"></span>**VI. Related assets**

- **4. Car [Engine](#page-87-0)** *Turbos To Load*, turbo/wastegate controllers, max boost, BOV
- **• 5 / 6. Car [Setup](#page-102-0) / [Limits](#page-118-0)** turbo boost level when *Is Adjustable*
- **8. Car [Tuning](#page-184-0) Parts** drift / upgrade packs that retarget .turbo files

### <span id="page-303-1"></span>**B. Schema**

├ 1. Max Boost : float ├ 2. Lag U P : float ├ 3. Lag D N : float ├ 4. Rpm Ref : float ├ 5. Gamma Rpm : float ├ 6. Gamma Gas : float ├ 7. Wastegate : float ├ 8. Is Adjustable : boolean ├ 9. CarData : string - path └ 10. Turbo no : integer

### <span id="page-303-2"></span>**C. Measurement Units & Descriptions**

| ID | Name      | Unit of Measurement                            | Description                                                                                                                                                                                                                                                  |
|----|-----------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. | Max Boost | bar ( Bar gauge pressure )                     | Peak compressor boost relative to<br>ambient (gauge). Typical street/<br>rally ~0.7–1.2 bar (205 T16), race/<br>drift up to ~2.0 bar; 0.0 disables<br>forced-induction output on that<br>stage. Aligns with Car Engine §18<br>Max Turbo Boost ceiling.       |
| 2. | Lag U P   | Dimensionless lag coeffi<br>cient<br>( 0 - 1 ) | Exponential spool-up filter toward<br>target boost under rising demand<br>(UP = up). Values near 1.0 (e.g.<br>0.995–0.9975) mean heavy turbo<br>lag; 0.0 = instantaneous rise<br>(Camaro ZL1 compressor /<br>supercharger-style response).                   |
| 3. | Lag D N   | Dimensionless lag coeffi<br>cient<br>( 0 - 1 ) | Exponential decay filter when<br>boost demand falls (DN = down):<br>throttle lift, gear change, or RPM<br>drop. Slightly below Lag UP in<br>examples (0.988–0.990) so boost<br>bleeds off a bit faster than it<br>builds; 0.0 with Lag UP = no lag<br>(ZL1). |

| ID  | Name          | Unit of Measurement                           | Description                                                                                                                                                                                                                                              |
|-----|---------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4.  | Rpm Ref       | RPM ( Revolutions per minute<br>)             | Reference engine speed for the<br>RPM-shaped boost curve (with<br>Gamma Rpm). Below this region<br>spool is weak; around/above it<br>boost builds toward Max Boost.<br>Examples: 2300/4100 (205 staged<br>twin), 6000 (ZL1), 3200–4400<br>(Supra drift). |
| 5.  | Gamma Rpm     | Dimensionless exponent<br>( power-law shape ) | Exponent shaping how boost<br>scales with RPM relative to Rpm<br>Ref. Higher gamma (>1, e.g. 2.5–<br>3.0) = abrupt high-RPM spool;<br>lower (0.5–1.0) = progressive/early<br>response (Supra stock / ZL1).                                               |
| 6.  | Gamma Gas     | Dimensionless exponent<br>( power-law shape ) | Exponent shaping boost vs.<br>throttle/gas pedal. Higher = needs<br>more pedal to spool; 0.0 = boost<br>independent of throttle position<br>(ZL1 compressor model); ~0.5–2.5<br>typical turbo response.                                                  |
| 7.  | Wastegate     | bar ( Bar gauge pressure )                    | Wastegate setpoint. Caps<br>regulated boost; often equals Max<br>Boost (205 T16) or slightly below<br>(ZL1 0.9 vs 1.0; Supra drift 1.5 vs<br>2.0 Max). Models mechanical/<br>electronic wastegate opening<br>pressure.                                   |
| 8.  | Is Adjustable | None ( Boolean : True /<br>False )            | When true, boost level is exposed<br>to setup / performance-mode<br>adjustment (Turbo Boost Lv); false<br>= fixed factory map (205 T16, ZL1,<br>Supra stock). Supra drift turbos<br>set true.                                                            |
| 9.  | CarData       | None ( File path )                            | Optional path linking this .turbo<br>asset to a Car Data context; None<br>in all documented examples<br>(boost controlled via Car Engine<br>Turbos To Load + controllers).                                                                               |
| 10. | Turbo no      | Integer index ( 0-based )                     | Ordinal index of this turbocharger<br>in a multi-turbo / sequential stack<br>(Turbo 0 = primary/low-RPM,<br>Turbo 1 = secondary). Examples<br>list file Turbo 0/1 but store index 0<br>in-asset—verify against loaded<br>stage order.                    |

### <span id="page-304-0"></span>**D. Example data**

### <span id="page-304-1"></span>**I. Chosen Cars for Example**

- Peugeot 205 T16 ( slug : ks\_peugeot\_205\_t16 ) [ 2 turbos ]

- Chevrolet Camaro ZL1 ( slug : ks\_chevrolet\_camaro\_zl1 ) [ compressor ]
- Toyota Supra MKIV ( slug : ks\_toyota\_supra\_mkiv ) [ 2 turbos / 2 types ]

### <span id="page-305-0"></span>**II. Example**

### <span id="page-305-1"></span>**Peugeot 205 T16**

*1. Turbo 0 ( file : ks\_peugeot\_205\_t15.turbo )* 

```
├ 1. Max Boost : 0.70000 
├ 2. Lag U P : 0.99500 
├ 3. Lag D N : 0.99000 
├ 4. Rpm Ref : 2300.00000 
├ 5. Gamma Rpm : 2.50000 
├ 6. Gamma Gas : 2.50000 
├ 7. Wastegate : 0.70000 
├ 8. Is Adjustable : false 
├ 9. CarData : None 
└ 10. Turbo no : 0
```

*2. Turbo 1 ( file : ks\_peugeot\_205\_t15\_turbo0.turbo )* 

```
├ 1. Max Boost : 1.20000 
├ 2. Lag U P : 0.99500 
├ 3. Lag D N : 0.99000 
├ 4. Rpm Ref : 4100.00000 
├ 5. Gamma Rpm : 2.50000 
├ 6. Gamma Gas : 2.50000 
├ 7. Wastegate : 1.20000 
├ 8. Is Adjustable : false 
├ 9. CarData : None 
└ 10. Turbo no : 0
```

### <span id="page-305-2"></span>**Chevrolet Camaro ZL1**

```
├ 1. Max Boost : 1.00000 
├ 2. Lag U P : 0.00000 
├ 3. Lag D N : 0.00000 
├ 4. Rpm Ref : 6000.00000 
├ 5. Gamma Rpm : 1.00000 
├ 6. Gamma Gas : 0.00000 
├ 7. Wastegate : 0.90000 
├ 8. Is Adjustable : false 
├ 9. CarData : None 
└ 10. Turbo no : 0
```

### <span id="page-305-3"></span>**Toyota Supra MKIV**

*1. Turbo 0 ( file : ks\_toyota\_supra\_mkiv0.turbo )* 

├ 1. Max Boost : 0.00000

```
├ 2. Lag U P : 0.99500 
├ 3. Lag D N : 0.99000 
├ 4. Rpm Ref : 3500.00000 
├ 5. Gamma Rpm : 0.50000 
├ 6. Gamma Gas : 0.50000 
├ 7. Wastegate : 0.00000 
├ 8. Is Adjustable : false 
├ 9. CarData : None 
└ 10. Turbo no : 0 
2. Turbo 1 ( file : ks_toyota_supra_mkiv1.turbo ) 
├ 1. Max Boost : 0.00000 
├ 2. Lag U P : 0.99100 
├ 3. Lag D N : 0.98800 
├ 4. Rpm Ref : 4000.00000 
├ 5. Gamma Rpm : 0.50000 
├ 6. Gamma Gas : 0.50000 
├ 7. Wastegate : 0.00000 
├ 8. Is Adjustable : false 
├ 9. CarData : None 
└ 10. Turbo no : 0 
3. Drift Turbo 0 ( file : ks_toyota_supra_mkiv_drift0.turbo ) 
├ 1. Max Boost : 0.30000 
├ 2. Lag U P : 0.99750 
├ 3. Lag D N : 0.98800 
├ 4. Rpm Ref : 3200.00000 
├ 5. Gamma Rpm : 1.00000 
├ 6. Gamma Gas : 1.00000 
├ 7. Wastegate : 0.30000 
├ 8. Is Adjustable : true 
├ 9. CarData : None 
└ 10. Turbo no : 0 
4. Drift Turbo 1 ( file : ks_toyota_supra_mkiv_drift1.turbo ) 
├ 1. Max Boost : 2.00000 
├ 2. Lag U P : 0.99650 
├ 3. Lag D N : 0.99700 
├ 4. Rpm Ref : 4400.00000 
├ 5. Gamma Rpm : 3.00000 
├ 6. Gamma Gas : 1.00000 
├ 7. Wastegate : 1.50000 
├ 8. Is Adjustable : true
```

├ 9. CarData : None └ 10. Turbo no : 0

# <span id="page-307-0"></span>**19. Tyre [ .tyre ]**

### <span id="page-307-1"></span>**A. Description**

Full tyre compound physics: carcass size and stiffness, brush/grip model, thermal mass and degradation (grain/blister), pressure and camber sensitivity, speed-dependent μ, rolling resistance, and groove factors.

Car Data only lists which .tyre paths sit on front/rear. Setup picks pressure, camber, and compound index. This file is where grip, heat, and wear actually live — usually under *common\_phsx\tyres\…* and shared across many cars.

Official Description prose in the source dump is unfinished placeholder text. Content below follows the schema and examples.

### <span id="page-307-2"></span>**I. Role in the stack**

| Concern                                     | Handled here             | Handled elsewhere              |
|---------------------------------------------|--------------------------|--------------------------------|
| Size, rate, flex, inertia, tread            | Tyre Data                | —                              |
| Peak grip / slip shape / Mz / wear<br>curve | Model Data               | Wear .curve                    |
| Heat, grain, blister, μ(T) curve            | Thermal Data             | Thermal perf .curve            |
| Ideal pressure / flex vs P                  | Pressure Data + Pressure | Setup cold pressures           |
| Camber sensitivity                          | Camber Data              | Setup camber                   |
| μ vs speed (lat/long)                       | Speed Sensitivity        | —                              |
| Rolling resistance                          | Rolling Resistance       | —                              |
| Wet / groove behaviour                      | Groove Data              | —                              |
| Which compounds a car offers                | —                        | .car Front/Rear Tyre Compounds |
| Compound index in garage                    | —                        | .carsetup Alignements          |

### <span id="page-307-3"></span>**II. What you are really tuning**

- 1. **Identity** Name / Short Name for UI. Tyre Compound enum tags the family: Eco, Road, SuperCar, HyperCar, Slick\_Medium, Wet, Racing\_Vintage, F1\_Soft/Medium/Hard/Wet/Intermediate, …
- 2. **Carcass (Tyre Data)** Width and radius (metres), vertical *Rate* / progressive rate, damping (+ *Damping Mode*: Simple / hystereticMaxwell / hystereticNando), angular inertia, rim radius, tread height and consumption, mass, lateral/longitudinal flex K/C, explosion / blanket temperatures, flat-spot K, contact patch camber/flex helpers.

Eco 165 mm / radius 0.25; Vintage 195 / 0.31; F1 wet 305 / 0.36. F1 wet tread height 3 mm vs 8 mm on Eco/Vintage. Vintage uses large negative flex K values in the dump — treat as authored offsets relative to the model's baseline, not "negative stiffness" in plain language.

3. **Grip model (Model Data)** — *Dy0* / *Dx0* lateral/longitudinal grip scales; load sensitivity exponents; *Fz0* reference load; friction limit angle; flex gain; combined / slip factors; wear curve path; relaxation lengths; self-aligning moment (Mz) tweaks; brush exponent.

Eco Dy0 about 0.96; Vintage about 1.11; F1 wet about 1.47 (with Dx0 about 1.56). Peak μ rises hard from economy rubber to open-wheel wet.

4. **Thermal world** — Density, specific heat, surface/core mass ratio, cool factors (dry + rain), road conduction, conductivity, rolling heat factor, grain/blister gains and slip-angle thresholds, brake heat transfer into the tyre, thermal performance curve path, friction-limit angle vs temperature.

Eco cools faster dry (*Cool Factor* 1.4) than Vintage (0.7) or F1 wet (0.9). F1 wet pushes grain gains much higher and heat partition 1.4 — aggressive thermal personality. Blister gains are 0 in all three samples.

- 5. **Pressure and camber** Ideal vs reference pressure (Eco 31 / 30; Vintage 31 / 28; F1 wet 26 / 17), pressure spring gain, curb puncture thresholds. Camber gain and vertical-K vs camber range shape how camber buys grip vs kills the patch.
- 6. **Speed, RR, grooves** Separate lateral and longitudinal μ–speed / μ–temp blocks (*Mu0 T*, *Ref Speed*, sensitivities, *Tref*). Rolling resistance Rr0/Rr1/slip/wear. *Groove Factor* about 0.49 on Eco/Vintage vs **68** on F1 wet — wet siping / drainage strength, not a typo scale shared with road tyres.
- 7. **Init Data** Human tyre-size metadata: width, aspect ratio, diameter (inch), load index, pressure Eco 165-60-12, Vintage 195-60-15, F1 wet 305-720-18 style sizing in the examples.

### <span id="page-308-0"></span>**III. Architecture**

### <span id="page-308-1"></span>**1 - HEADER (SCHEMA 1-3)**

Name, short name, compound enum.

### <span id="page-308-2"></span>**2 - STRUCTURE AND MODEL (SCHEMA 4-5)**

Tyre Data carcass; Model Data grip/wear/Mz.

### <span id="page-308-3"></span>**3 - ENVIRONMENT COUPLING (SCHEMA 6-8)**

Thermal Data; Pressure Data; Camber Data.

### <span id="page-308-4"></span>**4 - SPEED, RR, GROOVE, COLD FILL (SCHEMA 9-13)**

Speed Sensitivity; Rolling Resistance; Groove Data; scalar *Pressure*; Init Data size card.

### <span id="page-308-5"></span>**IV. How to read the examples**

### <span id="page-308-6"></span>**1 - ECO (165-60-12) — ECONOMY ROAD**

Small, light carcass, Dy0 under 1.0, ideal pressure about 31 psi, mild groove factor, eco wear + tcurve under *common\_phsx\tyres\eco\*. Soft contact flex vs race tyres. Baseline "efficient road" compound.

### <span id="page-308-7"></span>**2 - RACING VINTAGE (195-60-15) — PERIOD RACE**

Wider/taller, higher Dy0/Dx0 than Eco, cooler dry cool factor (0.7), much stronger grain gains, vintage wear/ tcurve paths. Flex K authored negative in the dump. Classic historic race rubber personality on a road-ish size.

### <span id="page-309-0"></span>**3 - F1 2025 WET (305-720-18) — OPEN-WHEEL WET**

Wide, high inertia, short tread, very high Dy0/Dx0, low reference pressure (17) vs ideal 26, huge groove factor (68), elevated grain and heat partition, F1 wet curves. Built for standing water and high peak load not a road compound with a wet label slapped on.

### <span id="page-309-1"></span>**V. Practical notes**

- Source Description section is placeholder ignore spring/alignment headings.
- Almost all live tyres sit in *common\_phsx*; editing one file hits every car that lists it.
- Setup pressure should track *Ideal Pressure* / *Pressure Reference*; running far off rewrites flex and heat via Pressure Data gains.
- Wear and thermal curves are mandatory personality swapping only Dy0 without curves gives inconsistent fade.
- Negative flex K on vintage is an authoring convention in this dump; verify in tooling before "correcting" it to positive.
- Compound enum must match how Car Data / UI filter lists; wrong enum can hide a tyre from selectors.
- Brake heat couples through *Brake Transfer Factor* (small but nonzero in samples) pad temp and tyre temp are not fully isolated.

### <span id="page-309-2"></span>**VI. Related assets**

- **3. Car [Data](#page-35-0)** Front/Rear Tyre Compounds path lists
- **• 5 / 6 / 7. Car [Setup](#page-102-0) / [Limits](#page-118-0) / Units** pressures, camber, compound index, PSI labels
- **2. [Brakes](#page-27-0)** thermal neighbour via brake transfer
- **17. [Suspension](#page-286-0)** camber/toe kinematics feeding the contact patch
- **External** .curve wear and thermal performance maps referenced here

### <span id="page-309-3"></span>**B. Schema**

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
│ ├ 4f. Angular Inertia : float
│ ├ 4g. Rim Radius : float
```

```
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
│ ├ 6k. Thermal Conductivity : float
│ ├ 6l. Rolling Factor : float
```

```
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
│ ├ 13c. Diameter : float
│ ├ 13d. Load Index : float
```

### **Enum - Car Tyre**

| 3  | Tyre Compound | Eco, Road, SuperCar, HyperCar, Slick_Medium, Wet,<br>Racing_Vintage, F1_Soft, F1_Medium, F1_Hard, F1_Wet,<br>F1_Intermediate |
|----|---------------|------------------------------------------------------------------------------------------------------------------------------|
| 4w | Damping Mode  | Simple, hystereticMaxwell, hystereticNando                                                                                   |

### <span id="page-312-0"></span>**C. Measurement Units & Descriptions**

| ID  | Name             | Unit of Measurement                                                                                                                                              | Description                                                                                                                     |
|-----|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Name             | None ( String )                                                                                                                                                  | Full display name of the<br>compound (e.g. Eco (E), Racing<br>Vintage (RV), Wet (W)).                                           |
| 2.  | Short Name       | None ( String )                                                                                                                                                  | Abbreviated HUD / telemetry label<br>(E, RV, W).                                                                                |
| 3.  | Tyre Compound    | None ( Enum : Eco / Road /<br>SuperCar / HyperCar /<br>Slick_Medium / Wet /<br>Racing_Vintage / F1_Soft /<br>F1_Medium / F1_Hard /<br>F1_Wet / F1_Intermediate ) | Compound class selecting grip,<br>thermal, and wear baselines (Eco<br>street, Racing_Vintage, F1_Wet,<br>etc.).                 |
| 4.  | Tyre Data        | None ( Object )                                                                                                                                                  | Structural carcass block:<br>geometry, vertical spring/damper,<br>flex, temperatures, and contact<br>patch parameters.          |
| 4a. | Width            | m ( Meters )                                                                                                                                                     | Contact-section width in SI (0.165<br>Eco = 165 mm, 0.305 F1 wet =<br>305 mm). Distinct from Init Data<br>width in mm.          |
| 4b. | Radius           | m ( Meters )                                                                                                                                                     | Unloaded overall tyre radius (Eco<br>0.251 m, Vintage 0.308 m, F1 wet<br>0.360 m). Sets rolling<br>circumference and gearing.   |
| 4c. | Rate             | N/m ( Newtons per meter )                                                                                                                                        | Vertical carcass spring rate (~263–<br>307 kN/m in examples). Primary<br>tyre contribution to wheel rate and<br>ride frequency. |
| 4d. | Progressive Rate | N/m² or N/m³ ( Progressive<br>stiffening )                                                                                                                       | Additional rate that rises with<br>deflection (progressive carcass).<br>0.0 in examples = linear spring.                        |
| 4e. | Damping          | N·s/m ( Newton-seconds per<br>meter )                                                                                                                            | Vertical viscous damping of the<br>tyre spring (Eco ~549, F1 wet<br>~846). Controls carcass oscillation<br>and curb impact.     |

| ID  | Name                  | Unit of Measurement                     | Description                                                                                                                                                             |
|-----|-----------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4f. | Angular Inertia       | kg·m² ( Kilogram square<br>meters )     | Rotational inertia of tyre + rim<br>about spin axis (Eco 0.91, Vintage<br>2.27, F1 wet 4.67). Affects<br>acceleration, braking, and ABS<br>feel.                        |
| 4g. | Rim Radius            | m ( Meters )                            | Wheel rim outer radius (12″ →<br>0.1524 m, 15″ → 0.1905 m, 18″ →<br>0.2286 m). Used with tyre radius<br>for sidewall height.                                            |
| 4h. | Radius Raise K        | m/N or dimensionless gain               | Radius growth coeffi<br>cient under<br>load/centrifugal effects (0.001 in<br>examples); slight diameter<br>increase with speed/load.                                    |
| 4i. | Tread Height M M      | mm ( Millimeters )                      | Usable tread depth (Eco/Vintage 8<br>mm, F1 wet 3 mm). Depletes via<br>wear; wet grooves need remaining<br>depth for water evacuation.                                  |
| 4j. | Tread Consumption K   | Dimensionless wear rate                 | Scalar converting slip/energy work<br>into tread-height loss (6.0 across<br>examples).                                                                                  |
| 4k. | Mass                  | kg ( Kilograms )                        | Tyre (and often rim share) mass for<br>unsprung dynamics (6 kg in<br>examples — simplified vs. real F1<br>~9–10 kg).                                                    |
| 4l. | Lateral Flex K        | N/m ( Newtons per meter )               | Lateral carcass stiffness (Eco 28<br>kN/m, F1 wet 30 kN/m). Negative<br>values (Vintage −10 kN/m) can<br>encode special flex models;<br>governs sidewall lean under Fy. |
| 4m. | Lateral Flex C        | Dimensionless damping ratio<br>or N·s/m | Lateral flex damping (typically<br>~2.0). Limits oscillation of the<br>contact patch relative to the rim.                                                               |
| 4n. | Longitudinal Flex K   | N/m ( Newtons per meter )               | Fore-aft carcass stiffness under Fx<br>(Eco 18 kN/m, F1 wet 20 kN/m).<br>Affects traction/braking<br>compliance feel.                                                   |
| 4o. | Longitudinal Flex C   | Dimensionless damping ratio<br>or N·s/m | Longitudinal flex damping (~2.0–<br>2.5).                                                                                                                               |
| 4p. | Explosion Temperature | °C ( Degrees Celsius )                  | Catastrophic overheat threshold<br>(450 °C in examples) above which<br>the tyre is considered failed/<br>exploded.                                                      |
| 4q. | Blanket Temperature   | °C ( Degrees Celsius )                  | Tyre-warmer / pit-blanket target<br>start temperature (40 °C in<br>examples).                                                                                           |
| 4r. | Flat Spot K           | Dimensionless gain                      | Sensitivity of flat-spot damage<br>under locked-wheel scrub (0.1 in<br>examples).                                                                                       |

| ID   | Name                              | Unit of Measurement                                                | Description                                                                                                                      |
|------|-----------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 4s.  | Normal To Flex Ratio              | Dimensionless ratio                                                | Coupling of vertical load into<br>carcass flex (0.0 = no extra<br>coupling in examples).                                         |
| 4t.  | Contact Camber                    | deg ( Degrees ) or model<br>coeffi<br>cient                        | Contact-patch camber sensitivity /<br>effective patch camber shaping<br>(Eco ~2.8, F1 wet ~11).                                  |
| 4u.  | Contact Flex                      | m ( Meters ) or dimensionless                                      | Lateral contact-patch flex<br>magnitude under load (Eco 0.023,<br>F1 wet 0.345).                                                 |
| 4v.  | Contact Vertical Flex             | Dimensionless or mm-scale                                          | Vertical contact-patch compliance<br>shaping (Eco ~3.6, F1 wet ~16.6).                                                           |
| 4w.  | Damping Mode                      | None ( Enum : Simple /<br>hystereticMaxwell /<br>hystereticNando ) | Carcass damping model: Simple<br>viscous, Maxwell hysteretic, or<br>Nando hysteretic (examples use<br>hystereticNando).          |
| 4x.  | Maxwell Damping Peak<br>Frequency | Hz ( Hertz )                                                       | Peak frequency for Maxwell<br>hysteretic damper (0 when unused<br>/ Nando mode).                                                 |
| 4y.  | Maxwell Stiffening<br>Percent     | % ( Percent )                                                      | Extra dynamic stiffening in<br>Maxwell mode (0 when unused).                                                                     |
| 4z.  | Damping Threshold<br>Speed Ms     | m/s ( Meters per second )                                          | Vertical deflection-speed threshold<br>where speed-dependent damping<br>engages (1.0 m/s in examples).                           |
| 4aa. | Speed Damping Factor              | Dimensionless gain                                                 | Multiplier on damping above the<br>speed threshold (0.5 in examples).                                                            |
| 4ab. | Deflection Damping<br>Factor      | Dimensionless gain                                                 | Multiplier scaling damping with<br>deflection amplitude (3.0 in<br>examples).                                                    |
| 5.   | Model Data                        | None ( Object )                                                    | Brush / friction model: peak μ,<br>load sensitivity, slip limits, wear,<br>relaxation lengths, and self<br>aligning torque (Mz). |
| 5a.  | Dy0                               | Dimensionless friction<br>coeffi<br>cient ( μ_y )                  | Peak lateral friction coeffi<br>cient at<br>reference load Fz0 (Eco 0.96,<br>Vintage 1.11, F1 wet 1.47).                         |
| 5b.  | Dx0                               | Dimensionless friction<br>coeffi<br>cient ( μ_x )                  | Peak longitudinal friction<br>coeffi<br>cient at Fz0 (Eco 1.00, F1<br>wet 1.56). Braking/traction grip<br>baseline.              |
| 5c.  | Ls Exp Y                          | Dimensionless exponent                                             | Lateral load-sensitivity exponent:<br>how μ_y falls as Fz rises above<br>Fz0 (~0.82–0.87).                                       |
| 5d.  | Ls Exp X                          | Dimensionless exponent                                             | Longitudinal load-sensitivity<br>exponent for μ_x (~0.83–1.07).                                                                  |
| 5e.  | Fz0                               | N ( Newtons )                                                      | Reference vertical load for Dy0/<br>Dx0 (~3840–4230 N ≈ 390–430 kgf<br>per tyre).                                                |

| ID  | Name                          | Unit of Measurement           | Description                                                                                                                     |
|-----|-------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 5f. | Friction Limit Angle          | deg ( Degrees )               | Slip angle (or slip equivalent) at<br>which peak friction is reached<br>(~7.8–8.6°). Beyond this, grip falls<br>toward sliding. |
| 5g. | Flex Gain                     | Dimensionless gain            | Scales carcass flex contribution<br>into the friction model (0.0207 in<br>examples).                                            |
| 5h. | Cf Xmult                      | Dimensionless multiplier      | Multiplier on longitudinal<br>cornering/stiffness factor Cf_x<br>(1.8–2.0).                                                     |
| 5i. | Brake D X Mod                 | Dimensionless gain            | Modifier reducing Dx under heavy<br>braking (Eco 0.05, F1 wet 0.00).<br>Models brake-lock μ drop.                               |
| 5j. | Combined Factor               | Dimensionless coeffi<br>cient | Combined-slip ellipse shaping<br>(Pacejka-like): how Fx and Fy<br>share friction budget (1.8–2.0).                              |
| 5k. | Grip Slip Factor              | Dimensionless coeffi<br>cient | Post-peak sliding grip retention vs.<br>peak (0.76–0.82). Higher = more<br>forgiving slide.                                     |
| 5l. | Wear Curve                    | None ( .curve file path )     | LUT of wear state → grip/thermal<br>modifiers (wear_eco.curve,<br>wear_f12025_wet.curve, …).                                    |
| 5m. | Grain Factor                  | Dimensionless gain            | Base graining susceptibility<br>(0.001). Raised in thermal grain<br>gains for soft compounds.                                   |
| 5n. | Contact Wear I M O            | Dimensionless I/M/O weights   | Inner / middle / outer contact-wear<br>distribution weight (4.0 in<br>examples).                                                |
| 5o. | Relaxation Length Y           | m ( Meters )                  | Lateral force lag distance (~0.10<br>m). Shorter = snappier turn-in;<br>longer = delayed Fy build-up.                           |
| 5p. | Relaxation Length X           | m ( Meters )                  | Longitudinal force relaxation<br>length (~0.10 m). Affects ABS and<br>throttle traction transient.                              |
| 5q. | Mz Tweak Mult                 | Dimensionless multiplier      | Global scale on self-aligning<br>torque Mz feel (0.6).                                                                          |
| 5r. | Mz Scale                      | Dimensionless multiplier      | Base Mz magnitude scale (0.12).<br>Steering weight / trail feedback.                                                            |
| 5s. | Mz Trail Nd Slip<br>Reduction | Dimensionless coeffi<br>cient | How pneumatic trail (Mz) shrinks<br>with normalized slip (0.5).                                                                 |
| 5t. | Mz Trail Remap                | Dimensionless coeffi<br>cient | Remapping curve intensity for trail<br>vs. slip (0.2).                                                                          |
| 5u. | Brush Exponent                | Dimensionless exponent        | Brush-model stress distribution<br>exponent (3.0). Shapes the force<br>build-up before peak slip.                               |

| ID  | Name                          | Unit of Measurement                        | Description                                                                                              |
|-----|-------------------------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 6.  | Thermal Data                  | None ( Object )                            | Heat capacity, cooling,<br>conduction, grain/blister, brake<br>heat soak, and temperature→grip<br>curve. |
| 6a. | Vertical Spring               | N/m or thermal model scale                 | Thermal-node coupling spring (40<br>in examples) between surface/core<br>temperature layers.             |
| 6b. | Vertical Damp K               | Thermal damping coeffi<br>cient            | Damping of surface㲗core<br>temperature exchange (2.0).                                                   |
| 6c. | Wear Mult                     | Dimensionless multiplier                   | Temperature-linked wear rate<br>multiplier (0.2).                                                        |
| 6d. | Density                       | kg/m³ ( Kilograms per cubic<br>meter )     | Rubber density (1100 kg/m³ —<br>typical elastomer). Used with<br>volume for thermal mass.                |
| 6e. | Specific Heat                 | J/(kg·K) ( Joules per<br>kilogram-kelvin ) | Specific heat capacity of the tread<br>rubber (1600 J/(kg·K) in examples).                               |
| 6f. | Surface Core Mass<br>Ratio    | Dimensionless ratio ( 0 -1 )               | Fraction of thermal mass in the<br>surface skin vs. core (0.15). Low =<br>surface heats/cools fast.      |
| 6g. | Cool Factor Rain              | Dimensionless gain                         | Extra convective cooling in wet/<br>rain conditions (3.0).                                               |
| 6h. | Cool Factor                   | Dimensionless gain                         | Base air/road cooling rate (Eco<br>1.4, Vintage 0.7, F1 wet 0.9).                                        |
| 6i. | Heat Partition Coef           | Dimensionless coeffi<br>cient              | Split of generated heat into<br>surface vs. bulk (0.5–1.4).                                              |
| 6j. | Road Conduction               | W/(m²·K) or model units                    | Conductive heat transfer to<br>asphalt (1000 in examples).                                               |
| 6k. | Thermal Conductivity          | W/(m·K) ( Watts per meter<br>kelvin )      | Rubber conductivity (Eco 0.20,<br>Vintage 0.28, F1 wet 0.35 W/<br>(m·K)).                                |
| 6l. | Rolling Factor                | Dimensionless gain                         | Heat generation from rolling<br>hysteresis (Eco 0.6, F1 wet 1.6).                                        |
| 6m. | Grain Gain                    | Dimensionless gain                         | Rate of surface graining under<br>thermal/slip stress (Eco 0.017, F1<br>wet 0.47).                       |
| 6n. | Grain Gamma                   | Dimensionless exponent                     | Non-linear shaping of grain growth<br>vs. drivers (matches Grain Gain in<br>examples).                   |
| 6o. | Grain Slip Angle Gain         | Dimensionless gain                         | Extra grain rate from slip angle (F1<br>wet 0.565 vs Eco 0.165).                                         |
| 6p. | Grain Slip Angle<br>Gamma     | Dimensionless exponent                     | Exponent on slip-angle grain<br>contribution.                                                            |
| 6q. | Grain Slip Angle<br>Threshold | deg ( Degrees )                            | Slip angle above which grain<br>acceleration engages (~10.5–<br>11.3°).                                  |

| ID  | Name                                  | Unit of Measurement            | Description                                                                                       |
|-----|---------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------|
| 6r. | Blister Gain                          | Dimensionless gain             | Blister formation rate (0 in these<br>compounds; used on soft slicks).                            |
| 6s. | Blister Gamma                         | Dimensionless exponent         | Non-linear blister growth shaping<br>(0 when blister unused).                                     |
| 6t. | Practical Temp Source                 | Dimensionless blend ( 0 - 1 )  | Blend between surface and core<br>temperature for "practical" grip<br>temp (0.8).                 |
| 6u. | Brake Transfer Factor                 | Dimensionless gain             | Fraction of brake rotor heat<br>conducted into the tyre (0.0007).                                 |
| 6v. | Thermal Performance<br>Curve          | None ( .curve file path )      | LUT temperature (°C) → friction<br>effi<br>ciency (tcurve_eco.curve,<br>tcurve_f12025_wet.curve). |
| 6w. | Contact I M O                         | Dimensionless I/M/O weights    | Inner/middle/outer contact thermal<br>weighting (1.6).                                            |
| 6x. | Tref Friction Limit Angle             | °C ( Degrees Celsius )         | Reference temperature for friction<br>limit-angle thermal correction (75<br>°C).                  |
| 6y. | Friction Limit Angle T<br>Sensitivity | deg/°C or gain                 | How Friction Limit Angle shifts<br>with temperature (0.06).                                       |
| 7.  | Pressure Data                         | None ( Object )                | Inflation effects on flex, rolling<br>resistance, heat, spring rate, and<br>curb puncture loss.   |
| 7a. | Pressure Flex Gain                    | Dimensionless gain             | How carcass flex changes with<br>pressure offset from reference<br>(0.25).                        |
| 7b. | Rolling Resistance Gain               | Dimensionless gain             | Pressure→rolling-resistance<br>coupling (1.2). Under-inflation<br>raises RR.                      |
| 7c. | Rolling Heat Gain                     | Dimensionless gain             | Extra heat from pressure-related<br>hysteresis (0.1).                                             |
| 7d. | Gain D                                | Dimensionless gain             | Pressure influence on longitudinal<br>grip/damping term (~0.0025–<br>0.0026).                     |
| 7e. | Ideal Pressure                        | psi ( Pounds per square inch ) | Target hot pressure for peak<br>performance (Eco/Vintage 31 psi,<br>F1 wet 26 psi).               |
| 7f. | Pressure Reference                    | psi ( Pounds per square inch ) | Cold/reference pressure for spring<br>and flex tables (Eco 30, Vintage<br>28, F1 wet 17 psi).     |
| 7g. | Pressure Spring Curve                 | None ( .curve file path )      | Optional LUT of pressure →<br>vertical spring rate; None when<br>using Pressure Spring Gain only. |
| 7h. | Pressure Spring Gain                  | N/m per psi ( or N/m )         | Vertical rate contribution from<br>inflation (~9.9–11.1 kN/m scale in<br>examples).               |

| ID  | Name                            | Unit of Measurement                               | Description                                                                                        |
|-----|---------------------------------|---------------------------------------------------|----------------------------------------------------------------------------------------------------|
| 7i. | Curb Pressure Loss<br>Must      | psi or loss amount                                | Pressure drop applied when curb<br>impact exceeds threshold (1.0).                                 |
| 7j. | Curb Pressure Loss<br>Threshold | m/s or impact units                               | Impact severity before curb<br>puncture loss (Eco/Vintage 10, F1<br>wet 30 — tougher wet carcass). |
| 8.  | Camber Data                     | None ( Object )                                   | Camber sensitivity of grip and<br>vertical stiffness.                                              |
| 8a. | Camber Gain                     | Dimensionless gain                                | Grip change per degree of camber<br>(0.2).                                                         |
| 8b. | Camber Vertical K<br>Range Deg  | deg ( Degrees )                                   | Camber window over which<br>vertical rate gain applies (±5°).                                      |
| 8c. | Camber Vertical K Gain          | Dimensionless gain                                | Vertical stiffness change with<br>camber (−0.1).                                                   |
| 8d. | Dcamber0                        | Dimensionless coeffi<br>cient                     | Camber-thrust / μ offset<br>coeffi<br>cient at small camber (0.6).                                 |
| 8e. | Dcamber1                        | Dimensionless coeffi<br>cient                     | Higher-order camber sensitivity<br>(−11). Shapes camber thrust<br>curve.                           |
| 9.  | Speed Sensitivity               | None ( Object )                                   | Speed- and temperature<br>dependent friction for lateral (T)<br>and longitudinal (X) axes.         |
| 9a. | Mu0 T                           | Dimensionless friction<br>coeffi<br>cient ( μ )   | Base lateral μ at reference speed/<br>temp (Eco 0.78, F1 wet 0.85).                                |
| 9b. | Ref Speed                       | m/s ( Meters per second )                         | Reference slip/ground speed for<br>lateral μ speed law (4.5 m/s).                                  |
| 9c. | Mu Speed Sensitivity            | Dimensionless gain                                | Lateral μ change with speed<br>relative to Ref Speed (Eco 0.78, F1<br>wet 1.2).                    |
| 9d. | Mu T Sensitivity                | 1/°C or gain                                      | Lateral μ temperature sensitivity<br>(0.025–0.035).                                                |
| 9e. | Tref Mu T                       | °C ( Degrees Celsius )                            | Reference temperature for lateral μ<br>thermal correction (70–80 °C).                              |
| 9f. | Mu0 T X                         | Dimensionless friction<br>coeffi<br>cient ( μ_x ) | Base longitudinal μ at reference<br>conditions (Eco 0.70, F1 wet 0.68).                            |
| 9g. | Ref Speed X                     | m/s ( Meters per second )                         | Reference speed for longitudinal μ<br>law (2.0–3.5 m/s).                                           |
| 9h. | Mu Speed Sensitivity            | Dimensionless gain                                | Longitudinal μ speed sensitivity<br>(Eco 0.62, F1 wet 1.8 — wet more<br>speed-critical).           |
| 9i. | Mu T Sensitivity X              | 1/°C or gain                                      | Longitudinal μ temperature<br>sensitivity (0.035–0.095).                                           |
| 9j. | Tref Mu T X                     | °C ( Degrees Celsius )                            | Reference temperature for<br>longitudinal μ thermal correction<br>(70–80 °C).                      |

| ID   | Name               | Unit of Measurement              | Description                                                                                                                 |
|------|--------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 10.  | Rolling Resistance | None ( Object )                  | Steady and slip-dependent rolling<br>drag opposing wheel rotation.                                                          |
| 10a. | Rr0                | N ( Newtons )                    | Constant rolling-resistance force<br>(~17.8–20.1 N). Dominant at low<br>speed.                                              |
| 10b. | Rr1                | N·s/m or N per (m/s)             | Speed-proportional RR term<br>(0.002). Small linear rise with<br>velocity.                                                  |
| 10c. | Rr Slip            | N or model units                 | Extra RR under slip/scrub (646).<br>Raises drag when sliding.                                                               |
| 10d. | Rr Wear Mult       | Dimensionless multiplier         | How wear state scales rolling<br>resistance (0.14).                                                                         |
| 11.  | Groove Data        | None ( Object )                  | Tread groove / void effects on wet<br>grip and aquaplaning (critical for<br>F1_Wet).                                        |
| 11a. | Groove Factor      | Dimensionless or groove<br>index | Overall groove/void intensity<br>(street Eco 0.49 vs F1 wet 68 —<br>deep rain channels).                                    |
| 11b. | Groove S A Factor  | Dimensionless coeffi<br>cient    | Groove effect on slip-angle grip<br>(0.45). SA = slip angle.                                                                |
| 11c. | Groove S R Factor  | Dimensionless coeffi<br>cient    | Groove effect on slip-ratio /<br>longitudinal grip (0.45). SR = slip<br>ratio.                                              |
| 12.  | Pressure           | psi ( Pounds per square inch )   | Default cold inflation for this<br>compound asset (Eco 30, Vintage<br>28, F1 wet 17 psi). Overridden by<br>setup pressures. |
| 13.  | Init Data          | None ( Object )                  | Human-readable tyre size<br>designation (width–aspect–rim)<br>and load/pressure ratings.                                    |
| 13a. | Width              | mm ( Millimeters )               | Nominal section width (165 / 195 /<br>305). Matches commercial size<br>marking.                                             |
| 13d. | Aspect Ratio       | % ( Percent of width )           | Sidewall height as % of width (60<br>street, 43 F1 wet ≈ low-profile<br>race).                                              |
| 13c. | Diameter           | in ( Inches )                    | Rim diameter (12 / 15 / 18). Must<br>match Rim Radius = Diameter ×<br>0.0254 / 2.                                           |
| 13d. | Load Index         | None ( Integer load index )      | ISO load index (Eco 99, Vintage<br>88) — max load capacity class.                                                           |
| 13e. | Pressure           | psi ( Pounds per square inch )   | Rated / nominal inflation for the<br>size designation (mirrors field 12 /<br>Pressure Reference).                           |

#### <span id="page-320-0"></span>D. Example data

#### <span id="page-320-1"></span>I. Chosen Tyres for Example

```
Eco (slug : eco_165_60_12)Vintage (slug : vintage_195_60_15)
```

- F1 2025 Wet (slug: f12025 wet 305 720 18)

#### <span id="page-320-2"></span>II. Example

<span id="page-320-3"></span>Eco | Size : 165 - 60 - 12

```
1. Name: Eco (E)
2. Short Name: E
3. Tyre Compound : Eco
4. Tyre Data
 - 4a. Width : 0.16500
 - 4b. Radius : 0.25140
  4c. Rate: 306900.00000
  4d. Progressive Rate: 0.00000
  4e. Damping: 549.08398
  4f. Angular Inertia: 0.91034
  4q. Rim Radius : 0.15240
 - 4h. Radius Raise K : 0.00100
  4i. Tread Height M M : 8.00000
  4j. Tread Consumption K: 6.00000
  4k. Mass: 6.00000
  41. Lateral Flex K: 28000.00000
  4m. Lateral Flex C: 2.00000
  4n. Longitudinal Flex K: 18000.00000
  4o. Longitudinal Flex C: 2.50000
  4p. Explosion Temperature: 450.00000
  4q. Blanket Temperature : 40.00000
  4r. Flat Spot K : 0.10000
  4s. Normal To Flex Ratio: 0.00000
  4t. Contact Camber: 2.79367
  4u. Contact Flex: 0.02293
  4v. Contact Vertical Flex: 3.58828
  4w. Damping Mode: hystereticNando
  4x. Maxwell Damping Peak Frequency: 0.00000
  4y. Maxwell Stiffening Percent: 0.00000
 - 4z. Damping Threshold Speed Ms : 1.00000
  4aa. Speed Damping Factor: 0.50000
<sup>L</sup> 4ab. Deflection Damping Factor: 3.00000
5. Model Data
 - 5a. Dy0 : 0.96160
  5b. Dx0 : 1.00483
  5c. Ls Exp Y: 0.82088
 - 5d. Ls Exp X : 1.07088
  5e. Fz0 : 4170.00000
  5f. Friction Limit Angle: 8.56818
  5g. Flex Gain: 0.02070
  5h. Cf Xmult : 2.00000
```

```
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
```

```
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

### <span id="page-322-0"></span>**Vintage | Size : 195 - 60 - 15**

```
├ 1. Name : Racing Vintage (RV) 
├ 2. Short Name : RV 
├ 3. Tyre Compound : Racing_Vintage 
├ 4. Tyre Data 
│ ├ 4a. Width : 0.19500 
│ ├ 4b. Radius : 0.30750 
│ ├ 4c. Rate : 272800.00000 
│ ├ 4d. Progressive Rate : 0.00000 
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
```

```
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
```

```
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
├ 13. Init Data 
│ ├ 13a. Width : 195.00000 
│ ├ 13b. Aspect Ratio : 60.00000 
│ ├ 13c. Diameter : 15.00000 
│ ├ 13d. Load Index : 88.00000 
└ └ 13e. Pressure : 28.00000
```

### <span id="page-324-0"></span>**F1 2025 [ Wet ] | Size : 305 - 720 - 18**

├ 1. Name : Wet (W) ├ 2. Short Name : W

```
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
```

```
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
```

│ └ 10d. Rr Wear Mult : 0.14000 ├ 11. Groove Data │ ├ 11a. Groove Factor : 68.00000 │ ├ 11b. Groove S A Factor : 0.45000 │ └ 11c. Groove S R Factor : 0.45000 ├ 12. Pressure : 17.00000 ├ 13. Init Data │ ├ 13a. Width : 305.00000 │ ├ 13b. Aspect Ratio : 43.00000 │ ├ 13c. Diameter : 18.00000 │ ├ 13d. Load Index : 101.00000

└ └ 13e. Pressure : 17.00000

# <span id="page-328-0"></span>**20. Wing [ .wing ]**

### <span id="page-328-1"></span>**A. Description**

Discrete aero element: a named lifting/drag surface with chord, span, world position, angle-of-attack CL/CD curves, optional ground-height multipliers, Cl/Cd gains, yaw sensitivity, damage stages, and optional wing controllers (active / linked aero).

Surface 3D maps handle the platform CX/CZ vs ride height. Wings are the individual BODY / FRONT / REAR / DIFFUSER pieces Car Data lists under Wings Path. Setup wing angles overlay the baseline *Angle* on adjustable elements.

Official Description prose in the source dump is unfinished placeholder text. Content below follows the schema and examples.

### <span id="page-328-2"></span>**I. Role in the stack**

| Concern                      | Handled here                | Handled elsewhere                 |
|------------------------------|-----------------------------|-----------------------------------|
| Element size and mount point | Chord, Span, Position       | —                                 |
| CL/CD vs AOA                 | Lut AOA CL/CD               | .curve files                      |
| Ground-effect multipliers    | Lut GH CL/CD Mult           | Height .curve                     |
| Gain, default angle, yaw     | Cl/Cd Gain, Angle, Yaw Gain | Setup wing angles                 |
| Damage sensitivity           | Damage CD/CL arrays         | Collision / wear systems          |
| Active angle logic           | Wing Controllers            | Input enums + LUTs                |
| Which elements load          | —                           | .car Aero Wings Path              |
| Platform maps                | —                           | .surface3d Front/Rear Lift / Drag |

### <span id="page-328-3"></span>**II. What you are really tuning**

- 1. **Element identity** *Name* labels the role (*BODY*, *FRONT*, *REAR*, *DIFFUSER\_F*, …). *Vertical* flags orientation (all samples *false* — horizontal aero planes). Chord × Span set reference area; Position (x,y,z) places the force application point (front bumper vs rear wing vs underfloor).
- 2. **AOA polar** *Lut AOA CL* / *Lut AOA CD* are required personality curves. Changing angle (setup or baseline *Angle*) walks these LUTs. BODY elements often carry drag with *Cl Gain : 0* and nonzero *Cd Gain* (RS6 body Cd 1.6; Emira body Cd 1.0).
- 3. **Ground height** Optional *Lut GH CL Mult* / *Lut GH CD Mult* scale lift/drag with ride height. RS6 front and SF-25 front wings / diffusers wire height curves; many rear wings leave them *None* (angledominated, less ground-effect in the authoring).
- 4. **Gains, angle, yaw** *Cl Gain* / *Cd Gain* multiply the LUT outputs. *Angle* is the default incidence (Emira front/rear 2°; SF-25 front 6°, rear 12°, body/diffuser 3.5°). *Yaw Gain* (often negative on race wings) bleeds or shifts aero in yaw — SF-25 rear −1.5, front elements about −0.57.

- 5. **Cooling and fans** *Drag Per Cool Transfer* couples cooling drag (0 in samples). *Has Fan* / *Fan Speed* for active blown elements — unused here.
- 6. **Damage stages** *Damage CD[x]* / *Damage CL[x]* (typically four slots) raise drag or kill lift as the element takes hits. Front wings often damage slot 1; rear slot 2; body uses mid/high slots progressive aero degradation.
- 7. **Controllers** Staged pipeline: Combinator (Add / Must OCR for Mult), Input (Brake, Gas, Yaw, LatG, LonG, Steer, Speed, suspension travel…), Filter, limits, Lut. Empty in these examples; used when DRS-like or dynamic wing logic lives on the element itself (Car Data may also own DRS hooks separately).

### <span id="page-329-0"></span>**III. Architecture**

### <span id="page-329-1"></span>**1 - GEOMETRY AND POLARS (SCHEMA 1-9)**

Vertical flag; name; chord/span; position; AOA CL/CD paths; optional GH CL/CD mult paths.

### <span id="page-329-2"></span>**2 - GAINS AND EXTRAS (SCHEMA 10-16)**

Cd/Cl gain; angle; yaw gain; cool-transfer drag; fan flags.

### <span id="page-329-3"></span>**3 - DAMAGE AND CONTROL (SCHEMA 17-19)**

Repeating damage CD/CL floats; Wing Controllers array.

### <span id="page-329-4"></span>**IV. How to read the examples**

### <span id="page-329-5"></span>**1 - AUDI RS6 AVANT — ROAD TRIAD**

Three wings, shared span 2.41: **BODY** (Cd only), **FRONT** (Cl 1.0, angle 2°, height CL/CD curves), **REAR** (Cl 1.0, no height LUTs). Classic road-car aero split: body drag + front height-sensitive + rear wing.

### <span id="page-329-6"></span>**2 - LOTUS EMIRA — SPORT TRIAD**

Same BODY/FRONT/REAR pattern, narrower span (1.945). Higher Cl gains (front 2.0, rear 2.2), both ends at 2° angle, no height multipliers. More "wing-driven" than ground-effect front.

### <span id="page-329-7"></span>**3 - FERRARI SF-25 — OPEN-WHEEL PACKAGE**

Many elements: BODY (Cl+Cd, yaw −0.2), **two FRONT** wings mirrored at x ±0.56 (span 0.42 each, Cl gain 3.9, angle 6°, height LUTs, strong yaw), REAR (chord 0.45, span 2.0, angle 12°, Cd 1.5 / Cl 0.7, yaw −1.5), plus DIFFUSER\_F and DIFFUSER\_RL (and further diffuser pieces in the dump) with height curves. Shows wings as a full aero assembly, not just a rear flap.

### <span id="page-329-8"></span>**V. Practical notes**

• Source Description section is placeholder; example header wrongly says "Chosen Tyres".

- Setup wing angle only matters if Car Data lists the corresponding .wing and Limits allow adjustment.
- Editing AOA curves without updating Cl/Cd gains (or vice versa) double-scales the element.
- Dual front wings (SF-25) must stay symmetric unless intentional aero balance asymmetry.
- OCR: Combinator *Must* ≈ Mult; input *SusTraveILR* ≈ suspension travel L/R.
- Surface 3D maps and wings stack changing only one layer leaves the other fighting your balance.

### <span id="page-330-0"></span>**VI. Related assets**

- **3. Car [Data](#page-35-0)** Aero *Wings Path* list, DRS hooks
- **• 16. [Surface](#page-275-0) 3D** platform CX/CZ vs ride height
- **5 / 6. Car [Setup](#page-102-0) / [Limits](#page-118-0)** wing angles and legal windows
- **8. Car [Tuning](#page-184-0) Parts** Wing / Aero Package redirects
- **External** .curve AOA and ground-height LUTs referenced here

### <span id="page-330-1"></span>**B. Schema**

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
├ 10. Cd Gain : float
├ 11. Cl Gain : float
├ 12. Angle : float
├ 13. Yaw Gain : float
├ 14. Drag Per Cool Transfer : float
├ 15. Has Fan : boolean
├ 16. Fan Speed : float
├ 17. Damage C D [x] : float | can have multiple Damage C D
├ 18. Damage C L [x] : float | can have multiple Damage C L
├ 19. Wing Controllers [x] : object | can have multiple Wing Controllers
│ ├ 19a. Combinator Mode : enum
│ ├ 19b. Input : enum
│ ├ 19c. Filter : float
│ ├ 19d. Up Limit : float
│ ├ 19e. Down Limit : float
│ ├ 19f. Lut : string - path
```

### **Enum - Car Wing**

| 19a | Combinator Mode | UndefinedMode, Add, Mult                                                               |
|-----|-----------------|----------------------------------------------------------------------------------------|
| 19b | Input           | UndefinedInput, Brake, Gas, Yaw, LatG, LonG, Steer, Speed,<br>SusTravelLR, SusTravelRR |

### <span id="page-331-0"></span>**C. Measurement Units & Descriptions**

| ID | Name             | Unit of Measurement                | Description                                                                                                                                                                                                                                       |
|----|------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. | Vertical         | None ( Boolean : True /<br>False ) | When true, the element is a<br>vertical aero surface (endplate /<br>fin) producing mainly side force;<br>false = horizontal wing, body, or<br>diffuser plane (all documented<br>examples are false).                                              |
| 2. | Name             | None ( String )                    | Element label used for authoring<br>and DRS/setup mapping (BODY,<br>FRONT, REAR, DIFFUSER_F,<br>DIFFUSER_RL/RR).                                                                                                                                  |
| 3. | Chord            | m ( Meters )                       | Streamwise reference length of the<br>aero element. Often 1.0 as a unit<br>chord for LUT scaling; physical<br>chords appear on race cars (SF-25<br>rear wing 0.45 m, front diffuser 2.5<br>m). With Span sets effective area<br>A ≈ Chord × Span. |
| 4. | Span             | m ( Meters )                       | Lateral width of the element (RS6/<br>Emira body ~1.95–2.41 m; SF-25<br>split front wings 0.42 m each, rear<br>wing 2.0 m, half-diffusers 0.683<br>m).                                                                                            |
| 5. | Position         | m ( Meters, X / Y / Z )            | Force application point in the car<br>body frame (m). Sets pitch/heave<br>moment arms: front wings at +Z,<br>rear at −Z, body near CG (e.g. RS6<br>FRONT z=1.9, REAR z=−2.1).                                                                     |
| 6. | Lut A O A C L    | None ( .curve file path )          | Look-up table: angle of attack<br>(AoA, deg) → lift coeffi<br>cient Cl<br>(wing_body/front/<br>rear_AOA_CL.curve). Core polar<br>for downforce vs. incidence.                                                                                     |
| 7. | Lut A O A C D    | None ( .curve file path )          | Look-up table: AoA → drag<br>coeffi<br>cient Cd (AOA_CD.curve).<br>Paired with Cl LUT for L/D trade<br>off.                                                                                                                                       |
| 8. | Lut G H C L Mult | None ( .curve file path )          | Ground-height (ride-height)<br>multiplier LUT on Cl<br>(height_front_CL.curve,<br>height_diffuser_CL.curve). Models<br>ground effect / diffuser sensitivity;<br>often None on body/rear wing.                                                     |
| 9. | Lut G H C D Mult | None ( .curve file path )          | Ground-height multiplier LUT on<br>Cd. Used with GH Cl Mult for front<br>wings and underbody elements.                                                                                                                                            |

| ID   | Name                   | Unit of Measurement                           | Description                                                                                                                                                                             |
|------|------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10.  | Cd Gain                | Dimensionless coeffi<br>cient                 | Scalar on Cd from LUTs (aligned<br>with Car Data §17c3). Body often<br>carries most drag (RS6 BODY 1.6,<br>Emira BODY 1.0); wings may use<br>0–1.5.                                     |
| 11.  | Cl Gain                | Dimensionless coeffi<br>cient                 | Scalar on Cl from LUTs (aligned<br>with Car Data §17c2). BODY often<br>0 (pure drag blob); FRONT/REAR<br>1–2 (street) up to ~3.9 (SF-25<br>front).                                      |
| 12.  | Angle                  | deg ( Degrees )                               | Static geometric incidence / flap<br>angle relative to the body (AoA<br>offset into CL/CD LUTs). Setup<br>adjustable on race cars (Emira<br>FRONT 2°, SF-25 FRONT 6°,<br>REAR 12°).     |
| 13.  | Yaw Gain               | Dimensionless coeffi<br>cient                 | Sensitivity of aero forces to vehicle<br>yaw (aligned with Car Data §17c4).<br>Negative values on F1 (SF-25 −0.2<br>to −1.5) model yaw-induced Cl/Cd<br>change and side-force coupling. |
| 14.  | Drag Per Cool Transfer | Dimensionless coeffi<br>cient                 | Drag penalty coupled to cooling<br>air / duct mass-flow (aligned with<br>Car Data §17c5). 0.0 in all<br>documented examples.                                                            |
| 15.  | Has Fan                | None ( Boolean : True /<br>False )            | Enables an active suction fan on<br>this element (e.g. fan-car / blown<br>diffuser). False on RS6, Emira, and<br>SF-25 examples.                                                        |
| 16.  | Fan Speed              | RPM or rad/s ( Fan rotational<br>speed )      | Commanded fan speed when Has<br>Fan is true; 0 when unused.                                                                                                                             |
| 17.  | Damage C D             | Dimensionless ΔCd per<br>damage stage         | Indexed [x] damage stages<br>increasing Cd after aero damage<br>(e.g. 0.005–0.015). Stages map to<br>progressive wing/body damage<br>levels.                                            |
| 18.  | Damage C L             | Dimensionless ΔCd per<br>damage stage         | Indexed [x] damage stages<br>reducing (or shifting) Cl after<br>damage; often matched to<br>Damage CD on the impacted side<br>(front crash → stage 1, rear →<br>stage 2).               |
| 19.  | Wing Controllers       | None ( Object array [x] )                     | Dynamic aero controllers (DRS,<br>brake-duct, speed-sensitive flaps).<br>None in documented examples;<br>schema exposes per-controller<br>fields 19a–19f.                               |
| 19a. | Combinator Mode        | None ( Enum :<br>UndefinedMode / Add / Mult ) | How this controller's LUT output<br>combines with base Angle/gains<br>(Add = offset; Must likely Mult/<br>override — schema spelling).                                                  |

| ID   | Name       | Unit of Measurement                                                                                                   | Description                                                                                                  |
|------|------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 19b. | Input      | None (Enum:<br>UndefinedInput / Brake / Gas<br>/ Yaw / LatG / LonG / Steer /<br>Speed / SusTraveILR /<br>SusTraveIRR) | Telemetry channel driving the controller (brake for DRS-off, speed, lateral G, suspension travel L/R, etc.). |
| 19c. | Filter     | Dimensionless filter coefficient (0 - 1)                                                                              | Low-pass smoothing on the controller input to avoid aero chatter.                                            |
| 19d. | Up Limit   | deg or gain ( Depends on controller output )                                                                          | Upper clamp on controller output (max flap angle / gain).                                                    |
| 19e. | Down Limit | deg or gain ( Depends on controller output )                                                                          | Lower clamp on controller output (min flap angle / gain).                                                    |
| 19f. | Lut        | None ( .curve file path )                                                                                             | Look-up table mapping Input → angle or Cl/Cd modifier for this wing controller.                              |

#### <span id="page-333-0"></span>D. Example data

### <span id="page-333-1"></span>I. Chosen Tyres for Example

- Audi RS6 Avant (slug: ks\_audi\_rs\_6\_avant) [ 3 wings ]
- Lotus Emira (slug: ks\_lotus\_emira)
- Ferrari SF-25 (slug: ks\_ferrari\_sf\_25)

#### <span id="page-333-2"></span>II. Example

### <span id="page-333-3"></span>**Audi RS6 Avant**

1. Wing 0 [ Body ] (file: ks\_audi\_rs\_6\_avant0.wing)

```
- 1. Vertical : false
```

- 2. Name : BODY

3. Chord : 1.00000

- 4. Span : 2.41000

5. Position: 0.00000, 0.18000, -0.10000

- 6. Lut A O A C L :

content\cars\ks\_audi\_rs\_6\_avant\data\wing\_body\_AOA\_CL.curve

- 7. Lut A O A C D :

content\cars\ks\_audi\_rs\_6\_avant\data\wing\_body\_AOA\_CD.curve

- | 8. Lut G H C L Mult : None
- 9. Lut G H C D Mult : None
- 10. Cd Gain : 1.60000
- 11. Cl Gain: 0.00000
- 12. Angle : 0.00000
- 13. Yaw Gain : 0.00000
- 14. Drag Per Cool Transfer: 0.00000
- 15. Has Fan : false
- 16. Fan Speed : 0.00000
- 17. Damage C D 1 : 0.00500

```
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
├ 6. Lut A O A C L : 
content\cars\ks_audi_rs_6_avant\data\wing_rear_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_audi_rs_6_avant\data\wing_rear_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 0.00000
```

```
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

### <span id="page-335-0"></span>**Lotus Emira**

### *1. Wing 0 [ Body ] ( file : ks\_lotus\_emira0.wing )*

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
```

```
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

### <span id="page-337-0"></span>**Ferrari SF-25**

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
2. Wing 1 [ Front ] ( file : ks_ferrari_sf_251.wing ) 
├ 1. Vertical : false 
├ 2. Name : FRONT 
├ 3. Chord : 1.00000
```

```
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
├ 11. Cl Gain : 3.90000 
├ 12. Angle : 6.00000 
├ 13. Yaw Gain : -0.57100 
├ 14. Drag Per Cool Transfer : 0.00000
```

├ 15. Has Fan : false ├ 16. Fan Speed : 0.00000 ├ 17. Damage C D 1 : 0.01000

```
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
├ 6. Lut A O A C L : 
content\cars\ks_ferrari_sf_25\data\aero\wing_rear_AOA_CL.curve 
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_rear_AOA_CD.curve 
├ 8. Lut G H C L Mult : None 
├ 9. Lut G H C D Mult : None 
├ 10. Cd Gain : 1.50000
```

```
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
6. Wing 5 [ Diffuser Rear Left ] ( file : ks_ferrari_sf_255.wing ) 
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_RL 
├ 3. Chord : 1.00000 
├ 4. Span : 0.68300 
├ 5. Position : -0.34230, -0.17500, -1.57000
```

```
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
```

```
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
```

### *9. Wing 8 [ Monkeyseat ] ( file : ks\_ferrari\_sf\_258.wing )*

```
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
├ 13. Yaw Gain : -0.15000 
├ 14. Drag Per Cool Transfer : 0.00000 
├ 15. Has Fan : false 
├ 16. Fan Speed : 0.00000 
├ 17. Damage C D 1 : 0.00000 
├ 17. Damage C D 2 : 0.01000 
├ 17. Damage C D 3 : 0.00000
```

```
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
├ 7. Lut A O A C D : 
content\cars\ks_ferrari_sf_25\data\aero\wing_diffuser_AOA_CD.curve 
├ 8. Lut G H C L Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CL.curve 
├ 9. Lut G H C D Mult : 
content\cars\ks_ferrari_sf_25\data\aero\height_diffuser_CD.curve 
├ 10. Cd Gain : 0.83000
```

```
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
├ 19. Wing Controllers : None 
13. Wing 12 [ Diffuser Front Right R ] ( file : ks_ferrari_sf_diff_rr.wing ) 
├ 1. Vertical : false 
├ 2. Name : DIFFUSER_FRR 
├ 3. Chord : 2.50000 
├ 4. Span : 0.35000 
├ 5. Position : -0.66000, -0.16000, 0.00000
```

```
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