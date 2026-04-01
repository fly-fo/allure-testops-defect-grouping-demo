import allure
import pytest
from allure_commons.types import Severity


PASSING_CASES = []

for i in range(1, 351):
    if i <= 120:
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
            "step_1": "Prepare valid authentication payloads",
            "step_2": "Validate successful sign-in response",
        })
    elif i <= 240:
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