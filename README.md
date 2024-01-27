## Language Learning App

## Overview:-

Welcome to Learn_Word, a Python-based application designed to enhance your vocabulary with a new word every day. This app caters to a diverse audience, including travelers, immigrants, language enthusiasts, and corporate professionals, aiming to bridge language gaps and promote cultural understanding.

 ## Table Of Contents: ##

## 1. Code(https://github.com/roshan4182/language-mastery-app/blob/main/README.md#code)
## 2. Changes in Braches(https://github.com/roshan4182/language-mastery-app#changes_made_with_the_branches)
## 2.UML Diagrams(https://github.com/roshan4182/language-mastery-app/blob/main/README.md#uml-diagrams)
## 3.Requirements Engineering(https://github.com/roshan4182/language-mastery-app/blob/main/README.md#requirements-engineering)
## 4.Analysis(https://github.com/roshan4182/language-mastery-app/blob/main/README.md#analysis)
## 5.DDD(https://github.com/roshan4182/language-mastery-app#ddd)
## 6.Metrics(https://github.com/roshan4182/language-mastery-app/tree/main#metrics)
## 7.Clean Code Development(https://github.com/roshan4182/language-mastery-app/tree/main#clean-code-development)
## 8.Build Management(https://github.com/roshan4182/language-mastery-app/tree/main#build-management)
## 9.Unit Tests(https://github.com/roshan4182/language-mastery-app/tree/main#unit-tests)
## 10.IDE(https://github.com/roshan4182/language-mastery-app#ide)
## 11.Functional Programming(https://github.com/roshan4182/language-mastery-app#functional-programming)


## Code  ##

TO ACCESS THE MAIN CODE : [Language-Mastery-app](https://github.com/roshan4182/language-mastery-app/blob/main/app/main.py)


## Changes_Made_With_The_Branches:##


[commits](https://github.com/roshan4182/language-mastery-app/commits?author=roshan4182)




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


Build management for the Language Mastery App project has been implemented using Github Actions

Python CI

Build management for the Language Mastery App project has been implemented using [Github Actions](https://github.com/roshan4182/language-mastery-app/actions)

[Python CI](https://github.com/roshan4182/language-mastery-app/actions)



### Unit Tests

The unit tests has been done in 2 parts and is written using the unittest framework in Python.

[Unit Test 1](https://github.com/roshan4182/language-mastery-app/blob/main/tests/test_main.py) [Unit Test 2](https://github.com/roshan4182/language-mastery-app/blob/main/tests/test_word_api.py)



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

![PYTHON](https://github.com/roshan4182/language-mastery-app/assets/149868016/a86a4844-3fbe-41f8-b1b5-684a8858f82a)![VISUAL CODE](https://github.com/roshan4182/language-mastery-app/assets/149868016/ed594f59-c471-4b44-add6-b3086f142de3)
















