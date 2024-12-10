# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Optional, Union
from urllib.parse import urlencode
from . import _common
from . import _transformers as t
from . import types
from ._api_client import ApiClient
from ._common import get_value_by_path as getv
from ._common import set_value_by_path as setv
from .pagers import AsyncPager, Pager


def _Part_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['video_metadata']):
    raise ValueError('video_metadata parameter is not supported in Google AI.')

  if getv(from_object, ['code_execution_result']) is not None:
    setv(
        to_object,
        ['codeExecutionResult'],
        getv(from_object, ['code_execution_result']),
    )

  if getv(from_object, ['executable_code']) is not None:
    setv(to_object, ['executableCode'], getv(from_object, ['executable_code']))

  if getv(from_object, ['file_data']) is not None:
    setv(to_object, ['fileData'], getv(from_object, ['file_data']))

  if getv(from_object, ['function_call']) is not None:
    setv(to_object, ['functionCall'], getv(from_object, ['function_call']))

  if getv(from_object, ['function_response']) is not None:
    setv(
        to_object,
        ['functionResponse'],
        getv(from_object, ['function_response']),
    )

  if getv(from_object, ['inline_data']) is not None:
    setv(to_object, ['inlineData'], getv(from_object, ['inline_data']))

  if getv(from_object, ['text']) is not None:
    setv(to_object, ['text'], getv(from_object, ['text']))

  return to_object


def _Part_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['video_metadata']) is not None:
    setv(to_object, ['videoMetadata'], getv(from_object, ['video_metadata']))

  if getv(from_object, ['code_execution_result']) is not None:
    setv(
        to_object,
        ['codeExecutionResult'],
        getv(from_object, ['code_execution_result']),
    )

  if getv(from_object, ['executable_code']) is not None:
    setv(to_object, ['executableCode'], getv(from_object, ['executable_code']))

  if getv(from_object, ['file_data']) is not None:
    setv(to_object, ['fileData'], getv(from_object, ['file_data']))

  if getv(from_object, ['function_call']) is not None:
    setv(to_object, ['functionCall'], getv(from_object, ['function_call']))

  if getv(from_object, ['function_response']) is not None:
    setv(
        to_object,
        ['functionResponse'],
        getv(from_object, ['function_response']),
    )

  if getv(from_object, ['inline_data']) is not None:
    setv(to_object, ['inlineData'], getv(from_object, ['inline_data']))

  if getv(from_object, ['text']) is not None:
    setv(to_object, ['text'], getv(from_object, ['text']))

  return to_object


def _Content_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['parts']) is not None:
    setv(
        to_object,
        ['parts'],
        [
            _Part_to_mldev(api_client, item, to_object)
            for item in getv(from_object, ['parts'])
        ],
    )

  if getv(from_object, ['role']) is not None:
    setv(to_object, ['role'], getv(from_object, ['role']))

  return to_object


def _Content_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['parts']) is not None:
    setv(
        to_object,
        ['parts'],
        [
            _Part_to_vertex(api_client, item, to_object)
            for item in getv(from_object, ['parts'])
        ],
    )

  if getv(from_object, ['role']) is not None:
    setv(to_object, ['role'], getv(from_object, ['role']))

  return to_object


