# PENETRATION-TESTING-TOOLKIT

 *COMPANY*: CODTECH IT SOLUTIONS

 *NAME*: LEO FRANCIS A

 *INTERN ID*: CT04DM1437 

 *DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

 *DURATION*: 4 WEEKS

 *MENTOR*: NEELA SANTOSH

 
PENETRATION-TESTING-TOOLKIT
 
   This is a Python-based Penetration Testing Toolkit designed to perform basic security assessments such as port scanning, brute-force login attempts, and directory enumeration. It is modular, easy to use, and suitable for students, ethical hackers, and cybersecurity beginners.
   The toolkit is designed with simplicity in mind, allowing users to select different modules from a menu-based interface. It can be used for basic internal security testing, training, and learning how real-world vulnerabilities are identified during penetration tests.

Features & Modules

1. Port Scanner

Scans a range of TCP ports on a given IP address to identify which ports are open and may be running services.

    Uses Python's built-in socket module

    Fast, timeout-based scanning with user-defined port range

    Helps identify possible attack vectors or misconfigured services

2. Brute Force Login

Attempts to guess login credentials on a web form using predefined common username-password pairs.

    Sends HTTP POST requests to the target login URL

    Detects valid credentials by checking for absence of failure message

    Demonstrates how weak login systems can be compromised

3. Directory Enumerator

Checks for common directories and paths on a target website that are not publicly listed.

    Uses HTTP GET requests with a predefined wordlist of common paths

    Detects hidden admin panels, config folders, and upload directories

    Useful for locating entry points in web application testing

Technologies Used

    Programming Language: Python 

    Libraries:

        [socket] – For low-level TCP port communication

        [requests] – For sending HTTP GET and POST requests to web servers

Platform Used

    Operating System: Ubuntu Linux

    Text Editor: Sublime Text 

    Execution Environment: Ubuntu Command Line (Terminal)

    Tested With: Python3


The script uses hardcoded wordlists for usernames, passwords, and directories, but these can be easily modified or replaced with external files.

Output:

Port Scanner:

![Image](https://github.com/user-attachments/assets/d74dc42b-9dbc-434d-ac6c-689d8a6e53d5)


    





