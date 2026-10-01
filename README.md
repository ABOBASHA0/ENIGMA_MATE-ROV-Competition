# ENIGMA — MATE ROV Competition 🤿

Welcome to the official GitHub repository of **ENIGMA**, a student team participating in the **MATE ROV Competition**.

This project is the beginning of our journey in underwater robotics, where we are designing and developing an ROV capable of performing different underwater tasks required by the competition.

---

## 📌 Quick Navigation

* [About the Project](#-about-the-project)
* [Software Description](#-software-description)
* [Technologies](#-technologies)
* [Setup & Installation](#-setup--installation)
* [Project Structure](#-project-structure)
* [Competition Progress](#-competition-progress)

---

## 🚀 About the Project

Our ROV combines **mechanical design, electronics, programming, computer vision, and autonomous systems** into one integrated platform.

This repository contains the software and development work created by the **ENIGMA** team for the MATE ROV Competition.

---

## 💻 Software Description

The ENIGMA software is designed to act as the main interface for operating and monitoring our ROV.

It provides tools for controlling the ROV, viewing multiple cameras, processing underwater images, detecting objects, recording mission data, and helping the team complete the required competition tasks.

The software is being developed continuously as our ROV and competition requirements evolve.

### Main Features

* Multi-camera video system
* ROV camera switching and monitoring
* Object detection and computer vision
* Real-time data visualization
* Mission and task timers
* Image and video recording
* Underwater measurements
* Navigation and map support
* ROV mission management

---

## 🛠️ Technologies

The project currently uses:

* Python
* PyQt5
* Qt Designer
* OpenCV
* Roboflow
* Supervision
* NumPy
* CSV data processing

---

## ⚙️ Setup & Installation

### Requirements

Before running the software, make sure you have:

* Windows
* Python **3.10.x**
* Git
* Qt Designer
* A working camera setup for camera-related features

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install the Required Packages

If the repository contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages manually:

```bash
pip install PyQt5
pip install opencv-python
pip install numpy
pip install supervision
```

Additional packages may be required depending on the computer-vision and Roboflow components used by the project.

### 4. Run the Application

After installing the dependencies:

```bash
python main.py
```

> The main Python file may be different depending on the current version of the project.

---

## 📁 Project Structure

The project is organized into different components for the ROV software, including the user interface, camera system, computer vision, data visualization, and mission tools.

The structure may change as ENIGMA continues developing the project.

---

## 🏁 Competition Progress

This repository will grow throughout our **MATE ROV Competition** journey.

We are currently at the beginning of the competition, so the project is still under active development.

Future updates will include new features, improvements, testing results, and solutions developed by the ENIGMA team.

---

## 🤿 ENIGMA

**One team. One ROV. One mission.**
