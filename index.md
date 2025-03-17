# Multi-Robot Task Cooperation (MRTC) Demo

**Efficient coordination of Unmanned Sanitation Vehicles (USVs) for urban cleaning.**

---

## Abstract

As urbanization scales up, the use of unmanned sanitation vehicles (USVs) for automated urban cleaning has gained significant attention. However, efficiently coordinating multiple USVs in large-scale areas (e.g., city-level) to perform cleaning tasks at low cost remains a major challenge. This is due to the complex interplay between dynamic environmental needs and the constraints of the USVs (e.g., waste transport capacity and battery life). We first identify the USV Collaborative Operation Problem (USVCOP) as a new challenge that remains unsolved due to significant difficulties such as individual USV resource limitations and the coupling of tasks across multiple USVs. To tackle this, we propose a multi-robot task cooperation system, MRTC. Our MRTC adopts an alternating optimization strategy to solve the optimization problem via two steps: 1) Dynamic Task Assignment, which uses a Markov decision process and an Actor-Critic algorithm to allocate cleaning tasks and determine the required number of USVs; and 2) Single-USV Path Planning, which optimizes USV paths using a two-layer iterative search. Extensive experiments demonstrate that our MRTC can reduce the system operation cost and improve the USV operation efficiency, with an average 13.68% decrease and 18% improvement with SOTA. Through collaboration with commercial companies, we deployed this system in three different areas, in which the total average driving distances reach 10,775 km per month, with estimated average savings of 20,575 kWh and 2,744 working hours per month.

---

## Demonstration Video

<video width="100%" controls>
    <source src="Demo.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

---

## Overview

MRTC is a novel system designed for coordinating multiple USVs in urban cleaning. It optimizes task assignment and path planning, reducing costs and improving efficiency.

---

## Key Features

- **Dynamic Task Assignment with AI**
- **Optimized Multi-USV Path Planning**
- **Real-time Adaptation to Environmental Changes**
- **Cost-effective Cleaning Operations**
- **Seamless Fleet Coordination**
- **Sustainable and Energy-efficient Solutions**

---

## Experimental Results

- Operation cost reduced by **13.68%**
- Efficiency improved by **18%** compared to SOTA
- Total driving distance: **10,775 km/month**
- Energy savings: **20,575 kWh/month**
- Labor savings: **2,744 working hours/month**

---

## Code Repository

Access the source code and implementation details on GitHub:

[![GitHub](https://img.shields.io/badge/View%20on%20GitHub-181717?logo=github)](https://github.com/example/MRTC)

---

<footer>
    <p>&copy; 2025 MRTC Research Team. All Rights Reserved.</p>
</footer>
