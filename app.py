"""
Data analysis tool.
An example module. 

Details about this module.

This module is the main app and is the start point for this application.
The main data explorer view is the default View.
It uses controllers for code that run when GUI actions are conducted.

The approach to be taken is to replace the PySimple GUI event loop - the "while" for a Window, with calls to controllers.
Each Controller decides which View to show, each View is linked to Controllers. 
Each controller accepts an input action from the GUI presented or rendered by View.
The controller then decides what to do with the input action and what View to show next.

"""

import sys
sys.dont_write_bytecode = True
from view.data_analyst_view import DES_View
from view.user_login_view import LoginView



if __name__ == "__main__" :
    """
    Code that runs when this is the main module.
    """

    login_view = LoginView()
    login_view.set_up_layout()
    login_view.render()
    login_view.accept_input()

    pass
