from Screens import LoginPage
from Screens import CreateNewApplication
from Screens import PrimaryInsured
from Screens import ProductSelection
from Screens import Owner
from Screens import Payor
from Screens import Beneficiary
from Screens import ExistingInsurance
from Screens import PaymentInformation
from Screens import PhysicianInformation
from Screens import UnderwritingQuestions
from Screens import SupplementalForms
from Screens import CompleteApplication


def navigate_screens(screen_name):
    if screen_name == 'LoginPage':
        LoginPage.Execute()
    if screen_name == 'CreateNewApplication':
        CreateNewApplication.Execute()
    if screen_name == 'PrimaryInsured':
        PrimaryInsured.Execute()
    if screen_name == 'ProductSelection':
        ProductSelection.Execute()
    if screen_name == 'Owner':
        Owner.Execute()
    if screen_name == 'Payor':
        Payor.Execute()
    if screen_name == 'Beneficiary':
        Beneficiary.Execute()
    if screen_name == 'ExistingInsurance':
        ExistingInsurance.Execute()
    if screen_name == 'PaymentInformation':
        PaymentInformation.Execute()
    if screen_name == 'PhysicianInformation':
        PhysicianInformation.Execute()
    if screen_name == 'UnderwritingQuestions':
        UnderwritingQuestions.Execute()
    if screen_name == 'SupplementalForms':
        SupplementalForms.Execute()
    if screen_name == 'CompleteApplication':
        CompleteApplication.Execute()


