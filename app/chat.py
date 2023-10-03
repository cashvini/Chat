from app import app

from flask import Flask,escape,render_template,jsonify, request, session
import dialogflow
import os
from google.protobuf.json_format import MessageToDict
from datetime import datetime as dt
from flask_login import current_user
from .model import Chat, User, db
from app import model

dic_chatHistory = {}
chatUsername = ""

#get response for question
def detect_intent_with_parameters(project_id, session_id, query_params, language_code, user_input):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text = user_input
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input, query_params=query_params)
    return response

#trigger on click send chat button
@app.route('/chat', methods=["Post"])
def chat():
    input_text = request.form['message']
    print(input_text)
    GOOGLE_AUTHENTICATION_FILE_NAME = "credentials/chatty-ghsj-3d42f7663a2b.json"
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

    GOOGLE_PROJECT_ID = "chatty-ghsj"
    session_id = "1234567891"
    context_short_name = "does_not_matter"

    context_name = "projects/" + GOOGLE_PROJECT_ID + "/agent/sessions/" + session_id + "/contexts/" + context_short_name.lower()

    parameters = dialogflow.types.struct_pb2.Struct()

    context_1 = dialogflow.types.context_pb2.Context(
        name=context_name,
        lifespan_count=2,
        parameters=parameters
    )
    query_params_1 = {"contexts": [context_1]}

    language_code = 'en'

    response = detect_intent_with_parameters(
        project_id=GOOGLE_PROJECT_ID,
        session_id=session_id,
        query_params=query_params_1,
        language_code=language_code,
        user_input=input_text
    )
    result = MessageToDict(response)
 
    
    if len(result['queryResult']['fulfillmentMessages']) == 2:
        response = {"message": result['queryResult']['fulfillmentText'],
                    "payload": result['queryResult']['fulfillmentMessages'][1]['payload']}
    else:
        response = {"message": result['queryResult']['fulfillmentText'], "payload": None}
    
    
    #save chat data in chat table
    fulfillment_text = result['queryResult']['fulfillmentText']
    
    print(fulfillment_text)
    
    #create new chat object
    new_chat = Chat(  
        question=input_text,
        answer=fulfillment_text,
        timestamp=dt.now(),
        user_id=current_user.get_id()           
    )
    session['question'] = new_chat.question
    session['answer'] = new_chat.answer
    db.session.add(new_chat)  # Adds new chat record to database
    db.session.commit() 
    return jsonify(response) 

#return chat history
@app.route('/chatHistory/', methods=["GET"])
def chatHistory():
# Get the chat history of the user
    chatHistory = Chat.query.filter_by(user_id=current_user.id).order_by(Chat.timestamp.desc()).all()    

#Iterate over the chat history
    for chat in chatHistory:
        timestamp = chat.timestamp
        question = chat.question
        answer = chat.answer
        dic_chatHistory[question]=answer
        #The loop was not being able to run the SECOND time since the render_template prevented it        
    print(current_user.id)
    print(dic_chatHistory)
    print(current_user.name)
    return render_template('chat_history.html',history=dic_chatHistory, chatUsername=current_user.name) #here is where the chat history is loaded
        

    


    
