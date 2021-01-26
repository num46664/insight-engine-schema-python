import json

from typing import cast, List
from fhir.resources.claim import Claim
from fhir.resources.claim import ClaimItem
from fhir.resources.address import Address
from fhir.resources.organization import Organization
from schema.insight_engine_response import InsightEngineResponse, Insight, InsightType

def test_Address():
    myAddr = Address()
    myAddr.city = 'City'
    assert myAddr.city == "City"


def test_claim1():
    with open("schema/claim1.json") as claim1file:
        claim1json = json.load(claim1file)
        claim1 = Claim(claim1json, strict=False)
        assert claim1.id == "claim1234"
        assert claim1.type.id == "something"
        items = cast(List[ClaimItem], claim1.item)
        item = items[0]
        coding = item.productOrService.coding[0]
        assert coding.code == "0028U"


def test_json_str():
    json_dict = {"resourceType": "Organization",
                 "id": "mmanu",
                 "active": True,
                 "name": "Acme Corporation",
                 "address": [{"country": "Swizterland"}]
                 }
    org = Organization(json_dict)
    assert isinstance(org.address[0], Address)
    assert org.address[0].country == "Swizterland"
    assert org.as_json()['active'] is True


def test_response():
    json_dict = {
        "id": "10",
        "insights": [
            {
                "id": "1"
            }
        ]
    }
    response = InsightEngineResponse(json_dict)
    assert len(response.insights) == 1

def test_file_deserialization():
    with open('schema/InsightEngineResponse.json', 'r') as file:
        response_json = json.load(file)
        print(response_json)
        response = InsightEngineResponse(response_json, strict = False)
        insight: Insight = response.insights[0]
        assert insight.description == "No"
        assert insight.type == InsightType.NotApplicable
