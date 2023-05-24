import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def create_df(filename0, filename1, filename2):
    df = pd.read_excel(filename0, sheet_name=1)
    df = df.drop([0, 1])
    df = df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Force'})
    df['Time'] = pd.to_numeric(df['Time'])
    df['Force'] = pd.to_numeric(df['Force'])

    df1 = df[df['Time'] <= 20]

    df21 = df[df['Time'] >= 25]
    df2 = df21[df21['Time'] <= 45]

    df31 = df[df['Time'] >= 45]
    df3 = df31[df31['Time'] <= 65]

    df41 = df[df['Time'] >= 95]
    df4 = df41[df41['Time'] <= 115]

    df51 = df[df['Time'] >= 140]
    df5 = df51[df51['Time'] <= 160]

    df61 = df[df['Time'] >= 190]
    df6 = df61[df61['Time'] <= 210]

    df71 = df[df['Time'] >= 235]
    df7 = df71[df71['Time'] <= 255]

    df81 = df[df['Time'] >= 280]
    df8 = df81[df81['Time'] <= 300]

    df91 = df[df['Time'] >= 330]
    df9 = df91[df91['Time'] <= 350]

    cycle1 = df1[['Time']].copy()
    cycle1['pos'] = df1['Force'].where(df1['Force'] > 0)
    cycle1['neg'] = df1['Force'].where(df1['Force'] < 0)

    cycle2 = df2[['Time']].copy()
    cycle2['pos'] = df2['Force'].where(df2['Force'] > 0)
    cycle2['neg'] = df2['Force'].where(df2['Force'] < 0)

    cycle3 = df3[['Time']].copy()
    cycle3['pos'] = df3['Force'].where(df3['Force'] > 0)
    cycle3['neg'] = df3['Force'].where(df3['Force'] < 0)

    cycle4 = df4[['Time']].copy()
    cycle4['pos'] = df4['Force'].where(df4['Force'] > 0)
    cycle4['neg'] = df4['Force'].where(df4['Force'] < 0)

    cycle5 = df5[['Time']].copy()
    cycle5['pos'] = df5['Force'].where(df5['Force'] > 0)
    cycle5['neg'] = df5['Force'].where(df5['Force'] < 0)

    cycle6 = df6[['Time']].copy()
    cycle6['pos'] = df6['Force'].where(df6['Force'] > 0)
    cycle6['neg'] = df6['Force'].where(df6['Force'] < 0)

    cycle7 = df7[['Time']].copy()
    cycle7['pos'] = df7['Force'].where(df7['Force'] > 0)
    cycle7['neg'] = df7['Force'].where(df7['Force'] < 0)

    cycle8 = df8[['Time']].copy()
    cycle8['pos'] = df8['Force'].where(df8['Force'] > 0)
    cycle8['neg'] = df8['Force'].where(df8['Force'] < 0)

    cycle9 = df9[['Time']].copy()
    cycle9['pos'] = df9['Force'].where(df9['Force'] > 0)
    cycle9['neg'] = df9['Force'].where(df9['Force'] < 0)

    # penetration
    max1p = cycle1['pos'].max()
    max2p = cycle2['pos'].max()
    max3p = cycle3['pos'].max()
    max4p = cycle4['pos'].max()
    max5p = cycle5['pos'].max()
    max6p = cycle6['pos'].max()
    max7p = cycle7['pos'].max()
    max8p = cycle8['pos'].max()
    max9p = cycle9['pos'].max()

    min1p = cycle1['pos'].min()
    min2p = cycle2['pos'].min()
    min3p = cycle3['pos'].min()
    min4p = cycle4['pos'].min()
    min5p = cycle5['pos'].min()
    min6p = cycle6['pos'].min()
    min7p = cycle7['pos'].min()
    min8p = cycle8['pos'].min()
    min9p = cycle9['pos'].min()

    # removal
    max1n = cycle1['neg'].max()
    max2n = cycle2['neg'].max()
    max3n = cycle3['neg'].max()
    max4n = cycle4['neg'].max()
    max5n = cycle5['neg'].max()
    max6n = cycle6['neg'].max()
    max7n = cycle7['neg'].max()
    max8n = cycle8['neg'].max()
    max9n = cycle9['neg'].max()

    min1n = cycle1['neg'].min()
    min2n = cycle2['neg'].min()
    min3n = cycle3['neg'].min()
    min4n = cycle4['neg'].min()
    min5n = cycle5['neg'].min()
    min6n = cycle6['neg'].min()
    min7n = cycle7['neg'].min()
    min8n = cycle8['neg'].min()
    min9n = cycle9['neg'].min()

    d = {filename0[:-5]: ['Cycle 0', 'Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 4', 'Cycle 5', 'Cycle 6', 'Cycle 7',
                          'Cycle 8'],
         'Min Penetration': [min1p, min2p, min3p, min4p, min5p, min6p, min7p, min8p, min9p],
         'Max Penetration': [max1p, max2p, max3p, max4p, max5p, max6p, max7p, max8p, max9p],
         'Min Removal': [max1n, max2n, max3n, max4n, max5n, max6n, max7n, max8n, max9n],
         'Max Removal': [min1n, min2n, min3n, min4n, min5n, min6n, min7n, min8n, min9n]}

    res0 = pd.DataFrame(data=d)

    df = pd.read_excel(filename1, sheet_name=1)
    df = df.drop([0, 1])
    df = df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Force'})
    df['Time'] = pd.to_numeric(df['Time'])
    df['Force'] = pd.to_numeric(df['Force'])

    df1 = df[df['Time'] <= 20]

    df21 = df[df['Time'] >= 25]
    df2 = df21[df21['Time'] <= 45]

    df31 = df[df['Time'] >= 45]
    df3 = df31[df31['Time'] <= 65]

    df41 = df[df['Time'] >= 95]
    df4 = df41[df41['Time'] <= 115]

    df51 = df[df['Time'] >= 140]
    df5 = df51[df51['Time'] <= 160]

    df61 = df[df['Time'] >= 190]
    df6 = df61[df61['Time'] <= 210]

    df71 = df[df['Time'] >= 235]
    df7 = df71[df71['Time'] <= 255]

    df81 = df[df['Time'] >= 280]
    df8 = df81[df81['Time'] <= 300]

    df91 = df[df['Time'] >= 330]
    df9 = df91[df91['Time'] <= 350]

    cycle1 = df1[['Time']].copy()
    cycle1['pos'] = df1['Force'].where(df1['Force'] > 0)
    cycle1['neg'] = df1['Force'].where(df1['Force'] < 0)

    cycle2 = df2[['Time']].copy()
    cycle2['pos'] = df2['Force'].where(df2['Force'] > 0)
    cycle2['neg'] = df2['Force'].where(df2['Force'] < 0)

    cycle3 = df3[['Time']].copy()
    cycle3['pos'] = df3['Force'].where(df3['Force'] > 0)
    cycle3['neg'] = df3['Force'].where(df3['Force'] < 0)

    cycle4 = df4[['Time']].copy()
    cycle4['pos'] = df4['Force'].where(df4['Force'] > 0)
    cycle4['neg'] = df4['Force'].where(df4['Force'] < 0)

    cycle5 = df5[['Time']].copy()
    cycle5['pos'] = df5['Force'].where(df5['Force'] > 0)
    cycle5['neg'] = df5['Force'].where(df5['Force'] < 0)

    cycle6 = df6[['Time']].copy()
    cycle6['pos'] = df6['Force'].where(df6['Force'] > 0)
    cycle6['neg'] = df6['Force'].where(df6['Force'] < 0)

    cycle7 = df7[['Time']].copy()
    cycle7['pos'] = df7['Force'].where(df7['Force'] > 0)
    cycle7['neg'] = df7['Force'].where(df7['Force'] < 0)

    cycle8 = df8[['Time']].copy()
    cycle8['pos'] = df8['Force'].where(df8['Force'] > 0)
    cycle8['neg'] = df8['Force'].where(df8['Force'] < 0)

    cycle9 = df9[['Time']].copy()
    cycle9['pos'] = df9['Force'].where(df9['Force'] > 0)
    cycle9['neg'] = df9['Force'].where(df9['Force'] < 0)

    # penetration
    max1p = cycle1['pos'].max()
    max2p = cycle2['pos'].max()
    max3p = cycle3['pos'].max()
    max4p = cycle4['pos'].max()
    max5p = cycle5['pos'].max()
    max6p = cycle6['pos'].max()
    max7p = cycle7['pos'].max()
    max8p = cycle8['pos'].max()
    max9p = cycle9['pos'].max()

    min1p = cycle1['pos'].min()
    min2p = cycle2['pos'].min()
    min3p = cycle3['pos'].min()
    min4p = cycle4['pos'].min()
    min5p = cycle5['pos'].min()
    min6p = cycle6['pos'].min()
    min7p = cycle7['pos'].min()
    min8p = cycle8['pos'].min()
    min9p = cycle9['pos'].min()

    # removal
    max1n = cycle1['neg'].max()
    max2n = cycle2['neg'].max()
    max3n = cycle3['neg'].max()
    max4n = cycle4['neg'].max()
    max5n = cycle5['neg'].max()
    max6n = cycle6['neg'].max()
    max7n = cycle7['neg'].max()
    max8n = cycle8['neg'].max()
    max9n = cycle9['neg'].max()

    min1n = cycle1['neg'].min()
    min2n = cycle2['neg'].min()
    min3n = cycle3['neg'].min()
    min4n = cycle4['neg'].min()
    min5n = cycle5['neg'].min()
    min6n = cycle6['neg'].min()
    min7n = cycle7['neg'].min()
    min8n = cycle8['neg'].min()
    min9n = cycle9['neg'].min()

    d = {filename1[:-5]: ['Cycle 0', 'Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 4', 'Cycle 5', 'Cycle 6', 'Cycle 7',
                          'Cycle 8'],
         'Min Penetration': [min1p, min2p, min3p, min4p, min5p, min6p, min7p, min8p, min9p],
         'Max Penetration': [max1p, max2p, max3p, max4p, max5p, max6p, max7p, max8p, max9p],
         'Min Removal': [max1n, max2n, max3n, max4n, max5n, max6n, max7n, max8n, max9n],
         'Max Removal': [min1n, min2n, min3n, min4n, min5n, min6n, min7n, min8n, min9n]}

    res1 = pd.DataFrame(data=d)

    df = pd.read_excel(filename2, sheet_name=1)
    df = df.drop([0, 1])
    df = df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Force'})
    df['Time'] = pd.to_numeric(df['Time'])
    df['Force'] = pd.to_numeric(df['Force'])

    df1 = df[df['Time'] <= 20]

    df21 = df[df['Time'] >= 25]
    df2 = df21[df21['Time'] <= 45]

    df31 = df[df['Time'] >= 45]
    df3 = df31[df31['Time'] <= 65]

    df41 = df[df['Time'] >= 95]
    df4 = df41[df41['Time'] <= 115]

    df51 = df[df['Time'] >= 140]
    df5 = df51[df51['Time'] <= 160]

    df61 = df[df['Time'] >= 190]
    df6 = df61[df61['Time'] <= 210]

    df71 = df[df['Time'] >= 235]
    df7 = df71[df71['Time'] <= 255]

    df81 = df[df['Time'] >= 280]
    df8 = df81[df81['Time'] <= 300]

    df91 = df[df['Time'] >= 330]
    df9 = df91[df91['Time'] <= 350]

    cycle1 = df1[['Time']].copy()
    cycle1['pos'] = df1['Force'].where(df1['Force'] > 0)
    cycle1['neg'] = df1['Force'].where(df1['Force'] < 0)

    cycle2 = df2[['Time']].copy()
    cycle2['pos'] = df2['Force'].where(df2['Force'] > 0)
    cycle2['neg'] = df2['Force'].where(df2['Force'] < 0)

    cycle3 = df3[['Time']].copy()
    cycle3['pos'] = df3['Force'].where(df3['Force'] > 0)
    cycle3['neg'] = df3['Force'].where(df3['Force'] < 0)

    cycle4 = df4[['Time']].copy()
    cycle4['pos'] = df4['Force'].where(df4['Force'] > 0)
    cycle4['neg'] = df4['Force'].where(df4['Force'] < 0)

    cycle5 = df5[['Time']].copy()
    cycle5['pos'] = df5['Force'].where(df5['Force'] > 0)
    cycle5['neg'] = df5['Force'].where(df5['Force'] < 0)

    cycle6 = df6[['Time']].copy()
    cycle6['pos'] = df6['Force'].where(df6['Force'] > 0)
    cycle6['neg'] = df6['Force'].where(df6['Force'] < 0)

    cycle7 = df7[['Time']].copy()
    cycle7['pos'] = df7['Force'].where(df7['Force'] > 0)
    cycle7['neg'] = df7['Force'].where(df7['Force'] < 0)

    cycle8 = df8[['Time']].copy()
    cycle8['pos'] = df8['Force'].where(df8['Force'] > 0)
    cycle8['neg'] = df8['Force'].where(df8['Force'] < 0)

    cycle9 = df9[['Time']].copy()
    cycle9['pos'] = df9['Force'].where(df9['Force'] > 0)
    cycle9['neg'] = df9['Force'].where(df9['Force'] < 0)

    # penetration
    max1p = cycle1['pos'].max()
    max2p = cycle2['pos'].max()
    max3p = cycle3['pos'].max()
    max4p = cycle4['pos'].max()
    max5p = cycle5['pos'].max()
    max6p = cycle6['pos'].max()
    max7p = cycle7['pos'].max()
    max8p = cycle8['pos'].max()
    max9p = cycle9['pos'].max()

    min1p = cycle1['pos'].min()
    min2p = cycle2['pos'].min()
    min3p = cycle3['pos'].min()
    min4p = cycle4['pos'].min()
    min5p = cycle5['pos'].min()
    min6p = cycle6['pos'].min()
    min7p = cycle7['pos'].min()
    min8p = cycle8['pos'].min()
    min9p = cycle9['pos'].min()

    # removal
    max1n = cycle1['neg'].max()
    max2n = cycle2['neg'].max()
    max3n = cycle3['neg'].max()
    max4n = cycle4['neg'].max()
    max5n = cycle5['neg'].max()
    max6n = cycle6['neg'].max()
    max7n = cycle7['neg'].max()
    max8n = cycle8['neg'].max()
    max9n = cycle9['neg'].max()

    min1n = cycle1['neg'].min()
    min2n = cycle2['neg'].min()
    min3n = cycle3['neg'].min()
    min4n = cycle4['neg'].min()
    min5n = cycle5['neg'].min()
    min6n = cycle6['neg'].min()
    min7n = cycle7['neg'].min()
    min8n = cycle8['neg'].min()
    min9n = cycle9['neg'].min()

    d = {filename2[:-5]: ['Cycle 0', 'Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 4', 'Cycle 5', 'Cycle 6', 'Cycle 7',
                          'Cycle 8'],
         'Min Penetration': [min1p, min2p, min3p, min4p, min5p, min6p, min7p, min8p, min9p],
         'Max Penetration': [max1p, max2p, max3p, max4p, max5p, max6p, max7p, max8p, max9p],
         'Min Removal': [max1n, max2n, max3n, max4n, max5n, max6n, max7n, max8n, max9n],
         'Max Removal': [min1n, min2n, min3n, min4n, min5n, min6n, min7n, min8n, min9n]}

    res2 = pd.DataFrame(data=d)

    df_concat = pd.concat([res0[res0.columns[1]], res1[res1.columns[1]], res2[res2.columns[1]],
                           res0[res0.columns[2]], res1[res1.columns[2]], res2[res2.columns[2]],
                           res0[res0.columns[3]], res1[res1.columns[3]], res2[res2.columns[3]],
                           res0[res0.columns[4]], res1[res1.columns[4]], res2[res2.columns[4]]],
                          axis=1)

    d1 = {filename1[:-7]: ['Cycle 0', 'Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 4', 'Cycle 5', 'Cycle 6', 'Cycle 7',
                           'Cycle 8'],
          'Min Penetration': df_concat.iloc[:, :3].mean(axis=1),
          'Max Penetration': df_concat.iloc[:, 3:6].mean(axis=1),
          'Min Removal': df_concat.iloc[:, 6:9].mean(axis=1),
          'Max Removal': df_concat.iloc[:, 9:].mean(axis=1)}

    df_mean = pd.DataFrame(data=d1)

    d2 = {filename1[:-7]: ['Cycle 0', 'Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 4', 'Cycle 5', 'Cycle 6', 'Cycle 7',
                           'Cycle 8'],
          'Min Penetration': df_concat.iloc[:, :3].std(axis=1),
          'Max Penetration': df_concat.iloc[:, 3:6].std(axis=1),
          'Min Removal': df_concat.iloc[:, 6:9].std(axis=1),
          'Max Removal': df_concat.iloc[:, 9:].std(axis=1)}

    df_std = pd.DataFrame(data=d2)
    df_std = df_std.iloc[3:, [0, 2, 4]].round(2)

    df_mean2 = df_mean.drop([0, 1, 2])

    # Select the columns 1 and 3
    df_selected1 = df_mean2.iloc[:, [0, 2]]
    # Select the columns 1 and 5
    df_selected2 = df_mean2.iloc[:, [0, 4]]

    return [df_mean2, df_std, df_selected1, df_selected2]