def _Schema_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['min_items']):
    raise ValueError('min_items parameter is not supported in Google AI.')

  if getv(from_object, ['example']):
    raise ValueError('example parameter is not supported in Google AI.')

  if getv(from_object, ['property_ordering']):
    raise ValueError(
        'property_ordering parameter is not supported in Google AI.'
    )

  if getv(from_object, ['pattern']):
    raise ValueError('pattern parameter is not supported in Google AI.')

  if getv(from_object, ['minimum']):
    raise ValueError('minimum parameter is not supported in Google AI.')

  if getv(from_object, ['default']):
    raise ValueError('default parameter is not supported in Google AI.')

  if getv(from_object, ['any_of']):
    raise ValueError('any_of parameter is not supported in Google AI.')

  if getv(from_object, ['max_length']):
    raise ValueError('max_length parameter is not supported in Google AI.')

  if getv(from_object, ['title']):
    raise ValueError('title parameter is not supported in Google AI.')

  if getv(from_object, ['min_length']):
    raise ValueError('min_length parameter is not supported in Google AI.')

  if getv(from_object, ['min_properties']):
    raise ValueError('min_properties parameter is not supported in Google AI.')

  if getv(from_object, ['max_items']):
    raise ValueError('max_items parameter is not supported in Google AI.')

  if getv(from_object, ['maximum']):
    raise ValueError('maximum parameter is not supported in Google AI.')

  if getv(from_object, ['nullable']):
    raise ValueError('nullable parameter is not supported in Google AI.')

  if getv(from_object, ['max_properties']):
    raise ValueError('max_properties parameter is not supported in Google AI.')

  if getv(from_object, ['type']) is not None:
    setv(to_object, ['type'], getv(from_object, ['type']))

  if getv(from_object, ['description']) is not None:
    setv(to_object, ['description'], getv(from_object, ['description']))

  if getv(from_object, ['enum']) is not None:
    setv(to_object, ['enum'], getv(from_object, ['enum']))

  if getv(from_object, ['format']) is not None:
    setv(to_object, ['format'], getv(from_object, ['format']))

  if getv(from_object, ['items']) is not None:
    setv(to_object, ['items'], getv(from_object, ['items']))

  if getv(from_object, ['properties']) is not None:
    setv(to_object, ['properties'], getv(from_object, ['properties']))

  if getv(from_object, ['required']) is not None:
    setv(to_object, ['required'], getv(from_object, ['required']))

  return to_object


def _Schema_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['min_items']) is not None:
    setv(to_object, ['minItems'], getv(from_object, ['min_items']))

  if getv(from_object, ['example']) is not None:
    setv(to_object, ['example'], getv(from_object, ['example']))

  if getv(from_object, ['property_ordering']) is not None:
    setv(
        to_object,
        ['propertyOrdering'],
        getv(from_object, ['property_ordering']),
    )

  if getv(from_object, ['pattern']) is not None:
    setv(to_object, ['pattern'], getv(from_object, ['pattern']))

  if getv(from_object, ['minimum']) is not None:
    setv(to_object, ['minimum'], getv(from_object, ['minimum']))

  if getv(from_object, ['default']) is not None:
    setv(to_object, ['default'], getv(from_object, ['default']))

  if getv(from_object, ['any_of']) is not None:
    setv(to_object, ['anyOf'], getv(from_object, ['any_of']))

  if getv(from_object, ['max_length']) is not None:
    setv(to_object, ['maxLength'], getv(from_object, ['max_length']))

  if getv(from_object, ['title']) is not None:
    setv(to_object, ['title'], getv(from_object, ['title']))

  if getv(from_object, ['min_length']) is not None:
    setv(to_object, ['minLength'], getv(from_object, ['min_length']))

  if getv(from_object, ['min_properties']) is not None:
    setv(to_object, ['minProperties'], getv(from_object, ['min_properties']))

  if getv(from_object, ['max_items']) is not None:
    setv(to_object, ['maxItems'], getv(from_object, ['max_items']))

  if getv(from_object, ['maximum']) is not None:
    setv(to_object, ['maximum'], getv(from_object, ['maximum']))

  if getv(from_object, ['nullable']) is not None:
    setv(to_object, ['nullable'], getv(from_object, ['nullable']))

  if getv(from_object, ['max_properties']) is not None:
    setv(to_object, ['maxProperties'], getv(from_object, ['max_properties']))

  if getv(from_object, ['type']) is not None:
    setv(to_object, ['type'], getv(from_object, ['type']))

  if getv(from_object, ['description']) is not None:
    setv(to_object, ['description'], getv(from_object, ['description']))

  if getv(from_object, ['enum']) is not None:
    setv(to_object, ['enum'], getv(from_object, ['enum']))

  if getv(from_object, ['format']) is not None:
    setv(to_object, ['format'], getv(from_object, ['format']))

  if getv(from_object, ['items']) is not None:
    setv(to_object, ['items'], getv(from_object, ['items']))

  if getv(from_object, ['properties']) is not None:
    setv(to_object, ['properties'], getv(from_object, ['properties']))

  if getv(from_object, ['required']) is not None:
    setv(to_object, ['required'], getv(from_object, ['required']))

  return to_object


def _FunctionDeclaration_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['response']):
    raise ValueError('response parameter is not supported in Google AI.')

  if getv(from_object, ['description']) is not None:
    setv(to_object, ['description'], getv(from_object, ['description']))

  if getv(from_object, ['name']) is not None:
    setv(to_object, ['name'], getv(from_object, ['name']))

  if getv(from_object, ['parameters']) is not None:
    setv(to_object, ['parameters'], getv(from_object, ['parameters']))

  return to_object


