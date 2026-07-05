# JeevanNet: When Silence Speaks
> **Passive Early Warning Infrastructure for Student Mental Health Support using Computer Vision & Edge AI**

---

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)
![Environment](https://img.shields.io/badge/environment-conda-green.svg)
![Framework](https://img.shields.io/badge/Framework-OpenCV%20%7C%20FER-orange.svg)

JeevanNet is a non-intrusive, privacy-first edge computing system integrated with campus CCTV infrastructure. It is engineered to capture subtle indicators of severe emotional distress, anxiety, and depression before they escalate—without expecting vulnerable students to actively self-report or initiate help-seeking behavior.

---

## 👥 Contributors (Project Team)

* **Pratik Tekale**
* **Arya Mohanrao Mandke**
* **Anushka Mandwade**
* **Samiksha Ravankole**

*Project Category: AI Health Detector*

---

## 📌 The Problem: A Crisis We Don't See

Most modern psychological interventions rely on **active self-reporting** (apps, quizzes, counselor visits). JeevanNet operates where students don't—or can't—vocalize their pain.

### 📊 Vital Statistics & Regional Insights

| Metric / Insight | Detail / Impact | Source |
| :--- | :--- | :--- |
| **Annual Student Suicides** | **13,044 deaths** recorded in India (2022 data) | National Crime Records Bureau (NCRB) |
| **Year-over-Year Growth** | Compounding at an average rate of **2% annually** | IC3 Institute |
| **Critical Milestone** | Student suicide rates have officially **surpassed farmer suicides** | India Today |
| **Female Student Trend** | Suicides **increased by 7%** (while male student numbers fell 6%) | Times of India |
| **Regional Hotspots** | **Highest volumes** reported in Maharashtra, Tamil Nadu, and MP | Mint |

---

## 👁️ The Vision: A Silent AI Guardian

JeevanNet introduces a paradigm shift from **reactive counseling** to **proactive early intervention**:

### ⚙️ How JeevanNet Works
1. **Passive Detection:** Works autonomously in public campus areas using existing CCTV cameras, minimizing setup costs and maximizing coverage.
2. **Privacy by Design:** Local edge computing (optimized for NVIDIA Jetson Nano hardware) ensures **zero raw video is saved or transmitted**. Video feeds are instantly discarded after local feature extraction, keeping data entirely anonymous.
3. **Selective Emotion Weights:** The system deliberately ignores common positive emotions (joy, surprise, excitement) to minimize compute overhead and prevent overfitting. It isolates specific withdrawal behaviors:
   * **Flat Affect:** Slowed or complete lack of variable facial micro-expressions.
   * **Physical Gaze Indicators:** Prolonged, downward-facing gaze angles and lack of eye contact.
   * **Posture Tracking:** Consistent slouched posture and long periods of social withdrawal from peers.

> 💡 **Preventing Alert Fatigue (The 3-Day Rolling Window)**
> To avoid false alerts caused by normal daily mood swings (e.g., getting a bad grade, a temporary disagreement, or a stressful exam morning), **JeevanNet does not trigger immediate alarms**. Alerts are only routed to trained mental health staff on the **Silent Alert Dashboard** if indicators of emotional distress remain consistently elevated over a continuous **72-hour window**.

---
## 🚀 Technical Implementation

### System Prerequisites
The prototype has been validated on **Windows** and **Linux (Ubuntu)** environments utilizing **Python 3.9**.

### Installation & Environment Setup
To ensure version alignment for libraries including TensorFlow, PyTorch, and OpenCV, configure your environment using our exported YAML setup parameters:

```bash
# 1. Clone this repository
git clone [https://github.com/Aarya-505/JeevanNet.git](https://github.com/Aarya-505/JeevanNet.git)
cd JeevanNet

# 2. Build the exact conda environment configuration
conda env create -f jeevannet_env.yml

# 3. Activate the virtual environment
conda activate JeevanNet

---

### Running the Live Prototype
To initialize local webcam capture and test the pre-trained neural networks:

```bash
python main.py

Press q to safely close the active window and clean up processing threads.

---

### License
This project is licensed under the GNU General Public License v3.0 (GPL-3). You are free to inspect, deploy, and modify this source code, provided all derivative projects remain fully open-source and preserve standard attribution to the original team.

Developed under the vision of creating empathetic, life-saving spaces across global academic institutions.
