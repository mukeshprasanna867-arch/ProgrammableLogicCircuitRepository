"""
Programmable Logic Circuit Repository
EC2201 - Digital System Design and Microprocessor

Test Runner
- 10+ normal test cases
- 5+ edge/fault test cases
- Reproducible test execution
"""

from backend.circuit import Circuit


# ============================================================
# HELPER
# ============================================================

def make_circuit(name, inputs, gates, outputs):
    return Circuit(
        name=name,
        inputs=inputs,
        gates=gates,
        outputs=outputs
    )


# ============================================================
# NORMAL TEST CASES
# ============================================================

normal_tests = [

    # 1. AND 0,0
    {
        "name": "AND - both inputs 0",
        "circuit": make_circuit(
            "AND_1",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "AND",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 0, "B": 0},
        "expected": {"OUT": 0}
    },

    # 2. AND 1,1
    {
        "name": "AND - both inputs 1",
        "circuit": make_circuit(
            "AND_2",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "AND",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 1},
        "expected": {"OUT": 1}
    },

    # 3. OR 0,1
    {
        "name": "OR - mixed inputs",
        "circuit": make_circuit(
            "OR_1",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "OR",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 0, "B": 1},
        "expected": {"OUT": 1}
    },

    # 4. OR 0,0
    {
        "name": "OR - both inputs 0",
        "circuit": make_circuit(
            "OR_2",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "OR",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 0, "B": 0},
        "expected": {"OUT": 0}
    },

    # 5. NOT 0
    {
        "name": "NOT - input 0",
        "circuit": make_circuit(
            "NOT_1",
            ["A"],
            [
                {
                    "id": "G1",
                    "type": "NOT",
                    "inputs": ["A"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 0},
        "expected": {"OUT": 1}
    },

    # 6. NOT 1
    {
        "name": "NOT - input 1",
        "circuit": make_circuit(
            "NOT_2",
            ["A"],
            [
                {
                    "id": "G1",
                    "type": "NOT",
                    "inputs": ["A"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1},
        "expected": {"OUT": 0}
    },

    # 7. NAND
    {
        "name": "NAND - both inputs 1",
        "circuit": make_circuit(
            "NAND_1",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "NAND",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 1},
        "expected": {"OUT": 0}
    },

    # 8. NOR
    {
        "name": "NOR - both inputs 0",
        "circuit": make_circuit(
            "NOR_1",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "NOR",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 0, "B": 0},
        "expected": {"OUT": 1}
    },

    # 9. XOR
    {
        "name": "XOR - different inputs",
        "circuit": make_circuit(
            "XOR_1",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "XOR",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 0},
        "expected": {"OUT": 1}
    },

    # 10. XNOR
    {
        "name": "XNOR - equal inputs",
        "circuit": make_circuit(
            "XNOR_1",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "XNOR",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 1},
        "expected": {"OUT": 1}
    },

    # 11. AND + NOT combination
    {
        "name": "Combined circuit - NOT(AND)",
        "circuit": make_circuit(
            "COMBINED_1",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "AND",
                    "inputs": ["A", "B"]
                },
                {
                    "id": "G2",
                    "type": "NOT",
                    "inputs": ["G1"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G2"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 1},
        "expected": {"OUT": 0}
    },

    # 12. OR + AND combination
    {
        "name": "Combined circuit - AND(OR)",
        "circuit": make_circuit(
            "COMBINED_2",
            ["A", "B", "C"],
            [
                {
                    "id": "G1",
                    "type": "OR",
                    "inputs": ["A", "B"]
                },
                {
                    "id": "G2",
                    "type": "AND",
                    "inputs": ["G1", "C"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G2"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 0, "C": 1},
        "expected": {"OUT": 1}
    },
]


# ============================================================
# EDGE / FAULT TEST CASES
# ============================================================

fault_tests = [

    # 1. Missing input
    {
        "name": "Missing input value",
        "circuit": make_circuit(
            "FAULT_1",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "AND",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1},
        "expected_error": "Missing input value"
    },

    # 2. Invalid digital input
    {
        "name": "Invalid input value",
        "circuit": make_circuit(
            "FAULT_2",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "AND",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 2, "B": 1},
        "expected_error": "must be 0 or 1"
    },

    # 3. Unknown signal
    {
        "name": "Unknown signal reference",
        "circuit": make_circuit(
            "FAULT_3",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "AND",
                    "inputs": ["A", "UNKNOWN"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 0},
        "expected_error": "Unknown signal"
    },

    # 4. Invalid gate type
    {
        "name": "Unsupported gate",
        "circuit": make_circuit(
            "FAULT_4",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "INVALID_GATE",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 1},
        "expected_error": "Unsupported gate"
    },

    # 5. Wrong number of inputs
    {
        "name": "Wrong gate input count",
        "circuit": make_circuit(
            "FAULT_5",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "AND",
                    "inputs": ["A"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 1},
        "expected_error": "requires exactly two inputs"
    },

    # 6. Duplicate gate ID
    {
        "name": "Duplicate gate ID",
        "circuit": make_circuit(
            "FAULT_6",
            ["A", "B"],
            [
                {
                    "id": "G1",
                    "type": "AND",
                    "inputs": ["A", "B"]
                },
                {
                    "id": "G1",
                    "type": "OR",
                    "inputs": ["A", "B"]
                }
            ],
            [
                {
                    "name": "OUT",
                    "source": "G1"
                }
            ]
        ),
        "inputs": {"A": 1, "B": 0},
        "expected_error": "Duplicate gate id"
    },
]


# ============================================================
# RUN NORMAL TESTS
# ============================================================

def run_normal_tests():
    print()
    print("=" * 70)
    print("NORMAL TEST CASES")
    print("=" * 70)

    passed = 0
    failed = 0

    for number, test in enumerate(normal_tests, start=1):

        try:
            output, signals = test["circuit"].evaluate(
                test["inputs"]
            )

            if output == test["expected"]:
                status = "PASS"
                passed += 1
            else:
                status = "FAIL"
                failed += 1

            print(
                f"Test {number:02d}: {status} - "
                f"{test['name']}"
            )

            if status == "FAIL":
                print("  Expected:", test["expected"])
                print("  Actual:  ", output)

        except Exception as error:
            failed += 1

            print(
                f"Test {number:02d}: FAIL - "
                f"{test['name']}"
            )
            print("  Unexpected error:", error)

    print("-" * 70)
    print("Normal Tests:", len(normal_tests))
    print("Passed:", passed)
    print("Failed:", failed)

    return passed, failed


# ============================================================
# RUN FAULT TESTS
# ============================================================

def run_fault_tests():
    print()
    print("=" * 70)
    print("EDGE / FAULT TEST CASES")
    print("=" * 70)

    passed = 0
    failed = 0

    for number, test in enumerate(fault_tests, start=1):

        try:
            # Explicitly validate first so schema faults
            # are caught before evaluation.
            test["circuit"].validate_schema()

            test["circuit"].evaluate(
                test["inputs"]
            )

            # If no exception occurs, fault test failed.
            failed += 1

            print(
                f"Fault {number:02d}: FAIL - "
                f"{test['name']}"
            )
            print("  Expected an error but none occurred.")

        except Exception as error:

            error_text = str(error)
            expected_text = test["expected_error"]

            if expected_text in error_text:
                passed += 1

                print(
                    f"Fault {number:02d}: PASS - "
                    f"{test['name']}"
                )
                print("  Detected:", error_text)

            else:
                failed += 1

                print(
                    f"Fault {number:02d}: FAIL - "
                    f"{test['name']}"
                )
                print("  Expected error containing:",
                      expected_text)
                print("  Actual error:", error_text)

    print("-" * 70)
    print("Fault Tests:", len(fault_tests))
    print("Passed:", passed)
    print("Failed:", failed)

    return passed, failed


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 70)
    print("PROGRAMMABLE LOGIC CIRCUIT REPOSITORY")
    print("AUTOMATED TEST RUNNER")
    print("=" * 70)

    normal_passed, normal_failed = run_normal_tests()

    fault_passed, fault_failed = run_fault_tests()

    total_tests = (
        len(normal_tests) +
        len(fault_tests)
    )

    total_passed = (
        normal_passed +
        fault_passed
    )

    total_failed = (
        normal_failed +
        fault_failed
    )

    print()
    print("=" * 70)
    print("FINAL TEST SUMMARY")
    print("=" * 70)

    print("Total Test Cases :", total_tests)
    print("Normal Cases     :", len(normal_tests))
    print("Fault Cases      :", len(fault_tests))
    print("Total Passed     :", total_passed)
    print("Total Failed     :", total_failed)

    print("-" * 70)

    if total_failed == 0:
        print("OVERALL STATUS   : ALL TESTS PASSED")
    else:
        print("OVERALL STATUS   : SOME TESTS FAILED")

    print("=" * 70)


if __name__ == "__main__":
    main()