'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge.
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# Done in part1_etl.py: felony_charge dataframe with ['arrest_id', 'has_felony_charge']

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe
# Done in part1_etl.py: pred_universe_merged

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes
# Done in main.py

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def catplot_felony_pred(pred_universe_merged):
    sns.catplot(data=pred_universe_merged, x='has_felony_charge', y='prediction_felony', kind='bar')
    plt.title('Predicted Felony Rearrest by Current Charge Type')
    plt.savefig('./data/part4_plots/catplot_felony_pred.png', bbox_inches='tight')
    plt.clf()

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
def catplot_nonfelony_pred(pred_universe_merged):
    sns.catplot(data=pred_universe_merged, x='has_felony_charge', y='prediction_nonfelony', kind='bar')
    plt.title('Predicted Nonfelony Rearrest by Current Charge Type')
    plt.savefig('./data/part4_plots/catplot_nonfelony_pred.png', bbox_inches='tight')
    plt.clf()
    print("Arrestees with a current felony charge typically have a higher predicted probability of felony rearrest but a lower predicted probability of nonfelony rearrest compared to those with misdemeanor charges.")

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def catplot_felony_pred_by_rearrest(pred_universe_merged):
    sns.catplot(data=pred_universe_merged, x='has_felony_charge', y='prediction_felony', hue='y_felony', kind='bar')
    plt.title('Predicted Felony Rearrest by Charge Type and Actual Felony Rearrest')
    plt.savefig('./data/part4_plots/catplot_felony_pred_by_rearrest.png', bbox_inches='tight')
    plt.clf()
    print("The model is more driven by the current charge than the future behavior. It over-predicts risk for current felony offenders and under-predicts risk for current misdemeanor offenders. The model might be poorly calibrated.")