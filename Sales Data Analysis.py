# This program accepts two files for employee IDs and sales data
# Using the files it creates an Annual Sales Report
# Author: Zaid Yazadi


# Uses id file to create IDs list for IDs and an empty sales data list
# Parameter filename
# return id_list, sales
def get_IDs(filename):
    file_id = open(filename, 'r')
    id_list = []
    for line in file_id:
        n = line.rstrip('\n')
        id_list.append(n)
    file_id.close()
    id_list.sort()
    sales = [[0.00 for i in range(4)] for j in range(len(id_list))]
    return id_list, sales


# Uses sales data file, id list, and empty sales list to process the data and
# update sales data list
# Parameters filename, id_list, sales_data
def process_sales_data(filename, id_list, sales_data):
    file_data = open(filename, 'r')
    for line in file_data:
        elements = line.split()
        i = elements[0]
        m = elements[1]
        x = elements[2]
        id_index = id_list.index(i)
        quarter = int((int(m) - 1)/3)
        sales_data[id_index][quarter] += round(float(x), 2)

    # rounds all values in sales_data to 2 decimal places
    for i in range(len(sales_data)):
        for j in range(len(sales_data[i])):
            sales_data[i][j] = round(sales_data[i][j], 2)


# Prints the sales report with quarterly totals and employee totals
# Also calculates the max sales by person and quarter
# Parameters id_list, sales_data
def print_report(id_list, sales_data):
    # Prints the sales data for each employee for each quarter and the employee totals
    print("ID \t\t\t QT1 \t\t\t QT2 \t\t\t QT3 \t\t\t QT4 \t\t\t Total\n")
    for i in range(len(id_list)):
        print(id_list[i], '\t\t', end="")
        for j in range(len(sales_data[i])):
            print(format(sales_data[i][j], '.2f'), end="")
            x = len(str(format(sales_data[i][j], '.2f')))
            whitespace_len = 16 - x
            for length in range(whitespace_len):      # Adds proper whitespace to columnize data
                print(' ', end="")
        print(format(sum(sales_data[i]), '.2f'), '\n')

    # Calculates quarterly totals and prints them under data
    total = [0.00, 0.00, 0.00, 0.00]
    for j in range(4):
        for i in range(len(id_list)):
            total[j] += sales_data[i][j]
    for i in range(len(total)):
        total[i] = round(total[i], 2)
    print("Total\t\t", end="")
    print(total[0], total[1], total[2], total[3], round(sum(total), 2), sep='\t\t\t')

    # Calculates max sales for quarter and employee
    max_sale = sales_data[0][0]
    for a in range(len(sales_data)):
        for b in range(len(sales_data[i])):
            if max_sale < sales_data[a][b]:
                max_sale = sales_data[a][b]
    print('\n', "Max sales by Salesperson: ID = ", id_list[sales_data[0].index(max_sale)], ", Amount = $",
          max_sale, sep='')
    print("Max sales by Quarter: Quarter = ", total.index(max(total)) + 1, ", Amount = $", max(total), sep='')


# Main function which creates flow of the program
# Prompts user for files
def main():
    id_file = input("Enter the name of the sales ids file: ")
    ids, sales = get_IDs(id_file)
    data_file = input("Enter the name of the sales data file: ")
    process_sales_data(data_file, ids, sales)
    print('\n ---------Annual Sales Report---------\n')
    print_report(ids, sales)


# Main function called to run program
main()






