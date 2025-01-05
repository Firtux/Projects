import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import probplot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.stats.stattools import durbin_watson

def diagnostics_LR_model(y, y_pred):
    residuals = y-y_pred
    residuals_mean = np.round(np.mean(residuals), 3)

    f, ((ax_rkde, ax_prob), (ax_ry, ax_auto), (ax_yy, ax_ykde)) = plt.subplots(nrows=3,
                                                                               ncols=2,
                                                                               figsize=(12,18))
    sns.kdeplot(residuals, fill=True, ax=ax_rkde)
    ax_rkde.set_title('Residuals distribution', fontsize=14)
    ax_rkde.set(xlabel=f'Residuals, mean: {residuals_mean}',
                ylabel='Density')
    
    probplot(residuals, dist='norm', plot=ax_prob)
    ax_prob.set_title('Residuals probability plot', fontsize=14)

    sns.scatterplot(x=y_pred, y=residuals, ax=ax_ry)
    sns.lineplot(x=[0, y.max()], y=0, color='black', linestyle='--', ax=ax_ry)
    ax_ry.set_title('Predicted vs Residuals', fontsize=14)
    ax_ry.set(xlabel='y_pred', ylabel='Residuals')

    plot_acf(residuals, lags=30, ax=ax_auto)
    ax_auto.set_title('Residuals Autocorrelation', fontsize=14)
    ax_auto.set(xlabel=f'Lags \ndurbin_watson: {durbin_watson(residuals).round(2)}',
                ylabel='Autocorrelation')
    
    sns.scatterplot(x=y, y=y_pred, ax=ax_yy)
    ax_yy.plot([y.min(), y.max()], [y.min(), y.max()], "k--", lw = 1)
    ax_yy.set_title('Actual vs. Predicted', fontsize = 14)
    ax_yy.set(xlabel='y_true', ylabel='y_pred')

    sns.kdeplot(y, fill=True, ax=ax_ykde, label='y_true')
    sns.kdeplot(y_pred, fill=True, ax=ax_ykde, label='y_pred')
    ax_ykde.set_title('Actual vs Predicted Distribution', fontsize=14)
    ax_ykde.set(xlabel='y_true and y_pred', ylabel='Density')
    ax_ykde.legend(loc='upper right', prop={'size' : 12})

    plt.tight_layout()

    plt.show()