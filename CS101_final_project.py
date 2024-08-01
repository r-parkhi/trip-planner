'''
CS101 Final Project: Trip Planner

Description: This program helps you choose a destination, manage your budget, and create a checklist all in one place.

Developer Name(s): Radhika Parkhi

Date: 07/29/2024
Modified 07/30/2024
'''
##########################################
# IMPORTS:
#   modules needed for program
##########################################
from tkinter import *;
from tkinter.ttk import Combobox;

##########################################
# GLOBAL VARIABLES:
#   variables needed for program
##########################################
name = '';
days = '';
selected_city = '';
combobox_us_cities = '';
combobox_intl_cities = '';
row_num = 15;
location = '';

##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
# function that sets the name
def set_name(event):
    global name;
    name = str(entry_name.get());
    
    # if string is not empty, change bg color
    if name != '':
        entry_name.config(bg = 'peach puff');

# function that sets the number of days
def set_days(event):
    global days;
    days = int(entry_days.get());
    entry_days.config(bg = 'peach puff');

# function that shows list of US cities
def show_us():
    # select label
    label_select = Label(root, text = 'Select a city:', font = ('Helvetica', 10, 'bold'), bg = 'light blue', fg = 'DarkOrange2');
    label_select.grid(row = 5, column = 1);
    
    # US city combobox
    global combobox_us_cities;
    combobox_us_cities = Combobox(root, width = 9, textvariable = selected_city, values = us_cities, );
    combobox_us_cities.grid(row = 5, column = 2);

    # bind US combobox to on_select function
    combobox_us_cities.bind('<<ComboboxSelected>>', on_us_select);

# function that shows list of international cities
def show_intl():
    # select label
    label_select = Label(root, text = 'Select a city:', font = ('Helvetica', 10, 'bold'), bg = 'light blue', fg = 'DarkOrange2');
    label_select.grid(row = 5, column = 1);
    
    # international city combobox
    global combobox_intl_cities;
    combobox_intl_cities = Combobox(root, width = 9, textvariable = selected_city, values = intl_cities);
    combobox_intl_cities.grid(row = 5, column = 2);    
    
    # bind US combobox to on_select function
    combobox_intl_cities.bind('<<ComboboxSelected>>', on_intl_select);

# function that executes when US cities (no button) is selected
def on_us_select(event):
    global days;
    global combobox_us_cities;
    global name;
    global location;
    
    location = 'us';
    days = str(days);
    
    selected_city = combobox_us_cities.get();
    
    # reconfigure trip info label
    label_trip_info.config(text = name + ' is traveling to ' + selected_city + ' for ' + days + ' days.');

# function that executes when international cities (yes button) is selected
def on_intl_select(event):
    global days;
    global combobox_intl_cities;
    global name;
    global location;
    
    location = 'intl';
    days = str(days);
    
    selected_city = combobox_intl_cities.get();
    
    # reconfigure trip info label
    label_trip_info.config(text = name + ' is traveling to ' + selected_city + ' for ' + days + ' days.');

# function that calculates estimated costs of the trip
def calculate_costs():
    global days;
    days = int(days);
    
    entry_budget.config(bg = 'peach puff');
    entry_hotel.config(bg = 'peach puff');
    entry_meals.config(bg = 'peach puff');
    entry_acts.config(bg = 'peach puff');
    
    budget = int(entry_budget.get());
    hotel = int(entry_hotel.get());
    meals = int(entry_meals.get());
    acts = int(entry_acts.get());
    
    # calculate & configure total costs label
    hotel = hotel * days;
    total = hotel + meals + acts;
    label_total_costs.config(text = 'The total estimated cost of ' + name + "'s trip is $" + str(total) + '\nand their budget is $' + str(budget) + '.');

# function that adds a task to the checklist
def add_task():
    # taskname entry
    entry_taskname = Entry(root, width = 15, fg = 'DodgerBlue2');
    entry_taskname.grid(row = 16, column = 2);
    
    #function that creates a checkbutton
    def create_checkbutton(event):
        # name task with input from taskname_entry
        taskname = str(entry_taskname.get());
        entry_taskname.config(bg = 'peach puff');
        checkbutton_custom = Checkbutton(root, text = taskname, font = ('Helvetica', 10), bg = 'light blue', fg = 'DodgerBlue2');
        
        # add 1 to row_num & place checkbutton
        global row_num;
        row_num += 1;
        checkbutton_custom.grid(row = row_num, column = 1);
        
    # bind 'return' key to create_checkbutton function
    entry_taskname.bind('<Return>', create_checkbutton, add = '+');
    
# function that adds suggested tasks to the checklist
def sug_tasks():
    global selected_city;
    global location;
    
    # if location is US, suggest from us_tasks list
    if location == 'us':
        for x in us_tasks:
            checkbutton_sug = Checkbutton(root, text = x, font = ('Helvetica', 10), bg = 'light blue', fg = 'DodgerBlue2');
            
            # add 1 to row_num & place checkbutton
            global row_num;
            row_num += 1;
            checkbutton_sug.grid(row = row_num, column = 1);
            
            button_sug_tasks.config(state = 'disabled');
    
    # if location is international, suggest from intl_tasks list
    if location == 'intl':
        for x in intl_tasks:
            checkbutton_sug = Checkbutton(root, text = x, font = ('Helvetica', 10), bg = 'light blue', fg = 'DodgerBlue2');
            
            # add 1 to row_num & place checkbutton
            #global row_num;
            row_num += 1;
            checkbutton_sug.grid(row = row_num, column = 1);
            
            button_sug_tasks.config(state = 'disabled');

