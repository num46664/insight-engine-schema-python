import uuid

from fhir.resources.claim import Claim
from fhir.resources import backboneelement, domainresource
from enum import Enum, unique


class InsightEngineResponse(domainresource.DomainResource):
    """Insight Engine response.

    Response contains the insights.
    """

    resource_type = "InsightEngineResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.insights = []
        self.referenceQueries = []

        super(InsightEngineResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(InsightEngineResponse, self).elementProperties()
        js.extend(
            [
                ("insights", "insights", Insight, "Insight", True, None, False),
                ("referenceQueries", "referenceQueries", ReferenceQueryMetadata, "ReferenceQueryMetadata", True, None, False),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = InsightEngineResponse()

        arrayInsights = dict.get('insights', [])
        for elemInsights in arrayInsights:
            obj.insights.append(
                Insight.dictToObject(elemInsights))
        
        arrayQueries = dict.get('referenceQueries', [])
        for query in arrayQueries:
            obj.referenceQueries.append(ReferenceQueryMetadata.dictToObject(query))
            
        return obj


class Insight(domainresource.DomainResource):
    """Insight is the result of running an insight engine on a claim.


    """

    resource_type = "Insight"

    def __init__(self, jsondict=None, strict=True):
        """Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.id = None
        self.type = "Error" # InsightType.Error
        self.description = None
        self.defense = None
        self.action = None
        super(Insight, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Insight, self).elementProperties()
        # ("name", "json_name", type, type_name, is_list, "of_many", not_optional)
        js.extend(
            [
                ("id",          "id",          str,         "string",  False, None, False,),
                ("type",        "type",        str,         "string",  False, None, False,),
                ("description", "description", str,         "string",  False, None, False,),
                ("defense",     "defense",     Defense,     "Defense", False, None, False,),
                ("action",      "action",      Action,      "Action",  False, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = Insight()
        obj.id          = dict.get('id', None)
        obj.type        = dict.get('type', None)
        obj.description = dict.get('description', None)
        obj.defense     = Defense.dictToObject(dict.get('defense', None))
        obj.action      = Action .dictToObject(dict.get('action', None))
        return obj

@unique
class InsightType(str, Enum):
	NotApplicable       = "Not Applicable"
	ClaimLineValid      = "Claim Line Valid"
	ClaimNotPayable     = "Claim Not Payable"
	ClaimLineNotPayable = "Claim Line Not Payable"
	RecodeClaimLine     = "Recode Claim Line"
	AdjustPayment       = "Adjust Payment"
	ManualReview        = "Manual Review"
	Error               = "Error"

class Defense(domainresource.DomainResource):
    """Defense provides some backing support information for the proposed change.
    """

    resource_type = "Defense"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.script = None
        self.referenceData = []
        super(Defense, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Defense, self).elementProperties()
        js.extend(
            [
                ("script",        "script",        MessageBundle, "MessageBundle", False, None, False,),
                ("referenceData", "referenceData", str,           "string",        True,  None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = Defense()

        obj.script = MessageBundle.dictToObject(dict.get('script', None))

        arrayReferenceData = dict.get('referenceData', [])
        for elemReferenceData in arrayReferenceData:
            obj.referenceData.append(elemReferenceData)
        return obj


class Action(domainresource.DomainResource):
    """Action describes the actual change in the claim (if any).
    """

    resource_type = "Action"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.removeObject = False
        self.updatedObject = None
        super(Action, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Action, self).elementProperties()
        js.extend(
            [
                ("removeObject",  "removeObject",  bool,  "boolean", False, None, False,),
                ("updatedObject", "updatedObject", Claim, "Claim",   False, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = Action()

        obj.removeObject = dict.get('removeObject', None)

        obj.updatedObject = Claim(jsondict=dict.get('updatedObject', None))
        return obj


class MessageBundle(domainresource.DomainResource):
    """MessageBundle .
    """

    resource_type = "MessageBundle"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.uuid = None

        self.messages = []

        super(MessageBundle, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageBundle, self).elementProperties()
        js.extend(
            [
                ("uuid", "uuid", uuid.UUID, "UUID", False, None, False,),
                ("messages", "messages", TranslatedMessage, "TranslatedMessage", True, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = MessageBundle()

        obj.uuid = dict.get('uuid', None)

        arrayMessages = dict.get('messages', [])
        for elemMessages in arrayMessages:
            obj.messages.append(
                TranslatedMessage.dictToObject(elemMessages))
        return obj


class TranslatedMessage(domainresource.DomainResource):
    """TranslatedMessage.
    """

    resource_type = "TranslatedMessage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.lang = None
        self.message = None
        super(TranslatedMessage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TranslatedMessage, self).elementProperties()
        js.extend(
            [
                ("lang",    "lang",    str, "string", False, None, False,),
                ("message", "message", str, "string", False, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = TranslatedMessage()
        obj.lang = dict.get('lang', None)
        obj.message = dict.get('message', None)
        return obj


class InsightRecord(domainresource.DomainResource):
    """InsightRecord is the result + metadata of an insight engine.
    """

    resource_type = "InsightRecord"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.clientId = None
        self.transactionId = None
        self.insightsRecordId = None
        self.insightEngineId = None
        self.createdAt = None
        self.context = None
        self.insights = []
        self.referenceQueries = None
        self.ttl = None
        super(InsightRecord, self).__init__(jsondict=jsondict, strict=strict)

        '''
         """ Returns a list of tuples, one tuple for each property that should
        be serialized, as: ("name", "json_name", type, type_name, is_list, "of_many", not_optional)
        """
        '''

    def elementProperties(self):
        js = super(InsightRecord, self).elementProperties()
        js.extend(
            [
                ("clientId", "clientId", str, "string", False, None, False,),
                ("transactionId", "transactionId", str, "string", False, None, False,),
                ("insightsRecordId", "insightsRecordId", str, "string", False, None, False,),
                ("insightEngineId", "insightEngineId", str, "string", False, None, False,),
                ("createdAt", "createdAt", str, "string", False, None, False,),
                ("context", "context", str, "string", False, None, False,),
                ("insights", "insights", Insight, "Insight", True, None, False,),
                ("referenceQueries", "referenceQueries", ReferenceQueryMetadata, "ReferenceQueryMetadata", True, None,
                 False),
                ("ttl", "ttl", int, "positiveInt", False, None, False)
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = InsightRecord()
        obj.clientId = dict.get("clientId", None)
        obj.transactionId = dict.get("transactionId", None)
        obj.insightsRecordId = dict.get("insightsRecordId", None)
        obj.insightEngineId = dict.get("insightEngineId", None)
        obj.createdAt = dict.get("createdAt", None)
        obj.context = dict.get("context", None)

        arrayInsight = dict.get('insights', [])
        for elemInsight in arrayInsight:
            obj.insights.append(
                Insight.dictToObject(elemInsight))

        arrayReferenceQueries = dict.get("referenceQueries", [])
        for elemReferenceQuery in arrayReferenceQueries:
            obj.referenceQueries.append(
                ReferenceQueryMetadata.dictToObject(elemReferenceQuery)
            )

        obj.ttl = dict.get("ttl", None)
        return obj


class ReferenceQueryMetadata(domainresource.DomainResource):
    """ReferenceQueryMetadata"""

    resource_type = "ReferenceQueryMetadata"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.referenceDataMetaQuery = None
        self.queryTimeInMilliseconds = None
        self.queriedBytes = None
        self.returnedBytes = None
        self.timestamp = None
        super(ReferenceQueryMetadata, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ReferenceQueryMetadata, self).elementProperties()
        js.extend(
            [
                ("queryTimeInMilliseconds", "queryTimeInMilliseconds", int, "positiveInt", False, None, False,),
                ("queriedBytes",            "queriedBytes",            int, "positiveInt", False, None, False,),
                ("returnedBytes",           "returnedBytes",           int, "positiveInt", False, None, False,),
                ("timestamp",               "timestamp",               int, "positiveInt", False, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = ReferenceQueryMetadata()
        obj.referenceDataMetaQuery = dict.get("referenceDataMetaQuery", None)
        obj.queryTimeInMilliseconds = dict.get("queryTimeInMilliseconds", None)
        obj.queriedBytes = dict.get("queriedBytes", None)
        obj.returnedBytes = dict.get("returnedBytes", None)
        obj.timestamp = dict.get("timestamp", None)
        return obj


class ReferenceDataMetaQuery(domainresource.DomainResource):
    """ReferenceDataMetaQuery"""

    resource_type = "ReferenceDataMetaQuery"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.name   = None
        self.source = None
        self.query  = None
        super(ReferenceDataMetaQuery, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ReferenceDataMetaQuery, self).elementProperties()
        js.extend(
            [
                ("name", "name", str, "string", False, None, False,),
                ("source", "source", ReferenceDataSource, "ReferenceDataSource", False, None, False,),
                ("query", "query", str, "string", False, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = ReferenceDataMetaQuery()
        obj.name   = dict.get("name", None)
        obj.source = dict.get("source", None)
        obj.query  = dict.get("query", None)

        return obj


class ReferenceDataSource(domainresource.DomainResource):
    """ReferenceDataSource"""

    resource_type = "ReferenceDataSource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.owner = None
        self.repository = None
        self.released = None
        self.ref = None
        super(ReferenceDataSource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ReferenceDataSource, self).elementProperties()
        js.extend(
            [
                ("owner", "owner", str, "string", False, None, False,),
                ("repository", "repository", str, "string", False, None, False,),
                ("released", "released", bool, "bool", False, None, False,),
                ("ref", "ref", str, "string", False, None, False),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = ReferenceDataSource()
        obj.owner = dict.get("owner", None)
        obj.repository = dict.get("repository", None)
        obj.released = dict.get("released", None)

        return obj

    def objectKey(self):
        refPrefix = "refs/heads"
        if self.released:
            refPrefix = "refs/tags"
        return self.owner + "/" + self.repository + "/" + refPrefix + "/" + self.ref


class InsightEngineConfig(domainresource.DomainResource):
    """InsightEngineConfig"""

    resource_type = "InsightEngineConfig"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties. """

        self.description = None
        self.language = None
        self.daysOfHistory = 0
        self.authorId = None
        self.queries = []
        self.tags = {}

        super(InsightEngineConfig, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(InsightEngineConfig, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False,),
                ("language", "language", str, "string", False, None, False,),
                ("daysOfHistory", "daysOfHistory", int, "positiveInt", False, None, False,),
                ("authorId", "authorId", str, "string", False, None, False,),
                ("queries", "queries", ReferenceDataMetaQuery, "ReferenceDataMetaQuery", True, None, False),
                ("tags", "tags", str, "string", True, None, False,),
            ]
        )
        return js

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = InsightEngineConfig()
        obj.description = dict.get("description", None)
        obj.language = dict.get("language", None)
        obj.daysOfHistory = dict.get("daysOfHistory", 0)
        arrayQuery = dict.get("queries", [])
        for query in arrayQuery:
            obj.queries.append(ReferenceDataMetaQuery.dictToObject(query))
        obj.tags = dict.get("tags", {})

        return obj
