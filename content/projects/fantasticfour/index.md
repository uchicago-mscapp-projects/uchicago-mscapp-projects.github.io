---
date: "2025-03-11"
tags: []
title: "Chicago Living Score Interactive Map"
authors: ['Lydia Liu', 'Yuri Chang', 'Hamza Tariq', 'Alejandro Armas']
courses: ["30122-W25"]
---

{{< github repo="uchicago-2025-capp30122/30122-project-fantasticfour" >}}

{{< youtube TODO >}}

This project develops an interactive, map-based platform to help individuals—especially those considering a move to Chicago—assess potential housing options. By incorporating index data like housing price, education resources, transit infrastructure, safety, the platform offers a comprehensive overview of an area's livability.

Our website offers two core services:

In the Service interface, users can enter a specific ZIP code (e.g., 60605) to receive a detailed breakdown of that area's individual indicators and overall Living Score. Alternatively, users may input a specific indicator keyword (such as “education” or “crime”) to visualize the performance of that indicator across different regions on an interactive map.

The Analysis interface provides an immediate, visual overview of the top 5 best and top 5 worst areas based on the overall Living Score, offering users a quick reference to compare different neighborhoods.

Leveraging Folium for map visualizations and Flask for backend integration, our platform delivers a dynamic and insightful experience that empowers users to explore Chicago’s livability landscape and make informed housing decisions.
