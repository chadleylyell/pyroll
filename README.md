# PyRoll
PyRoll is a time clock system that is written purely in Python. PyRoll reads a directory, `employees`, and checks for the employee PIN. If the PIN is correct, the employee can clock in or out, and view their time card. See below for more information

### Clocking In
Before an employee can clock in, they must enter their PIN. PyRoll will then search through the `employees` directory for the time card that corresponds with the entered PIN. If it cannot locate the time card that corresponds with the PIN, they will be prompted to enter a correct PIN.

If they log in successfully, they can go ahead and clock in. When an employee clocks in, the current date and time is written to the time card and saved.

### Clocking Out
When the employee clocks out, the current date and time is written to a file, and an indicator (simply a line) is drawn in the time card to show they ended the shift.

The flaw with this right now, is that if the employee hit clock out first, there would be no error message to alert them they need to clock in <b>before</b> they clock out. This system is still a work in progress.

### Viewing Hours
At any time, an employee can logon and view a copy of their time card. It will simply read out the entire time card.

### Admin Features
There is also an admin feature built into the system. If an admin logs in entering a specific, hardcoded PIN, then they will be able to access any employee time card to print out to the screen (not physically print... yet...)

# Upcoming Features
I am currently working on adding some features to improve the application. They are each discussed below.

### Web App or GUI
I am currently learning how to use web frameworks like Django. I may completely rebuild this into a web application. That'd be in the distant future. If I don't make it into a Django web app, I may use a GUI library like Tkinter to make an acutal application.

### Caluclate Total Hours
I will most likely make a function that actually informs the employee (or admin) how many hours they worked in a given week.

### Vacation Request
This feature would allow the employee to go in and request time off. I am thinking of adding email into this feature to inform the employee whether or not the time off was approved or denied. A feature will be implament

### Lunch
I am currently working on making it possible for the employee to take a lunch break.

# Upcoming Admin Features
I'm currently working on improving the administration features available to the system admin. The features are summarized below.

### Password Protection
As of right now, anyone could access the admin account because like any account, you simply need to enter a PIN. We'll be working to make it so after you enter a valid admin PIN, you need to enter the admin account password.

### Add or Remove Employees
In order to add (or remove an employee) you have to do it by navigating to the `employees` directory, and adding a `.txt` file with the employee PIN as the name or deleting that file if the employee no longer works there. We're working to improve this by making a feature for the admin able to do this right from their account, without the need to do it manually.

### Calcualte Pay
This is a pretty important feature in any payroll system, the money. We'll make the admin able to set the current wage, and then make it possible to caluclate the employees total hours to determine how much they get paid.
