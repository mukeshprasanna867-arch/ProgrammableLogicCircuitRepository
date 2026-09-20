from backend.circuit import Circuit
from backend.truth_table import TruthTableGenerator


# AND circuit
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


generator = TruthTableGenerator(circuit)

rows = generator.print_table()

print()
print("Total test combinations:", len(rows))