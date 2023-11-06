# Climb Tracker
#### Video Demo:  URL https://youtu.be/3cyXi5ooenQ

#### Description:   

This python program is a tracker for climbers who want to know what climbs they have climbed and the count of the climbs they did ordered by date. It keeps in once place a history of a user's climbs in a csv.  

##### How the program works:  

When project.py is run, a user will be asked to either enter their user name or create a new user. The program will only accept the letter "n" (upper or lower cased), or valid user name. If either one are not provided or the , the program will close out and the user will have to run the program again. I wanted to utilize the sys.exit function and understand that it isn't the most user friendly.  

When a current user enters their user name, they are prompted for a password.  The program will keep prompting for a password until a correct one is provided. 

A new user will be asked to create a user name and a password. The program will ask the user to confirm the password and if the passwords do not match, the user will be prompted to create a password until the passwords match. When the passwords match, the user and password is now added to the climber_info.csv file. A new tracker csv file is created for that user name, username+"_tracker.csv"

When a user is in their account, they are asked to select from four selections (this is all encapsulated in a while loop):  

A. Allows you to add to the user's tracker. A user is able to add as many grades they want to the tracker as long as they are valid YDS climbing grades. If one isn't entered correctly, the user will have to enter their grades again correctly. This is a feature that can be better made if the program picked out the incorrect grade and prompted the user to correct that particular one. I didn't have enough time to do that. When the grades are accepted, it will be added to the user's tracker csv file, where current date is the defaulted date. 

B. This selection accesses the user's csv file and returns data and tabulates it so it's easily readable to the user. 

C. This access the user's csv file counts the number of climbs done on a given date from the first entry date.  It is also tabulated for user readability.

D. This means the user is finished with the program whereby the program will exit and wish the user a good day. Selecting this will break out of the while loop.  

If a user doesn't select from a, b, c, or d, they will alerted that their selection is not valid and to select again. 

##### Skills learned: 

There were many skills I had to learn to create this functional program. One is not only learneding about pandas but also the balance between deciding when using pandas or csv. I learned that creating programs is much like construction work, give yourself a timeframe you think it will take to get done and double it. I learned how to effectively google, read documentation, read instructions and having the patience to fully understand how python works. Another skill that is probably the most important of all is figuring out what to name variables and functions for practical and readability purposes. I learned how to use matplotlib to plot date and number of climbs for each user and realized that I had to simplify my program for the time being and that a standard table would be more effective at this point in time. 

##### Potential future features: 

Features that would make this program better would be to allow users to add their own dates to their data instead of a default of today's date and add the name of the climb they climbed. It would be beneficial to climbers to be able to see charts or graphs of their data. Another feature that can be worked on in the future is encrypting passwords or at least making the passwords not appear when entering them. It would also be interesting to be able to show the progression of a climber through time, via showing them the grades they used to climb vs what they climb now.  I supsect I may need to brush up on statistics to add this function.

##### Final Thoughts: 

I have a new found appreciation for programmers who create the simplest programs. Just creating this bare bones version of a user and password took a long time and thought. 