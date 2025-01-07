import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

def plot_3d(surface, scatter, title=None, xaxis_title=None, yaxis_title=None, zaxis_title=None, X=None, Y=None, x1_min=None, x1_max=None, x2_min=None, x2_max=None, x=None, y=None, z=None):

    fig = go.Figure()

    if surface == True:
        model = LinearRegression()
        model.fit(X, Y)
        x1_range = np.linspace(x1_min, x1_max, 100)
        x2_range = np.linspace(x2_min, x2_max, 100)
        X1, X2 = np.meshgrid(x1_range, x2_range)
        X_grid = np.column_stack([X1.ravel(), X2.ravel()])
        y_pred = model.predict(X_grid).reshape(X1.shape)

        fig.add_trace(go.Surface(z=y_pred, x=X1, y=X2, colorscale='Rainbow'))

    if scatter == True:
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z,
                    mode='markers',
                    marker=dict(
                        size=4,
                        color='Black',
                        opacity=1)))
        
    fig.update_layout(title=title,
                  scene=dict(xaxis=dict(showgrid=True, gridcolor='Gray'),
                      yaxis=dict(showgrid=True, gridcolor='Gray'),
                      zaxis=dict(showgrid=True, gridcolor='Gray'), xaxis_title=xaxis_title, yaxis_title=yaxis_title, zaxis_title=zaxis_title),
                  autosize=True, margin=dict(l=80, r=80, b=0, t=50))

    fig.show()