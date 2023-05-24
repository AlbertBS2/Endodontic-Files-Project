# The influence of the heat treatment on the endodontic files

## Table of Contents
[I. Description](#description)  
[II. Prerequisites](#prerequisites)     
[III. Usage](#usage)    
[IV. File Structure](#file-structure)   
[V. Contributing](#contributing)

## Description
This Python project processes multiple .xlsx result files to generate a graph combining all the results. It also provides tables with mean and standard deviation calculations. The 'launcher.py' file serves as the main entry point for the analysis.

## Prerequisites
Make sure you have the following installed:

- Python
- Pandas library
- Matplotlib library

## Usage
1. Open the launcher.py file.
2. Modify the following variables:
    - *title*: Enter the desired title for the graph.
    - *filename0* to *filename20*: Enter the names of the 20 Excel files you want to consider in the analysis.
4. Save the changes to launcher.py.
5. Run the launcher.py file.

## File Structure
The project has the following structure:
- 'launcher.py': Main script to launch the analysis.
- 'project.py': Python module containing functions to generate the graph and tables.
- 'data/': Directory containing the input Excel files.

## Contributing
Contributions are welcome! If you find any issues or want to enhance this project, feel free to open a pull request.
