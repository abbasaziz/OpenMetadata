#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Test we map correctly struct columns for BQ
"""

from metadata.generated.schema.entity.data.table import Column
from metadata.profiler.orm.converter import _TYPE_MAP
from metadata.profiler.source.bigquery.type_mapper import bigquery_type_mapper


def test_map_struct():
    column = Column.parse_obj(
        {
            "name": "col",
            "dataType": "STRUCT",
            "children": [
                {
                    "name": "col1",
                    "dataType": "STRING",
                    "children": [],
                },
                {
                    "name": "col2",
                    "dataType": "STRUCT",
                    "children": [
                        {
                            "name": "col3",
                            "dataType": "STRING",
                            "children": [],
                        },
                        {
                            "name": "col4",
                            "dataType": "STRUCT",
                            "children": [
                                {
                                    "name": "col5",
                                    "dataType": "ARRAY",
                                    "arrayDataType": "STRING",
                                    "children": [],
                                }
                            ],
                        },
                    ],
                },
            ],
        }
    )

    type_ = bigquery_type_mapper(_TYPE_MAP, column)
    assert (
        type_.__repr__()
        == "STRUCT(col1=String(), col2=STRUCT(col3=String(), col4=STRUCT(col5=CustomArray(<DataType.STRING: 'STRING'>))))"
    )
