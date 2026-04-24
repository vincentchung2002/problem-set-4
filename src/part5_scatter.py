'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony.
def scatter_predictions_by_charge(pred_universe_merged):
    sns.lmplot(data=pred_universe_merged, x='prediction_felony', y='prediction_nonfelony', hue='has_felony_charge', fit_reg=False)
    plt.savefig('./data/part5_plots/scatter_predictions_by_charge.png', bbox_inches='tight')
    plt.clf()
    print("The group of dots on the right side of the plot are predominantly individuals with a current felony charge.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def scatter_pred_vs_actual(pred_universe_merged):
    sns.lmplot(data=pred_universe_merged, x='prediction_felony', y='y_felony', fit_reg=False)
    plt.savefig('./data/part5_plots/scatter_pred_vs_actual.png', bbox_inches='tight')
    plt.clf()
    print("I would say the model is not well calibrated because a calibrated model would show that as the predicted probability of felony rearrest increases, the proportion of individuals who were actually rearrested should also increase.")
