# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ActiveDeploymentCollection
    from ._models_py3 import ApiPortalCustomDomainProperties
    from ._models_py3 import ApiPortalCustomDomainResource
    from ._models_py3 import ApiPortalCustomDomainResourceCollection
    from ._models_py3 import ApiPortalInstance
    from ._models_py3 import ApiPortalProperties
    from ._models_py3 import ApiPortalResource
    from ._models_py3 import ApiPortalResourceCollection
    from ._models_py3 import ApiPortalResourceRequests
    from ._models_py3 import AppResource
    from ._models_py3 import AppResourceCollection
    from ._models_py3 import AppResourceProperties
    from ._models_py3 import ApplicationInsightsAgentVersions
    from ._models_py3 import AvailableOperations
    from ._models_py3 import AvailableRuntimeVersions
    from ._models_py3 import AzureFileVolume
    from ._models_py3 import BindingResource
    from ._models_py3 import BindingResourceCollection
    from ._models_py3 import BindingResourceProperties
    from ._models_py3 import Build
    from ._models_py3 import BuildCollection
    from ._models_py3 import BuildProperties
    from ._models_py3 import BuildResult
    from ._models_py3 import BuildResultCollection
    from ._models_py3 import BuildResultLog
    from ._models_py3 import BuildResultProperties
    from ._models_py3 import BuildResultUserSourceInfo
    from ._models_py3 import BuildService
    from ._models_py3 import BuildServiceAgentPoolProperties
    from ._models_py3 import BuildServiceAgentPoolResource
    from ._models_py3 import BuildServiceAgentPoolResourceCollection
    from ._models_py3 import BuildServiceAgentPoolSizeProperties
    from ._models_py3 import BuildServiceCollection
    from ._models_py3 import BuildServiceProperties
    from ._models_py3 import BuildServicePropertiesResourceRequests
    from ._models_py3 import BuildStageProperties
    from ._models_py3 import BuilderProperties
    from ._models_py3 import BuilderResource
    from ._models_py3 import BuilderResourceCollection
    from ._models_py3 import BuildpackBindingLaunchProperties
    from ._models_py3 import BuildpackBindingProperties
    from ._models_py3 import BuildpackBindingResource
    from ._models_py3 import BuildpackBindingResourceCollection
    from ._models_py3 import BuildpackProperties
    from ._models_py3 import BuildpacksGroupProperties
    from ._models_py3 import CertificateProperties
    from ._models_py3 import CertificateResource
    from ._models_py3 import CertificateResourceCollection
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import ClusterResourceProperties
    from ._models_py3 import ConfigServerGitProperty
    from ._models_py3 import ConfigServerProperties
    from ._models_py3 import ConfigServerResource
    from ._models_py3 import ConfigServerSettings
    from ._models_py3 import ConfigServerSettingsErrorRecord
    from ._models_py3 import ConfigServerSettingsValidateResult
    from ._models_py3 import ConfigurationServiceGitProperty
    from ._models_py3 import ConfigurationServiceGitPropertyValidateResult
    from ._models_py3 import ConfigurationServiceGitRepository
    from ._models_py3 import ConfigurationServiceInstance
    from ._models_py3 import ConfigurationServiceProperties
    from ._models_py3 import ConfigurationServiceResource
    from ._models_py3 import ConfigurationServiceResourceCollection
    from ._models_py3 import ConfigurationServiceResourceRequests
    from ._models_py3 import ConfigurationServiceSettings
    from ._models_py3 import ConfigurationServiceSettingsValidateResult
    from ._models_py3 import ContainerProbeSettings
    from ._models_py3 import ContentCertificateProperties
    from ._models_py3 import CustomContainer
    from ._models_py3 import CustomContainerUserSourceInfo
    from ._models_py3 import CustomDomainProperties
    from ._models_py3 import CustomDomainResource
    from ._models_py3 import CustomDomainResourceCollection
    from ._models_py3 import CustomDomainValidatePayload
    from ._models_py3 import CustomDomainValidateResult
    from ._models_py3 import CustomPersistentDiskProperties
    from ._models_py3 import CustomPersistentDiskResource
    from ._models_py3 import DeploymentInstance
    from ._models_py3 import DeploymentResource
    from ._models_py3 import DeploymentResourceCollection
    from ._models_py3 import DeploymentResourceProperties
    from ._models_py3 import DeploymentSettings
    from ._models_py3 import DiagnosticParameters
    from ._models_py3 import Error
    from ._models_py3 import GatewayApiMetadataProperties
    from ._models_py3 import GatewayApiRoute
    from ._models_py3 import GatewayCorsProperties
    from ._models_py3 import GatewayCustomDomainProperties
    from ._models_py3 import GatewayCustomDomainResource
    from ._models_py3 import GatewayCustomDomainResourceCollection
    from ._models_py3 import GatewayInstance
    from ._models_py3 import GatewayOperatorProperties
    from ._models_py3 import GatewayOperatorResourceRequests
    from ._models_py3 import GatewayProperties
    from ._models_py3 import GatewayResource
    from ._models_py3 import GatewayResourceCollection
    from ._models_py3 import GatewayResourceRequests
    from ._models_py3 import GatewayRouteConfigProperties
    from ._models_py3 import GatewayRouteConfigResource
    from ._models_py3 import GatewayRouteConfigResourceCollection
    from ._models_py3 import GitPatternRepository
    from ._models_py3 import ImageRegistryCredential
    from ._models_py3 import JarUploadedUserSourceInfo
    from ._models_py3 import KeyVaultCertificateProperties
    from ._models_py3 import LoadedCertificate
    from ._models_py3 import LogFileUrlResponse
    from ._models_py3 import LogSpecification
    from ._models_py3 import ManagedIdentityProperties
    from ._models_py3 import MetricDimension
    from ._models_py3 import MetricSpecification
    from ._models_py3 import MonitoringSettingProperties
    from ._models_py3 import MonitoringSettingResource
    from ._models_py3 import NameAvailability
    from ._models_py3 import NameAvailabilityParameters
    from ._models_py3 import NetCoreZipUploadedUserSourceInfo
    from ._models_py3 import NetworkProfile
    from ._models_py3 import NetworkProfileOutboundIPs
    from ._models_py3 import OperationDetail
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationProperties
    from ._models_py3 import PersistentDisk
    from ._models_py3 import ProxyResource
    from ._models_py3 import RegenerateTestKeyRequestPayload
    from ._models_py3 import RequiredTraffic
    from ._models_py3 import Resource
    from ._models_py3 import ResourceRequests
    from ._models_py3 import ResourceSku
    from ._models_py3 import ResourceSkuCapabilities
    from ._models_py3 import ResourceSkuCollection
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import ResourceSkuRestrictionInfo
    from ._models_py3 import ResourceSkuRestrictions
    from ._models_py3 import ResourceSkuZoneDetails
    from ._models_py3 import ResourceUploadDefinition
    from ._models_py3 import ServiceRegistryInstance
    from ._models_py3 import ServiceRegistryProperties
    from ._models_py3 import ServiceRegistryResource
    from ._models_py3 import ServiceRegistryResourceCollection
    from ._models_py3 import ServiceRegistryResourceRequests
    from ._models_py3 import ServiceResource
    from ._models_py3 import ServiceResourceList
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Sku
    from ._models_py3 import SkuCapacity
    from ._models_py3 import SourceUploadedUserSourceInfo
    from ._models_py3 import SsoProperties
    from ._models_py3 import StackProperties
    from ._models_py3 import StorageAccount
    from ._models_py3 import StorageProperties
    from ._models_py3 import StorageResource
    from ._models_py3 import StorageResourceCollection
    from ._models_py3 import SupportedBuildpackResource
    from ._models_py3 import SupportedBuildpackResourceProperties
    from ._models_py3 import SupportedBuildpacksCollection
    from ._models_py3 import SupportedRuntimeVersion
    from ._models_py3 import SupportedStackResource
    from ._models_py3 import SupportedStackResourceProperties
    from ._models_py3 import SupportedStacksCollection
    from ._models_py3 import SystemData
    from ._models_py3 import TemporaryDisk
    from ._models_py3 import TestKeys
    from ._models_py3 import TrackedResource
    from ._models_py3 import TriggeredBuildResult
    from ._models_py3 import UploadedUserSourceInfo
    from ._models_py3 import UserSourceInfo
    from ._models_py3 import ValidationMessages
