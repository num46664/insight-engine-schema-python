from fhir.resources.claim import Claim
from fhir.resources import backboneelement, domainresource
from schema.insight_engine_response import InsightEngineConfig


class InsightEngineRequest(domainresource.DomainResource):
    """ Insight Engine request.

    Request contains the original claim, history of the patient and 
    additional reference data that is required by the insight engine.
    """

    resource_type = "InsightEngineRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.claim = None

        self.transactionId = None
        super(InsightEngineRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(InsightEngineRequest, self).elementProperties()
        js.extend(
            [
                (
                    "claim",
                    "claim",
                    Claim,
                    "Claim",
                    False,
                    None,
                    False,
                ),
                ("transactionId", "transactionId", str, "string", False, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = InsightEngineRequest()

        obj.claim = Claim(jsondict=dict.get('claim', None))
        obj.transactionId = dict.get('transactionId', None)

        return obj


class InsightEngineRequestReferenceData(backboneelement.BackboneElement):
    """InsightEngineRequest reference data

    Reference data that is requested by the engine and might be used during 
    request processing.
    """

    resource_type = "InsightEngineRequestReferenceData"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        super(InsightEngineRequestReferenceData, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(InsightEngineRequestReferenceData, self).elementProperties()
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = InsightEngineRequestReferenceData()
        return obj


class HistoryClaim(backboneelement.BackboneElement):
    """HistoryClaim

    This is the claim that has been processed previously and are stored in history.
    """

    resource_type = "HistoryClaim"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.clientId = None

        self.transactionId = None

        self.memberId = None

        self.createdAt = None

        self.claim = None

        self.context = None

        super(HistoryClaim, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HistoryClaim, self).elementProperties()
        js.extend(
            [
                (
                    "clientId",
                    "clientId",
                    str,
                    "string",
                    False,
                    None,
                    True,
                ),
                (
                    "transactionId",
                    "transactionId",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "memberId",
                    "memberId",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "createdAt",
                    "createdAt",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "claim",
                    "claim",
                    Claim,
                    "Claim",
                    False,
                    None,
                    False,
                ),
                (
                    "context",
                    "context",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = HistoryClaim()

        obj.clientId = dict.get('clientId', None)

        obj.transactionId = dict.get('transactionId', None)

        obj.memberId = dict.get('memberId', None)

        obj.createdAt = dict.get('createdAt', None)

        obj.claim = Claim(jsondict=dict.get('claim', None))

        obj.context = dict.get('context', None)

        return obj


class QueryStreamResponse(backboneelement.BackboneElement):
    """QueryStreamResponse"""

    resource_type = "QueryStreamResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties. """

        self.results = None

        self.returned_bytes = None

        self.processed_bytes = None

        super(QueryStreamResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QueryStreamResponse, self).elementProperties()
        js.extend(
            [
                ("results", "results", list, "list", False, None, False,),
                ("returned_bytes", "returned_bytes", int, "positiveInt", False, None, False,),
                ("processed_bytes", "processed_bytes", int, "positiveInt", False, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = QueryStreamResponse()

        obj.results = dict.get("results", None)

        obj.returned_bytes = dict.get("returned_bytes", None)

        obj.processed_bytes = dict.get("processed_bytes", None)

        return obj

class ReferenceDataEvent(backboneelement.BackboneElement):
    """ReferenceDataEvent"""

    resource_type = "ReferenceDataEvent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties. """

        self.claim = None

        self.insightConfig = None


        super(ReferenceDataEvent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ReferenceDataEvent, self).elementProperties()
        js.extend(
            [
                ("claim", "claim", Claim, "Claim", False, None, False,),
                ("insightConfig", "insightConfig", InsightEngineConfig, "InsightEngineConfig", False, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = ReferenceDataEvent()

        obj.claim = Claim(jsondict=dict.get('claim', None))

        obj.insightConfig = InsightEngineConfig.dictToObject(dict.get("insightConfig", None))

        return obj
