#Medication Reminder & Pill Identifier

● Overview of the project
A simple Python application that helps users manage their medication schedule and identify unknown pills. It combines a reminder system that alerts users when it's time to take their medicine with a basic pill identifier that matches pills by color, shape, and imprint code.

● Features

Add medications with specific reminder times

Background reminder system that checks every minute

Pill identification using color, shape, and imprint codes

Persistent storage of medication data

Simple text-based interface that's easy to use

● Technologies/tools used

Python 3

JSON for data storage

datetime and time modules for scheduling

Standard file I/O for saving user data

● Steps to install & run the project

Make sure you have Python installed on your computer

Download the meds_app.py file

Open terminal/command prompt in the same folder

Run: python meds_app.py

The app will create a meds_data.json file automatically to store your medications

● Instructions for testing

Start by adding a medication using option 1 - try setting the time a few minutes ahead

Use option 2 to test pill identification - try "white", "round", "AP" for Aspirin

Start reminders with option 3 to see alerts when scheduled times match current time

Close and reopen the app to verify your medications are saved

Test with different pill combinations from the small built-in database

Try entering invalid pill details to see the "no idea" response