except (SyntaxError, ImportError):
    from ._models import ActiveDeploymentCollection  # type: ignore
    from ._models import ApiPortalCustomDomainProperties  # type: ignore
    from ._models import ApiPortalCustomDomainResource  # type: ignore
    from ._models import ApiPortalCustomDomainResourceCollection  # type: ignore
    from ._models import ApiPortalInstance  # type: ignore
    from ._models import ApiPortalProperties  # type: ignore
    from ._models import ApiPortalResource  # type: ignore
    from ._models import ApiPortalResourceCollection  # type: ignore
    from ._models import ApiPortalResourceRequests  # type: ignore
    from ._models import AppResource  # type: ignore
    from ._models import AppResourceCollection  # type: ignore
    from ._models import AppResourceProperties  # type: ignore
    from ._models import ApplicationInsightsAgentVersions  # type: ignore
    from ._models import AvailableOperations  # type: ignore
    from ._models import AvailableRuntimeVersions  # type: ignore
    from ._models import AzureFileVolume  # type: ignore
    from ._models import BindingResource  # type: ignore
    from ._models import BindingResourceCollection  # type: ignore
    from ._models import BindingResourceProperties  # type: ignore
    from ._models import Build  # type: ignore
    from ._models import BuildCollection  # type: ignore
    from ._models import BuildProperties  # type: ignore
    from ._models import BuildResult  # type: ignore
    from ._models import BuildResultCollection  # type: ignore
    from ._models import BuildResultLog  # type: ignore
    from ._models import BuildResultProperties  # type: ignore
    from ._models import BuildResultUserSourceInfo  # type: ignore
    from ._models import BuildService  # type: ignore
    from ._models import BuildServiceAgentPoolProperties  # type: ignore
    from ._models import BuildServiceAgentPoolResource  # type: ignore
    from ._models import BuildServiceAgentPoolResourceCollection  # type: ignore
    from ._models import BuildServiceAgentPoolSizeProperties  # type: ignore
    from ._models import BuildServiceCollection  # type: ignore
    from ._models import BuildServiceProperties  # type: ignore
    from ._models import BuildServicePropertiesResourceRequests  # type: ignore
    from ._models import BuildStageProperties  # type: ignore
    from ._models import BuilderProperties  # type: ignore
    from ._models import BuilderResource  # type: ignore
    from ._models import BuilderResourceCollection  # type: ignore
    from ._models import BuildpackBindingLaunchProperties  # type: ignore
    from ._models import BuildpackBindingProperties  # type: ignore
    from ._models import BuildpackBindingResource  # type: ignore
    from ._models import BuildpackBindingResourceCollection  # type: ignore
    from ._models import BuildpackProperties  # type: ignore
    from ._models import BuildpacksGroupProperties  # type: ignore
    from ._models import CertificateProperties  # type: ignore
    from ._models import CertificateResource  # type: ignore
    from ._models import CertificateResourceCollection  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import ClusterResourceProperties  # type: ignore
    from ._models import ConfigServerGitProperty  # type: ignore
    from ._models import ConfigServerProperties  # type: ignore
    from ._models import ConfigServerResource  # type: ignore
    from ._models import ConfigServerSettings  # type: ignore
    from ._models import ConfigServerSettingsErrorRecord  # type: ignore
    from ._models import ConfigServerSettingsValidateResult  # type: ignore
    from ._models import ConfigurationServiceGitProperty  # type: ignore
    from ._models import ConfigurationServiceGitPropertyValidateResult  # type: ignore
    from ._models import ConfigurationServiceGitRepository  # type: ignore
    from ._models import ConfigurationServiceInstance  # type: ignore
    from ._models import ConfigurationServiceProperties  # type: ignore
    from ._models import ConfigurationServiceResource  # type: ignore
    from ._models import ConfigurationServiceResourceCollection  # type: ignore
    from ._models import ConfigurationServiceResourceRequests  # type: ignore
    from ._models import ConfigurationServiceSettings  # type: ignore
    from ._models import ConfigurationServiceSettingsValidateResult  # type: ignore
    from ._models import ContainerProbeSettings  # type: ignore
    from ._models import ContentCertificateProperties  # type: ignore
    from ._models import CustomContainer  # type: ignore
    from ._models import CustomContainerUserSourceInfo  # type: ignore
    from ._models import CustomDomainProperties  # type: ignore
    from ._models import CustomDomainResource  # type: ignore
    from ._models import CustomDomainResourceCollection  # type: ignore
    from ._models import CustomDomainValidatePayload  # type: ignore
    from ._models import CustomDomainValidateResult  # type: ignore
    from ._models import CustomPersistentDiskProperties  # type: ignore
    from ._models import CustomPersistentDiskResource  # type: ignore
    from ._models import DeploymentInstance  # type: ignore
    from ._models import DeploymentResource  # type: ignore
    from ._models import DeploymentResourceCollection  # type: ignore
    from ._models import DeploymentResourceProperties  # type: ignore
    from ._models import DeploymentSettings  # type: ignore
    from ._models import DiagnosticParameters  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import GatewayApiMetadataProperties  # type: ignore
    from ._models import GatewayApiRoute  # type: ignore
    from ._models import GatewayCorsProperties  # type: ignore
    from ._models import GatewayCustomDomainProperties  # type: ignore
    from ._models import GatewayCustomDomainResource  # type: ignore
    from ._models import GatewayCustomDomainResourceCollection  # type: ignore
    from ._models import GatewayInstance  # type: ignore
    from ._models import GatewayOperatorProperties  # type: ignore
    from ._models import GatewayOperatorResourceRequests  # type: ignore
    from ._models import GatewayProperties  # type: ignore
    from ._models import GatewayResource  # type: ignore
    from ._models import GatewayResourceCollection  # type: ignore
    from ._models import GatewayResourceRequests  # type: ignore
    from ._models import GatewayRouteConfigProperties  # type: ignore
    from ._models import GatewayRouteConfigResource  # type: ignore
    from ._models import GatewayRouteConfigResourceCollection  # type: ignore
    from ._models import GitPatternRepository  # type: ignore
    from ._models import ImageRegistryCredential  # type: ignore
    from ._models import JarUploadedUserSourceInfo  # type: ignore
    from ._models import KeyVaultCertificateProperties  # type: ignore
    from ._models import LoadedCertificate  # type: ignore
    from ._models import LogFileUrlResponse  # type: ignore
    from ._models import LogSpecification  # type: ignore
    from ._models import ManagedIdentityProperties  # type: ignore
    from ._models import MetricDimension  # type: ignore
    from ._models import MetricSpecification  # type: ignore
    from ._models import MonitoringSettingProperties  # type: ignore
    from ._models import MonitoringSettingResource  # type: ignore
    from ._models import NameAvailability  # type: ignore
    from ._models import NameAvailabilityParameters  # type: ignore
    from ._models import NetCoreZipUploadedUserSourceInfo  # type: ignore
    from ._models import NetworkProfile  # type: ignore
    from ._models import NetworkProfileOutboundIPs  # type: ignore
    from ._models import OperationDetail  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationProperties  # type: ignore
    from ._models import PersistentDisk  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import RegenerateTestKeyRequestPayload  # type: ignore
    from ._models import RequiredTraffic  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceRequests  # type: ignore
    from ._models import ResourceSku  # type: ignore
    from ._models import ResourceSkuCapabilities  # type: ignore
    from ._models import ResourceSkuCollection  # type: ignore
    from ._models import ResourceSkuLocationInfo  # type: ignore
    from ._models import ResourceSkuRestrictionInfo  # type: ignore
    from ._models import ResourceSkuRestrictions  # type: ignore
    from ._models import ResourceSkuZoneDetails  # type: ignore
    from ._models import ResourceUploadDefinition  # type: ignore
    from ._models import ServiceRegistryInstance  # type: ignore
    from ._models import ServiceRegistryProperties  # type: ignore
    from ._models import ServiceRegistryResource  # type: ignore
    from ._models import ServiceRegistryResourceCollection  # type: ignore
    from ._models import ServiceRegistryResourceRequests  # type: ignore
    from ._models import ServiceResource  # type: ignore
    from ._models import ServiceResourceList  # type: ignore
    from ._models import ServiceSpecification  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuCapacity  # type: ignore
    from ._models import SourceUploadedUserSourceInfo  # type: ignore
    from ._models import SsoProperties  # type: ignore
    from ._models import StackProperties  # type: ignore
    from ._models import StorageAccount  # type: ignore
    from ._models import StorageProperties  # type: ignore
    from ._models import StorageResource  # type: ignore
    from ._models import StorageResourceCollection  # type: ignore
    from ._models import SupportedBuildpackResource  # type: ignore
    from ._models import SupportedBuildpackResourceProperties  # type: ignore
    from ._models import SupportedBuildpacksCollection  # type: ignore
    from ._models import SupportedRuntimeVersion  # type: ignore
    from ._models import SupportedStackResource  # type: ignore
    from ._models import SupportedStackResourceProperties  # type: ignore
    from ._models import SupportedStacksCollection  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TemporaryDisk  # type: ignore
    from ._models import TestKeys  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import TriggeredBuildResult  # type: ignore
    from ._models import UploadedUserSourceInfo  # type: ignore
    from ._models import UserSourceInfo  # type: ignore
    from ._models import ValidationMessages  # type: ignore

