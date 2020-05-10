# Sales Data Analysis

## Introduction

A company has multiple sales people. Every month, they go on road trips to sell the company's product. At the end of each month, the total sales for each sales person, together with that salesperson's ID and the month, is recorded in a file. At the end of each year, the manager of the company wants to see an Annual Sales Report in the format illustrated in the sample execution below. Your report should look substantially similar to the example execution and the numbers should all be the same.

In this report, QT1 stands for quarter 1 (months 1-3), QT2 for quarter 2 (months 4-6), and so on.

The salespeople's IDs are stored in one file and the sales data is stored in another file. The sales data is in the following form:

SalespersonID month salesAmount
.
.
.

The names of the salesID file and sales data file will be entered by the user when the program is executed. The salesID file and the sales data file are in no particular order. View the two provided files in notepad to see what the files look like after you download them. They should be placed in the same directory where your Final Project .py file will be saved.

Notice that the data in the report is in sorted order by salesID.

The program will have the following functions:

### def getIDs(filename):

Where filename is a parameter which will contain the name of the file containing the salesperson's IDs.
The getIDs function will read the salesperson's IDs file and create two Python lists: a list of the IDs and a list that is a two dimensional list of the sales data by quarter for each salesperson. The four columns will be float values that will contain the 4 quarters totals in columns 0-3. Two dimensional lists will be explain in more detail in the accompanying video. This list will contain the value 0.0 for all of the entries.The getIDs functions will return both of these lists.

### def process_sales_data(filename, id_list, sales_data):

where filename will contain the name of the file containing the sales data, and id_list and sales_data are the two Python lists created by the getIDs function.
The process_sales_data function will read the sales data file and add all the sales data to the sales_data list totaling all the monthly data into the totals for the proper quarter by sales ID. This function will not return any variables but the sales_data list will have been modified with the sales data.

### def print_report(id_list, sales_data):

where id_list and sales_data are the two Python lists created by the getIDs function and modified by the process_sales_data function.

This function will produce the printed Annual Sales Report from the data supplied in the id_list and sales_data lists. It will also calculate the totals by quarter and determine the maximum sales by a sales person in a quarter and maximum sales by quarter for the Annual Sales Report.

### def main():

The main function will control the overall flow of the program. It will ask the user for the name of each of the input files and then call the other three functions in order. The program will be executed by a statement calling the main function. Use as many Python built in functions to do your calculations as possible. It will save you programming.

