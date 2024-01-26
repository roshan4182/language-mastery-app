## Language Learning App

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
[Class Diagram](https://github.com/roshan4182/language-mastery-app/blob/main/Class_Diagram2.png)




2.  PACKAGE_DIAGRAM:

This PlantUML diagram represents the structure of a hypothetical "language-mastery-app." The app is organized into several components within distinct packages. The "app" package includes main functionality implemented in "main.py," notifications in "notification.py," and interaction with a word API in "word_api.py." The "backend" package comprises an "api" package with an "__init__.py" file and "word_api.py" for API-related functionality, a "database" package with "__init__.py" and "models.py" for database-related functionality, and standalone scripts like "populate_languages.py" and "server.py."
Additionally, there is a "features" package containing "__init__.py" and "new_features.py" for new app features, a "shared" package with "__init__.py" and "words_api_logic.py" for shared logic, and a "tests" package with "__init__.py" and "test_word_api.py" for testing the word API. The diagram provides a visual representation of the app's structural organization, helping developers understand the relationships and dependencies between different components.
[Package Diagram](https://github.com/roshan4182/language-mastery-app/blob/main/Package_Diagram1.png)


3. ACTIVITY_DIAGRAM:

This PlantUML diagram outlines the flow of user interaction within a language learning application. The process begins with the user initiating interaction. The user is then presented with the option to "Set Notification Time." If the user chooses to set the notification time, they proceed to input a specific time in HH:MM:SS format, leading to the successful setting of the notification.
Subsequently, if the user opts to receive notifications ("User chooses yes"), the application proceeds to fetch the "Word of the Day" from a WordsAPI, displaying a random word and its meaning in a dialogue. The user engages in learning the presented word, and the application adjusts the difficulty level accordingly. The learning process is marked as complete, and the user is shown achievement or level progress. Regardless of the user's choice to receive notifications or not, the interaction loop returns to the initial state, allowing for continuous engagement. This diagram provides a clear visualization of the decision flow in the user's language learning journey within the application.
[Activity Diagram](https://github.com/roshan4182/language-mastery-app/blob/main/Activity_Diagram1.png)



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
 
 >>  Tasklist(Image())

## Jira(https://privaterelay-nj5tfybqkh.atlassian.net/jira/software/projects/STUD/boards/2?atlOrigin=eyJpIjoiMGY1NDRhMGQ3M2FjNDE3N2JkYzM5MmE3ZWE5NWNjYzciLCJwIjoiaiJ9)

 >>  Kanban Board(Image())




## ANALYSIS:


### Language-Mastery-App Analysis Checklist(https://www.notion.so/Language-Mastery-App-CHECKLIST-7671f3d50e9346a791264111e3678d93?pvs=4)

### Language-Mastery-App Analysis(https://www.notion.so/Language-Mastery-App-Analysis-299b01216c414780b455faea677fba82?pvs=4)


### DDD: 

DDD is basically an approach of software development which concentrates on what real- world problems a software system has to solve.With the help of shared language(UL) communication between technical and non technical teams are more clearer.In order to simplify the design of the system or the software it uses concepts like Aggregates, Repositories and Domain Events.
[Pdf.pdf](https://github.com/roshan4182/language-mastery-app/files/14059437/Pdf.pdf)


## Metrics
![Image 26-01-24 at 4 53 AM](https://github.com/roshan4182/language-mastery-app/assets/149868016/498dfdda-3d7f-4355-b178-9ced78f6cd45)




[Quality gate_Passed](https://sonarcloud.io/summary/new_code?id=roshan4182_language-mastery-app)

[Reliability](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=roshan4182_language-mastery-app)

[Maintanability](https://sonarcloud.io/project/issues?resolved=false&types=CODE_SMELL&id=roshan4182_language-mastery-app)

[Security](https://sonarcloud.io/project/issues?resolved=false&types=VULNERABILITY&id=roshan4182_language-mastery-app)

[SecurityReview](https://sonarcloud.io/project/security_hotspots?id=roshan4182_language-mastery-app)

[Duplications](https://sonarcloud.io/component_measures?id=roshan4182_language-mastery-app&metric=duplicated_lines_density&view=list)



### Clean Code Development:

Clean Code Development (CCD) focuses on writing code that is easy to read, understand, and maintain.










## Frontend:-
   *App Framework: Tkinter
   *UI/UX Design: canva
## Backend:-
   *Server: Flask
   *API Integration: Flask-RESTful
   *Database: SQLite


















