import allure
import pytest
from allure_commons.types import Severity


PASSING_CASES = []

for i in range(1, 351):
    if i <= 120:
        PASSING_CASES.append({
            "title": f"Passed API auth flow case {i:03}",
            "epic": "Identity",
            "feature": "Authentication",
            "story": "Validate sign-in flow",
            "suite": "Auth Service",
            "severity": Severity.NORMAL,
            "layer": "api",
        })
    elif i <= 240:
        PASSING_CASES.append({
            "title": f"Passed API order flow case {i:03}",
            "epic": "Commerce",
            "feature": "Orders",
            "story": "Create valid order",
            "suite": "Order Service",
            "severity": Severity.NORMAL,
            "layer": "api",
        })
    else:
        PASSING_CASES.append({
            "title": f"Passed E2E storefront case {i:03}",
            "epic": "Storefront",
            "feature": "Catalog",
            "story": "Browse product catalog",
            "suite": "Catalog Page",
            "severity": Severity.MINOR,
            "layer": "e2e",
        })


@pytest.mark.parametrize("case_data", PASSING_CASES, ids=[c["title"] for c in PASSING_CASES])
def test_generated_passes(case_data):
    allure.dynamic.title(case_data["title"])
    allure.dynamic.epic(case_data["epic"])
    allure.dynamic.feature(case_data["feature"])
    allure.dynamic.story(case_data["story"])
    allure.dynamic.suite(case_data["suite"])
    allure.dynamic.severity(case_data["severity"])
    allure.dynamic.label("layer", case_data["layer"])
    assert True