"""# Invoking start script/function for user to begin the proccess of using the application.  
"""
#import view.login as login
from view import login_view as login

if __name__ == "__main__":
    login.login_main()