from ._app_platform_management_client_enums import (
    ApiPortalProvisioningState,
    AppResourceProvisioningState,
    BindingType,
    BuildProvisioningState,
    BuildResultProvisioningState,
    BuildServiceProvisioningState,
    BuilderProvisioningState,
    BuildpackBindingProvisioningState,
    ConfigServerState,
    ConfigurationServiceProvisioningState,
    CreatedByType,
    DeploymentResourceProvisioningState,
    DeploymentResourceStatus,
    GatewayProvisioningState,
    KPackBuildStageProvisioningState,
    LastModifiedByType,
    ManagedIdentityType,
    MonitoringSettingState,
    PowerState,
    ProvisioningState,
    ResourceSkuRestrictionsReasonCode,
    ResourceSkuRestrictionsType,
    ServiceRegistryProvisioningState,
    SkuScaleType,
    SupportedRuntimePlatform,
    SupportedRuntimeValue,
    TestKeyType,
    TrafficDirection,
)

__all__ = [
    'ActiveDeploymentCollection',
    'ApiPortalCustomDomainProperties',
    'ApiPortalCustomDomainResource',
    'ApiPortalCustomDomainResourceCollection',
    'ApiPortalInstance',
    'ApiPortalProperties',
    'ApiPortalResource',
    'ApiPortalResourceCollection',
    'ApiPortalResourceRequests',
    'AppResource',
    'AppResourceCollection',
    'AppResourceProperties',
    'ApplicationInsightsAgentVersions',
    'AvailableOperations',
    'AvailableRuntimeVersions',
    'AzureFileVolume',
    'BindingResource',
    'BindingResourceCollection',
    'BindingResourceProperties',
    'Build',
    'BuildCollection',
    'BuildProperties',
    'BuildResult',
    'BuildResultCollection',
    'BuildResultLog',
    'BuildResultProperties',
    'BuildResultUserSourceInfo',
    'BuildService',
    'BuildServiceAgentPoolProperties',
    'BuildServiceAgentPoolResource',
    'BuildServiceAgentPoolResourceCollection',
    'BuildServiceAgentPoolSizeProperties',
    'BuildServiceCollection',
    'BuildServiceProperties',
    'BuildServicePropertiesResourceRequests',
    'BuildStageProperties',
    'BuilderProperties',
    'BuilderResource',
    'BuilderResourceCollection',
    'BuildpackBindingLaunchProperties',
    'BuildpackBindingProperties',
    'BuildpackBindingResource',
    'BuildpackBindingResourceCollection',
    'BuildpackProperties',
    'BuildpacksGroupProperties',
    'CertificateProperties',
    'CertificateResource',
    'CertificateResourceCollection',
    'CloudErrorBody',
    'ClusterResourceProperties',
    'ConfigServerGitProperty',
    'ConfigServerProperties',
    'ConfigServerResource',
    'ConfigServerSettings',
    'ConfigServerSettingsErrorRecord',
    'ConfigServerSettingsValidateResult',
    'ConfigurationServiceGitProperty',
    'ConfigurationServiceGitPropertyValidateResult',
    'ConfigurationServiceGitRepository',
    'ConfigurationServiceInstance',
    'ConfigurationServiceProperties',
    'ConfigurationServiceResource',
    'ConfigurationServiceResourceCollection',
    'ConfigurationServiceResourceRequests',
    'ConfigurationServiceSettings',
    'ConfigurationServiceSettingsValidateResult',
    'ContainerProbeSettings',
    'ContentCertificateProperties',
    'CustomContainer',
    'CustomContainerUserSourceInfo',
    'CustomDomainProperties',
    'CustomDomainResource',
    'CustomDomainResourceCollection',
    'CustomDomainValidatePayload',
    'CustomDomainValidateResult',
    'CustomPersistentDiskProperties',
    'CustomPersistentDiskResource',
    'DeploymentInstance',
    'DeploymentResource',
    'DeploymentResourceCollection',
    'DeploymentResourceProperties',
    'DeploymentSettings',
    'DiagnosticParameters',
    'Error',
    'GatewayApiMetadataProperties',
    'GatewayApiRoute',
    'GatewayCorsProperties',
    'GatewayCustomDomainProperties',
    'GatewayCustomDomainResource',
    'GatewayCustomDomainResourceCollection',
    'GatewayInstance',
    'GatewayOperatorProperties',
    'GatewayOperatorResourceRequests',
    'GatewayProperties',
    'GatewayResource',
    'GatewayResourceCollection',
    'GatewayResourceRequests',
    'GatewayRouteConfigProperties',
    'GatewayRouteConfigResource',
    'GatewayRouteConfigResourceCollection',
    'GitPatternRepository',
    'ImageRegistryCredential',
    'JarUploadedUserSourceInfo',
    'KeyVaultCertificateProperties',
    'LoadedCertificate',
    'LogFileUrlResponse',
    'LogSpecification',
    'ManagedIdentityProperties',
    'MetricDimension',
    'MetricSpecification',
    'MonitoringSettingProperties',
    'MonitoringSettingResource',
    'NameAvailability',
    'NameAvailabilityParameters',
    'NetCoreZipUploadedUserSourceInfo',
    'NetworkProfile',
    'NetworkProfileOutboundIPs',
    'OperationDetail',
    'OperationDisplay',
    'OperationProperties',
    'PersistentDisk',
    'ProxyResource',
    'RegenerateTestKeyRequestPayload',
    'RequiredTraffic',
    'Resource',
    'ResourceRequests',
    'ResourceSku',
    'ResourceSkuCapabilities',
    'ResourceSkuCollection',
    'ResourceSkuLocationInfo',
    'ResourceSkuRestrictionInfo',
    'ResourceSkuRestrictions',
    'ResourceSkuZoneDetails',
    'ResourceUploadDefinition',
    'ServiceRegistryInstance',
    'ServiceRegistryProperties',
    'ServiceRegistryResource',
    'ServiceRegistryResourceCollection',
    'ServiceRegistryResourceRequests',
    'ServiceResource',
    'ServiceResourceList',
    'ServiceSpecification',
    'Sku',
    'SkuCapacity',
    'SourceUploadedUserSourceInfo',
    'SsoProperties',
    'StackProperties',
    'StorageAccount',
    'StorageProperties',
    'StorageResource',
    'StorageResourceCollection',
    'SupportedBuildpackResource',
    'SupportedBuildpackResourceProperties',
    'SupportedBuildpacksCollection',
    'SupportedRuntimeVersion',
    'SupportedStackResource',
    'SupportedStackResourceProperties',
    'SupportedStacksCollection',
    'SystemData',
    'TemporaryDisk',
    'TestKeys',
    'TrackedResource',
    'TriggeredBuildResult',
    'UploadedUserSourceInfo',
    'UserSourceInfo',
    'ValidationMessages',
    'ApiPortalProvisioningState',
    'AppResourceProvisioningState',
    'BindingType',
    'BuildProvisioningState',
    'BuildResultProvisioningState',
    'BuildServiceProvisioningState',
    'BuilderProvisioningState',
    'BuildpackBindingProvisioningState',
    'ConfigServerState',
    'ConfigurationServiceProvisioningState',
    'CreatedByType',
    'DeploymentResourceProvisioningState',
    'DeploymentResourceStatus',
    'GatewayProvisioningState',
    'KPackBuildStageProvisioningState',
    'LastModifiedByType',
    'ManagedIdentityType',
    'MonitoringSettingState',
    'PowerState',
    'ProvisioningState',
    'ResourceSkuRestrictionsReasonCode',
    'ResourceSkuRestrictionsType',
    'ServiceRegistryProvisioningState',
    'SkuScaleType',
    'SupportedRuntimePlatform',
    'SupportedRuntimeValue',
    'TestKeyType',
    'TrafficDirection',
]
