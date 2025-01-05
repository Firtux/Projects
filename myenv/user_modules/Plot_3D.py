import plotly.graph_objects as go

def scatter_plot_3D(x, y, z):
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                    mode='markers',
                    marker=dict(
                        size=5,
                        color='blue',                # set color to an array/list of desired values
                        colorscale='Viridis',   # choose a colorscale
                        opacity=1))])
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()