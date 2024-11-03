# Enter the title for the graph
title = "Graph Title"

# File paths for each group of measurements
# Enter paths as 'data/filename.xlsx' for each file
group1_files = [
    "data/file1.xlsx",
    "data/file2.xlsx", 
    "data/file3.xlsx"
]

group2_files = [
    "data/file4.xlsx",
    "data/file5.xlsx",
    "data/file6.xlsx"
]

group3_files = [
    "data/file7.xlsx", 
    "data/file8.xlsx",
    "data/file9.xlsx"
]

group4_files = [
    "data/file10.xlsx",
    "data/file11.xlsx",
    "data/file12.xlsx"
]

group5_files = [
    "data/file13.xlsx",
    "data/file14.xlsx", 
    "data/file15.xlsx"
]

group6_files = [
    "data/file16.xlsx",
    "data/file17.xlsx",
    "data/file18.xlsx"
]

group7_files = [
    "data/file19.xlsx",
    "data/file20.xlsx",
    "data/file21.xlsx"
]

# Combine all files in order
all_files = (
    group1_files + group2_files + group3_files + group4_files +
    group5_files + group6_files + group7_files
)

# Import and run analysis
import project

project.graph(title, *all_files)
project.mean(*group1_files)
project.std(*group1_files)
