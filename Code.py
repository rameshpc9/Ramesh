# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
data = pd.read_csv('COVID-19 Global Statistics Dataset.csv')

# Displaying the first few rows of the dataset
print(data.head(5))

# Function to create a Line Plot
def plot_line_plot(data, x_column, y_column, x_label, y_label, title):
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.plot(data[x_column], data[y_column], marker='o', linestyle='-')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45)  # Rotate the x-axis labels by 45 degrees
    plt.grid(True)  # Add grid lines
    plt.show()

# Plotting a Line Plot of total COVID-19 cases by country
plot_line_plot(data.head(20), 'Country', 'Total Cases', 'Country', 'Total Cases', 'Total Cases by Country')

# Function to create a pie chart
def plot_pie_chart(data, labels, sizes):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Proportion of COVID-19 Deaths by Continent')
    plt.show()

# Example data for pie chart
labels = ['Asia', 'Europe', 'Africa', 'North America', 'South America', 'Oceania']
sizes = [30, 25, 15, 20, 5, 5]  # Example sizes, replace with actual data

# Plotting a pie chart of COVID-19 deaths by continent
plot_pie_chart(data, labels, sizes)

def plot_box_plot(data, x_column, y_column):
    if x_column not in data.columns or y_column not in data.columns:
        print("Error: One or both of the specified columns not found in the DataFrame.")
        return
    
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.boxplot(x=x_column, y=y_column, data=data)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Distribution of COVID-19 Recoveries by Country')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust spacing to prevent overlapping
    plt.show()

# Plotting a box plot of COVID-19 recoveries by region
plot_box_plot(data.head(20), 'Country', 'Total Recovered')


# Descriptive statistics of the dataset
print(data.describe())

# Correlation matrix for numeric columns
numeric_data = data.select_dtypes(include='number')
correlation_matrix = numeric_data.corr()
print(correlation_matrix)



