# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
""""""
from dynamodb_encryption_sdk.internal.str_ops import to_bytes


def sorted_key_map(item, transform=to_bytes):
    """Creates a list of the item's key/value pairs as tuples, sorted by the keys transformed by transform.

    :param dict item: Source dictionary
    :param function transform: Transform function
    :returns: List of tuples containing transformed key, original value, and original key for each entry
    :rtype: list of tuples
    """
    sorted_items = []
    for key, value in item.items():
        _key = transform(key)
        sorted_items.append((_key, value, key))
    sorted_items = sorted(sorted_items, key=lambda x: x[0])
    return sorted_items