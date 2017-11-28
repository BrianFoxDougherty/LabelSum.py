LabelSum.Py README

Author: Brian Fox Dougherty

------------------------------
COMPATIBILITY:

Runs on Python version 3, tested on version 3.63 on Windows 10.  Latest version of Python can be obtained here:

https://www.python.org/downloads/


INSTRUCTIONS:

To run, make sure Python is installed with the correct PATH set to its executable.  

Copy LabelSum.py and Data.json to a convenient directory.

Then execute by running from a command line with the JSON file path as the first argument, -f.  There is an optional argument of -d which will output a lot more operational information.  

Example:

LabelSum.py -f "c:\temp\Data.json"

Example of running with debugging turned on:

LabelSum.py -f "c:\temp\Data.json" -d


OPERATION:

Given a JSON string which describes a menu, calculate the SUM of the IDs of all "items", as long as a "label" exists for that item.


NOTES:

This was my first Python project after a few years hiatus from it so I used this project as an opportunity to refresh my skills.  As a result I played around a little with data types, using Lists and Dicts in loops just to get the feel of them again.  There probably is a more efficient way of splitting this data up and typing it, but it seems to work well for the scope of this project.  Please feel free to suggest a better implementation!


------------------------------