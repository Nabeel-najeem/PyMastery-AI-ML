# ♾️ PyMastery-AI-ML
### Continuous Upskilling & Technical Evolution

This repository is a live log of my daily consistency in Python and AI development. Technology is constantly evolving; this space is where I bridge the gap between theory and high-performance code. There is no end date—only progress.

---

## 🛠 Technical Focus
- **Advanced OOP:** Modular system design using Inheritance and Abstraction.
- **Data Engineering:** Building resilient pipelines with NumPy and Pandas.
- **Computer Vision:** Real-time processing, edge detection, and color targeting.
- **Interaction Design:** Gesture-based control and screen positioning logic.

---

## 📅 Daily Activity Log

| Day | Date | Technical Milestones & Commits |
| :--- | :--- | :--- |
| **Day 01** | Jan 16 | **OOP Foundations:** Implementing Inheritance logic. |
| **Day 02** | Jan 17 | Core Python syntax and logic refinement. |
| **Day 03** | Jan 18 | **Abstraction Practice:** Mastering modular code structures. |
| **Day 04** | Jan 19 | **NumPy Foundations:** 1D and 2D Array manipulations. |
| **Day 05** | Jan 20 | Logic optimization and algorithmic practice. |
| **Day 06** | Jan 21 | **Data Analysis:** Initializing basic Pandas workflows. |
| **Day 07** | Jan 22 | Scripting efficiency and daily logic challenges. |
| **Day 08** | Jan 23 | **OpenCV Init:** First CV2 file integrations. |
| **Day 09** | Jan 24 | Integration of daily Python scripts with CV modules. |
| **Day 10** | Jan 25 | **Color Detection:** Tool practice using OpenCV. |
| **Day 11** | Jan 26 | Refactoring detection logic for consistency. |
| **Day 12** | Jan 27 | **Object Targeting:** Boundary box implementation for color targets. |
| **Day 13** | Jan 28 | **Project: Air Brush v1** - Initial task logic. |
| **Day 14** | Jan 29 | **Advanced CV:** Noise reduction, Edge detection, and Air Brush v2. |
| **Day 15** | Jan 30 | **Hardware Integration:** Basic Webcam access and frame processing. |
| **Day 16** | Jan 31 | **Gesture Control:** Index/Thumb tracking and screen positioning. |
| **Day 18** | Feb 01 | **AI Landmarks:** MediaPipe Hand tracking & Adaptive EMA Smoothing logic. |
| **Day 19** | Feb 02 | **OS Integration & Depth Scaling :** Multi-click gestures, adaptive scroll, and dynamic depth-aware thresholds. |
| **Day 20** | Feb 03 | **Advanced HID :** Dynamic Interaction Zone scaling & State-based Drag-and-Drop logic.. |
| **Day 21** | Feb 04 | **skip:** skip |
| **Day 22** | Feb 05 | **Project Complete :** Finalized Hand-Controlled Mouse with gesture isolation and stable Drag-and-Drop state logic. |
| **Day 23** | Feb 06 | **face mesh :** face mesh started. |
| **Day 24** | Feb 07 | **Face Mesh Foundation:** Implemented real-time landmark detection and isolated drawing for Iris, Contours, and Nose features. |
| **Day 25** | Feb 08 | **Modular Transition:** Migrated Face Mesh logic into an OOP-based engine for scale-invariant iris tracking. |
| **Day 26** | Feb 09 | **Modular Transition:** Successfully implemented OOP-based face_detector and established main.py as the project index. |
| **Day 27** | Feb 10 | **Face-Mouse Logic:** Integrated Dynamic Thresholding based on cranial width. Implemented bilateral Blink Detection (EAR-lite). |
| **Day 28** | Feb 11 | **Modular Architecture Finalized :** Completed the Face Engine and Adaptive Signal Processor with dual-eye stabilization. |
| **Day 29** | Feb 12 | **3D Calibration Complete :** Integrated Deapth_caliibration with dual-plane (Near/Far) logic. Successfully mapped pupil movement to 1080p screen coordinates using depth-adjusted scaling. |
| **Day 30** | Feb 13 | **pose Vision Initialized :** Successfully integrated MediaPipe Pose into the modular repo and rendered the real-time skeletal overlay. |
| **Day 31** | Feb 14 | **Gesture Engineering :** Developed a modular possDetector class and successfully implemented a dual-shoulder shrug detection system. |
| **Day 32** | Feb 15 | **Gesture Synergy & Tuning :** Integrated joint angle kinematics with shrug detection in main.py. Finalized gesture thresholds for 3D command execution. |
| **Day 33** | Feb 16 | **System State & Spatial Health :** Implemented persistent toggle logic with debouncing. Engineered a posture monitoring system using neck-to-shoulder displacement for real-time health alerts. |
| **Day 34** | Feb 17 | **Hardware Interfacing :** Successfully mapped gesture-based state toggles to system audio via pyautogui. Finalized the MediaPipe training phase. |
| **Day 35** | Feb 18 | **Modular Object Detection :** Engineered object_engine.py using a class-based architecture. Implemented GPU-accelerated YOLOv8 inference and data serialization (JSON-like dictionary outputs) for real-time tracking. |
| **Day 36** | Feb 19 | **Spatial Data Inspection:** Optimized object_engine.py to extract raw $xywh$ Tensors. Implemented a Logic Gate to filter detections by Aspect Ratio ($>1.2$) and real-time Area Calculation for laptop targets. |
| **Day 37** | Feb 20 | **Data Serialization & Tensor Parsing:** Refined detection loop to parse raw ultralytics Results objects. Extracted human-readable labels and confidence scores while mapping spatial metadata (Width/Height) to real-time object metrics. |
| **Day 38** | Feb 21 | **Data Parsing & Geometry Mapping:** Refined the results loop to extract raw $xywh$ dimensions. Implemented real-time Area and Aspect Ratio calculation logic for object-specific telemetry.  |
| **Day 39** | Feb 22 | **Temporal Spatial Tracking:** Successfully implemented model.track() with persistent ID states. Engineered a real-time distance estimation loop using monocular vision geometry and cv2 telemetry overlays.  |
| **Day 40** | Feb 23 | **Multi-Object Distance Logic:** Refined monocular depth estimation using a dictionary-based lookup for real-world widths ($W_{real}$). Integrated real_width mapping to allow seamless switching between phone and bottle detection.  |
| **Day 41** | Feb 24 | **Real-Time Frequency Aggregation:** Integrated a dynamic object counter into the monocular distance estimation pipeline. Implemented an auto-stacking UI overlay to display class-specific totals alongside spatial telemetry.  |
| **Day 42** | Feb 25 | **Velocity Estimation Engine:** Implemented temporal distance tracking using time.time() deltas. Developed a tracking history buffer to calculate real-time object speed (cm/s) based on monocular depth shifts.  |
| **Day 43** | Feb 26 | **Visual Spatial Overlay:** Integrated real-time spatial metrics (Area/Ratio) directly into the OpenCV rendering pipeline. Developed an automated object summary generator for static image inference on an RTX 2050.  |
| **Day 44** | Feb 27 | **Temporal Signal Smoothing:** Developed a velocity stabilization layer using a Moving Average Buffer. Reduced pixel-jitter noise in speed calculations, resulting in a consistent cm/s telemetry output for tracked objects.  |
| **Day 45** | Feb 28 | **YOLO Fundamentals (Re-Zero):** Analyzed One-Stage detection theory (Backbone vs. Head). Implemented manual benchmarking for RTX 2050 inference speeds (~19 FPS) and engineered a targeted filtering logic gate using COCO Class ID 3 (Motorcycles) with NMS tuning. |
| **Day 46** | Mar 1 | **Live Inference & Spatial UI:** Transitioned to manual rendering of YOLOv8 outputs. Engineered a dynamic labeling system using (x1-y1) offsets to anchor metadata to moving targets. Implemented frame-mirroring logic for natural-view webcam interaction and benchmarked live inference stability. |
| **Day 47** | Mar 02 | **Temporal Logic & Real-Time Aggregation:** Engineered a frame-resetting counter system to manage dynamic populations in live video. Successfully implemented additive assignment logic ($+=1$) to calculate real-time "Person" occupancy within a mirrored OpenCV pipeline. |
| **Day 48** | Mar 03 | **Dynamic UI & Loop Decoupling:** Successfully engineered a multi-object telemetry dashboard. Implemented frame-level coordinate resetting for stable Y-axis text distribution and decoupled the detection loop from the rendering loop to ensure UI consistency in real-time streams. |
| **Day 49** | Mar 04 | **Boolean Alert Systems:** Implemented a full-screen alert engine triggered by occupancy thresholds. Engineered a global 'Alert Mode' state to dynamically alter UI color palettes and render situational overlays based on real-time population density. |
| **Day 50** | Mar 05 | **Spatial Logic & Virtual Fencing:** Engineered a real-time Region of Interest (ROI) system. Implemented centroid-based ($cx$) boundary detection to trigger situational alerts. Mastered resolution-independent UI anchoring to provide dynamic visual feedback for intruders. |
| **Day 51** | Mar 06 | **AI UX & Temporal Tracking:** Engineered a semi-transparent 'Red Zone' using OpenCV Alpha Blending (addWeighted) for visual ROI demarcation. Migrated from static detection to ByteTrack-based persistence to prepare for unique object ID counting and jitter reduction on the RTX 2050. |
| **Day 52** | Mar 07 | **Persistent Identity & Set Logic:** Successfully migrated to `model.track()` for temporal object persistence. Implemented Python Sets to manage unique ID tracking, resolving the issue of redundant counts and establishing the architecture for a "Unique Visitor" metrics dashboard. |
| **Day 53** | Mar 08 | **Security Event Auditing & Tripwire Logic:** Developed a conditional filtering system using `model.track()` and Python Sets. Engineered a digital tripwire that only logs unique IDs upon spatial violations ($cx < gate\_line\_x$), effectively creating a persistent security audit log on the RTX 2050. |
| **Day 54** | Mar 09 | **Performance Monitoring & FPS Benchmarking:** Integrated a real-time temporal calculation engine to monitor inference speeds. Established a baseline for the RTX 2050's performance while simultaneously running ByteTrack persistence and alpha-blended UI overlays. |
| **Day 55** | Mar 10 | **Evidence Archiving & Temporal Versioning:** Engineered an automated capture system with unique timestamp string formatting (`YMD_HMS`) to prevent file overwriting. Integrated membership testing to ensure single-event capture per unique ID, optimizing local storage I/O. |
| **Day 56** | Mar 11 | **Persistent Storage Implementation:** Successfully integrated SQLite3 for cross-session data logging. Engineered a conditional SQL query pipeline to prevent redundant file I/O and established a permanent audit trail for security events on the RTX 2050. |
| **Day 57** | Mar 12 | **End-to-End System Persistence:** Finalized the integration of SQLite3 as the primary backend. Engineered a `sync_memory()` function to reconstruct local object states from historical data. Implemented high-fidelity temporal overlays (Live CCTV Clock) and resolution-independent UI anchoring on the RTX 2050. |
| **Day 58** | Mar 13 | **Visual Evidence Refactoring:** Optimized the capture pipeline to save 'marked' frames with burnt-in UI overlays (timestamps/zones). Established state-persistence logic to ensure data integrity between the CV2 rendering engine and the SQLite backend. |
| **Day 59** | Mar 14 | **Logic Integrity Patch:** Refactored the event-writing block to use persistent state variables (`current_intruder_id`). This ensures data synchronization between the tracking engine and the SQLite backend remains accurate during multi-object frames. |
| **Day 60** | Mar 15 | **System Health Monitoring:** Implemented a real-time status dashboard overlay. Optimized the UI layer to provide visual confirmation of Database connectivity and Model state, improving the UX for end-user security operators. |
| **Day 61** | Mar 16 | **Session Analytics:** Integrated a live runtime clock into the status dashboard to monitor system uptime and hardware stability. |
| **Day 62** | Mar 17 | **Intelligent Event Throttling:** Successfully implemented a dictionary-based cooldown system. Optimized storage I/O by enforcing a 30-second re-entry delay, ensuring high-value evidence capture without redundant data bloat. |
| **Day 63** | Mar 18 | **Dynamic Directory Indexing:** Engineered an automated date-based archiving system. Implemented dynamic pathing logic to categorize evidence by temporal metadata, optimizing filesystem performance. |
| **Day 64** | Mar 19 | **Automated Audit Reporting:** Engineered a local text-logging engine. Implemented recursive file-writing logic to generate daily security summaries within date-stamped directories for the Hexer Services suite. |
| **Day 65** | Mar 20 | **Resource Management & Data Integrity:** Implemented explicit connection termination logic for the SQLite3 backend. Ensured graceful teardown of database handles to prevent header corruption on the Asus TUF A15. |
| **Day 66** | Mar 21 | **Multi-Stage Spatial Logic:** Engineered a dual-zone boundary system (Warning vs. Critical). Implemented nested conditional logic gates to manage situational alerts based on real-time centroid proximity, enhancing the security depth of the Hexer suite on the RTX 2050. |
| **Day 67** | Mar 22 | **Reactive UI State Management:** Engineered a dynamic color-coding system for real-time visual feedback. Implemented conditional BGR color mapping to differentiate between Warning and Critical zones, improving the situational awareness of the Hexer Security interface. |
| **Day 68** | Mar 24 | **Resolution-Independent Rendering:** Engineered a dynamic scaling engine for the OpenCV UI layer. Implemented width-based font and thickness calculation logic to ensure visual consistency across various hardware display outputs on the RTX 2050. |
| **Day 69** | Mar 27 | **Fault-Tolerant System Architecture:** Implemented a global exception handling layer using try-except-finally blocks. Engineered a guaranteed resource teardown protocol to preserve data integrity during unexpected hardware interrupts on the Asus TUF A15. |
| **Day 70** | Mar 28 | **Custom Model Training Prep:** Pivoted from UI features to the core Deep Learning pipeline. Engineered the YAML configuration for transfer learning and initialized the training environment for the RTX 2050. |
| **Day 71** | Mar 29 | **Execution Logic for Model Training:** Engineered the training script for GPU-accelerated transfer learning. Optimized hyperparameters (Epochs/Imgsz) for the RTX 2050 |
| **Day 72** | Mar 31 | **Dataset-Model Integration:** Successfully engineered a 5-sample custom dataset using mobile-captured imagery. Initialized a "Sanity Check" training pipeline on the RTX 2050 to validate YOLO label-image synchronization for the Hexer vision suite |
| **Day 73** | Apr 1 | **Backend Genesis & API Foundations:** Initialized the "Nervous System" phase using FastAPI. Engineered a basic asynchronous server architecture and successfully verified the first "Hello Hexer" heartbeat via a Uvicorn-hosted local environment |
| **Day 74** | Apr 2 | **Hardware Telemetry & OOP Integration:** Engineered a SystemEngine class to bridge the FastAPI backend with local hardware. Successfully implemented real-time RAM monitoring and verified dynamic data output (77.5% load) via the web interface |
| **Day 75** | Apr 3 | **Data Validation & Pydantic Integration:** Implemented BaseModel schemas for type-safe API responses. Verified successful data routing (200 OK) after debugging initial URI typos |
| **Day 76** | Apr 4 | **Full-Stack Decoupling:** Successfully implemented Static File mounting and Jinja2 template rendering. Migrated styling to an external CSS file and verified dynamic data injection (RAM Usage) for the Hexer AI Dashboard on the RTX 2050 |
| **Day 77** | Apr 5 | **Advanced Telemetry Injection:** Engineered a multi-variable data pipeline. Integrated real-time CPU frequency and Disk usage monitoring alongside RAM telemetry into the Hexer Dashboard |
| **Day 78** | Apr 6 | **Network I/O Implementation:** Engineered real-time network throughput tracking (MB Sent/Received). Optimized telemetry pipeline to monitor data flow for future remote AI inference |
| **Day 79** | Apr 7 | **Storage Capacity Analytics:** Integrated deep-disk telemetry. Engineered logic to calculate and display Total vs. Free storage in GB for the Hexer Services infrastructure |
| **Day 80** | Apr 8 | **Temporal System Diagnostics:** Implemented boot_time tracking using psutil and datetime. Engineered logic to convert Unix timestamps into human-readable uptime markers for the Hexer Services dashboard |
| **Day 81** | Apr 9 | **Multi-Core Architecture Mapping:** Integrated cpu_count telemetry. Engineered logic to differentiate between physical cores and logical threads for future AI parallel processing |
---

## 📈 Consistency Tracking
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Nabeel-najeem&show_icons=true&theme=dark)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Nabeel-najeem&layout=compact&theme=dark)

---

## 🛡️ Core Principles
1. **Continuous Growth:** Tech evolves daily; my scripts evolve with it.
2. **Clean Code:** Prioritizing modularity and efficient logic in every commit.
3. **Habit over Motivation:** Committing code every single day to stay ahead.

---
*Last updated: march 2026*