def _FunctionDeclaration_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['response']) is not None:
    setv(
        to_object,
        ['response'],
        _Schema_to_vertex(
            api_client, getv(from_object, ['response']), to_object
        ),
    )

  if getv(from_object, ['description']) is not None:
    setv(to_object, ['description'], getv(from_object, ['description']))

  if getv(from_object, ['name']) is not None:
    setv(to_object, ['name'], getv(from_object, ['name']))

  if getv(from_object, ['parameters']) is not None:
    setv(to_object, ['parameters'], getv(from_object, ['parameters']))

  return to_object


def _GoogleSearch_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}

  return to_object


def _GoogleSearch_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}

  return to_object


def _DynamicRetrievalConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['mode']) is not None:
    setv(to_object, ['mode'], getv(from_object, ['mode']))

  if getv(from_object, ['dynamic_threshold']) is not None:
    setv(
        to_object,
        ['dynamicThreshold'],
        getv(from_object, ['dynamic_threshold']),
    )

  return to_object


def _DynamicRetrievalConfig_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['mode']) is not None:
    setv(to_object, ['mode'], getv(from_object, ['mode']))

  if getv(from_object, ['dynamic_threshold']) is not None:
    setv(
        to_object,
        ['dynamicThreshold'],
        getv(from_object, ['dynamic_threshold']),
    )

  return to_object


def _GoogleSearchRetrieval_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['dynamic_retrieval_config']) is not None:
    setv(
        to_object,
        ['dynamicRetrievalConfig'],
        _DynamicRetrievalConfig_to_mldev(
            api_client,
            getv(from_object, ['dynamic_retrieval_config']),
            to_object,
        ),
    )

  return to_object


def _GoogleSearchRetrieval_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['dynamic_retrieval_config']) is not None:
    setv(
        to_object,
        ['dynamicRetrievalConfig'],
        _DynamicRetrievalConfig_to_vertex(
            api_client,
            getv(from_object, ['dynamic_retrieval_config']),
            to_object,
        ),
    )

  return to_object


def _Tool_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['function_declarations']) is not None:
    setv(
        to_object,
        ['functionDeclarations'],
        [
            _FunctionDeclaration_to_mldev(api_client, item, to_object)
            for item in getv(from_object, ['function_declarations'])
        ],
    )

  if getv(from_object, ['retrieval']):
    raise ValueError('retrieval parameter is not supported in Google AI.')

  if getv(from_object, ['google_search']) is not None:
    setv(
        to_object,
        ['googleSearch'],
        _GoogleSearch_to_mldev(
            api_client, getv(from_object, ['google_search']), to_object
        ),
    )

  if getv(from_object, ['google_search_retrieval']) is not None:
    setv(
        to_object,
        ['googleSearchRetrieval'],
        _GoogleSearchRetrieval_to_mldev(
            api_client,
            getv(from_object, ['google_search_retrieval']),
            to_object,
        ),
    )

  if getv(from_object, ['code_execution']) is not None:
    setv(to_object, ['codeExecution'], getv(from_object, ['code_execution']))

  return to_object


def _Tool_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['function_declarations']) is not None:
    setv(
        to_object,
        ['functionDeclarations'],
        [
            _FunctionDeclaration_to_vertex(api_client, item, to_object)
            for item in getv(from_object, ['function_declarations'])
        ],
    )

  if getv(from_object, ['retrieval']) is not None:
    setv(to_object, ['retrieval'], getv(from_object, ['retrieval']))

  if getv(from_object, ['google_search']) is not None:
    setv(
        to_object,
        ['googleSearch'],
        _GoogleSearch_to_vertex(
            api_client, getv(from_object, ['google_search']), to_object
        ),
    )

  if getv(from_object, ['google_search_retrieval']) is not None:
    setv(
        to_object,
        ['googleSearchRetrieval'],
        _GoogleSearchRetrieval_to_vertex(
            api_client,
            getv(from_object, ['google_search_retrieval']),
            to_object,
        ),
    )

  if getv(from_object, ['code_execution']) is not None:
    setv(to_object, ['codeExecution'], getv(from_object, ['code_execution']))

  return to_object


