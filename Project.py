import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
file_path = "Credi_Card_Fraud.xlsx"
sheet_name = "Original"
DB = pd.read_excel(file_path, sheet_name=sheet_name)

# Display the DataFrame
# print(DB)

# Display the DataFrame information
# print(DB.info())

# print(DB.describe())

sns.set_theme()


# Display a distribution plot for the 'Amount' column
# sns.distplot(DB['Amount'])

# Show the plot
# plt.show()

# Create a boxplot for the 'Amount' column
# sns.boxplot(x=DB['Amount'])

# Show the plot
# plt.show()


import plotly.express as px
# Create a histogram for the 'Amount' column using Plotly Express
fig = px.histogram(DB, x='Amount')
fig.show()


# Create a count plot for the 'Type' column
# sns.countplot(x='Type', data=DB)

# Show the plot
# plt.show()


# Create a pie chart for the 'Type' column
# DB['Type'].value_counts().plot(kind='pie', autopct="%.1f%%")

# Show the plot
# plt.show()



# Group by 'Month' and 'Type' and calculate the sum of 'Amount'
Group = DB.groupby(['Month', 'Type'])['Amount'].sum()

# Display the grouped data
print(Group)

# Display a histogram plot for the 'Amount' column
# sns.histplot(DB['Amount'], kde=True)

# Show the plot
# plt.show()