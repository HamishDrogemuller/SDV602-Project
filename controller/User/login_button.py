"""
Login controller
"""
import sys
sys.dont_write_bytecode = True
from view.chat_view import ChatView
import PySimpleGUI as sg
from view.data_analyst_view import DES_View

def accept( event, values,state):
    
    keep_going = True
    if event == "Login":   
        # Just testing
        #print("Got login - just testing")

        # Work with a UserManager object
        from model.user_manager import UserManager
        a_user_manager = UserManager()
        
        #a_user_manager.dropDatabase()

        # get user name and password from the "values" or "state"
        user_name = values['User']
        password = values['Password']
        #print(f"Got User = {user_name} , Password = {password} - just testing")

        login_result = a_user_manager.login(user_name,password)
        #print(f"Got login result: {login_result}")

        # Testing Chat
        if login_result == "Login Success":
            UserManager.current_screen = "Data Explorer"
            des_view = DES_View()
            des_view.set_up_layout()
            des_view.render()
            des_view.accept_input()
        
        
            
        
            


    else:
        keep_going = True

    return keep_going 