def _FunctionCallingConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['mode']) is not None:
    setv(to_object, ['mode'], getv(from_object, ['mode']))

  if getv(from_object, ['allowed_function_names']) is not None:
    setv(
        to_object,
        ['allowedFunctionNames'],
        getv(from_object, ['allowed_function_names']),
    )

  return to_object


def _FunctionCallingConfig_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['mode']) is not None:
    setv(to_object, ['mode'], getv(from_object, ['mode']))

  if getv(from_object, ['allowed_function_names']) is not None:
    setv(
        to_object,
        ['allowedFunctionNames'],
        getv(from_object, ['allowed_function_names']),
    )

  return to_object


def _ToolConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['function_calling_config']) is not None:
    setv(
        to_object,
        ['functionCallingConfig'],
        _FunctionCallingConfig_to_mldev(
            api_client,
            getv(from_object, ['function_calling_config']),
            to_object,
        ),
    )

  return to_object


def _ToolConfig_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['function_calling_config']) is not None:
    setv(
        to_object,
        ['functionCallingConfig'],
        _FunctionCallingConfig_to_vertex(
            api_client,
            getv(from_object, ['function_calling_config']),
            to_object,
        ),
    )

  return to_object


def _CreateCachedContentConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['http_options']) is not None:
    setv(to_object, ['httpOptions'], getv(from_object, ['http_options']))

  if getv(from_object, ['ttl']) is not None:
    setv(parent_object, ['ttl'], getv(from_object, ['ttl']))

  if getv(from_object, ['expire_time']) is not None:
    setv(parent_object, ['expireTime'], getv(from_object, ['expire_time']))

  if getv(from_object, ['display_name']) is not None:
    setv(parent_object, ['displayName'], getv(from_object, ['display_name']))

  if getv(from_object, ['system_instruction']) is not None:
    setv(
        parent_object,
        ['systemInstruction'],
        _Content_to_mldev(
            api_client,
            t.t_content(api_client, getv(from_object, ['system_instruction'])),
            to_object,
        ),
    )

  if getv(from_object, ['tools']) is not None:
    setv(
        parent_object,
        ['tools'],
        [
            _Tool_to_mldev(api_client, item, to_object)
            for item in getv(from_object, ['tools'])
        ],
    )

  if getv(from_object, ['tool_config']) is not None:
    setv(
        parent_object,
        ['toolConfig'],
        _ToolConfig_to_mldev(
            api_client, getv(from_object, ['tool_config']), to_object
        ),
    )

  return to_object


def _CreateCachedContentConfig_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['http_options']) is not None:
    setv(to_object, ['httpOptions'], getv(from_object, ['http_options']))

  if getv(from_object, ['ttl']) is not None:
    setv(parent_object, ['ttl'], getv(from_object, ['ttl']))

  if getv(from_object, ['expire_time']) is not None:
    setv(parent_object, ['expireTime'], getv(from_object, ['expire_time']))

  if getv(from_object, ['display_name']) is not None:
    setv(parent_object, ['displayName'], getv(from_object, ['display_name']))

  if getv(from_object, ['system_instruction']) is not None:
    setv(
        parent_object,
        ['systemInstruction'],
        _Content_to_vertex(
            api_client,
            t.t_content(api_client, getv(from_object, ['system_instruction'])),
            to_object,
        ),
    )

  if getv(from_object, ['tools']) is not None:
    setv(
        parent_object,
        ['tools'],
        [
            _Tool_to_vertex(api_client, item, to_object)
            for item in getv(from_object, ['tools'])
        ],
    )

  if getv(from_object, ['tool_config']) is not None:
    setv(
        parent_object,
        ['toolConfig'],
        _ToolConfig_to_vertex(
            api_client, getv(from_object, ['tool_config']), to_object
        ),
    )

  return to_object


