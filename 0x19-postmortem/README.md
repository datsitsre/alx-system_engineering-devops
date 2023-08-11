A postmortem by Atsitsre Daniel about a incident that happened at Headquarters on the database server at around 2:00 am
Issue Summary
The website wasn’t able to display information to the user. Any time the user accesses the company website the output was website down. Users across the continent experience the same problem. Although the web address correct and the website wasn’t appearing for users to access. 
Timeline Summary
•	Start 2:00 GMT 19 August 2020 - 3:00 am GMT  19 August 2020
•	Duration was about a 1 hour 
•	At around 2.:00 GMT
•	The monitoring system alerted the staff about 2:15 GMT
•	Check all system for errors that may have cause the problem
•	Later found out the database server was down
•	Moved the website to run on a backup database and isolate the system
•	Resolved the issue by correcting the issue in the address
•	At about 3:00GMT the problem was resolved
Root Cause
At around 2:15 am GMT the incident report team was alerted about the website being down across the continent. Most user went on twitter to pour out their displeasure of them not being able to access the website. Some users contacted the team to alert us about the issues through about help desk our social media handles especially twitter and posting images of errors they have encounter. The information was much help cause to help us the narrow down the problem. Our internal system offers us more information about the actually problem. We took most serves offline example database, proxy server, file server. Firstly, we check the file server if the website is able to access the files and also the database server where we notice that there was an error in the web address of the website making it difficult for database to resolve the web address timely. 
Correction and Resolution
Since the problem was from the database server, we redirect access to the backup database server and worked on the main database server correction the address. Later test it out with redundant website and it worked perfectly. The actual website we redirected back to the main database server and test for further errors where everything worked well.

Preventive remedies 
•	Timely check of the database server every hour to pick up likely issues
•	Every server should have an alert system to alert engineers early 
•	The alert should be sent by mal or text message.
