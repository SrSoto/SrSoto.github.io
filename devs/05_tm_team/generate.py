import plotly.graph_objects as go

# Performance evolution data for 2023
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

# Response times in seconds (Evolution from 2.0s to 0.1s)
# Initial state: 2.0s
# Optimization phases: Service test executor, parallel workers, ISO20022 logic tuning
n_members = [
    3, 4, 6, 5, 8, 9, 9, 11, 13, 14, 14, 15
]

fig = go.Figure()

# Add the main performance line
fig.add_trace(go.Scatter(
    x=months, 
    y=n_members,
    mode='lines+markers',
    name='Core Team Members',
    line=dict(color='#b4654a', width=4),
    marker=dict(size=10, symbol='diamond'),
    hovertemplate='%{x}: %{y} members<extra></extra>'
))

# Night mode layout consistent with other project visualizations
fig.update_layout(
    title='Transaction Monitoring Core Team evolution (2025)',
    xaxis_title='Timeline (2025)',
    yaxis_title='Team Size',
    template='plotly_dark',
    showlegend=False,
    yaxis=dict(
        range=[0, 20],
        gridcolor='rgba(255, 255, 255, 0.1)',
        zerolinecolor='rgba(255, 255, 255, 0.2)'
    ),
    xaxis=dict(
        gridcolor='rgba(255, 255, 255, 0.1)'
    ),
)

# Save as HTML
output_path = 'devs/05_tm_team/plotly.html'
fig.write_html(output_path, include_plotlyjs='cdn')

print(f"TM Team chart generated and saved to: {output_path}")
