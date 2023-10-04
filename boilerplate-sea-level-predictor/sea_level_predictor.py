import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("/content/epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    ax.set_xlabel("Year)")
    ax.set_ylabel("CSIRO Adjusted Sea Level")
    plt.show()
    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    xres = np.arange(df['Year'].min(),2050,1)
    yres = res.intercept + res.slope*xres
    
    plt.plot(df["Year"], df["CSIRO Adjusted Sea Level"], 'o', label='original data')
    plt.plot(xres, yres, 'r', label='fitted line')
    plt.legend()
    plt.show()

    # Create second line of best fit
    res2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    xres2 = np.arange(df2['Year'].min(),2050,1)
    yres2 = res2.intercept + res2.slope*xres2
    
    plt.plot(df["Year"], df["CSIRO Adjusted Sea Level"], 'o', label='original data')
    plt.plot(xres, yres, 'r', label='fitted line')
    plt.plot(xres2, yres2, 'r', label='fitted line (>2000)')

    # Add labels and title
    plt.xlabel("Year") 
    plt.ylabel("Sea Level (inches)") 
    plt.title("Rise in Sea Level")

    plt.legend()
    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()