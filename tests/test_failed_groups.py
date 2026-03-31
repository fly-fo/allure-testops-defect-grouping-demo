import allure
import pytest
from allure_commons.types import Severity


def fail_with_message(message: str, case_number: int):
    pytest.fail(f"{message} | case={case_number}")


# ============================
# Failed Group 1
# 10 failed results
# ============================

@allure.title("FG1 - Auth token expired - case 01")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_01():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 1)


@allure.title("FG1 - Auth token expired - case 02")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_02():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 2)


@allure.title("FG1 - Auth token expired - case 03")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_03():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 3)


@allure.title("FG1 - Auth token expired - case 04")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_04():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 4)


@allure.title("FG1 - Auth token expired - case 05")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_05():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 5)


@allure.title("FG1 - Auth token expired - case 06")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_06():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 6)


@allure.title("FG1 - Auth token expired - case 07")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_07():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 7)


@allure.title("FG1 - Auth token expired - case 08")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_08():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 8)


@allure.title("FG1 - Auth token expired - case 09")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_09():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 9)


@allure.title("FG1 - Auth token expired - case 10")
@allure.epic("Identity")
@allure.feature("Authentication")
@allure.story("Refresh expired session")
@allure.suite("Auth Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg1_auth_token_expired_case_10():
    fail_with_message("AUTH_TOKEN_EXPIRED: token validation failed", 10)


# ============================
# Failed Group 2
# 10 failed results
# ============================

@allure.title("FG2 - Payment gateway 502 - case 01")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_01():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 1)


@allure.title("FG2 - Payment gateway 502 - case 02")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_02():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 2)


@allure.title("FG2 - Payment gateway 502 - case 03")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_03():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 3)


@allure.title("FG2 - Payment gateway 502 - case 04")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_04():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 4)


@allure.title("FG2 - Payment gateway 502 - case 05")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_05():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 5)


@allure.title("FG2 - Payment gateway 502 - case 06")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_06():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 6)


@allure.title("FG2 - Payment gateway 502 - case 07")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_07():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 7)


@allure.title("FG2 - Payment gateway 502 - case 08")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_08():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 8)


@allure.title("FG2 - Payment gateway 502 - case 09")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_09():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 9)


@allure.title("FG2 - Payment gateway 502 - case 10")
@allure.epic("Commerce")
@allure.feature("Payments")
@allure.story("Process card payment")
@allure.suite("Payment Service")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "api")
def test_fg2_payment_gateway_502_case_10():
    fail_with_message("PAYMENT_GATEWAY_502: upstream returned 502", 10)


# ============================
# Failed Group 3
# 10 failed results
# ============================

@allure.title("FG3 - Order schema mismatch - case 01")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_01():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 1)


@allure.title("FG3 - Order schema mismatch - case 02")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_02():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 2)


@allure.title("FG3 - Order schema mismatch - case 03")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_03():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 3)


@allure.title("FG3 - Order schema mismatch - case 04")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_04():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 4)


@allure.title("FG3 - Order schema mismatch - case 05")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_05():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 5)


@allure.title("FG3 - Order schema mismatch - case 06")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_06():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 6)


@allure.title("FG3 - Order schema mismatch - case 07")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_07():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 7)


@allure.title("FG3 - Order schema mismatch - case 08")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_08():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 8)


@allure.title("FG3 - Order schema mismatch - case 09")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_09():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 9)


@allure.title("FG3 - Order schema mismatch - case 10")
@allure.epic("Commerce")
@allure.feature("Orders")
@allure.story("Create new order")
@allure.suite("Order Service")
@allure.severity(Severity.NORMAL)
@allure.label("layer", "api")
def test_fg3_order_schema_mismatch_case_10():
    fail_with_message("ORDER_SCHEMA_MISMATCH: expected number but got string", 10)


# ============================
# Failed Group 4
# 10 failed results
# ============================

@allure.title("FG4 - UI cart button hidden - case 01")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_01():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 1)


@allure.title("FG4 - UI cart button hidden - case 02")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_02():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 2)


@allure.title("FG4 - UI cart button hidden - case 03")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_03():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 3)


@allure.title("FG4 - UI cart button hidden - case 04")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_04():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 4)


@allure.title("FG4 - UI cart button hidden - case 05")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_05():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 5)


@allure.title("FG4 - UI cart button hidden - case 06")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_06():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 6)


@allure.title("FG4 - UI cart button hidden - case 07")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_07():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 7)


@allure.title("FG4 - UI cart button hidden - case 08")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_08():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 8)


@allure.title("FG4 - UI cart button hidden - case 09")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_09():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 9)


@allure.title("FG4 - UI cart button hidden - case 10")
@allure.epic("Storefront")
@allure.feature("Cart")
@allure.story("Proceed to checkout")
@allure.suite("Cart Page")
@allure.severity(Severity.CRITICAL)
@allure.label("layer", "e2e")
def test_fg4_ui_cart_button_hidden_case_10():
    fail_with_message("UI_CART_BUTTON_HIDDEN: checkout button is not visible", 10)