def _CreateCachedContentParameters_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['model']) is not None:
    setv(
        to_object,
        ['model'],
        t.t_caches_model(api_client, getv(from_object, ['model'])),
    )

  if getv(from_object, ['contents']) is not None:
    setv(
        to_object,
        ['contents'],
        [
            _Content_to_mldev(api_client, item, to_object)
            for item in t.t_contents(
                api_client, getv(from_object, ['contents'])
            )
        ],
    )

  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _CreateCachedContentConfig_to_mldev(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _CreateCachedContentParameters_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['model']) is not None:
    setv(
        to_object,
        ['model'],
        t.t_caches_model(api_client, getv(from_object, ['model'])),
    )

  if getv(from_object, ['contents']) is not None:
    setv(
        to_object,
        ['contents'],
        [
            _Content_to_vertex(api_client, item, to_object)
            for item in t.t_contents(
                api_client, getv(from_object, ['contents'])
            )
        ],
    )

  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _CreateCachedContentConfig_to_vertex(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _GetCachedContentConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['http_options']) is not None:
    setv(to_object, ['httpOptions'], getv(from_object, ['http_options']))

  return to_object


def _GetCachedContentConfig_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['http_options']) is not None:
    setv(to_object, ['httpOptions'], getv(from_object, ['http_options']))

  return to_object


def _GetCachedContentParameters_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['name']) is not None:
    setv(
        to_object,
        ['_url', 'name'],
        t.t_cached_content_name(api_client, getv(from_object, ['name'])),
    )

  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _GetCachedContentConfig_to_mldev(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _GetCachedContentParameters_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['name']) is not None:
    setv(
        to_object,
        ['_url', 'name'],
        t.t_cached_content_name(api_client, getv(from_object, ['name'])),
    )

  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _GetCachedContentConfig_to_vertex(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _DeleteCachedContentConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['http_options']) is not None:
    setv(to_object, ['httpOptions'], getv(from_object, ['http_options']))

  return to_object


def _DeleteCachedContentConfig_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['http_options']) is not None:
    setv(to_object, ['httpOptions'], getv(from_object, ['http_options']))

  return to_object


def _DeleteCachedContentParameters_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['name']) is not None:
    setv(
        to_object,
        ['_url', 'name'],
        t.t_cached_content_name(api_client, getv(from_object, ['name'])),
    )

  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _DeleteCachedContentConfig_to_mldev(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _DeleteCachedContentParameters_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['name']) is not None:
    setv(
        to_object,
        ['_url', 'name'],
        t.t_cached_content_name(api_client, getv(from_object, ['name'])),
    )

  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _DeleteCachedContentConfig_to_vertex(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _UpdateCachedContentConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['http_options']) is not None:
    setv(to_object, ['httpOptions'], getv(from_object, ['http_options']))

  if getv(from_object, ['ttl']) is not None:
    setv(parent_object, ['ttl'], getv(from_object, ['ttl']))

  if getv(from_object, ['expire_time']) is not None:
    setv(parent_object, ['expireTime'], getv(from_object, ['expire_time']))

  return to_object


def _UpdateCachedContentConfig_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['http_options']) is not None:
    setv(to_object, ['httpOptions'], getv(from_object, ['http_options']))

  if getv(from_object, ['ttl']) is not None:
    setv(parent_object, ['ttl'], getv(from_object, ['ttl']))

  if getv(from_object, ['expire_time']) is not None:
    setv(parent_object, ['expireTime'], getv(from_object, ['expire_time']))

  return to_object


def _UpdateCachedContentParameters_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['name']) is not None:
    setv(
        to_object,
        ['_url', 'name'],
        t.t_cached_content_name(api_client, getv(from_object, ['name'])),
    )

  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _UpdateCachedContentConfig_to_mldev(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _UpdateCachedContentParameters_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['name']) is not None:
    setv(
        to_object,
        ['_url', 'name'],
        t.t_cached_content_name(api_client, getv(from_object, ['name'])),
    )

  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _UpdateCachedContentConfig_to_vertex(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _ListCachedContentsConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['page_size']) is not None:
    setv(
        parent_object, ['_query', 'pageSize'], getv(from_object, ['page_size'])
    )

  if getv(from_object, ['page_token']) is not None:
    setv(
        parent_object,
        ['_query', 'pageToken'],
        getv(from_object, ['page_token']),
    )

  return to_object


def _ListCachedContentsConfig_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['page_size']) is not None:
    setv(
        parent_object, ['_query', 'pageSize'], getv(from_object, ['page_size'])
    )

  if getv(from_object, ['page_token']) is not None:
    setv(
        parent_object,
        ['_query', 'pageToken'],
        getv(from_object, ['page_token']),
    )

  return to_object


