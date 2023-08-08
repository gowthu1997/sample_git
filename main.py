import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self):
        self.data = None

    def load_data_from_csv(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Data loaded successfully from CSV.")
        except FileNotFoundError:
            print("Error: File not found.")

    def load_data_from_excel(self, file_path, sheet_name):
        try:
            self.data = pd.read_excel(file_path, sheet_name=sheet_name)
            print("Data loaded successfully from Excel.")
        except FileNotFoundError:
            print("Error: File not found.")

    def summarize_data(self):
        if self.data is None:
            print("Error: Data not loaded.")
            return

        # Calculate mean of each numeric column
        numeric_columns = self.data.select_dtypes(include=[float, int]).columns
        means = self.data[numeric_columns].mean()

        # Calculate percentage of missing values in each column
        percentages = (self.data.isnull().sum() / len(self.data)) * 100

        summary_data = pd.DataFrame({"Mean": means, "Missing Percentage": percentages})
        print(summary_data)

    def visualize_bar_graph(self, x_column):
        if self.data is None:
            print("Error: Data not loaded.")
            return

        if x_column not in self.data.columns:
            print(f"Error: Column '{x_column}' not found in the dataset.")
            return

        sns.countplot(x=x_column, data=self.data)
        plt.xlabel(x_column)
        plt.ylabel("Count")
        plt.title(f"Bar graph of {x_column}")
        plt.show()

    def visualize_scatter_plot(self, x_column, y_column):
        if self.data is None:
            print("Error: Data not loaded.")
            return

        if x_column not in self.data.columns or y_column not in self.data.columns:
            print("Error: One or both of the provided columns not found in the dataset.")
            return

        plt.scatter(self.data[x_column], self.data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"Scatter plot of {y_column} vs {x_column}")
        plt.show()

# Example usage:
if __name__ == "__main__":
    analyzer = DataAnalyzer()
    analyzer.load_data_from_csv("train.csv")
    analyzer.summarize_data()

    # Example usage of visualize_bar_graph and visualize_scatter_plot
    analyzer.visualize_bar_graph("Sex")
    analyzer.visualize_scatter_plot("Fare","Age")
