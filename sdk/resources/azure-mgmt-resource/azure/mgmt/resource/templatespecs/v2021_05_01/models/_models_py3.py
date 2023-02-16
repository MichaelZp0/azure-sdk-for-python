# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
import sys
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class AzureResourceBase(_serialization.Model):
    """Common properties for all Azure resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.SystemData
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.resource.templatespecs.v2021_05_01.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.resource.templatespecs.v2021_05_01.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorResponse]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class LinkedTemplateArtifact(_serialization.Model):
    """Represents a Template Spec artifact containing an embedded Azure Resource Manager template for
    use as a linked template.

    All required parameters must be populated in order to send to Azure.

    :ivar path: A filesystem safe relative path of the artifact. Required.
    :vartype path: str
    :ivar template: The Azure Resource Manager template. Required.
    :vartype template: JSON
    """

    _validation = {
        "path": {"required": True},
        "template": {"required": True},
    }

    _attribute_map = {
        "path": {"key": "path", "type": "str"},
        "template": {"key": "template", "type": "object"},
    }

    def __init__(self, *, path: str, template: JSON, **kwargs: Any) -> None:
        """
        :keyword path: A filesystem safe relative path of the artifact. Required.
        :paramtype path: str
        :keyword template: The Azure Resource Manager template. Required.
        :paramtype template: JSON
        """
        super().__init__(**kwargs)
        self.path = path
        self.template = template


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or
     ~azure.mgmt.resource.templatespecs.v2021_05_01.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or
     ~azure.mgmt.resource.templatespecs.v2021_05_01.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at


class TemplateSpec(AzureResourceBase):
    """Template Spec object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.SystemData
    :ivar location: The location of the Template Spec. It cannot be changed after Template Spec
     creation. It must be one of the supported Azure locations. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar description: Template Spec description.
    :vartype description: str
    :ivar display_name: Template Spec display name.
    :vartype display_name: str
    :ivar metadata: The Template Spec metadata. Metadata is an open-ended object and is typically a
     collection of key-value pairs.
    :vartype metadata: JSON
    :ivar versions: High-level information about the versions within this Template Spec. The keys
     are the version names. Only populated if the $expand query parameter is set to 'versions'.
    :vartype versions: dict[str,
     ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersionInfo]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "description": {"max_length": 4096},
        "display_name": {"max_length": 64},
        "versions": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "description": {"key": "properties.description", "type": "str"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "metadata": {"key": "properties.metadata", "type": "object"},
        "versions": {"key": "properties.versions", "type": "{TemplateSpecVersionInfo}"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        metadata: Optional[JSON] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: The location of the Template Spec. It cannot be changed after Template Spec
         creation. It must be one of the supported Azure locations. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword description: Template Spec description.
        :paramtype description: str
        :keyword display_name: Template Spec display name.
        :paramtype display_name: str
        :keyword metadata: The Template Spec metadata. Metadata is an open-ended object and is
         typically a collection of key-value pairs.
        :paramtype metadata: JSON
        """
        super().__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.description = description
        self.display_name = display_name
        self.metadata = metadata
        self.versions = None


class TemplateSpecsError(_serialization.Model):
    """Template Specs error response.

    :ivar error: Common error response for all Azure Resource Manager APIs to return error details
     for failed operations. (This also follows the OData error response format.).
    :vartype error: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.ErrorResponse
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorResponse"},
    }

    def __init__(self, *, error: Optional["_models.ErrorResponse"] = None, **kwargs: Any) -> None:
        """
        :keyword error: Common error response for all Azure Resource Manager APIs to return error
         details for failed operations. (This also follows the OData error response format.).
        :paramtype error: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.ErrorResponse
        """
        super().__init__(**kwargs)
        self.error = error


class TemplateSpecsListResult(_serialization.Model):
    """List of Template Specs.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: An array of Template Specs.
    :vartype value: list[~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpec]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[TemplateSpec]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.TemplateSpec"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: An array of Template Specs.
        :paramtype value: list[~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpec]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None


class TemplateSpecUpdateModel(AzureResourceBase):
    """Template Spec properties to be updated (only tags are currently supported).

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.tags = tags


class TemplateSpecVersion(AzureResourceBase):  # pylint: disable=too-many-instance-attributes
    """Template Spec Version object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.SystemData
    :ivar location: The location of the Template Spec Version. It must match the location of the
     parent Template Spec. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar description: Template Spec version description.
    :vartype description: str
    :ivar linked_templates: An array of linked template artifacts.
    :vartype linked_templates:
     list[~azure.mgmt.resource.templatespecs.v2021_05_01.models.LinkedTemplateArtifact]
    :ivar metadata: The version metadata. Metadata is an open-ended object and is typically a
     collection of key-value pairs.
    :vartype metadata: JSON
    :ivar main_template: The main Azure Resource Manager template content.
    :vartype main_template: JSON
    :ivar ui_form_definition: The Azure Resource Manager template UI definition content.
    :vartype ui_form_definition: JSON
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "description": {"max_length": 4096},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "description": {"key": "properties.description", "type": "str"},
        "linked_templates": {"key": "properties.linkedTemplates", "type": "[LinkedTemplateArtifact]"},
        "metadata": {"key": "properties.metadata", "type": "object"},
        "main_template": {"key": "properties.mainTemplate", "type": "object"},
        "ui_form_definition": {"key": "properties.uiFormDefinition", "type": "object"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        linked_templates: Optional[List["_models.LinkedTemplateArtifact"]] = None,
        metadata: Optional[JSON] = None,
        main_template: Optional[JSON] = None,
        ui_form_definition: Optional[JSON] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: The location of the Template Spec Version. It must match the location of the
         parent Template Spec. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword description: Template Spec version description.
        :paramtype description: str
        :keyword linked_templates: An array of linked template artifacts.
        :paramtype linked_templates:
         list[~azure.mgmt.resource.templatespecs.v2021_05_01.models.LinkedTemplateArtifact]
        :keyword metadata: The version metadata. Metadata is an open-ended object and is typically a
         collection of key-value pairs.
        :paramtype metadata: JSON
        :keyword main_template: The main Azure Resource Manager template content.
        :paramtype main_template: JSON
        :keyword ui_form_definition: The Azure Resource Manager template UI definition content.
        :paramtype ui_form_definition: JSON
        """
        super().__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.description = description
        self.linked_templates = linked_templates
        self.metadata = metadata
        self.main_template = main_template
        self.ui_form_definition = ui_form_definition


class TemplateSpecVersionInfo(_serialization.Model):
    """High-level information about a Template Spec version.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar description: Template Spec version description.
    :vartype description: str
    :ivar time_created: The timestamp of when the version was created.
    :vartype time_created: ~datetime.datetime
    :ivar time_modified: The timestamp of when the version was last modified.
    :vartype time_modified: ~datetime.datetime
    """

    _validation = {
        "description": {"readonly": True},
        "time_created": {"readonly": True},
        "time_modified": {"readonly": True},
    }

    _attribute_map = {
        "description": {"key": "description", "type": "str"},
        "time_created": {"key": "timeCreated", "type": "iso-8601"},
        "time_modified": {"key": "timeModified", "type": "iso-8601"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.description = None
        self.time_created = None
        self.time_modified = None


class TemplateSpecVersionsListResult(_serialization.Model):
    """List of Template Specs versions.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: An array of Template Spec versions.
    :vartype value: list[~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[TemplateSpecVersion]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.TemplateSpecVersion"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: An array of Template Spec versions.
        :paramtype value:
         list[~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None


class TemplateSpecVersionUpdateModel(AzureResourceBase):
    """Template Spec Version properties to be updated (only tags are currently supported).

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.tags = tags
