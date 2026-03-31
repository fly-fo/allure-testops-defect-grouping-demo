import allure
from allure_commons.types import Severity


def break_with_message(message: str, case_number: int):
    raise RuntimeError(f"{message} | case={case_number}")


@allure.title("BG1 - Profile sync timeout - case 01")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_01():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 1)


@allure.title("BG1 - Profile sync timeout - case 02")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_02():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 2)


@allure.title("BG1 - Profile sync timeout - case 03")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_03():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 3)


@allure.title("BG1 - Profile sync timeout - case 04")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_04():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 4)


@allure.title("BG1 - Profile sync timeout - case 05")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_05():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 5)


@allure.title("BG1 - Profile sync timeout - case 06")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_06():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 6)


@allure.title("BG1 - Profile sync timeout - case 07")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_07():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 7)


@allure.title("BG1 - Profile sync timeout - case 08")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_08():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 8)


@allure.title("BG1 - Profile sync timeout - case 09")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_09():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 9)


@allure.title("BG1 - Profile sync timeout - case 10")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
def test_bg1_profile_sync_timeout_case_10():
    break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", 10)