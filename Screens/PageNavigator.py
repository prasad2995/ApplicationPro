import Screens.LoginPage as LoginPage
import Screens.CreateNewApplication as CreateNewApplication
import Screens.PrimaryInsured as PrimaryInsured

def navigate_screens(screen_name):
    if screen_name == 'LoginPage':
        LoginPage.Execute()
    if screen_name == 'CreateNewApplication':
        CreateNewApplication.Execute()
    if screen_name == 'PrimaryInsured':
        PrimaryInsured.Execute()
    if screen_name == 'ProductSelection':
        ProductSelection.Execute()

