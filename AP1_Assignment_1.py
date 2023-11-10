# This code imports the necessary libraries 

import matplotlib.pyplot as plt
import pandas as pd

# Function to read data from a CSV file
# This function reads the data from the CSV file and returns a Pandas DataFrame.

def read_data(filename):
  """Reads data from a CSV file and returns a Pandas DataFrame.
  Args:
    filename: The name of the CSV file to read.
  """

  df = pd.read_csv(filename)
  return df


# Define a function to plot a line plot with multiple lines
def map_line_plot(data, x_col, y_cols, labels, title, x_label, y_label):
    fig, ax = plt.subplots()
    
    # Plot the line for the current y-col column
    for i, col in enumerate(y_cols):
        ax.plot(data[x_col], data[col], label=labels[i])
        
    # Set the title, x-axis label, and y-axis label
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Set the legend
    ax.legend()

    # Save the figure
    plt.savefig('lineplot_fig.png', dpi=300)
        
    # Show the plot
    plt.show()

# Define a function to plot a bar plot
def map_bar_plot(data, x_col, y_col, title, x_label, y_label):
    fig, ax = plt.subplots()

    ax.bar(data[x_col], data[y_col])
        
    # Set the title, x-axis label, and y-axis label    
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    # Save the figure
    plt.savefig('barplot_fig.png', dpi=300)
        
    # Show the plot
    plt.show()

# Define a function to plot a Scatter plot
def map_scatter_plot(data, x_col, y_col, title, xlabel, ylabel, marker, color):

    fig, ax = plt.subplots()
    ax.scatter(data[x_col], data[y_col], marker=marker, color=color)
        
    # Set the title, x-axis label, and y-axis label    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    
    # Save the figure
    plt.savefig('scatterplot_fig.png', dpi=300)
            
    # Show the plot
    plt.show()  

# Read the data
data_crime = read_data("US_Crime_Rates.csv")
data_os = read_data("os_share_2023.csv")
data_income = read_data("adult_income.csv")


# Plot a line plot showing multiple lines with proper labels and legend

map_line_plot(
    data=data_crime,
    x_col="Year",
    y_cols=["Violent","Property","Murder","Robbery","Burglary","Vehicle_Theft"],
    labels=["Violent","Property","Murder","Robbery","Burglary","Vehicle Theft"],
    title="Total Crime over the Years",
    x_label="Year",
    y_label="Amount in Hundred Thousand",
)

# Plot a bar plot showing the Market Share for Windows in 2023

map_bar_plot(
    data=data_os,
    x_col="Month",
    y_col="Windows",
    title="Windows Market Share through 2023",
    x_label="Months of 2023",
    y_label="Percentage Market Share",
)


# Plot a Scatter plot showing the Relationship between hours work to age
map_scatter_plot(
    data=data_income, 
    x_col='age', 
    y_col='hours-per-week', 
    title='Hours worked by Age', 
    xlabel='Age', 
    ylabel='Hours per Week',
    marker='.',
    color='blue'
)

# Summary

#The three visualization methods used in this code are:

#* Line plot: To show how multiple variables change over time.
#* Bar plot: To compare the values of a variable across different categories.
#* Pie chart: To show the distribution of a variable.

"""

Data References

#Links 1- US_Crime_Rates_1960_2014 on #kaggle via @KaggleDatasets https://www.kaggle.com/datasets/mahmoudshogaa/us-crime-rates-1960-2014?utm_medium=social&utm_campaign=kaggle-dataset-share&utm_source=twitter 
#Links 2- American Citizens Annual Income on #kaggle via @KaggleDatasets https://www.kaggle.com/datasets/amirhosseinmirzaie/americancitizenincome?utm_medium=social&utm_campaign=kaggle-dataset-share&utm_source=twitter 
#Links 3- https://gs.statcounter.com/os-market-share#monthly-202301-202310 This work by Statcounter is licensed under a Creative Commons Attribution-Share Alike 3.0 Unported License 

"""