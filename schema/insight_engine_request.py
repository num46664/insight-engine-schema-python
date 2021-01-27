# -*- coding: utf-8 -*-
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from fhir.resources import backboneelement, domainresource, fhirtypes

from fhir.resources.claim import Claim


class InsightEngineRequest(domainresource.DomainResource):
    """ Insight Engine request.

    Request contains the original claim, history of the patient and 
    additional reference data that is required by the insight engine.
    """

    resource_type = Field("InsightEngineRequest", const=True)

    claim: Claim = Field(
        None,
        alias="claim",
        title="Claim Under Evaluation (CUE)",
        description=(
            "Claim that this policy should evaluate"
        ),
        # if property is element of this resource.
        element_property=True,
    )
    
    transaction_id: string = Field(
        None,
        alias="transactionId",
        title="Transaction identifier",
        description=(
            "This is part of clients' request. Is needed to correlate the incoming request "
            "and subsequent response"
        ),
        # if property is element of this resource.
        element_property=True,
    )

