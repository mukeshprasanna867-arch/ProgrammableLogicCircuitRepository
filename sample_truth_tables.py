"""
Sample Circuit Truth Tables
EC2201 - Digital System Design and Microprocessor
"""

from backend.sample_circuits import (
    create_half_adder,
    create_full_adder,
    create_2_to_1_mux
)

from backend.truth_table import TruthTableGenerator


def show_truth_table(circuit):
    print()
    print("=" * 60)
    print(f"TRUTH TABLE: {circuit.name}")
    print("=" * 60)

    generator = TruthTableGenerator(circuit)
    rows = generator.generate()

    columns = list(rows[0].keys())

    print(" | ".join(columns))
    print("-" * 60)

    for row in rows:
        print(
            " | ".join(
                str(row[column])
                for column in columns
            )
        )

    print("-" * 60)
    print("Total combinations:", len(rows))


def main():

    print("=" * 60)
    print("SAMPLE CIRCUIT TRUTH TABLE VERIFICATION")
    print("=" * 60)

    circuits = [
        create_half_adder(),
        create_full_adder(),
        create_2_to_1_mux()
    ]

    for circuit in circuits:
        show_truth_table(circuit)

    print()
    print("=" * 60)
    print("TRUTH TABLE GENERATION COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()