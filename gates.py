"""
Programmable Logic Circuit Repository
EC2201 - Digital System Design and Microprocessor

Core digital logic gate implementation.
"""


def normalize(value):
    """Convert an input into a valid digital value: 0 or 1."""

    if value in (0, False, "0"):
        return 0

    if value in (1, True, "1"):
        return 1

    raise ValueError(
        f"Invalid digital input: {value}. Expected 0 or 1."
    )


def AND(a, b):
    return normalize(a) & normalize(b)


def OR(a, b):
    return normalize(a) | normalize(b)


def NOT(a):
    return 1 - normalize(a)


def NAND(a, b):
    return 1 - AND(a, b)


def NOR(a, b):
    return 1 - OR(a, b)


def XOR(a, b):
    return normalize(a) ^ normalize(b)


def XNOR(a, b):
    return 1 - XOR(a, b)


GATES = {
    "AND": AND,
    "OR": OR,
    "NOT": NOT,
    "NAND": NAND,
    "NOR": NOR,
    "XOR": XOR,
    "XNOR": XNOR,
}


def execute_gate(gate_name, inputs):
    """Execute a logic gate using supplied inputs."""

    gate_name = gate_name.upper()

    if gate_name not in GATES:
        raise ValueError(f"Unsupported gate: {gate_name}")

    gate = GATES[gate_name]

    if gate_name == "NOT":
        if len(inputs) != 1:
            raise ValueError("NOT gate requires exactly one input.")
    else:
        if len(inputs) != 2:
            raise ValueError(
                f"{gate_name} gate requires exactly two inputs."
            )

    return gate(*inputs)