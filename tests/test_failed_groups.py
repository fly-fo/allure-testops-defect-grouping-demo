import allure
import pytest
from allure_commons.types import Severity


def fail_with_message(message: str, case_number: int):
    pytest.fail(f"{message} | case={case_number}")


def execute_failed_api_flow(
    *,
    case_number: int,
    error_message: str,
    precondition_text: str,
    request_step: str,
    validation_step: str,
    nested_check_1: str,
    nested_check_2: str,
):
    with allure.step(f"Precondition: {precondition_text}"):
        pass

    with allure.step(request_step):
        pass

    with allure.step(validation_step):
        with allure.step(nested_check_1):
            pass
        with allure.step(nested_check_2):
            fail_with_message(error_message, case_number)


def execute_failed_e2e_flow(
    *,
    case_number: int,
    error_message: str,
    precondition_text: str,
    navigation_step: str,
    action_step: str,
    validation_step: str,
    nested_check_1: str,
    nested_check_2: str,
):
    with allure.step(f"Precondition: {precondition_text}"):
        pass

    with allure.step(navigation_step):
        pass

    with allure.step(action_step):
        pass

    with allure.step(validation_step):
        with allure.step(nested_check_1):
            pass
        with allure.step(nested_check_2):
            fail_with_message(error_message, case_number)


# ============================
# Failed Group 1
# 10 failed results
# ============================

@allure.title("FG1 - Auth token expired - case 01")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_01():
    execute_failed_api_flow(
        case_number=1,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 02")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_02():
    execute_failed_api_flow(
        case_number=2,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 03")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_03():
    execute_failed_api_flow(
        case_number=3,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 04")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_04():
    execute_failed_api_flow(
        case_number=4,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 05")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_05():
    execute_failed_api_flow(
        case_number=5,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 06")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_06():
    execute_failed_api_flow(
        case_number=6,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 07")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_07():
    execute_failed_api_flow(
        case_number=7,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 08")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_08():
    execute_failed_api_flow(
        case_number=8,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 09")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_09():
    execute_failed_api_flow(
        case_number=9,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


@allure.title("FG1 - Auth token expired - case 10")
@allure.description("Validates session refresh flow for an expired token. Expected result: a valid refreshed session is returned.")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "auth")
def test_fg1_auth_token_expired_case_10():
    execute_failed_api_flow(
        case_number=10,
        error_message="AUTH_TOKEN_EXPIRED: token validation failed",
        precondition_text="An expired session token exists for the user",
        request_step="Send refresh-session request to Auth Service",
        validation_step="Validate refreshed session response",
        nested_check_1="Check response status and token presence",
        nested_check_2="Check that token validation succeeds",
    )


# ============================
# Failed Group 2
# 10 failed results
# ============================

@allure.title("FG2 - Payment gateway 502 - case 01")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_01():
    execute_failed_api_flow(
        case_number=1,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 02")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_02():
    execute_failed_api_flow(
        case_number=2,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 03")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_03():
    execute_failed_api_flow(
        case_number=3,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 04")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_04():
    execute_failed_api_flow(
        case_number=4,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 05")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_05():
    execute_failed_api_flow(
        case_number=5,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 06")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_06():
    execute_failed_api_flow(
        case_number=6,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 07")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_07():
    execute_failed_api_flow(
        case_number=7,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 08")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_08():
    execute_failed_api_flow(
        case_number=8,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 09")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_09():
    execute_failed_api_flow(
        case_number=9,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


@allure.title("FG2 - Payment gateway 502 - case 10")
@allure.description("Validates payment processing through the external payment gateway. Expected result: upstream gateway returns a successful payment response.")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "payments")
def test_fg2_payment_gateway_502_case_10():
    execute_failed_api_flow(
        case_number=10,
        error_message="PAYMENT_GATEWAY_502: upstream returned 502",
        precondition_text="A valid order and payment payload are prepared",
        request_step="Send payment request to Payment Service",
        validation_step="Validate gateway response",
        nested_check_1="Check gateway HTTP status",
        nested_check_2="Check upstream response is successful",
    )


# ============================
# Failed Group 3
# 10 failed results
# ============================

@allure.title("FG3 - Order schema mismatch - case 01")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_01():
    execute_failed_api_flow(
        case_number=1,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 02")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_02():
    execute_failed_api_flow(
        case_number=2,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 03")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_03():
    execute_failed_api_flow(
        case_number=3,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 04")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_04():
    execute_failed_api_flow(
        case_number=4,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 05")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_05():
    execute_failed_api_flow(
        case_number=5,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 06")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_06():
    execute_failed_api_flow(
        case_number=6,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 07")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_07():
    execute_failed_api_flow(
        case_number=7,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 08")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_08():
    execute_failed_api_flow(
        case_number=8,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 09")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_09():
    execute_failed_api_flow(
        case_number=9,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


@allure.title("FG3 - Order schema mismatch - case 10")
@allure.description("Validates order creation payload. Expected result: numeric fields are returned with the expected data types.")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
@allure.tag("demo", "synthetic", "regression", "api", "orders")
def test_fg3_order_schema_mismatch_case_10():
    execute_failed_api_flow(
        case_number=10,
        error_message="ORDER_SCHEMA_MISMATCH: expected number but got string",
        precondition_text="A valid order payload is available for submission",
        request_step="Send create-order request to Order Service",
        validation_step="Validate response schema",
        nested_check_1="Check required fields are present",
        nested_check_2="Check total amount field has numeric type",
    )


# ============================
# Failed Group 4
# 10 failed results
# ============================

@allure.title("FG4 - UI cart button hidden - case 01")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_01():
    execute_failed_e2e_flow(
        case_number=1,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 02")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_02():
    execute_failed_e2e_flow(
        case_number=2,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 03")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_03():
    execute_failed_e2e_flow(
        case_number=3,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 04")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_04():
    execute_failed_e2e_flow(
        case_number=4,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 05")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_05():
    execute_failed_e2e_flow(
        case_number=5,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 06")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_06():
    execute_failed_e2e_flow(
        case_number=6,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 07")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_07():
    execute_failed_e2e_flow(
        case_number=7,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 08")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_08():
    execute_failed_e2e_flow(
        case_number=8,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 09")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_09():
    execute_failed_e2e_flow(
        case_number=9,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )


@allure.title("FG4 - UI cart button hidden - case 10")
@allure.description("Validates visibility of the checkout button on the cart page. Expected result: checkout button is visible and actionable.")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
@allure.tag("demo", "synthetic", "regression", "e2e", "ui")
def test_fg4_ui_cart_button_hidden_case_10():
    execute_failed_e2e_flow(
        case_number=10,
        error_message="UI_CART_BUTTON_HIDDEN: checkout button is not visible",
        precondition_text="Cart contains at least one available item",
        navigation_step="Open cart page",
        action_step="Wait for cart summary and checkout section",
        validation_step="Validate checkout entry point",
        nested_check_1="Locate checkout button",
        nested_check_2="Check that checkout button is visible",
    )