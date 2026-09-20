"""
Programmable Logic Circuit Repository
EC2201 - Digital System Design and Microprocessor

Circuit schema and circuit evaluation.
"""

from backend.gates import execute_gate


class Circuit:
    def __init__(self, name, inputs, gates, outputs):
        self.name = name
        self.inputs = inputs
        self.gates = gates
        self.outputs = outputs

    def validate_schema(self):
        """Validate the basic circuit structure."""

        if not self.name:
            raise ValueError("Circuit name cannot be empty.")

        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list.")

        if not isinstance(self.gates, list):
            raise ValueError("Gates must be a list.")

        if not isinstance(self.outputs, list):
            raise ValueError("Outputs must be a list.")

        input_names = set(self.inputs)

        if len(input_names) != len(self.inputs):
            raise ValueError("Duplicate input names found.")

        gate_ids = set()

        for gate in self.gates:
            if "id" not in gate:
                raise ValueError("Every gate must have an id.")

            if "type" not in gate:
                raise ValueError(
                    f"Gate {gate['id']} is missing type."
                )

            if gate["id"] in gate_ids:
                raise ValueError(
                    f"Duplicate gate id: {gate['id']}"
                )

            gate_ids.add(gate["id"])

        return True

    def evaluate(self, input_values):
        """
        Evaluate the circuit using supplied input values.

        Example:
            {"A": 1, "B": 0}
        """

        self.validate_schema()

        # Validate inputs
        for input_name in self.inputs:
            if input_name not in input_values:
                raise ValueError(
                    f"Missing input value: {input_name}"
                )

            if input_values[input_name] not in (0, 1):
                raise ValueError(
                    f"Input {input_name} must be 0 or 1."
                )

        signals = dict(input_values)

        # Evaluate gates in declared order
        for gate in self.gates:
            gate_id = gate["id"]
            gate_type = gate["type"]
            gate_inputs = gate["inputs"]

            resolved_inputs = []

            for source in gate_inputs:
                if source not in signals:
                    raise ValueError(
                        f"Unknown signal '{source}' "
                        f"used by gate '{gate_id}'."
                    )

                resolved_inputs.append(signals[source])

            result = execute_gate(
                gate_type,
                resolved_inputs
            )

            signals[gate_id] = result

        # Generate outputs
        result = {}

        for output in self.outputs:
            output_name = output["name"]
            source = output["source"]

            if source not in signals:
                raise ValueError(
                    f"Unknown output source: {source}"
                )

            result[output_name] = signals[source]

        return result, signals