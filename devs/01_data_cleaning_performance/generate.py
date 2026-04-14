import plotly.graph_objects as go

# Data validation types
categories = [
    'String', 
    'CategoricalString', 
    'BoundedNumeric', 
    'IP', 
    'BIC', 
    'Card', 
    'GeolocatableString'
]

# Average validation times for 1 million records (mean, std_dev) in milliseconds
times_2021 = [
    (102.1, 5.2), # String
    (302.4, 12.1), # CategoricalString
    (283.2, 10.5), # BoundedNumeric
    (1121.7, 45.3), # IP
    (624.2, 22.8), # BIC
    (910.0, 31.4), # Card
    (813.1, 28.6)  # GeolocatableString
]

times_2022 = [
    (15.2, 0.8), # String
    (51.4, 2.3), # CategoricalString
    (42.6, 1.9), # BoundedNumeric
    (127.9, 6.4), # IP
    (72.0, 3.1), # BIC
    (132.3, 5.8), # Card
    (142.5, 6.2)  # GeolocatableString
]

# Extract means and standard deviations
y_2021 = [t[0] for t in times_2021]
error_y_2021 = [t[1] for t in times_2021]

y_2022 = [t[0] for t in times_2022]
error_y_2022 = [t[1] for t in times_2022]

fig = go.Figure(data=[
    go.Bar(
        name='2021 (Pandas/Python)', 
        x=categories, 
        y=y_2021, 
        error_y=dict(type='data', array=error_y_2021, visible=True),
        marker_color='#1f77b4'
    ),
    go.Bar(
        name='2022 (Numpy/Cython)', 
        x=categories, 
        y=y_2022, 
        error_y=dict(type='data', array=error_y_2022, visible=True),
        marker_color='#ff7f0e'
    )
])

# Night mode layout
fig.update_layout(
    title='Data Cleaning Performance Evolution (1M Records)',
    xaxis_title='Data Type',
    yaxis_title='Validation Time (ms)',
    barmode='group',
    template='plotly_dark',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# Save as HTML
output_path = 'devs/01_data_cleaning_performance.html'
fig.write_html(output_path, include_plotlyjs='cdn')

print(f"Plotly chart generated and saved to: {output_path}")
