# WizzWeb Scraper

This is an initial version 0.1, later on changes will be added

The scope of the application is to export Price from a certain flight and continously monitor the price of the flight at a certain amount of time.
For instance the default value is 300 secounds - 5 minutes. 

URL value must be changed based on the flight you're interested.
Code is using an XPATH value to get the price from the DIV container, however this can be changed.
It depends if Wizz is changing their frontweb page elements.

There are 3 headers & columns on the CSV exported
PATH of the CSV export is defined as your current user Desktop.

DATE, PRICE & TIME

Later on, i'll be adding new elements. (Like Flight Time, Sold Out tickets, Price Alert Notification, etc.)

GUI interface upcoming
