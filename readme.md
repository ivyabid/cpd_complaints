# Investigating Chicago Police Department complaint data

This project had two major goals, namely:
- investigate overall rates of discipline in CPD to see if creating IPRA (an independent, but unelected investigatory board comprised largely of former police officers) had any impact on how often police were disciplined

- to build a model that could identify the features most correlated with discipline, and predict outcomes of unresolved complaints


# Data
All data from this project was obtained from the [Citizens Police Data Project](https://cpdp.co/). I specifically focused on complaint data and overall officer demographic data. I specifically did not bring TRR data (use of serious force or weapons against a police target) into my analysis to constrain the tone of the project to daily police misconduct. Analysis that includes TRR data is available at the CPDP website.

# Complaint Presentation
This presentation summarizes major findings of the investigation in this project, as well as the model

# Code Folder
setup-cpdp-sql: schema for creating a SQL database used in CPDP_dataclean notebook

Jupyter Notebooks:
CPDP_dataclean - importing the raw data from SQL, pre-processing, and simplifying features

CPDP_modelling - includes the full modelling workflow and optimization of parameters

CPDP_plotly - raw code used to create visualizations found in the project