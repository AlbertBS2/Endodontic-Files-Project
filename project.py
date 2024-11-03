import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def create_df(filename0, filename1, filename2):
    def process_single_file(filename):
        # Read and preprocess data
        df = pd.read_excel(filename, sheet_name=1)
        df = df.drop([0, 1])
        df = df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Force'})
        df['Time'] = pd.to_numeric(df['Time'])
        df['Force'] = pd.to_numeric(df['Force'])
        
        # Time ranges for cycles
        time_ranges = [
            (0, 20), (25, 45), (45, 65), (95, 115),
            (140, 160), (190, 210), (235, 255), (280, 300), (330, 350)
        ]
        
        cycles = []
        max_penetrations = []
        min_penetrations = []
        max_removals = []
        min_removals = []
        
        # Process each cycle
        for start, end in time_ranges:
            # Filter data for cycle
            cycle_data = df[(df['Time'] >= start) & (df['Time'] <= end)]
            
            # Create cycle dataframe
            cycle = cycle_data[['Time']].copy()
            cycle['pos'] = cycle_data['Force'].where(cycle_data['Force'] > 0)
            cycle['neg'] = cycle_data['Force'].where(cycle_data['Force'] < 0)
            
            cycles.append(cycle)
            
            # Calculate statistics
            max_penetrations.append(cycle['pos'].max())
            min_penetrations.append(cycle['pos'].min())
            max_removals.append(cycle['neg'].max())
            min_removals.append(cycle['neg'].min())
            
        # Create results dataframe
        d = {filename[:-5]: [f'Cycle {i}' for i in range(9)],
             'Min Penetration': min_penetrations,
             'Max Penetration': max_penetrations,
             'Min Removal': max_removals,
             'Max Removal': min_removals}
             
        return pd.DataFrame(data=d)

    # Process all three files
    res0 = process_single_file(filename0)
    res1 = process_single_file(filename1) 
    res2 = process_single_file(filename2)

    # Concatenate results
    df_concat = pd.concat([
        res0[res0.columns[1]], res1[res1.columns[1]], res2[res2.columns[1]],
        res0[res0.columns[2]], res1[res1.columns[2]], res2[res2.columns[2]], 
        res0[res0.columns[3]], res1[res1.columns[3]], res2[res2.columns[3]],
        res0[res0.columns[4]], res1[res1.columns[4]], res2[res2.columns[4]]
    ], axis=1)

    # Calculate mean results
    d1 = {filename1[5:-7]: [f'Cycle {i}' for i in range(9)],
          'Min Penetration': df_concat.iloc[:, :3].mean(axis=1),
          'Max Penetration': df_concat.iloc[:, 3:6].mean(axis=1),
          'Min Removal': df_concat.iloc[:, 6:9].mean(axis=1),
          'Max Removal': df_concat.iloc[:, 9:].mean(axis=1)}
    
    df_mean = pd.DataFrame(data=d1)

    # Calculate standard deviation
    d2 = {filename1[5:-7]: [f'Cycle {i}' for i in range(9)],
          'Min Penetration': df_concat.iloc[:, :3].std(axis=1),
          'Max Penetration': df_concat.iloc[:, 3:6].std(axis=1),
          'Min Removal': df_concat.iloc[:, 6:9].std(axis=1),
          'Max Removal': df_concat.iloc[:, 9:].std(axis=1)}
    
    df_std = pd.DataFrame(data=d2)
    df_std = df_std.iloc[3:, [0, 2, 4]].round(2)

    df_mean2 = df_mean.drop([0, 1, 2])

    # Select required columns
    df_selected1 = df_mean2.iloc[:, [0, 2]]  # Columns 1 and 3
    df_selected2 = df_mean2.iloc[:, [0, 4]]  # Columns 1 and 5

    return [df_mean2, df_std, df_selected1, df_selected2]

def graph(title, *filenames):
    if len(filenames) != 21:
        raise ValueError("Expected 21 filenames (7 groups of 3 files)")
        
    # Plot settings
    bar_width = 0.08
    fig, ax = plt.subplots(figsize=(13, 6))
    positions = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]
    colors = ['blue', 'darkorange', 'green', 'r', 'purple', 'chocolate', 'darkturquoise']
    legend_labels = []
    
    # Process each group of 3 files
    for i in range(0, 21, 3):
        group_files = filenames[i:i+3]
        group_idx = i // 3
        
        # Get data for this group
        results = create_df(*group_files)
        df_selected1, df_selected2 = results[2], results[3]
        df_std = results[1]
        
        std1 = df_std.iloc[:, 1].tolist()
        std2 = df_std.iloc[:, 2].tolist()
        
        # Plot bars for this group
        df_selected1.plot(kind='bar', x=df_selected1.columns[0], y=df_selected1.columns[1], 
                         ax=ax, width=bar_width, position=positions[group_idx],
                         color=colors[group_idx], yerr=std1, capsize=2.5)
                         
        df_selected2.plot(kind='bar', x=df_selected2.columns[0], y=df_selected2.columns[1],
                         ax=ax, width=bar_width, position=positions[group_idx],
                         color=colors[group_idx], alpha=0.7, yerr=std2, capsize=2.5)
                         
        legend_labels.append(group_files[0][5:-7])

    # Configure plot
    plt.title(title)
    plt.xlabel('Cycles')
    plt.ylabel('Force (N)')
    
    # Add legend
    legend_elements = [Patch(facecolor=color, edgecolor='none', label=label)
                      for label, color in zip(legend_labels, colors)]
    ax.legend(handles=legend_elements)
    
    # Adjust plot limits
    ax.set_xlim(left=ax.get_xlim()[0] - 5 * bar_width, 
                right=ax.get_xlim()[1] + 5 * bar_width)
                
    x_ticks = ax.get_xticks()
    ax.set_xlim(x_ticks[0] - 0.5 * (x_ticks[1] - x_ticks[0]),
                x_ticks[-1] + 0.5 * (x_ticks[1] - x_ticks[0]))

    plt.show()
    plt.savefig(f'results/{title}-graph.png', bbox_inches='tight')
    plt.close()

def mean(filename0, filename1, filename2):
    df_mean2 = create_df(filename0, filename1, filename2)[0]

    df_mean_rounded = df_mean2.round(2)

    selected_columns = [0, 2, 4]
    df_selected = df_mean_rounded.iloc[:, selected_columns]

    plt.axis('off')

    plt.table(cellText=df_selected.values, colLabels=df_selected.columns, cellLoc='center', loc='center')

    plt.savefig(f'results/{filename0[5:-7]}-mean.png')
    plt.show()

    plt.close()

def std(filename0, filename1, filename2):
    df_std = create_df(filename0, filename1, filename2)[1]

    plt.axis('off')

    plt.table(cellText=df_std.values, colLabels=df_std.columns, cellLoc='center', loc='center')

    plt.savefig(f'results/{filename0[5:-7]}-std.png')
    plt.show()

    plt.close()