def _ListCachedContentsParameters_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _ListCachedContentsConfig_to_mldev(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _ListCachedContentsParameters_to_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['config']) is not None:
    setv(
        to_object,
        ['config'],
        _ListCachedContentsConfig_to_vertex(
            api_client, getv(from_object, ['config']), to_object
        ),
    )

  return to_object


def _CachedContent_from_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['name']) is not None:
    setv(to_object, ['name'], getv(from_object, ['name']))

  if getv(from_object, ['displayName']) is not None:
    setv(to_object, ['display_name'], getv(from_object, ['displayName']))

  if getv(from_object, ['model']) is not None:
    setv(to_object, ['model'], getv(from_object, ['model']))

  if getv(from_object, ['createTime']) is not None:
    setv(to_object, ['create_time'], getv(from_object, ['createTime']))

  if getv(from_object, ['updateTime']) is not None:
    setv(to_object, ['update_time'], getv(from_object, ['updateTime']))

  if getv(from_object, ['expireTime']) is not None:
    setv(to_object, ['expire_time'], getv(from_object, ['expireTime']))

  if getv(from_object, ['usageMetadata']) is not None:
    setv(to_object, ['usage_metadata'], getv(from_object, ['usageMetadata']))

  return to_object


def _CachedContent_from_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['name']) is not None:
    setv(to_object, ['name'], getv(from_object, ['name']))

  if getv(from_object, ['displayName']) is not None:
    setv(to_object, ['display_name'], getv(from_object, ['displayName']))

  if getv(from_object, ['model']) is not None:
    setv(to_object, ['model'], getv(from_object, ['model']))

  if getv(from_object, ['createTime']) is not None:
    setv(to_object, ['create_time'], getv(from_object, ['createTime']))

  if getv(from_object, ['updateTime']) is not None:
    setv(to_object, ['update_time'], getv(from_object, ['updateTime']))

  if getv(from_object, ['expireTime']) is not None:
    setv(to_object, ['expire_time'], getv(from_object, ['expireTime']))

  if getv(from_object, ['usageMetadata']) is not None:
    setv(to_object, ['usage_metadata'], getv(from_object, ['usageMetadata']))

  return to_object


def _DeleteCachedContentResponse_from_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}

  return to_object


def _DeleteCachedContentResponse_from_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}

  return to_object


def _ListCachedContentsResponse_from_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['nextPageToken']) is not None:
    setv(to_object, ['next_page_token'], getv(from_object, ['nextPageToken']))

  if getv(from_object, ['cachedContents']) is not None:
    setv(
        to_object,
        ['cached_contents'],
        [
            _CachedContent_from_mldev(api_client, item, to_object)
            for item in getv(from_object, ['cachedContents'])
        ],
    )

  return to_object


def _ListCachedContentsResponse_from_vertex(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['nextPageToken']) is not None:
    setv(to_object, ['next_page_token'], getv(from_object, ['nextPageToken']))

  if getv(from_object, ['cachedContents']) is not None:
    setv(
        to_object,
        ['cached_contents'],
        [
            _CachedContent_from_vertex(api_client, item, to_object)
            for item in getv(from_object, ['cachedContents'])
        ],
    )

  return to_object


