# LIGO-India Experimental Lectures and “Ask Rana Anything” Series
### Comprehensive Curriculum for Detector Installation, Commissioning, and Operation

## A. Mathematical & Computational Foundations
1. **Matrix-Inversion Method for Optical Fields**
   - Adjacency matrices, self-consistent field solutions.
   - PDH signal derivation; extension to Michelson and PRFPMI.
2. **Frequency Response and Linearization**
   - Optical transfer functions; cavity pole; sensing & actuation matrices.
3. **Modeling of Linear Systems**
   - Mechanical and electronic state-space models; transfer-function fitting.
4. **Feedback Control Fundamentals**
   - Loop algebra, stability margins, MIMO coupling, digital filter design.
5. **Simulation Tools**
   - Python/Numpy and FINESSE-style modeling; comparing analytic vs. numeric results.

## B. Interferometer Sensing and Control
6. **Length Sensing & Control (LSC)**
   - DOFs: DARM, CARM, MICH, PRCL, SRCL; demodulation phases, lock acquisition.
7. **Alignment Sensing & Control (ASC)**
   - Wavefront sensors, optical levers, dither alignment, alignment matrices.
8. **Cross-Couplings and Noise in Controls**
   - Radiation-pressure and alignment couplings; optical springs; sideband asymmetries.
9. **Automation and Guardian Systems**
   - State machines, interlocks, watchdogs, autonomous lock recovery.

## C. Mechanical Systems
10. **Seismic Isolation (SEI)**
    - Ground spectra; HEPI/ISI topology; sensor blending; feedforward design.
11. **Suspensions (SUS)**
    - Single/triple/quad pendula; OSEMs, coil drivers, damping loops, diagonalization.
12. **Mechanical Characterization**
    - Mode identification, transfer-function measurement, modeling vs. data.
13. **Environmental Inputs & Feedforward**
    - Wind, microseism, anthropogenic noise; PEM sensors; adaptive subtraction.

## D. Electronics, Control, and Data Systems
14. **Actuation & Sensing Electronics**
    - Coil drivers, whitening/de-whitening, ADC/DAC limits, grounding practice.
15. **CDS Architecture**
    - Front-end models, EPICS, real-time code, channel naming, testing.
16. **Automation Infrastructure**
    - Sequencing, watchdogs, slow controls, failure recovery procedures.

## E. Optical Subsystems
17. **Input Optics (IO)**
    - PSL, EOMs, AOMs, mode cleaner, Faraday isolators, beam diagnostics.
18. **Output Optics (OO)**
    - Output mode cleaner, photodiodes, DC readout, shot-noise calibration.
19. **Higher-Order Spatial Modes & Mode Matching**
    - HG basis, Gouy phase, misalignment/figure errors, telescope tuning.
20. **Scattering & Stray-Light Control**
    - BRDF, baffles, scatter coupling models, measurement and mitigation.

## F. Vacuum & Infrastructure
21. **Vacuum System**
    - Beam-tube/chamber layout, pumping, RGA, leak detection, bakeout.
22. **Cleanroom & Optics Handling**
    - CO₂ cleaning, contamination control, witness samples, clean-build rules.
23. **Site Infrastructure**
    - HVAC, electrical grounding, EMI/RFI suppression, timing distribution.

## G. High-Power & Advanced Opto-Mechanical Phenomena
24. **Thermal Compensation System (TCS)**
    - Absorption-driven lensing; CO₂ projector & ring heater; Hartmann sensor; control loops.
25. **Parametric Instabilities (PI)**
    - Three-mode coupling, gain calculations, damping strategies, diagnostics.
26. **Optical Springs & Sidles–Sigg Instabilities**
    - Angular optical spring physics, measurement, and loop tuning.
27. **Thermal Effects in Coatings & Substrates**
    - Absorption measurements, compensation interplay, operational tuning.
28. **High-Power Commissioning Practices**
    - Ramp-up procedures, saturation management, safety interlocks.

## H. Calibration, Diagnostics, and Noise Budgets
29. **Noise Budget Generation & Automation**
    - Building dynamic noise models; comparing measured vs. predicted spectra.
30. **Calibration Systems**
    - Photon calibrators, actuator hierarchy, absolute strain calibration chain.
31. **Detector Characterization (DetChar)**
    - Glitch studies, vetoes, coherence analysis, data-quality flags.
32. **Timing & Synchronization**
    - GPS/IRIG systems, ADC/DAC alignment, timing jitter effects.

## I. Quantum & Squeezing Systems
33. **Quantum Noise Fundamentals**
    - Shot noise, radiation pressure, standard quantum limit.
34. **Squeezed-Light Generation & Injection**
    - Optical parametric oscillator, phase control, squeezer alignment.
35. **Squeezer Diagnostics & Commissioning**
    - Noise ellipse measurement, angle control loops, degradation mechanisms.
36. **Interfacing Squeezing with LIGO-India Detector**
    - Injection path optics, isolation requirements, joint operation with ISC.

## J. LIGO-India Design Optimization & Upgrades
37. **LIGO-India Baseline & Site-Specific Design**
    - A1 parameters, seismic/thermal environment, infrastructure adaptation.
38. **Mode-Matching Sensitivity Studies**
    - Telescope design, recycling gain optimization, error propagation.
39. **Laser Systems Engineering**
    - Frequency/intensity stabilization, reference cavities, diagnostics.
40. **Coating & Optics Development**
    - Material R&D, loss-angle measurement, indigenization strategy.
41. **Adaptive Optics & Future Upgrades**
    - Real-time thermal correction, next-generation technology planning.

## K. Commissioning Culture & Operations
42. **Commissioning Workflow and Troubleshooting**
    - Measurement sequences, null-measurement mindset, logbook discipline.
43. **Operations & Reliability**
    - Shift protocols, fault analysis, preventive maintenance.
44. **Safety and Human Factors**
    - Laser & vacuum safety, interlock systems, configuration management.

## L. Capstone Integration
45. **Full-IFO Digital Twin**
    - Integrate optical, mechanical, and control models; simulate lock acquisition and noise budget.
46. **Field Commissioning Practicum**
    - Real data exercises; noise hunting, filter tuning, alignment recovery; final presentations.

---
**Cadence:** 1 session/month (~90 min)  
**Format:** 50 min lecture + 25 min coding or data demo + 15 min ARA  
**Deliverables:** slides, example code, reading list, homework, recording  
**Archive:** shared internal repository indexed by subsystem
