# Enter the desired title for the graph as 'graph_title'
title = 
# Enter the names of the 20 Excel files you want to consider in the analysis as 'data/name_of_file.xlsx'
filename0 = 
filename1 = 
filename2 = 

filename3 = 
filename4 = 
filename5 = 

filename6 = 
filename7 = 
filename8 = 

filename9 = 
filename10 = 
filename11 = 

filename12 = 
filename13 = 
filename14 = 

filename15 = 
filename16 = 
filename17 = 

filename18 = 
filename19 = 
filename20 = 






# Ignore
import project

project.graph(title,
              filename0, filename1, filename2,
              filename3, filename4, filename5,
              filename6, filename7, filename8,
              filename9, filename10, filename11,
              filename12, filename13, filename14,
              filename15, filename16, filename17,
              filename18, filename19, filename20)

project.mean(filename0, filename1, filename2)

project.std(filename0, filename1, filename2)
