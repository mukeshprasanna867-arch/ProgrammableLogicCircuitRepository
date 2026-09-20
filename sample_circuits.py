"""
Sample Circuit Designs
EC2201 - Digital System Design and Microprocessor

Reusable sample circuits for the Programmable Logic
Circuit Repository.
"""

from backend.circuit import Circuit


def create_and_gate():
    """Simple AND gate."""

    return Circuit(
        name="AND_Gate",
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


def create_half_adder():
    """
    Half Adder

    Sum   = A XOR B
    Carry = A AND B
    """

    return Circuit(
        name="Half_Adder",
        inputs=["A", "B"],
        gates=[
            {
                "id": "SUM",
                "type": "XOR",
                "inputs": ["A", "B"]
            },
            {
                "id": "CARRY",
                "type": "AND",
                "inputs": ["A", "B"]
            }
        ],
        outputs=[
            {
                "name": "SUM",
                "source": "SUM"
            },
            {
                "name": "CARRY",
                "source": "CARRY"
            }
        ]
    )


def create_full_adder():
    """
    Full Adder

    Inputs:
        A, B, CIN

    Outputs:
        SUM, COUT
    """

    return Circuit(
        name="Full_Adder",
        inputs=["A", "B", "CIN"],
        gates=[
            {
                "id": "X1",
                "type": "XOR",
                "inputs": ["A", "B"]
            },
            {
                "id": "SUM",
                "type": "XOR",
                "inputs": ["X1", "CIN"]
            },
            {
                "id": "A1",
                "type": "AND",
                "inputs": ["A", "B"]
            },
            {
                "id": "A2",
                "type": "AND",
                "inputs": ["X1", "CIN"]
            },
            {
                "id": "COUT",
                "type": "OR",
                "inputs": ["A1", "A2"]
            }
        ],
        outputs=[
            {
                "name": "SUM",
                "source": "SUM"
            },
            {
                "name": "COUT",
                "source": "COUT"
            }
        ]
    )


def create_2_to_1_mux():
    """
    2:1 Multiplexer

    Inputs:
        D0, D1, S

    Output:
        OUT

    Logic:
        OUT = (D0 AND NOT S) OR (D1 AND S)
    """

    return Circuit(
        name="MUX_2_to_1",
        inputs=["D0", "D1", "S"],
        gates=[
            {
                "id": "NOT_S",
                "type": "NOT",
                "inputs": ["S"]
            },
            {
                "id": "A1",
                "type": "AND",
                "inputs": ["D0", "NOT_S"]
            },
            {
                "id": "A2",
                "type": "AND",
                "inputs": ["D1", "S"]
            },
            {
                "id": "OUT",
                "type": "OR",
                "inputs": ["A1", "A2"]
            }
        ],
        outputs=[
            {
                "name": "OUT",
                "source": "OUT"
            }
        ]
    )


def get_all_samples():
    """Return all sample circuits."""

    return [
        create_and_gate(),
        create_half_adder(),
        create_full_adder(),
        create_2_to_1_mux()
    ]


if __name__ == "__main__":

    print("=" * 60)
    print("SAMPLE CIRCUIT DESIGNS")
    print("=" * 60)

    for circuit in get_all_samples():

        print()
        print("Circuit:", circuit.name)
        print("Inputs:", circuit.inputs)
        print("Gates:", len(circuit.gates))
        print("Outputs:", circuit.outputs)

        circuit.validate_schema()

        print("Schema: VALID")

    print()
    print("=" * 60)
    print("ALL SAMPLE CIRCUITS VALID")
    print("=" * 60)