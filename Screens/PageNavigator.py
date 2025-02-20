import AppPro.Screens.LoginPage as LoginPage
import AppPro.Screens.CreateNewApplication as CreateNewApplication
import AppPro.Screens.PrimaryInsured as PrimaryInsured

def navigate_screens(screen_name):
    if screen_name == 'LoginPage':
        LoginPage.Execute()
    if screen_name == 'CreateNewApplication':
        CreateNewApplication.Execute()
    if screen_name == 'PrimaryInsured':
        PrimaryInsured.Execute()
