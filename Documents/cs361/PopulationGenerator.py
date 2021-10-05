import sys
import csv

data_filename = 'AllStates.csv'

def main():
    print(sys.argv)
    year_sel = int(sys.argv[1])
    year_str = sys.argv[1]
    print('year_sel=%d' % year_sel)
    print('year = %s' % year_str)
    input_filename = year_str + data_filename
    print(input_filename)
    state_sel= sys.argv[2]
    result=getFirstDataRowValue(input_filename,1,state_sel)
    print(result)
    
    # if input_filename:
        # year = getInputtedYearFromCSV(input_filename)
        # state = getInputtedStateFromCSV(input_filename)
        # population = getStatePopulationFromDataFile(input_filename)
        # print("Year: ",year)
        # print("State: ",state)
        # print("Population: ",population)

def getInputFilename():
    return sys.argv[1]

def getFirstDataRowValue(input_filename, col_number,state):
    
    population = -1
    with open(input_filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 
        # next(csvfile)
        for row in reader:
            data = row[col_number]
            # print(data)
            if data == state:
                population=row[2]
    return population
    
    
def getInputtedYearFromCSV(input_filename):
    return getFirstDataRowValue(input_filename,0)

def getInputtedStateFromCSV(input_filename):
    return getFirstDataRowValue(input_filename,1)

def getStatePopulationFromDataFile(input_filename):
    population = ''
    with open(data_filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            state = row[0]
            if state == input_filename:
                population = row[1]
    return getFirstDataRowValue(input_filename,2)
main()


# from os import path
# from tkinter import *

# # import pandas as pd

import tkinter as t
from tkinter.constants import END
from tkinter.filedialog import askopenfile



# root = t.Tk()
# myLabel = Label(root,text="Population Generator - Search by state and year")
# # root.title("Population Generator - Search by state and year")
# root.geometry('1000x500')
# myLabel.place(x=900, y=250)
# root.mainloop()

# canvas = t.Canvas(root, width=250, height=150)
# canvas.grid()

# states = []
# years = []
# root.mainloop()
# with open("input.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader)
#     for categories in reader:
#         selection_list = categories[8].split('>')
#         selection_list2 = years[8].split('>')

#         if selection_list[0] not in states or years:
#             states.append(selection_list[0])
#             years.append(selection_list2[0])
#         states.sort()
#         years.sort()

# category_menu = t.StringVar(root)
# category_menu.set("select by Year and State")

# o = t.OptionMenu(root, category_menu)
# o.place(x=400, y=50)

# entry= t.Entry(root, width=10, justify='center')

# canvas.create_window(150,100,window= entry)
# entry.place(x=440, y=120)

# text_box = t.Text(root, width=200, height = 30)
# text_box.grid(row=4, column= 0, columnspan= 2)

# def show_population():
#     text_box.delete('1.0', END)
#     user_input = int(entry.get())

    # data = pd.read_csv("output.csv")
    # pd.set_option('display.max_colums', None)
    # pd.set_option('display.max_rows',None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)
    # pd.set_option('colheader_justify','left')
    # data.head()

    # selection_list.reset_index(drop=True, inplace=True)

    # text_box.insert("end", selection_list[["year","state","population"]].head(user_input))

# button1 = t.Button(root, text='display population', command=show_population, bg='grey',fg='white').grid(row=3)
# canvas.create_window(150,140,window=button1)

# if path.exists('input.csv'):

#     with open('input.csv', 'r',) as file:
#         reader= csv.reader(file, delimiter=',')
#         next(file)
#         for row in reader:
#             category_chosen =row[1]
#             number_gen = row[2]
#         if not category_chosen:
#             category_chosen= None
#         if not number_gen:
#             number_gen = 0
#     output = pd.read_csv("output.csv")

#     to_excel = {'input_item_type': 'states', 'input_item_category': category_chosen, 'input_number_to_generate': number_gen, 'output_item_name': ["state_name"]}

#     df= pd.DataFrame(to_excel)

#     df.to_csv('output.csv', index=False)



            
    


