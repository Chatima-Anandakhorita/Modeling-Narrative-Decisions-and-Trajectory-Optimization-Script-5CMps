
# Modeling Narrative Decisions and Trajectory Optimization in "5 Centimeters per Second" Using Weight-Directed Graphs

This repository contains the discrete computational state-space simulation framework developed to quantify and optimize emotional trauma trajectories within qualitative narrative structures. Using Makoto Shinkai's 2007 film "5 Centimeters per Second" as a behavioral case study, this project models decision paths, lifestyle modifications, and environmental stressors as a mathematical network topology.

## Repository Structure

* **`story_data.py`**: Defines the master weight-directed graph configuration, consisting of 20 narrative nodes and 25 directed transition edges embedded with localized trauma costs (c) and conditional probabilities (p).
* **`analyze.py`**: The core computational execution engine containing the algorithmic pipelines for graph traversal and state optimization.

## Core Algorithmis
The execution engine evaluates the state machine architecture through two distinct discrete mathematical protocols:

1.  **Dijkstra's Shortest Path Algorithm**
    * **Objective**: Computes the absolute cost-minimized path of emotional self-preservation across a lifecycle, establishing a baseline mathematical "survival strategy".
    * **Implementation**: Utilizes min-priority queue relaxation vectors targeting global trauma value accumulation as distance metrics.

2.  **Depth-First Search (DFS) Timeline Traversal**
    * **Objective**: Exhaustively maps the entire narrative spectrum across all 16 distinct alternative timelines.
    * **Implementation**: Traces global joint probability matrices alongside compounding cumulative trauma debts. Includes dynamic tracking flags to properly calculate the truncated infinite geometric tail of cyclic overwork nodes without recursive stack overflows.

## Technical Prerequisites & Usage

### Setup
Ensure you have Python 3.x installed on your local workstation. Clone this repository using the following terminal commands:

```bash
git clone [https://github.com/anandakhoritac-hub/Modeling-Narrative-Decisions-and-Trajectory-Optimization-Script-5CMps.git](https://github.com/anandakhoritac-hub/Modeling-Narrative-Decisions-and-Trajectory-Optimization-Script-5CMps.git)
cd Modeling-Narrative-Decisions-and-Trajectory-Optimization-Script-5CMps

```

### Running the Engine

Execute the processing engine to calculate path efficiencies, total trauma outputs, and probability distributions:

```bash
python analyze.py

```

## Key Analytical Insights

* **Canonical Trajectory Suboptimality**: The simulation identifies the film's canonical track as a trajedy triggered by compounding low-probability stressors (P_joint = 1.3%), accumulating 310 trauma units.
* **Path Efficiency Coefficient**: Comparing the canonical storyline against the optimized Dijkstra baseline (C = 70) yields a Path Efficiency Coefficient (eta) of 22.6%, mathematically demonstrating the severity of maladaptive human coping mechanisms over pure algorithmic optimization models.

## Academic Affiliation

* **Author**: Chatima Anandakhorita (NIM: 13525133)
* **Institution**: Program Studi Teknik Informatika, Sekolah Teknik Elektro dan Informatika, Institut Teknologi Bandung
* **Course Assignment**: Makalah IF1220 Matematika Diskrit (Semester II Tahun 2025/2026)

```

```