def graph(title,
          filename0, filename1, filename2,
          filename3, filename4, filename5,
          filename6, filename7, filename8,
          filename9, filename10, filename11,
          filename12, filename13, filename14,
          filename15, filename16, filename17,
          filename18, filename19, filename20):
    df_selected1 = create_df(filename0, filename1, filename2)[2]
    df_selected2 = create_df(filename0, filename1, filename2)[3]
    df_std = create_df(filename0, filename1, filename2)[1]

    std1 = df_std.iloc[:, 1].tolist()

    std2 = df_std.iloc[:, 2].tolist()

    bar_width = 0.08

    fig, ax = plt.subplots(figsize=(13, 6))

    df_selected1.plot(kind='bar', x=df_selected1.columns[0], y=df_selected1.columns[1], ax=ax, width=bar_width,
                      position=-2.5, color='blue', yerr=std1, capsize=2.5)

    df_selected2.plot(kind='bar', x=df_selected2.columns[0], y=df_selected2.columns[1], ax=ax, width=bar_width,
                      position=-2.5, color='blue', alpha=0.7, yerr=std2, capsize=2.5)

    ###############################################################################################################
    ###############################################################################################################
    df_selected1 = create_df(filename3, filename4, filename5)[2]
    df_selected2 = create_df(filename3, filename4, filename5)[3]
    df_std = create_df(filename3, filename4, filename5)[1]

    std1 = df_std.iloc[:, 1].tolist()

    std2 = df_std.iloc[:, 2].tolist()

    df_selected1.plot(kind='bar', x=df_selected1.columns[0], y=df_selected1.columns[1], ax=ax, width=bar_width,
                      position=-1.5, color='darkorange', yerr=std1, capsize=2.5)

    df_selected2.plot(kind='bar', x=df_selected2.columns[0], y=df_selected2.columns[1], ax=ax, width=bar_width,
                      position=-1.5, color='darkorange', alpha=0.7, yerr=std2, capsize=2.5)

    ###############################################################################################################
    ###############################################################################################################
    df_selected1 = create_df(filename6, filename7, filename8)[2]
    df_selected2 = create_df(filename6, filename7, filename8)[3]
    df_std = create_df(filename6, filename7, filename8)[1]

    std1 = df_std.iloc[:, 1].tolist()

    std2 = df_std.iloc[:, 2].tolist()

    df_selected1.plot(kind='bar', x=df_selected1.columns[0], y=df_selected1.columns[1], ax=ax, width=bar_width,
                      position=-0.5, color='green', yerr=std1, capsize=2.5)

    df_selected2.plot(kind='bar', x=df_selected2.columns[0], y=df_selected2.columns[1], ax=ax, width=bar_width,
                      position=-0.5, color='green', alpha=0.7, yerr=std2, capsize=2.5)

    ###############################################################################################################
    ###############################################################################################################
    df_selected1 = create_df(filename9, filename10, filename11)[2]
    df_selected2 = create_df(filename9, filename10, filename11)[3]
    df_std = create_df(filename9, filename10, filename11)[1]

    std1 = df_std.iloc[:, 1].tolist()

    std2 = df_std.iloc[:, 2].tolist()

    df_selected1.plot(kind='bar', x=df_selected1.columns[0], y=df_selected1.columns[1], ax=ax, width=bar_width,
                      position=0.5, color='r', yerr=std1, capsize=2.5)

    df_selected2.plot(kind='bar', x=df_selected2.columns[0], y=df_selected2.columns[1], ax=ax, width=bar_width,
                      position=0.5, color='r', alpha=0.7, yerr=std2, capsize=2.5)

    ###############################################################################################################
    ###############################################################################################################
    df_selected1 = create_df(filename12, filename13, filename14)[2]
    df_selected2 = create_df(filename12, filename13, filename14)[3]
    df_std = create_df(filename12, filename13, filename14)[1]

    std1 = df_std.iloc[:, 1].tolist()

    std2 = df_std.iloc[:, 2].tolist()

    df_selected1.plot(kind='bar', x=df_selected1.columns[0], y=df_selected1.columns[1], ax=ax, width=bar_width,
                      position=1.5, color='purple', yerr=std1, capsize=2.5)

    df_selected2.plot(kind='bar', x=df_selected2.columns[0], y=df_selected2.columns[1], ax=ax, width=bar_width,
                      position=1.5, color='purple', alpha=0.7, yerr=std2, capsize=2.5)

    ###############################################################################################################
    ###############################################################################################################
    df_selected1 = create_df(filename15, filename16, filename17)[2]
    df_selected2 = create_df(filename15, filename16, filename17)[3]
    df_std = create_df(filename15, filename16, filename17)[1]

    std1 = df_std.iloc[:, 1].tolist()

    std2 = df_std.iloc[:, 2].tolist()

    df_selected1.plot(kind='bar', x=df_selected1.columns[0], y=df_selected1.columns[1], ax=ax, width=bar_width,
                      position=2.5, color='chocolate', yerr=std1, capsize=2.5)

    df_selected2.plot(kind='bar', x=df_selected2.columns[0], y=df_selected2.columns[1], ax=ax, width=bar_width,
                      position=2.5, color='chocolate', alpha=0.7, yerr=std2, capsize=2.5)

    ###############################################################################################################
    ###############################################################################################################
    df_selected1 = create_df(filename18, filename19, filename20)[2]
    df_selected2 = create_df(filename18, filename19, filename20)[3]
    df_std = create_df(filename18, filename19, filename20)[1]

    std1 = df_std.iloc[:, 1].tolist()

    std2 = df_std.iloc[:, 2].tolist()

    df_selected1.plot(kind='bar', x=df_selected1.columns[0], y=df_selected1.columns[1], ax=ax, width=bar_width,
                      position=3.5, color='darkturquoise', yerr=std1, capsize=2.5)

    df_selected2.plot(kind='bar', x=df_selected2.columns[0], y=df_selected2.columns[1], ax=ax, width=bar_width,
                      position=3.5, color='darkturquoise', alpha=0.7, yerr=std2, capsize=2.5)

    plt.title(title)
    plt.xlabel('Cycles')
    plt.ylabel('Force (N)')

    legend_labels = [filename0[:-7], filename3[:-7], filename6[:-7], filename9[:-7], filename12[:-7], filename15[:-7],
                     filename18[:-7]]
    odd_positions = [True, True, True, True, True, True, True]
    bar_colors = ['blue', 'darkorange', 'green', 'r', 'purple', 'chocolate', 'darkturquoise']

    legend_elements = [Patch(facecolor=color, edgecolor='none', label=label)
                       for label, position, color in zip(legend_labels, odd_positions, bar_colors) if position]
    ax.legend(handles=legend_elements)

    ax.set_xlim(left=ax.get_xlim()[0] - 5 * bar_width, right=ax.get_xlim()[1] + 5 * bar_width)

    x_ticks = ax.get_xticks()
    ax.set_xlim(x_ticks[0] - 0.5 * (x_ticks[1] - x_ticks[0]),
                x_ticks[-1] + 0.5 * (x_ticks[1] - x_ticks[0]))

    plt.show()
    plt.savefig(f'{title}-graph.png', bbox_inches='tight')

    plt.close()

def mean(filename0, filename1, filename2):
    df_mean2 = create_df(filename0, filename1, filename2)[0]

    df_mean_rounded = df_mean2.round(2)

    selected_columns = [0, 2, 4]
    df_selected = df_mean_rounded.iloc[:, selected_columns]

    plt.axis('off')

    plt.table(cellText=df_selected.values, colLabels=df_selected.columns, cellLoc='center', loc='center')

    filename0 = filename0.replace('/', '-')
    plt.savefig(f'{filename0[:-7]}-mean.png')
    plt.show()

    plt.close()

def std(filename0, filename1, filename2):
    df_std = create_df(filename0, filename1, filename2)[1]

    plt.axis('off')

    plt.table(cellText=df_std.values, colLabels=df_std.columns, cellLoc='center', loc='center')

    filename0 = filename0.replace('/', '-')
    plt.savefig(f'{filename0[:-7]}-std.png')
    plt.show()

    plt.close()