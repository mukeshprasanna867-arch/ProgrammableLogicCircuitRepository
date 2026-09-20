from backend.circuit import Circuit
from backend.repository import CircuitRepository


# Create an AND circuit
circuit = Circuit(
    name="and_demo",
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


print("=" * 50)
print("PROGRAMMABLE LOGIC CIRCUIT REPOSITORY")
print("=" * 50)

# Test 1
output, signals = circuit.evaluate({
    "A": 1,
    "B": 1
})

print("Circuit:", circuit.name)
print("Inputs:", {"A": 1, "B": 1})
print("Intermediate Signals:", signals)
print("Output:", output)


# Save
repository = CircuitRepository()

saved_path = repository.save(circuit)

print("Saved to:", saved_path)


# Load
loaded = repository.load("and_demo")

print("Loaded circuit:", loaded.name)


# Test loaded circuit
loaded_output, loaded_signals = loaded.evaluate({
    "A": 1,
    "B": 0
})

print("Loaded Inputs:", {"A": 1, "B": 0})
print("Loaded Signals:", loaded_signals)
print("Loaded Output:", loaded_output)

print("Available circuits:", repository.list_circuits())

print("=" * 50)
print("CIRCUIT TEST COMPLETED")
print("=" * 50)