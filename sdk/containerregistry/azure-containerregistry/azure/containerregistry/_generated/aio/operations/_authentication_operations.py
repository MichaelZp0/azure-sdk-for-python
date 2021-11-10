# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.6.6, generator: @autorest/python@5.11.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._authentication_operations import build_exchange_aad_access_token_for_acr_refresh_token_request, build_exchange_acr_refresh_token_for_acr_access_token_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AuthenticationOperations:
    """AuthenticationOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~container_registry.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def exchange_aad_access_token_for_acr_refresh_token(
        self,
        service: str,
        access_token: str,
        **kwargs: Any
    ) -> "_models.AcrRefreshToken":
        """Exchange AAD tokens for an ACR refresh Token.

        :param service: Indicates the name of your Azure container registry.
        :type service: str
        :param access_token: AAD access token, mandatory when grant_type is access_token_refresh_token
         or access_token.
        :type access_token: str
        :keyword grant_type: Can take a value of access_token. The default value is "access_token".
         Note that overriding this default value may result in unsupported behavior.
        :paramtype grant_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AcrRefreshToken, or the result of cls(response)
        :rtype: ~container_registry.models.AcrRefreshToken
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AcrRefreshToken"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/x-www-form-urlencoded")  # type: Optional[str]
        grant_type = kwargs.pop('grant_type', "access_token")  # type: str

        # Construct form data
        data = {
            "grant_type": grant_type,
            "service": service,
            "access_token": access_token,
        }

        request = build_exchange_aad_access_token_for_acr_refresh_token_request(
            content_type=content_type,
            data=data,
            template_url=self.exchange_aad_access_token_for_acr_refresh_token.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "url": self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AcrRefreshToken', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    exchange_aad_access_token_for_acr_refresh_token.metadata = {'url': '/oauth2/exchange'}  # type: ignore


    @distributed_trace_async
    async def exchange_acr_refresh_token_for_acr_access_token(
        self,
        service: str,
        scope: str,
        refresh_token: str,
        grant_type: Union[str, "_models.TokenGrantType"] = "refresh_token",
        **kwargs: Any
    ) -> "_models.AcrAccessToken":
        """Exchange ACR Refresh token for an ACR Access Token.

        :param service: Indicates the name of your Azure container registry.
        :type service: str
        :param scope: Which is expected to be a valid scope, and can be specified more than once for
         multiple scope requests. You obtained this from the Www-Authenticate response header from the
         challenge.
        :type scope: str
        :param refresh_token: Must be a valid ACR refresh token.
        :type refresh_token: str
        :param grant_type: Grant type is expected to be refresh_token.
        :type grant_type: str or ~container_registry.models.TokenGrantType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AcrAccessToken, or the result of cls(response)
        :rtype: ~container_registry.models.AcrAccessToken
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AcrAccessToken"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/x-www-form-urlencoded")  # type: Optional[str]

        # Construct form data
        data = {
            "service": service,
            "scope": scope,
            "refresh_token": refresh_token,
            "grant_type": grant_type,
        }

        request = build_exchange_acr_refresh_token_for_acr_access_token_request(
            content_type=content_type,
            data=data,
            template_url=self.exchange_acr_refresh_token_for_acr_access_token.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "url": self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AcrAccessToken', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    exchange_acr_refresh_token_for_acr_access_token.metadata = {'url': '/oauth2/token'}  # type: ignore

