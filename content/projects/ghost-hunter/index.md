---
date: "2024-03-15"
tags: []
title: "Ghost Hunter"
authors: ["gabe-barrett", "magdalena-barros", "paula-cadena"]
courses: ["30122-W24"]
---

A pervasive problem in the American Healthcare system is the existence of “ghost networks.” These are lists of providers that a health insurance plan falsely presents to healthcare consumers as “in-network.” Ghost Hunter is an application that audits the provider network of County Care, one of Illinois five Medicaid Managed Care Organizations. The goal is to see how what percentage of County Care’s network can be independently verified. First, we scraped County Care’s [find a provider](https://countycare.valence.care/member/#findAProvider) intermittently from February 16th until March 6th, 2024 to construct an original sample database of their healthcare service provider network.  Second, we attempt to verify that each located provider is accurately represented by matching them either in the State of Illinois’ [IMPACT database](https://ext2.hfs.illinois.gov/hfsindprovdirectory) or in the [National NPI Registry](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination). IMPACT is a state database that tracks all providers approved to bill Illinois Medicaid. If no trace of a provider exists in IMPACT, the provider is not eligible to treat patients on Medicaid. The NPI registry is a registry of all individual or corporate entities that need to bill health insurance. Matching on the NPI is important as a way to verify a provider’s contact information and residence in Illinois, as well as a source for future researchers as NPI numbers, are very close to unique identifiers in the healthcare space. From this analysis, we estimate groups of providers that while listed in County Care’s directory are not actually seeing or billing Medicaid patients, and whose presence in County Care’s directory is misleading to patients and inflates the strength of their network. Our initial match percentages reflect the difficulty of linking records with inconsistent identifiers, but we hope that this data can be of use to us and future researchers examining health insurance network adequacy.


{{< github repo="uchicago-mscapp-projects/Ghost-Hunter" >}}

