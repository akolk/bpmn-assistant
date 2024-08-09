from bpmn_assistant.services import BpmnJsonGenerator


class TestBpmnJsonGenerator:

    def test_create_bpmn_json_linear_process(self, bpmn_xml_linear_process):

        bpmn_json_generator = BpmnJsonGenerator()

        result = bpmn_json_generator.create_bpmn_json(bpmn_xml_linear_process)

        expected = [
            {
                "type": "startEvent",
                "id": "StartEvent_1",
            },
            {
                "type": "task",
                "id": "Activity_0o5d60h",
                "label": "Task 1",
            },
            {
                "type": "task",
                "id": "Activity_01dwvnb",
                "label": "Task 2",
            },
            {"type": "endEvent", "id": "Event_0htbpx6"},
        ]

        assert result == expected

    def test_create_bpmn_json_exclusive_gateway(self, bpmn_xml_exclusive_gateway):

        bpmn_json_generator = BpmnJsonGenerator()

        result = bpmn_json_generator.create_bpmn_json(bpmn_xml_exclusive_gateway)

        expected = [
            {"type": "startEvent", "id": "StartEvent_1"},
            {
                "type": "exclusiveGateway",
                "id": "Gateway_0zyhktn",
                "label": "Decision",
                "has_join": False,
                "branches": [
                    {
                        "condition": "Yes",
                        "path": [
                            {
                                "type": "task",
                                "id": "Activity_0s9i4gj",
                                "label": "Task 1",
                            }
                        ],
                    },
                    {
                        "condition": "No",
                        "path": [
                            {
                                "type": "task",
                                "id": "Activity_0bbgeui",
                                "label": "Task 2",
                            }
                        ],
                    },
                ],
            },
            {"type": "endEvent", "id": "Event_0pht86l"},
        ]

        assert result == expected

    def test_create_bpmn_json_exclusive_gateway_join(
        self, bpmn_xml_exclusive_gateway_join
    ):

        bpmn_json_generator = BpmnJsonGenerator()

        result = bpmn_json_generator.create_bpmn_json(bpmn_xml_exclusive_gateway_join)

        expected = [
            {"type": "startEvent", "id": "Event_18zhj8z"},
            {
                "type": "exclusiveGateway",
                "id": "Gateway_0zyhktn",
                "label": "Decision",
                "has_join": True,
                "branches": [
                    {
                        "condition": "Yes",
                        "path": [
                            {
                                "type": "task",
                                "id": "Activity_0s9i4gj",
                                "label": "Task 1",
                            }
                        ],
                    },
                    {
                        "condition": "No",
                        "path": [
                            {
                                "type": "task",
                                "id": "Activity_0bbgeui",
                                "label": "Task 2",
                            }
                        ],
                    },
                ],
            },
            {"type": "endEvent", "id": "Event_0pht86l"},
        ]

        assert result == expected

    def test_create_bpmn_json_nested_exclusive_gateway(
        self, bpmn_xml_nested_exclusive_gateway
    ):

        bpmn_json_generator = BpmnJsonGenerator()

        result = bpmn_json_generator.create_bpmn_json(bpmn_xml_nested_exclusive_gateway)

        expected = [
            {"type": "startEvent", "id": "Event_0otoryk"},
            {
                "type": "exclusiveGateway",
                "id": "Gateway_0zyhktn",
                "label": "Decision 1",
                "has_join": False,
                "branches": [
                    {
                        "condition": "Yes 1",
                        "path": [
                            {
                                "type": "task",
                                "id": "Activity_0s9i4gj",
                                "label": "Task 1",
                            },
                            {
                                "type": "exclusiveGateway",
                                "id": "Gateway_1wtifva",
                                "label": "Decision 2",
                                "has_join": False,
                                "branches": [
                                    {
                                        "condition": "Yes 2",
                                        "path": [
                                            {
                                                "type": "task",
                                                "id": "Activity_0jz7afz",
                                                "label": "Task 3",
                                            }
                                        ],
                                    },
                                    {
                                        "condition": "No 2",
                                        "path": [
                                            {
                                                "type": "task",
                                                "id": "Activity_0u109f4",
                                                "label": "Task 4",
                                            }
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "condition": "No 1",
                        "path": [
                            {
                                "type": "task",
                                "id": "Activity_0bbgeui",
                                "label": "Task 2",
                            }
                        ],
                    },
                ],
            },
            {"type": "endEvent", "id": "Event_13rn7yc"},
        ]

        assert result == expected

    def test_create_bpmn_json_parallel_gateway(self, bpmn_xml_parallel_gateway):

        bpmn_json_generator = BpmnJsonGenerator()

        result = bpmn_json_generator.create_bpmn_json(bpmn_xml_parallel_gateway)

        expected = [
            {"type": "startEvent", "id": "StartEvent_1"},
            {
                "type": "parallelGateway",
                "id": "Gateway_02p5qhx",
                "branches": [
                    [
                        {
                            "type": "task",
                            "id": "Activity_0xtw59y",
                            "label": "Task 1",
                        }
                    ],
                    [
                        {
                            "type": "task",
                            "id": "Activity_1pcsm18",
                            "label": "Task 2",
                        }
                    ],
                ],
            },
            {"type": "endEvent", "id": "Event_13alrua"},
        ]

        assert result == expected

    def test_create_bpmn_json_pg_inside_eg(self, bpmn_xml_pg_inside_eg):

        bpmn_json_generator = BpmnJsonGenerator()

        result = bpmn_json_generator.create_bpmn_json(bpmn_xml_pg_inside_eg)

        expected = [
            {"type": "startEvent", "id": "StartEvent_1"},
            {
                "type": "exclusiveGateway",
                "id": "Gateway_01vw8ri",
                "label": "What shall I do today",
                "has_join": True,
                "branches": [
                    {
                        "condition": "Focus",
                        "path": [
                            {
                                "type": "task",
                                "id": "Activity_0up0fuz",
                                "label": "Do one thing",
                            }
                        ],
                    },
                    {
                        "condition": "Multitask",
                        "path": [
                            {
                                "type": "parallelGateway",
                                "id": "Gateway_10rxkr7",
                                "branches": [
                                    [
                                        {
                                            "type": "task",
                                            "id": "Activity_0uje8a9",
                                            "label": "Do the first thing",
                                        }
                                    ],
                                    [
                                        {
                                            "type": "task",
                                            "id": "Activity_09r4jdn",
                                            "label": "Do the second thing",
                                        }
                                    ],
                                ],
                            }
                        ],
                    },
                ],
            },
            {"type": "endEvent", "id": "Event_09mvj7a"},
        ]

        assert result == expected

    def test_create_bpmn_json_eg_inside_pg(self, bpmn_xml_eg_inside_pg):
        bpmn_json_generator = BpmnJsonGenerator()

        result = bpmn_json_generator.create_bpmn_json(bpmn_xml_eg_inside_pg)

        expected = [
            {"type": "startEvent", "id": "StartEvent_1"},
            {
                "type": "parallelGateway",
                "id": "Gateway_1eyobl0",
                "branches": [
                    [
                        {
                            "type": "task",
                            "id": "Activity_1oirso2",
                            "label": "Task 1",
                        }
                    ],
                    [
                        {
                            "type": "exclusiveGateway",
                            "id": "Gateway_1yv434l",
                            "label": "Decision",
                            "has_join": True,
                            "branches": [
                                {
                                    "condition": "Yes",
                                    "path": [
                                        {
                                            "type": "task",
                                            "id": "Activity_0xtreye",
                                            "label": "Task 2",
                                        }
                                    ],
                                },
                                {
                                    "condition": "No",
                                    "path": [
                                        {
                                            "type": "task",
                                            "id": "Activity_01s7h04",
                                            "label": "Task 3",
                                        }
                                    ],
                                },
                            ],
                        }
                    ],
                ],
            },
            {"type": "endEvent", "id": "Event_1nctra5"},
        ]

        assert result == expected

    def test_create_bpmn_json_eg_next(self, bpmn_xml_eg_next):
        bpmn_json_generator = BpmnJsonGenerator()

        result = bpmn_json_generator.create_bpmn_json(bpmn_xml_eg_next)

        expected = [
            {"type": "startEvent", "id": "StartEvent_1"},
            {
                "type": "task",
                "id": "Activity_1seg49t",
                "label": "Enter exam room",
            },
            {
                "type": "task",
                "id": "Activity_0nhhj6o",
                "label": "Take test",
            },
            {
                "type": "exclusiveGateway",
                "id": "Gateway_0zyhktn",
                "label": "Score more than 50%?",
                "has_join": False,
                "branches": [
                    {
                        "condition": "Yes",
                        "path": [
                            {
                                "type": "task",
                                "id": "Activity_0s9i4gj",
                                "label": "Enter grade",
                            },
                            {"type": "endEvent", "id": "Event_10cwi32"},
                        ],
                    },
                    {"condition": "No", "path": [], "next": "Activity_1seg49t"},
                ],
            },
        ]

        assert result == expected
