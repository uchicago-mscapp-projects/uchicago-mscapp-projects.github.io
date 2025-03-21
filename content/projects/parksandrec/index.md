---
date: "2025-03-11"
tags: []
title: "parksAndRec: Understanding the Spatial and Demographic Distribution of Open Space in Chicago"
authors: ['José María (Chema) Gálvez Enríquez', 'Pablo Hernandez Pedraza', 'Raghav Mehrotra', 'Sarah Hussain']
courses: ["30122-W25"]
---

{{< github repo="uchicago-2025-capp30122/30122-project-parksandrec" >}}

{{< youtube kKwFxz4AmzY >}}

This project asks two questions: How is open space spatially distributed across Cook County? Who has access to these open spaces?$

We use 2018 land use data from the Chicago Metropolitan Agency for Planning, which classifies open spaces into five subcategories: Recreational, Golf Courses, Conservation, Non-Public, and Trails/Greenways. We also spatialize Vacant Land from the same dataset to argue that not all open space can be understood in the same way.

To understand who has access to open space (that falls within the five subcategories), we assign each land parcel from the spatial dataset to a census tract, and produce socio-demographic statistics at tract level. We downloaded census tract spatial data from the pygris package and accessed statistical data on the tracts from the American Community Survey API. These include attributes such as median household income, race, and property values. In addition to this visual, we provide the user with an interactive tool that allows them to filter Cook County by specific land use area and understand how that impacts income distributions across Census tracts.
