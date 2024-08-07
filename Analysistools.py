import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

def generate_latex_table(data):
    num_rows = len(data)
    num_cols = len(data[0]) if num_rows > 0 else 0

    if num_cols == 0:
        print("Das Array ist leer. Kann keine Tabelle generieren.")
        return

    latex_code = "\\begin{tabular}{|" + "c|" * num_cols + "}\n"
    latex_code += "\\hline\n"

    for row in data:
        for item in row:
            latex_code += str(item) + " & "
        latex_code = latex_code[:-2]  # Remove the last "& "
        latex_code += " \\\\\n"  # End the row
        latex_code += "\\hline\n"

    latex_code += "\\end{tabular}"

    print(latex_code)

def read_csv_file(file_name):
    data = []
    with open(f"../Experiment_Data(CVS-files)/{file_name}", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            print(", ".join(row))
            row_data = []
            if row == []:
                continue
            if row[1] == "":
                continue
            for cell in row:
                # Check if the cell is a string
                try:
                    # Try converting the cell to a float
                    value = float(cell)
                except ValueError:
                    # If it's not a float, keep it as a string
                    value = cell
                row_data.append(value)
            data.append(row_data)
    return data

def plot_data(data, file_name, data2=None, plot_fit=True, get_pdf=True, scale_x="linear", scale_y="linear", error_bars=False, error_bars_data=None, lable_x="Zeit in s", lable_y="Abstand in m", slope=None, intercept=None, std_err=None, lable_daten="Datenwerte", lable_fit="Fit zu den Datenwerten"):
    data = np.array(data)
    if data2 is not None:
        data2 = np.array(data2)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xscale(scale_x)
    ax.set_yscale(scale_y)
    if plot_fit:
        plt.plot(data[:, 0], data[:, 1], '-', color='r', label='Fit zu den Datenwerten')  # Data points
        #ax.plot(data[:, 0], data[:, 1], 'o', color='b', label='Datenwerte')  # Data points
    elif error_bars:
        ax.errorbar(data[:, 0], data[:, 1], yerr=error_bars_data, fmt='o', color='b', label='Datenwerte')
    else:
        ax.plot(data[:, 0], data[:, 1], 'o', color='b', label=lable_daten)  # Data points
    if data2 is not None:
        plt.plot(data2[:, 0], data2[:, 1], color='r', label=lable_fit, linestyle='--')

    # Plot the confidence interval if the slope, intercept, and std_err are provided
    if slope is not None and intercept is not None and std_err is not None:
        # Calculate the predicted values
        y_pred = slope * data[:, 0] + intercept

        # Calculate the lower and upper bounds of the confidence interval
        t = 1.96  # t-value for a 95% confidence level
        lower_bound = y_pred - t * std_err
        upper_bound = y_pred + t * std_err

        # Plot the confidence interval
        ax.fill_between(data[:, 0], lower_bound, upper_bound, color='b', alpha=0.1, label='Confidence Interval')

    ax.set_xlabel(lable_x)
    ax.set_ylabel(lable_y)
    ax.legend()
    ax.grid()
    fig.show()
    if get_pdf:
        if not os.path.isdir(f"../Graphics/{file_name}.pdf"):
            fig.savefig(f"../Graphics/{file_name}.pdf")
        else:
            fig.savefig(f"../Graphics/{file_name}_1.pdf")