## Automatically Tracking File Changes with Python ##

about this LiveProject

In this liveProject, you will fill the role of a software developer at PharmaDeal Iberia,
A pharmaceutical supply chain company that operates across southern Spain and Portugal. 
You have been given the task to learn and work with the company’s audit team.
Implement a Python tool that can produce a report of what important documents 
change through the organization and their frequency. 
This tool will be deployed and used per user. 
Your work as a developer in understanding how to find what files change across an organization is crucial, 
as compliance regulations across the EU become tighter by the day, 
there is a need within PharmaDeal to track what important 
documents change within the organization so that the company’s document 
audit team ensures that all-important documents comply with all industry 
and EU regulations—which is something that Microsoft Office doesn’t have out-of-the-box support for.

### Assignment ###

Therefore, your assignment at PharmaDeal is as follows:

*  Create and connect to a local SQLite database
*  Create tables and cursors specifically designed for tracking file changes
*  Understand and work with file information and MD5 hashes
*  Understand and work with tables specifically designed for tracking file changes
*  Apply Automation principles to the tool
*  Generate a Change Report

### To Do ###

Techniques employed

The following are some of the techniques you’ll employ throughout this project.
Don’t worry if you haven’t mastered any of these areas 
we’ll give you the necessary resources to learn more about each.
Automation developers use a diverse range of techniques to achieve the goal
set forth for this project, many of which are picked up on the job.

Listed under the bullet points that follow, are the steps required to implement this project.

- [ ] Create and connect to a local SQLite database
        Usage of the built-in Python OS, sys, and SQLite libraries
        Write a series of Python functions that can create an SQLite instance
        Write a Python function that can query the master database for the SQLite instance created
        Write a series of Python functions that can create and connect to a database hosted within the SQLite instance

- [ ] Create tables and cursors specifically designed for tracking file changes
        Write a series of Python functions that can create file-level tracking database tables on an SQLite instance
        Write a Python function that can create file-level tracking table indexes on an SQLite instance
        Write a Python function that can perform query the master database and determine if a database table exists on an SQLite instance
        Write a Python function that can create a database table cursor on an existing database table, on an SQLite instance

- [ ] Understand and work with file information and MD5 hashes
        Write a Python function that can read file-level access and DateTime info on any given file
        Write a Python function that can generate an MD5 hash for any given file
        Write a Python function that can determine (calculate) the MD5 hash of any given file, which will be later used to determine if a file has changed
        Write a Python function that can secure a file using an MD5 hash

- [ ] Understand and work with tables specifically designed for tracking file changes
        Write a Python function that can insert file-level data into database tables using the SQLite INSERT command
        Write a Python function that can update file-level data into database tables using the SQLite UPDATE command
        Write a Python function that can remove file-level data from database tables using the SQLite DELETE command
        Write a Python function that can query file-level data from database tables using the SQLite SELECT command

- [ ] Apply Automation principles to the tool
        Write a Python function that can traverse (navigate) through a complete folder structure (including subfolders) and can filter out specific file types
        Write a Python function that can monitor file changes on specific files types and folders
        Write a Python function that can query file data on an SQLite instance after detecting file changes, using calculated MD5 hashes to check for file differences

- [ ] Generate a Change Report
        Create a series of Python functions that can use the openpyxl library to create an Excel report, using built-in functions provided by the openpyxl library
        Create a Python function that can aggregate existing data gathered through file monitoring and consolidate it into an Excel report, using built-in functions provided by the openpyxl library
        Create a batch file that can invoke Python and run the script, which can be executed through the command line, during operating system startup, or through a scheduled task. 
            This technique will allow the finalized tool to easily be deployed and executed on a Windows environment.

Note: The company-wide consolidation of the various Excel reports from each user machine, is beyond the scope of the project. The tool that you will be creating throughout this project produces a report of the files that change, per user/machine only.

