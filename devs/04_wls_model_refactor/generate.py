import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Normalized confusion matrices (%)
# Rows = actual class, columns = predicted class
# Order:
#   row 0: Actual Negative
#   row 1: Actual Positive
#   col 0: Predicted Negative
#   col 1: Predicted Positive

cm_before = np.array([
    [92, 8],   # Actual negative -> TN, FP
    [0, 100]   # Actual positive -> FN, TP
])

cm_after = np.array([
    [97, 3],   # Actual negative -> TN, FP
    [0, 100]   # Actual positive -> FN, TP
])

x_labels = ["Predicted: Negative", "Predicted: Positive"]
y_labels = ["Actual: Negative", "Actual: Positive"]

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=[
        "Before (FP = 8%, FN = 0%)",
        "After (FP = 3%, FN = 0%)"
    ],
    horizontal_spacing=0.12
)

for i, cm in enumerate([cm_before, cm_after], start=1):
    fig.add_trace(
        go.Heatmap(
            z=cm,
            x=x_labels,
            y=y_labels,
            zmin=0,
            zmax=100,
            colorscale="Blues",
            text=[[f"{v}%" for v in row] for row in cm],
            texttemplate="%{text}",
            textfont={"size": 18},
            hovertemplate=(
                "<b>%{y}</b><br>"
                "%{x}<br>"
                "Value: %{z}%<extra></extra>"
            ),
            showscale=(i == 2),
            colorbar=dict(title="%")
        ),
        row=1,
        col=i
    )

fig.update_layout(
    title="Confusion Matrix Comparison",
    template="plotly_dark",
    width=1000,
    height=500,
    font=dict(size=14)
)

fig.update_yaxes(autorange="reversed")

fig.add_annotation(
    text="Main improvement: false positives dropped from 8% to 3%, while false negatives stayed at 0%.",
    x=0.5,
    y=-0.12,
    xref="paper",
    yref="paper",
    showarrow=False,
    font=dict(size=14)
)

# Save as HTML
output_path = 'devs/04_wls_model_refactor/plotly.html'
fig.write_html(output_path, include_plotlyjs='cdn')

print(f"Watchlists Models FP chart generated and saved to: {output_path}")