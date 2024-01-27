![VISUAL CODE](https://github.com/roshan4182/language-mastery-app/assets/149868016/ed594f59-c471-4b44-add6-b3086f142de3)![PYTHON](https://github.com/roshan4182/language-mastery-app/assets/149868016/a86a4844-3fbe-41f8-b1b5-684a8858f82a)## Language Learning App

## Overview:-

Welcome to Learn_Word, a Python-based application designed to enhance your vocabulary with a new word every day. This app caters to a diverse audience, including travelers, immigrants, language enthusiasts, and corporate professionals, aiming to bridge language gaps and promote cultural understanding.

 ## Table Of Contents: ##

## 1. Code(https://github.com/roshan4182/language-mastery-app/blob/main/README.md#code)
## 2. Changes in Braches()
## 2.UML Diagrams(https://github.com/roshan4182/language-mastery-app/blob/main/README.md#uml-diagrams)
## 3.Requirements Engineering(https://github.com/roshan4182/language-mastery-app/blob/main/README.md#requirements-engineering)
## 4.Analysis(https://github.com/roshan4182/language-mastery-app/blob/main/README.md#analysis)
## 5.DDD(https://github.com/roshan4182/language-mastery-app#ddd)
## 6.Metrics()
## 7.Clean Code Development()
## 8.Build Management()
## 9.Unit Tests()
## 10.IDE()
## 11.Functional Programming()


## Code  ##

TO ACCESS THE CODE : Language-Mastery-app()


## Changes_Made_With_The_Branches:##


[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/7a90c821da32bb4009ef58da937e76a841ab05e7)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/c4f02ad095a33c224945c11d565d9df338c4ac74)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/41b619b3951da4d501e519a28319d755411173bd)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/48c5840f2b2abcd64787f033b3a42e0af383fb65)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/eed26bf1081f5b1405807f2fd222ec7eb594dc7d)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/bf727ef5460679ea35ba6ce23e15ca21262ce7bc)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/f6b40de9989ad3987963043be32ea6ce4be14c89)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/761ecd5e82a7c20992b780a48753fd02321395e1)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/d031b4bcbc6bf9bcab356831330e7db4c7d2fff8)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/a64a577ef77e53ce513b0020f7db85e4e9c13009)
[Part_B(1)](https://github.com/roshan4182/language-mastery-app/commit/189733d1ff4708045cc72d7582f9ac10b14299f1)





## UML Diagrams:

1. CLASS_DIAGRAM:

This PlantUML diagram illustrates the relationships and dependencies among key entities in a language learning application. The "Word" class represents a vocabulary item with attributes such as id, text, meaning, and translations. Users are represented by the "User" class, which includes attributes like id, username, difficultyLevel, and notificationTime. Learning sessions, depicted by the "LearningSession" class, involve users and are associated with specific words.
The diagram further introduces the "Language" class, representing different languages in the application. The "WordAPI" class handles interactions with an external word API, defining attributes like API_KEY and WORD_API_URL. Notifications are managed by the "Notifications" class, providing a method to show word dialogues. The application's data persistence is facilitated by the "WordRepository" and "UserRepository" classes, responsible for saving and retrieving word and user data, respectively. The directional associations between entities indicate relationships, such as a word belonging to a learning session, a learning session involving a user, and users being associated with repositories for data management. Overall, the diagram provides a concise overview of the core entities and their interactions within the language learning application.

[Class Diagram](https://github.com/roshan4182/language-mastery-app/blob/main/Images/Class_Diagram2.png)




2.  PACKAGE_DIAGRAM:

This PlantUML diagram represents the structure of a hypothetical "language-mastery-app." The app is organized into several components within distinct packages. The "app" package includes main functionality implemented in "main.py," notifications in "notification.py," and interaction with a word API in "word_api.py." The "backend" package comprises an "api" package with an "__init__.py" file and "word_api.py" for API-related functionality, a "database" package with "__init__.py" and "models.py" for database-related functionality, and standalone scripts like "populate_languages.py" and "server.py."
Additionally, there is a "features" package containing "__init__.py" and "new_features.py" for new app features, a "shared" package with "__init__.py" and "words_api_logic.py" for shared logic, and a "tests" package with "__init__.py" and "test_word_api.py" for testing the word API. The diagram provides a visual representation of the app's structural organization, helping developers understand the relationships and dependencies between different components.

[Package Diagram](https://github.com/roshan4182/language-mastery-app/blob/main/Images/Package_Diagram1.png)


3. ACTIVITY_DIAGRAM:

This PlantUML diagram outlines the flow of user interaction within a language learning application. The process begins with the user initiating interaction. The user is then presented with the option to "Set Notification Time." If the user chooses to set the notification time, they proceed to input a specific time in HH:MM:SS format, leading to the successful setting of the notification.
Subsequently, if the user opts to receive notifications ("User chooses yes"), the application proceeds to fetch the "Word of the Day" from a WordsAPI, displaying a random word and its meaning in a dialogue. The user engages in learning the presented word, and the application adjusts the difficulty level accordingly. The learning process is marked as complete, and the user is shown achievement or level progress. Regardless of the user's choice to receive notifications or not, the interaction loop returns to the initial state, allowing for continuous engagement. This diagram provides a clear visualization of the decision flow in the user's language learning journey within the application.

[Activity Diagram](https://github.com/roshan4182/language-mastery-app/blob/main/Images/Activity_Diagram1.png)



## REQUIREMENTS ENGINEERING:


## Functional Requirements:
1. Custom Notification Timing.
2. Difficulty Level Adjustment.
3. Word Of the day Alerts!
4. Multilingual Support.
5. User Registration.
6. Leearning Paths.

## Non-Functional Requirements:
1. Performance.
2. Security.
3. Scalability.
4. Usability.
5. Monitoring and Analytics.
6. Documentation.

## Trello(https://trello.com/b/vrps9Md5/language-mastery-app)

 ** Tasklist **
 >>  [Screenshot1](https://github.com/roshan4182/language-mastery-app/blob/main/Images/Trello1.png)
 >>  [Screenshot2](https://github.com/roshan4182/language-mastery-app/blob/main/Images/Trello2.png)

## Jira(https://privaterelay-nj5tfybqkh.atlassian.net/jira/software/projects/STUD/boards/2?atlOrigin=eyJpIjoiMGY1NDRhMGQ3M2FjNDE3N2JkYzM5MmE3ZWE5NWNjYzciLCJwIjoiaiJ9)

** Kanboard **
 >> [Screenshot1](https://github.com/roshan4182/language-mastery-app/blob/main/Images/Jira1.png)
 >> [Screenshot2](https://github.com/roshan4182/language-mastery-app/blob/main/Images/Jira2.png)




## ANALYSIS:


### Language-Mastery-App Analysis Checklist(https://www.notion.so/Language-Mastery-App-CHECKLIST-7671f3d50e9346a791264111e3678d93?pvs=4)

### Language-Mastery-App Analysis(https://www.notion.so/Language-Mastery-App-Analysis-299b01216c414780b455faea677fba82?pvs=4)


### DDD: 

DDD is basically an approach of software development which concentrates on what real- world problems a software system has to solve.With the help of shared language(UL) communication between technical and non technical teams are more clearer.In order to simplify the design of the system or the software it uses concepts like Aggregates, Repositories and Domain Events.

[pdf](https://github.com/roshan4182/language-mastery-app/blob/main/Docs/DDD.pdf)

## Metrics


[SonarQube](https://github.com/roshan4182/language-mastery-app/blob/main/Images/SonarQube.png)



[Quality gate_Passed](https://sonarcloud.io/summary/new_code?id=roshan4182_language-mastery-app)

[Reliability](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=roshan4182_language-mastery-app)

[Maintanability](https://sonarcloud.io/project/issues?resolved=false&types=CODE_SMELL&id=roshan4182_language-mastery-app)

[Security](https://sonarcloud.io/project/issues?resolved=false&types=VULNERABILITY&id=roshan4182_language-mastery-app)

[SecurityReview](https://sonarcloud.io/project/security_hotspots?id=roshan4182_language-mastery-app)

[Duplications](https://sonarcloud.io/component_measures?id=roshan4182_language-mastery-app&metric=duplicated_lines_density&view=list)



### Clean Code Development:

Clean Code Development (CCD) focuses on writing code that is easy to read, understand, and maintain.

[Pdf](https://github.com/roshan4182/language-mastery-app/blob/main/Docs/Clean%20Code%20Development.pdf)



### Build Management: 

Build management for the Language Mastery App project has been implemented using [Github Actions](https://github.com/roshan4182/language-mastery-app/actions)

[Python CI](https://github.com/roshan4182/language-mastery-app/actions)



### Unit Tests

The unit tests has been done in 2 parts and is written using the unittest framework in Python.

Unit Test 1 Unit Test 2



1. [TestLearnWordApp Class](TestLearnWordApp)

 [test_set_notification_time](test_set_notification_time):
 For TestLearnWordApp, it uses the unittest.mock.patch decorator to mock the user input and plyer.notification.schedule function. It tests whether the set_notification_time method correctly calls the askstring and schedule functions.

 [test_button_click](test_button_click):
 The test_button_click method tests if clicking the "Get Word of the Day" button correctly invokes the get_word_of_the_day method.

 [test_get_word](test_get_word):
 The test_get_word method tests the get_word method of the WordAPI class returns a dictionary with keys "word" and "definition." It is using the unittest framework along with mocking to isolate and test the behavior of the get_word method independently. The assertions verify the expected structure of the output dictionary.


2. [TestNotifications Class](TestNotifications)

[test_show_word_dialogue](test_show_word_dialogue): 

For TestNotifications, it checks if the show_word_dialogue method correctly calls tkinter.messagebox.showinfo with the expected parameters.


3. Running Tests:

The [main](tests/test_main.py) block ensures that if the script is run directly (not imported as a module), the 'unittest.main()' function is called, which discovers and runs the tests.

[Result](https://github.com/roshan4182/language-mastery-app/assets/149868016/864b9b70-af8d-4f15-bce6-1b68b31b700b)


## IDE

I have createed this project on Visual Code IDE,and the shortcuts which are my favourite when using this Environment are as follows:

F5 : Run and Debug

Ctrl + ] / Ctrl + [ : Indentation

Ctrl + / : Comment/Uncomment code lines

Ctrl + B : Show or hide the sidebar

Ctrl + Shift + P : Open the command palette



## Functional Programming

In my Language Mastery App, certain functional programming principles are applied. Here's how the code adheres to these principles:

Final Data Structures: The 'data' attribute in [LearnWordApp](TestLearnWordApp) is initialized with the final result of the API call ('response.json()'), representing exchange rates. It remains unmodified afterward.

Side-Effect-Free Functions: The [get_word_data](test_get_word) function has no side effects, performing an HTTP GET request and returning the JSON response without modifying external state. The convert method is also side-effect-free.



## BUILT USING:

![Uploading PYTHON.svg…](<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="97.5" height="28" role="img" aria-label="PYTHON"><title>PYTHON</title><g shape-rendering="crispEdges"><rect width="97.5" height="28" fill="#3670a0"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="100"><image x="9" y="7" width="14" height="14" xlink:href="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjZmZkZDU0IiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+UHl0aG9uPC90aXRsZT48cGF0aCBkPSJNMTQuMjUuMThsLjkuMi43My4yNi41OS4zLjQ1LjMyLjM0LjM0LjI1LjM0LjE2LjMzLjEuMy4wNC4yNi4wMi4yLS4wMS4xM1Y4LjVsLS4wNS42My0uMTMuNTUtLjIxLjQ2LS4yNi4zOC0uMy4zMS0uMzMuMjUtLjM1LjE5LS4zNS4xNC0uMzMuMS0uMy4wNy0uMjYuMDQtLjIxLjAySDguNzdsLS42OS4wNS0uNTkuMTQtLjUuMjItLjQxLjI3LS4zMy4zMi0uMjcuMzUtLjIuMzYtLjE1LjM3LS4xLjM1LS4wNy4zMi0uMDQuMjctLjAyLjIxdjMuMDZIMy4xN2wtLjIxLS4wMy0uMjgtLjA3LS4zMi0uMTItLjM1LS4xOC0uMzYtLjI2LS4zNi0uMzYtLjM1LS40Ni0uMzItLjU5LS4yOC0uNzMtLjIxLS44OC0uMTQtMS4wNS0uMDUtMS4yMy4wNi0xLjIyLjE2LTEuMDQuMjQtLjg3LjMyLS43MS4zNi0uNTcuNC0uNDQuNDItLjMzLjQyLS4yNC40LS4xNi4zNi0uMS4zMi0uMDUuMjQtLjAxaC4xNmwuMDYuMDFoOC4xNnYtLjgzSDYuMThsLS4wMS0yLjc1LS4wMi0uMzcuMDUtLjM0LjExLS4zMS4xNy0uMjguMjUtLjI2LjMxLS4yMy4zOC0uMi40NC0uMTguNTEtLjE1LjU4LS4xMi42NC0uMS43MS0uMDYuNzctLjA0Ljg0LS4wMiAxLjI3LjA1em0tNi4zIDEuOThsLS4yMy4zMy0uMDguNDEuMDguNDEuMjMuMzQuMzMuMjIuNDEuMDkuNDEtLjA5LjMzLS4yMi4yMy0uMzQuMDgtLjQxLS4wOC0uNDEtLjIzLS4zMy0uMzMtLjIyLS40MS0uMDktLjQxLjA5em0xMy4wOSAzLjk1bC4yOC4wNi4zMi4xMi4zNS4xOC4zNi4yNy4zNi4zNS4zNS40Ny4zMi41OS4yOC43My4yMS44OC4xNCAxLjA0LjA1IDEuMjMtLjA2IDEuMjMtLjE2IDEuMDQtLjI0Ljg2LS4zMi43MS0uMzYuNTctLjQuNDUtLjQyLjMzLS40Mi4yNC0uNC4xNi0uMzYuMDktLjMyLjA1LS4yNC4wMi0uMTYtLjAxaC04LjIydi44Mmg1Ljg0bC4wMSAyLjc2LjAyLjM2LS4wNS4zNC0uMTEuMzEtLjE3LjI5LS4yNS4yNS0uMzEuMjQtLjM4LjItLjQ0LjE3LS41MS4xNS0uNTguMTMtLjY0LjA5LS43MS4wNy0uNzcuMDQtLjg0LjAxLTEuMjctLjA0LTEuMDctLjE0LS45LS4yLS43My0uMjUtLjU5LS4zLS40NS0uMzMtLjM0LS4zNC0uMjUtLjM0LS4xNi0uMzMtLjEtLjMtLjA0LS4yNS0uMDItLjIuMDEtLjEzdi01LjM0bC4wNS0uNjQuMTMtLjU0LjIxLS40Ni4yNi0uMzguMy0uMzIuMzMtLjI0LjM1LS4yLjM1LS4xNC4zMy0uMS4zLS4wNi4yNi0uMDQuMjEtLjAyLjEzLS4wMWg1Ljg0bC42OS0uMDUuNTktLjE0LjUtLjIxLjQxLS4yOC4zMy0uMzIuMjctLjM1LjItLjM2LjE1LS4zNi4xLS4zNS4wNy0uMzIuMDQtLjI4LjAyLS4yMVY2LjA3aDIuMDlsLjE0LjAxem0tNi40NyAxNC4yNWwtLjIzLjMzLS4wOC40MS4wOC40MS4yMy4zMy4zMy4yMy40MS4wOC40MS0uMDguMzMtLjIzLjIzLS4zMy4wOC0uNDEtLjA4LS40MS0uMjMtLjMzLS4zMy0uMjMtLjQxLS4wOC0uNDEuMDh6Ii8+PC9zdmc+"/><text transform="scale(.1)" x="587.5" y="175" textLength="535" fill="#fff" font-weight="bold">PYTHON</text></g></svg>)



![Uploading VISUAL CODE.svg…]<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="190.5" height="28" role="img" aria-label="VISUAL STUDIO CODE"><title>VISUAL STUDIO CODE</title><g shape-rendering="crispEdges"><rect width="190.5" height="28" fill="#0078d7"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="100"><image x="9" y="7" width="14" height="14" xlink:href="data:image/svg+xml;base64,PHN2ZyBmaWxsPSJ3aGl0ZSIgcm9sZT0iaW1nIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHRpdGxlPlZpc3VhbCBTdHVkaW8gQ29kZTwvdGl0bGU+PHBhdGggZD0iTTIzLjE1IDIuNTg3TDE4LjIxLjIxYTEuNDk0IDEuNDk0IDAgMCAwLTEuNzA1LjI5bC05LjQ2IDguNjMtNC4xMi0zLjEyOGEuOTk5Ljk5OSAwIDAgMC0xLjI3Ni4wNTdMLjMyNyA3LjI2MUExIDEgMCAwIDAgLjMyNiA4Ljc0TDMuODk5IDEyIC4zMjYgMTUuMjZhMSAxIDAgMCAwIC4wMDEgMS40NzlMMS42NSAxNy45NGEuOTk5Ljk5OSAwIDAgMCAxLjI3Ni4wNTdsNC4xMi0zLjEyOCA5LjQ2IDguNjNhMS40OTIgMS40OTIgMCAwIDAgMS43MDQuMjlsNC45NDItMi4zNzdBMS41IDEuNSAwIDAgMCAyNCAyMC4wNlYzLjkzOWExLjUgMS41IDAgMCAwLS44NS0xLjM1MnptLTUuMTQ2IDE0Ljg2MUwxMC44MjYgMTJsNy4xNzgtNS40NDh2MTAuODk2eiIvPjwvc3ZnPg=="/><text transform="scale(.1)" x="1052.5" y="175" textLength="1465" fill="#fff" font-weight="bold">VISUAL STUDIO CODE</text></g></svg>()
















