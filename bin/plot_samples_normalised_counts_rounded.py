#!/usr/bin/env python3

import plotly.graph_objs as go
from plotly.offline import plot

# Data
# Read data from the tab-delimited text file
data_raw = []

with open('results.txt', 'r') as file:
    next(file)
    for line in file:
        # Split the line into columns using tab as the delimiter
        columns = line.strip().split('\t')
        data_raw.append(columns)

# Extract the data for plotting
samples = [row[0] for row in data_raw]
print(samples)
counts = [float(row[-1]) for row in data_raw]  # set to float if not using counts
print(counts)


# Combine data into a list of tuples
data = list(zip(samples, counts))

# Sorts and groups samples on name
data.sort(key=lambda x: (x[1] >= 1, int(x[0][6:])))  # TODO figure out why this shifts

# Separate sorted data into samples and counts
samples, counts = zip(*data)

# Define colors and labels
custom = ['#1AFF1A' if count >= 1 else ('#4B0092' if (count > 0 and count < 1) else '#FAFAFA') for count in counts] # for colourblindedness
legend_labels = ['treated' if count >= 1 else ('uncertain' if (count > 0 and count < 1) else 'controls') for count in counts] # treated >1, unknown ==1, controls == 0

# Create separate traces for each group of bars with the same colour
traces = []
unique_legend_labels = set(legend_labels)

for label in unique_legend_labels:
    x_values = [sample for sample, lab in zip(samples, legend_labels) if lab == label]
    y_values = [count for count, lab in zip(counts, legend_labels) if lab == label]

    trace = go.Bar(
        x=x_values,
        y=y_values,
        marker=dict(color=custom[legend_labels.index(label)]),
        name=label
    )
    traces.append(trace)

# Layout configuration
layout = go.Layout(
    title='Fig 1.0 Bar Chart of samples grouped by normalised rounded counts and treatment.',
    xaxis=dict(title='Samples'),
    yaxis=dict(title='Normalised Counts')
)

# Create a figure with all traces
fig = go.Figure(data=traces, layout=layout)

# Save the plot as an HTML file
plot(fig, filename='Plot-DBS_normalised_count_results.html')