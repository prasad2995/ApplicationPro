import Screens.LoginPage as LoginPage
import Screens.CreateNewApplication as CreateNewApplication
import Screens.PrimaryInsured as PrimaryInsured
import Screens.ProductSelection as ProductSelection
import Screens.Owner as Owner
import Screens.Payor as Payor
import Screens.Beneficiary as Beneficiary
import Screens.ExistingInsurance as ExistingInsurance
import Screens.PaymentInformation as PaymentInformation
import Screens.PhysicianInformation as PhysicianInformation
import Screens.UnderwritingQuestions as UnderwritingQuestions
import Screens.SupplementalForms as SupplementalForms


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


