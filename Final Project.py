# Description: This program reads two text files named 'salesids.txt' and 'salesdata.txt' and
# prints out an Annual Sales Report table which contains the quarterly and total sales of each salesman. It also
# contains the total annual sales of the company and of each salesperson.

# Author: Shashwat Shekhar

# Function getIDs has 'filename' as a parameter which contains the name of the file containing the salesperson's IDs.
# It reads the text file and creates two different lists: a list of the IDs ['id_list'] and a list
# that is a two dimensional list of the sales data by quarter for each salesperson ['sales_data']. The getIDs functions
# will return both of these lists.
def getIDs(filename):
    new_file = open(filename, "r")

    # This line breaks the list and reads it.
    new_file_Contents = new_file.read().split()
    new_file.close()

    # This command sorts the employee ID numbers and arranges it in the correct order.
    sales_data = []

    for employee in new_file_Contents:
        # Initiating the values by 0 / Place Holders
        sales_data.append([0.0, 0.0, 0.0, 0.0])
    return  new_file_Contents,sales_data

# Function process_sales_data contains sales data, and id_list and  sales_data  as the parameters. It then reads the
# sales data file and adds all the sales data to the sales_data list totaling all the monthly data into the totals
# for the proper quarter by sales ID. This function does not return any variables.
def process_sales_data(filename, id_list, sales_data):
    new_file = open(filename, "r")
    for entry in new_file:
        sales = entry.split()

        index = id_list.index(sales[0])
        # This line divides it into 3 quarters, 0-1,1-2,2-3 for QT 1,2,3 respectively.
        quart = int((int(sales[1]) - 1) / 3)

        sales_data[index][quart] += float(sales[2])

    new_file.close()


# Function print_report will produce the printed Annual Sales Report from the data supplied in the id_list and
# sales_data lists. It will also calculate the totals by quarter and determine the maximum sales by a sales person
# in a quarter and maximum sales by quarter for the Annual Sales Report.
def print_report(id_list, sales_data):
    saleByID = []
    saleByQuart = [0.0, 0.0, 0.0, 0.0]
    for salePerEmployee in sales_data:
        saleByID.append(sum(salePerEmployee))
        saleByQuart[0] += salePerEmployee[0]
        saleByQuart[1] += salePerEmployee[1]
        saleByQuart[2] += salePerEmployee[2]
        saleByQuart[3] += salePerEmployee[3]
    print("\n\n")
    print("ID\t\tQT1\t\tQT2\t\tQT3\t\tQT4\t\tTotal")
    for index in range(len(id_list)):
        print("%s\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f" % (
        id_list[index], sales_data[index][0], sales_data[index][1], sales_data[index][2], sales_data[index][3],
        saleByID[index]))
    total = sum(saleByQuart)
    print("Total\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f" % (
    saleByQuart[0], saleByQuart[1], saleByQuart[2], saleByQuart[3], total))
    max_sales_by_employee = 0.0
    max_sales_employee = 0
    for employee in sales_data:
        for sale in employee:
            if sale > max_sales_by_employee:
                max_sales_by_employee = sale
                max_sales_employee = sales_data.index(employee)
    max_sale_by_quarter = max(saleByQuart)
    max_sale_quarter = saleByQuart.index(max_sale_by_quarter) + 1
    print("\nMax sales by Salesperson: ID = %s,Amount = $%.2f" % (id_list[max_sales_employee], max_sales_by_employee))
    print("Max sales by Quarter: Quarter = %d, Amount = $%.2f" % (max_sale_quarter, max_sale_by_quarter))

# The main function is controls the overall flow of the program. It will ask the user for the name of
# each of the input files and then call the other three functions in order and the program will be executed by a
# statement calling the main function.
def main():
    # The user is asked to enter the name of the sales id file
    idListFile = input("Enter the name of the sales ids file: ")

    idList, sales_data = getIDs(idListFile)

    # The user is asked to enter the name of the sales data file
    sales_dataFile = input("Enter the name of sales data file: ")

    # Printing the title of the Report to be printed
    print('\n' '\n')
    print('------------Annual Sales Report---------------')

    # Printing the final Annual Sales Report table
    process_sales_data(sales_dataFile, idList, sales_data)
    print_report(idList, sales_data)
main()