class Caches(_common.BaseModule):

  def create(
      self,
      *,
      model: str,
      contents: Union[types.ContentListUnion, types.ContentListUnionDict],
      config: Optional[types.CreateCachedContentConfigOrDict] = None,
  ) -> types.CachedContent:
    """Creates cached content, this call will initialize the cached

    content in the data storage, and users need to pay for the cache data
    storage.

    Usage:

    .. code-block:: python

      contents = ... // Initialize the content to cache.
      response = await client.aio.caches.create(
          model= ... // The publisher model id
          contents=contents,
          config={
              'display_name': 'test cache',
              'system_instruction': 'What is the sum of the two pdfs?',
              'ttl': '86400s',
          },
      )
    """

    parameter_model = types._CreateCachedContentParameters(
        model=model,
        contents=contents,
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _CreateCachedContentParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = 'cachedContents'.format_map(request_dict.get('_url'))
    else:
      request_dict = _CreateCachedContentParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = 'cachedContents'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = self.api_client.request(
        'post', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _CachedContent_from_vertex(self.api_client, response_dict)
    else:
      response_dict = _CachedContent_from_mldev(self.api_client, response_dict)

    return_value = types.CachedContent._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  def get(
      self,
      *,
      name: str,
      config: Optional[types.GetCachedContentConfigOrDict] = None,
  ) -> types.CachedContent:
    """Gets cached content configurations.

    .. code-block:: python

      await client.aio.caches.get(name= ... ) // The server-generated resource
      name.
    """

    parameter_model = types._GetCachedContentParameters(
        name=name,
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _GetCachedContentParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    else:
      request_dict = _GetCachedContentParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = self.api_client.request(
        'get', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _CachedContent_from_vertex(self.api_client, response_dict)
    else:
      response_dict = _CachedContent_from_mldev(self.api_client, response_dict)

    return_value = types.CachedContent._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  def delete(
      self,
      *,
      name: str,
      config: Optional[types.DeleteCachedContentConfigOrDict] = None,
  ) -> types.DeleteCachedContentResponse:
    """Deletes cached content.

    Usage:

    .. code-block:: python

      await client.aio.caches.delete(name= ... ) // The server-generated
      resource name.
    """

    parameter_model = types._DeleteCachedContentParameters(
        name=name,
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _DeleteCachedContentParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    else:
      request_dict = _DeleteCachedContentParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = self.api_client.request(
        'delete', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _DeleteCachedContentResponse_from_vertex(
          self.api_client, response_dict
      )
    else:
      response_dict = _DeleteCachedContentResponse_from_mldev(
          self.api_client, response_dict
      )

    return_value = types.DeleteCachedContentResponse._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  def update(
      self,
      *,
      name: str,
      config: Optional[types.UpdateCachedContentConfigOrDict] = None,
  ) -> types.CachedContent:
    """Updates cached content configurations.

    .. code-block:: python

      response = await client.aio.caches.update(
          name= ... // The server-generated resource name.
          config={
              'ttl': '7600s',
          },
      )
    """

    parameter_model = types._UpdateCachedContentParameters(
        name=name,
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _UpdateCachedContentParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    else:
      request_dict = _UpdateCachedContentParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = self.api_client.request(
        'patch', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _CachedContent_from_vertex(self.api_client, response_dict)
    else:
      response_dict = _CachedContent_from_mldev(self.api_client, response_dict)

    return_value = types.CachedContent._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  def _list(
      self, *, config: Optional[types.ListCachedContentsConfigOrDict] = None
  ) -> types.ListCachedContentsResponse:
    """Lists cached content configurations.

    .. code-block:: python

      cached_contents = await client.aio.caches.list(config={'page_size': 2})
      async for cached_content in cached_contents:
        print(cached_content)
    """

    parameter_model = types._ListCachedContentsParameters(
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _ListCachedContentsParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = 'cachedContents'.format_map(request_dict.get('_url'))
    else:
      request_dict = _ListCachedContentsParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = 'cachedContents'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = self.api_client.request(
        'get', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _ListCachedContentsResponse_from_vertex(
          self.api_client, response_dict
      )
    else:
      response_dict = _ListCachedContentsResponse_from_mldev(
          self.api_client, response_dict
      )

    return_value = types.ListCachedContentsResponse._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  def list(
      self, *, config: Optional[types.ListCachedContentsConfigOrDict] = None
  ) -> Pager[types.CachedContent]:
    return Pager(
        'cached_contents',
        self._list,
        self._list(config=config),
        config,
    )


class AsyncCaches(_common.BaseModule):

  async def create(
      self,
      *,
      model: str,
      contents: Union[types.ContentListUnion, types.ContentListUnionDict],
      config: Optional[types.CreateCachedContentConfigOrDict] = None,
  ) -> types.CachedContent:
    """Creates cached content, this call will initialize the cached

    content in the data storage, and users need to pay for the cache data
    storage.

    Usage:

    .. code-block:: python

      contents = ... // Initialize the content to cache.
      response = await client.aio.caches.create(
          model= ... // The publisher model id
          contents=contents,
          config={
              'display_name': 'test cache',
              'system_instruction': 'What is the sum of the two pdfs?',
              'ttl': '86400s',
          },
      )
    """

    parameter_model = types._CreateCachedContentParameters(
        model=model,
        contents=contents,
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _CreateCachedContentParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = 'cachedContents'.format_map(request_dict.get('_url'))
    else:
      request_dict = _CreateCachedContentParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = 'cachedContents'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = await self.api_client.async_request(
        'post', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _CachedContent_from_vertex(self.api_client, response_dict)
    else:
      response_dict = _CachedContent_from_mldev(self.api_client, response_dict)

    return_value = types.CachedContent._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  async def get(
      self,
      *,
      name: str,
      config: Optional[types.GetCachedContentConfigOrDict] = None,
  ) -> types.CachedContent:
    """Gets cached content configurations.

    .. code-block:: python

      await client.aio.caches.get(name= ... ) // The server-generated resource
      name.
    """

    parameter_model = types._GetCachedContentParameters(
        name=name,
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _GetCachedContentParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    else:
      request_dict = _GetCachedContentParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = await self.api_client.async_request(
        'get', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _CachedContent_from_vertex(self.api_client, response_dict)
    else:
      response_dict = _CachedContent_from_mldev(self.api_client, response_dict)

    return_value = types.CachedContent._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  async def delete(
      self,
      *,
      name: str,
      config: Optional[types.DeleteCachedContentConfigOrDict] = None,
  ) -> types.DeleteCachedContentResponse:
    """Deletes cached content.

    Usage:

    .. code-block:: python

      await client.aio.caches.delete(name= ... ) // The server-generated
      resource name.
    """

    parameter_model = types._DeleteCachedContentParameters(
        name=name,
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _DeleteCachedContentParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    else:
      request_dict = _DeleteCachedContentParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = await self.api_client.async_request(
        'delete', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _DeleteCachedContentResponse_from_vertex(
          self.api_client, response_dict
      )
    else:
      response_dict = _DeleteCachedContentResponse_from_mldev(
          self.api_client, response_dict
      )

    return_value = types.DeleteCachedContentResponse._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  async def update(
      self,
      *,
      name: str,
      config: Optional[types.UpdateCachedContentConfigOrDict] = None,
  ) -> types.CachedContent:
    """Updates cached content configurations.

    .. code-block:: python

      response = await client.aio.caches.update(
          name= ... // The server-generated resource name.
          config={
              'ttl': '7600s',
          },
      )
    """

    parameter_model = types._UpdateCachedContentParameters(
        name=name,
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _UpdateCachedContentParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    else:
      request_dict = _UpdateCachedContentParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = '{name}'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = await self.api_client.async_request(
        'patch', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _CachedContent_from_vertex(self.api_client, response_dict)
    else:
      response_dict = _CachedContent_from_mldev(self.api_client, response_dict)

    return_value = types.CachedContent._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  async def _list(
      self, *, config: Optional[types.ListCachedContentsConfigOrDict] = None
  ) -> types.ListCachedContentsResponse:
    """Lists cached content configurations.

    .. code-block:: python

      cached_contents = await client.aio.caches.list(config={'page_size': 2})
      async for cached_content in cached_contents:
        print(cached_content)
    """

    parameter_model = types._ListCachedContentsParameters(
        config=config,
    )

    if self.api_client.vertexai:
      request_dict = _ListCachedContentsParameters_to_vertex(
          self.api_client, parameter_model
      )
      path = 'cachedContents'.format_map(request_dict.get('_url'))
    else:
      request_dict = _ListCachedContentsParameters_to_mldev(
          self.api_client, parameter_model
      )
      path = 'cachedContents'.format_map(request_dict.get('_url'))
    query_params = request_dict.get('_query')
    if query_params:
      path = f'{path}?{urlencode(query_params)}'
    # TODO: remove the hack that pops config.
    config = request_dict.pop('config', None)
    http_options = config.pop('httpOptions', None) if config else None
    request_dict = _common.convert_to_dict(request_dict)
    request_dict = _common.apply_base64_encoding(request_dict)

    response_dict = await self.api_client.async_request(
        'get', path, request_dict, http_options
    )

    if self.api_client.vertexai:
      response_dict = _ListCachedContentsResponse_from_vertex(
          self.api_client, response_dict
      )
    else:
      response_dict = _ListCachedContentsResponse_from_mldev(
          self.api_client, response_dict
      )

    return_value = types.ListCachedContentsResponse._from_response(
        response_dict, parameter_model
    )
    self.api_client._verify_response(return_value)
    return return_value

  async def list(
      self, *, config: Optional[types.ListCachedContentsConfigOrDict] = None
  ) -> AsyncPager[types.CachedContent]:
    return AsyncPager(
        'cached_contents',
        self._list,
        await self._list(config=config),
        config,
    )