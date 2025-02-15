# Heat Treatment's Influence on Endodontic Files

## Table of Contents
[I. Description](#description)  
[II. Installation](#installation)    
[III. Usage](#usage)    
[IV. File Structure](#file-structure)   

## Description
This Python project processes multiple .xlsx files (containing results from tests performed on endodontic files) to generate a graph combining all the results. It also provides tables with mean and standard deviation calculations.

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Endodontic-Files-Project.git
   ```
  
2. Install required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Open the launcher.py file.
2. Modify the following variables:
    - *title*: Enter the desired title for the graph.
    - *filenames*: Enter the names of the 21 Excel files (in groups of 3) you want to consider in the analysis.
4. Save the changes to launcher.py.
5. Run the launcher.py file.

## File Structure
The project has the following structure:
- 'launcher.py': Main script to launch the analysis.
- 'project.py': Python module containing functions to generate and save the graph and tables.
- 'data/': Directory containing the input Excel files.
- 'results/': Directory to store the graph and tables generated.
