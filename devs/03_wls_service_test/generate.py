import plotly.graph_objects as go

# Performance evolution data for 2023
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

# Response times in seconds (Evolution from 2.0s to 0.1s)
# Initial state: 2.0s
# Optimization phases: Service test executor, parallel workers, ISO20022 logic tuning
response_times = [
    2.00, 1.95, 1.95, 1.96, 0.62, 0.52, 
    0.43, 0.40, 0.38, 0.15, 0.12, 0.11
]

fig = go.Figure()

# Add the main performance line
fig.add_trace(go.Scatter(
    x=months, 
    y=response_times,
    mode='lines+markers',
    name='Avg Response Time',
    line=dict(color='#00ffcc', width=4),
    marker=dict(size=10, symbol='diamond'),
    hovertemplate='%{x}: %{y}s<extra></extra>'
))

# Night mode layout consistent with other project visualizations
fig.update_layout(
    title='Watchlists Realtime API Performance Evolution (2023)',
    xaxis_title='Timeline (2023)',
    yaxis_title='Response Time (seconds)',
    template='plotly_dark',
    showlegend=False,
    yaxis=dict(
        range=[0, 2.2],
        gridcolor='rgba(255, 255, 255, 0.1)',
        zerolinecolor='rgba(255, 255, 255, 0.2)'
    ),
    xaxis=dict(
        gridcolor='rgba(255, 255, 255, 0.1)'
    ),
    annotations=[
        dict(
            x='Apr', y=1.96,
            xref="x", yref="y",
            text="Crucial optimization findings<br>with service tests",
            showarrow=True,
            arrowhead=2,
            ax=50, ay=-50,
            bgcolor="#ffa500",
            font=dict(color="black")
        ),
        dict(
            x='Dec', y=0.10,
            xref="x", yref="y",
            text="0.1s Goal Reached",
            showarrow=True,
            arrowhead=2,
            ax=-40, ay=-40,
            bgcolor="#00ffcc",
            font=dict(color="black")
        )
    ]
)

# Save as HTML
output_path = 'devs/03_wls_service_test/plotly.html'
fig.write_html(output_path, include_plotlyjs='cdn')

print(f"Watchlists performance chart generated and saved to: {output_path}")
