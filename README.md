# Chatty (a bot that helps you cook anything) 
Welcome to **Chatty**, a chatbot group project for **CITS5505 UWA** aimed at providing recipe suggestions for food enthusiasts. Whether you're looking for new meal ideas, want to explore different cuisines, or simply need inspiration for your next cooking adventure, **Chatty** is here to assist you.

## Project Overview 
**Chatty** is a Python-based chatbot that utilizes natural language processing (NLP) techniques and a food recipe database to offer personalized recipe recommendations. It interacts with users through a user-friendly chat interface, where you can input your details to receive tailored recipe suggestions. 
## Key Features  
 -  **Personalized Recipe Recommendations**: **Chatty** takes into account your preferences to offer customized recipe suggestions. 
 -  **Natural Language Processing (NLP)**: This chatbot employs NLP techniques to understand user queries and provide accurate responses based on the available recipe database.  
 -  **Ingredient Substitutions**: **Chatty** can suggest ingredient substitutions based on your queries


## Getting Started 

 
 
To run **Chatty** locally or contribute to the project, follow the instructions below to set 
 - Clone the repository:

	`git clone https://github.com/cashvini/Chatty.git`

 - Create Virtual Environment(being careful with the versions):

	`python -m venv venv`

 - Activate the Virtual Environment
	**For Windows(PowerShell):**
	
	`.\venv\Scripts\Activate.ps1`

	**For Windows(PowerShell):**
	
	`.\venv\Scripts\activate.bat`

    **For MacOS (or Linux):**
    
	`source venv/bin/activate`

 - Install the required dependencies:

	`pip install -r requirements.txt`

 - Set the Flask app environment variable:

	**For Windows (PowerShell):**
	
	`$env:FLASK_APP=your_app.py`

	**For Windows (Command Prompt):**
	
	`set FLASK_APP=your_app.py`

	**For macOS and Linux:**
	
	`export FLASK_APP=your_app.py`	

 - Run the Flask development server:

	`flask run`

 - By this step, everything will be set & ***Bon Appétit***

## Tools used
### [Flask](https://flask.palletsprojects.com/) Framework
### [Dialog flow](https://help.socialintents.com/article/91-how-to-find-my-dialogflow-key-for-my-chatbot) AI engine
### [sqlite](https://www.sqlite.org/docs.html) SQL database engine
### [sql alchemy](https://www.sqlalchemy.org/) Python SQL Toolkit
### [html5](https://html.com/) Markup language
### [jinja2](https://jinja.palletsprojects.com/en/3.1.x/) Templating engine
### [css3](https://www.w3.org/Style/CSS/Overview.en.html) Style sheets
### [pytest](https://docs.pytest.org/en/7.3.x/) Python testing framework


## Directions of use
	

 - You will be taken to a beautiful UI with a ***cupcake*** as a reference to what this Bot can do.
 - It requires you to sign up just like any friendly website and login.
 - Afterwards you will be taken to an eye-catchy UI where you basically input the recipe that you want and get instant results and directions on how to  move forward with this process.
 - If you do not have the time to cook or bake , your progress will be saved in our **View History** link on the ***navbar*** so that you can go back and check on the recipe and start according the suggestions provided
 - As Simple As That!

## Running Tests
Call this command for unit tests and functionality tests
`python -m pytest -v`

## Contributing

We welcome contributions to improve this project, including the project documentation! If you'd like to contribute to the documentation, please follow these guidelines:

1.  Fork the repository and clone it to your local machine.
    
2.  Make the necessary changes to the documentation files.
    
3.  Test your changes to ensure they are accurate and well-formatted.
    
4.  Commit your changes with a descriptive commit message.
    
5.  Push your changes to your forked repository.
    
6.  Submit a pull request, explaining the changes you made and why they are beneficial.
    

We appreciate your contributions in making the documentation more comprehensive and user-friendly.

## Acknowledgements

 - [Tahmid Ahmed](https://www.youtube.com/watch?v=IXucQAEkIMo) (for ideas about UI)
- [Chat-GPT](https://chat.openai.com/) (for ideas about JavasScript & handling exceptions to identify bugs)
- [Chat-GPT](https://chat.openai.com/) (to learn about Read.me about formats)
- [Chat-GPT](https://chat.openai.com/) (to learn about Read.me about formats)
- [Othneildrew](https://github.com/othneildrew/Best-README-Template) (to learn about formats of Read.me)

## License 
This project is licensed under the [MIT License](LICENSE).