##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################
root = Tk();
root['bg'] = 'light blue';

# title label
label_title = Label(root, text = 'Trip Planner', font = ('Helvetica', 22, 'bold'), bg = 'light blue', fg = 'dark orange');
label_title.grid(row = 1, column = 1);

# BASIC QUESTIONS
# name label & entry
label_name = Label(root, text = 'What is your name?', font = ('Helvetica', 10, 'bold'), bg = 'light blue', fg = 'DarkOrange2');
label_name.grid(row = 2, column = 1);
entry_name = Entry(root, width = 10, fg = 'DodgerBlue2');
entry_name.grid(row = 2, column = 2);

entry_name.bind('<Return>', set_name);

# days label & entry
label_days = Label(root, text = 'How many days are you traveling?', font = ('Helvetica', 10), bg = 'light blue', fg = 'DarkOrange2');
label_days.grid(row = 3, column = 1);
entry_days = Entry(root, width = 5, fg = 'DodgerBlue2');
entry_days.grid(row = 3, column = 2);

entry_days.bind('<Return>', set_days, add = '+');


# DESTINATION QUESTIONS
# destination label
label_dest = Label(root, text = 'Are you traveling internationally?', font = ('Helvetica', 10), bg = 'light blue', fg = 'DarkOrange2');
label_dest.grid(row = 4, column = 1);

# yes button
button_dest_yes = Button(root, text = 'Yes', command = show_intl, fg = 'DodgerBlue2', activeforeground = 'DodgerBlue4');
button_dest_yes.grid(row = 4, column = 2);

# no button
button_dest_no = Button(root, text = 'No', command = show_us, fg = 'DodgerBlue2', activeforeground = 'DodgerBlue4');
button_dest_no.grid(row = 4, column = 3);

# US city list
us_cities = ['Honolulu',
             'New York',
             'Seattle',
             'Chicago',
             'Salt Lake'];

# international city list
intl_cities = ['Mumbai',
               'Barcelona',
               'Seoul',
               'Sydney',
               'Prague'];

# trip info label
label_trip_info = Label(root, text = '', font = ('Helvetica', 10, 'bold'), bg = 'light blue', fg = 'DodgerBlue2');
label_trip_info.grid(row = 13, column = 1);

# divider label
divider = Label(root, text = '', font = ('Helvetica', 10), bg = 'light blue', fg = 'DarkOrange2');
divider.grid(row = 6, column = 1);


# BUDGET QUESTIONS
# budget intro label
label_budget_intro = Label(root, text = 'Fill in the following questions...', font = ('Helvetica', 10, 'bold'), bg = 'light blue', fg = 'dark orange');
label_budget_intro.grid(row = 8, column = 1);

# your budget label & entry
label_budget = Label(root, text = 'Initial budget: $', font = ('Helvetica', 10), bg = 'light blue', fg = 'DarkOrange2');
label_budget.grid(row = 9, column = 1);
entry_budget = Entry(root, width = 5, fg = 'DodgerBlue2');
entry_budget.grid(row = 9, column = 2);

# hotel cost label & entry
label_hotel = Label(root, text = 'Rate per night of hotel: $', font = ('Helvetica', 10), bg = 'light blue', fg = 'DarkOrange2');
label_hotel.grid(row = 10, column = 1);
entry_hotel = Entry(root, width = 5, fg = 'DodgerBlue2');
entry_hotel.grid(row = 10, column = 2);

# meal cost label & entry
label_meals = Label(root, text = 'Max meal expenses: $', font = ('Helvetica', 10), bg = 'light blue', fg = 'DarkOrange2');
label_meals.grid(row = 11, column = 1);
entry_meals = Entry(root, width = 5, fg = 'DodgerBlue2');
entry_meals.grid(row = 11, column = 2);

# activities cost label & entry
label_acts = Label(root, text = 'Max activity expenses: $', font = ('Helvetica', 10), bg = 'light blue', fg = 'DarkOrange2');
label_acts.grid(row = 12, column = 1);
entry_acts = Entry(root, width = 5, fg = 'DodgerBlue2');
entry_acts.grid(row = 12, column = 2);

# calculate button
calculate_costs = Button(root, text = 'Calculate', command = calculate_costs, fg = 'DodgerBlue2', activeforeground = 'DodgerBlue4');
calculate_costs.grid(row = 13, column = 3);

# total costs label
label_total_costs = Label(root, text = '', font = ('Helvetica', 10, 'bold'), bg = 'light blue', fg = 'DodgerBlue2');
label_total_costs.grid(row = 14, column = 1);


# TRAVEL CHECKLIST
# list title label
label_list_title = Label(root, text = 'Travel Checklist', font = ('Helvetica', 10, 'bold'), bg = 'light blue', fg = 'dark orange');
label_list_title.grid(row = 15, column = 1);

# add task buttton
button_add_task = Button(root, text = 'Add task', command = add_task, fg = 'DodgerBlue2', activeforeground = 'DodgerBlue4');
button_add_task.grid(row = 15, column = 2);

# suggested tasks buttton
button_sug_tasks = Button(root, text = 'Suggested tasks', command = sug_tasks, fg = 'DodgerBlue2', activeforeground = 'DodgerBlue4');
button_sug_tasks.grid(row = 15, column = 3);

# US trip tasklist
us_tasks = ['buy travel tickets',
            'reserve rental car',
            'pack carry-on snacks'];

# international trip tasklist
intl_tasks = ['pack passport',
              'exchange foreign currency',
              'get necessary vaccinations']


root.mainloop();