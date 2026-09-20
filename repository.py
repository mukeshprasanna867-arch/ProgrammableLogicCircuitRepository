"""
Circuit Repository

Handles saving and loading circuit designs
using JSON files.
"""

import json
from pathlib import Path

from backend.circuit import Circuit


class CircuitRepository:

    def __init__(self, directory="data/circuits"):
        self.directory = Path(directory)
        self.directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, circuit):
        """Save a circuit as a JSON file."""

        circuit.validate_schema()

        file_path = self.directory / f"{circuit.name}.json"

        data = {
            "name": circuit.name,
            "inputs": circuit.inputs,
            "gates": circuit.gates,
            "outputs": circuit.outputs
        }

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                indent=4
            )

        return file_path

    def load(self, name):
        """Load a circuit from JSON."""

        file_path = self.directory / f"{name}.json"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Circuit '{name}' was not found."
            )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        circuit = Circuit(
            name=data["name"],
            inputs=data["inputs"],
            gates=data["gates"],
            outputs=data["outputs"]
        )

        circuit.validate_schema()

        return circuit

    def list_circuits(self):
        """Return all saved circuit names."""

        return sorted(
            path.stem
            for path in self.directory.glob("*.json")
        )