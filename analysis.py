import numpy as np
import pandas as pd
import pandas_bokeh
pandas_bokeh.output_file('./index.html', title='PoE - G2G Price Chart')

full_df = pd.read_csv('./full_price_chart.csv',header=0)
summary_df = pd.read_csv('./price_summary.csv',header=0)
full_df['timestamp'] = pd.to_datetime(full_df.timestamp)
summary_df['timestamp'] = pd.to_datetime(summary_df.timestamp)
maxmin_df = summary_df.drop(['deviation'], axis=1)

min_Val = np.min(maxmin_df['min price'])
max_Val = np.max(maxmin_df['max price'])

min_Dat = np.min(maxmin_df['timestamp'])
max_Dat = np.max(maxmin_df['timestamp'])

p_plot = maxmin_df.plot_bokeh.area(
    x='timestamp',
    stacked=False,
    figsize=(1900, 950),
    legend='bottom_left',
    toolbar_location='above',
    colormap=['red', 'blue'],
    title='Exalted Orb Price in GBP',
    ylabel='Price Per Unit [£]',
    xlabel='Date',
    ylim=(min_Val, max_Val),
    xlim=(min_Dat, max_Dat))

html = r"""
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

<title> PoE - G2G Price Chart </title>
"""

p_plot.plot_width = 2000
p_plot.plot_height = 1000

layout = pandas_bokeh.column(p_plot)