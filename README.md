# Python-Entropy-of-FileNames-in-a-CSV

# Overview

Current Work in Progress, not allowed to show what type of data due to related to senstive infomation. 

This Python script analyzes a CSV file containing system execution logs, extracts file paths, and calculates entropy scores using Shannon entropy. The script is designed to help identify anomalous or suspicious executable file names by sorting and displaying the top 10 highest and lowest entropy values.

As part of the Elevance Health - The Data Mine initiative, this script plays a crucial role in cybersecurity anomaly detection by analyzing entropy variations in executable paths. Identifying high-entropy file names can help detect potential security threats, unauthorized processes, or malicious software execution patterns.

# Features

1. Extracts executable file names from command line entries using regex.

2. Computes Shannon entropy to measure randomness in file names.

3. Identifies the top 10 highest and lowest entropy file names.

4. Displays results in tabular format.

5. Generates bar charts for visualization.


# Contribution to The Data Mine - Elevance Health Project

This script enhances cybersecurity research within The Data Mine - Elevance Health project by:

1. Threat Detection: Identifying anomalous executable file names indicative of malware or unauthorized system processes.

2. Data Preprocessing: Preparing structured datasets for machine learning models that predict security risks.

3. Live Monitoring & Anomaly Detection: Enabling automated analysis of system logs to flag irregular activities in real time.
