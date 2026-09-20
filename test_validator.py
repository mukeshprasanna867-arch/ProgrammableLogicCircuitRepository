from backend.circuit import Circuit
from backend.validator import TruthTableValidator


# AND gate circuit
circuit = Circuit(
    name="AND Gate",
    inputs=["A", "B"],
    gates=[
        {
            "id": "G1",
            "type": "AND",
            "inputs": ["A", "B"]
        }
    ],
    outputs=[
        {
            "name": "OUT",
            "source": "G1"
        }
    ]
)


# Expected AND truth table
expected_rows = [
    {"A": 0, "B": 0, "OUT": 0},
    {"A": 0, "B": 1, "OUT": 0},
    {"A": 1, "B": 0, "OUT": 0},
    {"A": 1, "B": 1, "OUT": 1}
]


validator = TruthTableValidator(
    circuit,
    expected_rows
)

validator.print_report()