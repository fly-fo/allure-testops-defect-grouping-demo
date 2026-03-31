import allure
from allure_commons.types import Severity


def break_with_message(message: str, case_number: int):
    raise RuntimeError(f"{message} | case={case_number}")


def execute_broken_flow(case_number: int):
    with allure.step("Precondition: customer profile exists and sync is enabled"):
        pass

    with allure.step("Open profile page and trigger synchronization"):
        pass

    with allure.step("Wait for synchronization completion"):
        with allure.step("Poll synchronization status"):
            pass
        with allure.step("Check timeout threshold and final sync state"):
            break_with_message("PROFILE_SYNC_TIMEOUT: synchronization exceeded timeout", case_number)


@allure.title("BG1 - Profile sync timeout - case 01")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_01():
    execute_broken_flow(1)


@allure.title("BG1 - Profile sync timeout - case 02")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_02():
    execute_broken_flow(2)


@allure.title("BG1 - Profile sync timeout - case 03")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_03():
    execute_broken_flow(3)


@allure.title("BG1 - Profile sync timeout - case 04")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_04():
    execute_broken_flow(4)


@allure.title("BG1 - Profile sync timeout - case 05")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_05():
    execute_broken_flow(5)


@allure.title("BG1 - Profile sync timeout - case 06")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_06():
    execute_broken_flow(6)


@allure.title("BG1 - Profile sync timeout - case 07")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_07():
    execute_broken_flow(7)


@allure.title("BG1 - Profile sync timeout - case 08")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_08():
    execute_broken_flow(8)


@allure.title("BG1 - Profile sync timeout - case 09")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_09():
    execute_broken_flow(9)


@allure.title("BG1 - Profile sync timeout - case 10")
@allure.description("Validates profile synchronization flow. Expected result: synchronization completes within the allowed timeout.")
@allure.epic("Customer Account")
@allure.feature("Profile")
@allure.story("Sync customer profile")
@allure.suite("Profile Page")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "sync")
def test_bg1_profile_sync_timeout_case_10():
    execute_broken_flow(10)