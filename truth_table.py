"""
Truth Table Generator
EC2201 - Digital System Design and Microprocessor
"""

from itertools import product


class TruthTableGenerator:

    def __init__(self, circuit):
        self.circuit = circuit

    def generate(self):
        """
        Generate all possible input combinations
        and evaluate the circuit for each combination.
        """

        input_names = self.circuit.inputs
        rows = []

        combinations = product([0, 1], repeat=len(input_names))

        for values in combinations:

            input_values = dict(
                zip(input_names, values)
            )

            outputs, signals = self.circuit.evaluate(
                input_values
            )

            row = {}

            # Add inputs
            for name in input_names:
                row[name] = input_values[name]

            # Add outputs
            for name, value in outputs.items():
                row[name] = value

            rows.append(row)

        return rows

    def print_table(self):
        """Print the truth table in the terminal."""

        rows = self.generate()

        if not rows:
            print("No truth-table rows generated.")
            return

        columns = list(rows[0].keys())

        print()
        print("=" * 50)
        print(f"TRUTH TABLE: {self.circuit.name}")
        print("=" * 50)

        print(" | ".join(columns))

        print("-" * 50)

        for row in rows:

            values = [
                str(row[column])
                for column in columns
            ]

            print(" | ".join(values))

        print("=" * 50)

        return rows