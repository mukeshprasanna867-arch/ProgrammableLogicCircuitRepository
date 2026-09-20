"""
Circuit Simulator
EC2201 - Digital System Design and Microprocessor

Provides detailed circuit simulation with:
- Input states
- Intermediate gate states
- Final outputs
"""

from backend.circuit import Circuit


class CircuitSimulator:

    def __init__(self, circuit):
        if not isinstance(circuit, Circuit):
            raise TypeError("circuit must be a Circuit object.")

        self.circuit = circuit

    def simulate(self, input_values):
        """
        Simulate the complete circuit and return
        inputs, intermediate states and outputs.
        """

        outputs, signals = self.circuit.evaluate(
            input_values
        )

        intermediate = {}

        for gate in self.circuit.gates:
            gate_id = gate["id"]

            if gate_id in signals:
                intermediate[gate_id] = signals[gate_id]

        return {
            "circuit": self.circuit.name,
            "inputs": input_values,
            "intermediate": intermediate,
            "outputs": outputs
        }

    def print_simulation(self, input_values):
        """Print a detailed simulation report."""

        result = self.simulate(input_values)

        print()
        print("=" * 60)
        print("CIRCUIT SIMULATION")
        print("=" * 60)

        print("Circuit:", result["circuit"])

        print()
        print("INPUT STATES")
        print("-" * 60)

        for name, value in result["inputs"].items():
            print(f"{name:10} = {value}")

        print()
        print("INTERMEDIATE GATE STATES")
        print("-" * 60)

        for gate_id, value in result["intermediate"].items():
            print(f"{gate_id:10} = {value}")

        print()
        print("FINAL OUTPUTS")
        print("-" * 60)

        for name, value in result["outputs"].items():
            print(f"{name:10} = {value}")

        print()
        print("=" * 60)
        print("SIMULATION COMPLETED")
        print("=" * 60)

        return result


if __name__ == "__main__":

    from backend.sample_circuits import create_full_adder

    circuit = create_full_adder()

    simulator = CircuitSimulator(circuit)

    simulator.print_simulation({
        "A": 1,
        "B": 0,
        "CIN": 1
    })