import allure
import pytest
from allure_commons.types import Severity


PASSING_CASES = []

for i in range(1, 351):
    # 1-97 -> Authentication / Auth Service
    if i <= 97:
        PASSING_CASES.append({
            "title": f"Passed API auth flow case {i:03}",
            "description": "Validates positive authentication flow. Expected result: user session is created successfully.",
            "epic": "Identity",
            "feature": "Authentication",
            "story": "Validate sign-in flow",
            "suite": "Auth Service",
            "severity": Severity.NORMAL,
            "layer": "api",
            "tags": ["demo", "synthetic", "api", "smoke", "auth"],
            "step_1": "Prepare valid authentication payload",
            "step_2": "Validate successful sign-in response",
        })

    # 98-120 -> Authentication / Session Service
    elif i <= 120:
        PASSING_CASES.append({
            "title": f"Passed API session flow case {i:03}",
            "description": "Validates positive session management flow. Expected result: session data is refreshed successfully.",
            "epic": "Identity",
            "feature": "Authentication",
            "story": "Validate session lifecycle",
            "suite": "Session Service",
            "severity": Severity.NORMAL,
            "layer": "api",
            "tags": ["demo", "synthetic", "api", "regression", "auth"],
            "step_1": "Prepare valid session refresh payload",
            "step_2": "Validate successful session refresh response",
        })

    # 121-208 -> Orders / Order Service
    elif i <= 208:
        PASSING_CASES.append({
            "title": f"Passed API order flow case {i:03}",
            "description": "Validates positive order creation flow. Expected result: order is created successfully.",
            "epic": "Commerce",
            "feature": "Orders",
            "story": "Create valid order",
            "suite": "Order Service",
            "severity": Severity.NORMAL,
            "layer": "api",
            "tags": ["demo", "synthetic", "api", "regression", "orders"],
            "step_1": "Send valid create-order request",
            "step_2": "Validate successful order creation response",
        })

    # 209-240 -> Orders / Checkout Flow
    elif i <= 240:
        PASSING_CASES.append({
            "title": f"Passed checkout preparation flow case {i:03}",
            "description": "Validates order preparation before checkout. Expected result: checkout-ready order is created successfully.",
            "epic": "Commerce",
            "feature": "Orders",
            "story": "Prepare order for checkout",
            "suite": "Checkout Flow",
            "severity": Severity.NORMAL,
            "layer": "api",
            "tags": ["demo", "synthetic", "api", "regression", "orders"],
            "step_1": "Prepare checkout-ready order payload",
            "step_2": "Validate successful checkout preparation response",
        })

    # 241-242 -> Cart / Cart Page
    elif i <= 242:
        PASSING_CASES.append({
            "title": f"Passed cart page validation case {i:03}",
            "description": "Validates positive cart page flow. Expected result: cart page is displayed with checkout entry point available.",
            "epic": "Storefront",
            "feature": "Cart",
            "story": "View cart summary",
            "suite": "Cart Page",
            "severity": Severity.MINOR,
            "layer": "e2e",
            "tags": ["demo", "synthetic", "e2e", "smoke", "cart"],
            "step_1": "Open cart page with available items",
            "step_2": "Validate cart summary is visible",
        })

    # 243-350 -> Catalog / Catalog Page
    else:
        PASSING_CASES.append({
            "title": f"Passed E2E storefront case {i:03}",
            "description": "Validates storefront browsing flow. Expected result: product catalog is displayed successfully.",
            "epic": "Storefront",
            "feature": "Catalog",
            "story": "Browse product catalog",
            "suite": "Catalog Page",
            "severity": Severity.MINOR,
            "layer": "e2e",
            "tags": ["demo", "synthetic", "e2e", "smoke", "catalog"],
            "step_1": "Open storefront catalog page",
            "step_2": "Validate product catalog is visible",
        })


@pytest.mark.parametrize("case_data", PASSING_CASES, ids=[c["title"] for c in PASSING_CASES])
def test_generated_passes(case_data):
    allure.dynamic.title(case_data["title"])
    allure.dynamic.description(case_data["description"])
    allure.dynamic.epic(case_data["epic"])
    allure.dynamic.feature(case_data["feature"])
    allure.dynamic.story(case_data["story"])
    allure.dynamic.suite(case_data["suite"])
    allure.dynamic.severity(case_data["severity"])
    allure.dynamic.label("layer", case_data["layer"])
    for tag in case_data["tags"]:
        allure.dynamic.tag(tag)

    with allure.step(case_data["step_1"]):
        pass

    with allure.step(case_data["step_2"]):
        pass

    assert True