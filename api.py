"""
Programmable Logic Circuit Repository
EC2201 - Digital System Design and Microprocessor

FastAPI Web API
"""

from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.circuit import Circuit
from backend.repository import CircuitRepository
from backend.truth_table import TruthTableGenerator
from backend.simulator import CircuitSimulator

from backend.sample_circuits import (
    create_and_gate,
    create_half_adder,
    create_full_adder,
    create_2_to_1_mux
)


# ============================================================
# APPLICATION
# ============================================================

app = FastAPI(
    title="Programmable Logic Circuit Repository",
    description=(
        "EC2201 Digital System Design and Microprocessor "
        "Circuit Repository and Simulator"
    ),
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ============================================================
# STATIC FRONTEND MOUNT
# ============================================================

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

if FRONTEND_DIR.exists():
    app.mount("/app", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")


# ============================================================
# REPOSITORY
# ============================================================

repository = CircuitRepository()


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "project": "Programmable Logic Circuit Repository",
        "course": "EC2201 - Digital System Design and Microprocessor",
        "status": "running",
        "version": "1.0.0"
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/api/health")
def health():

    return {
        "status": "healthy",
        "service": "Programmable Logic Circuit Repository"
    }


# ============================================================
# LIST CIRCUITS
# ============================================================

@app.get("/api/circuits")
def list_circuits():

    return {
        "circuits": repository.list_circuits()
    }


# ============================================================
# SAVE CIRCUIT
# ============================================================

@app.post("/api/circuits")
def save_circuit(data: dict):

    try:

        circuit = Circuit(
            name=data["name"],
            inputs=data["inputs"],
            gates=data["gates"],
            outputs=data["outputs"]
        )

        circuit.validate_schema()

        path = repository.save(circuit)

        return {
            "status": "saved",
            "name": circuit.name,
            "path": str(path)
        }

    except KeyError as error:

        raise HTTPException(
            status_code=400,
            detail=f"Missing field: {error}"
        )

    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# ============================================================
# LOAD CIRCUIT
# ============================================================

@app.get("/api/circuits/{name}")
def load_circuit(name: str):

    try:

        circuit = repository.load(name)

        return {
            "name": circuit.name,
            "inputs": circuit.inputs,
            "gates": circuit.gates,
            "outputs": circuit.outputs
        }

    except FileNotFoundError:

        raise HTTPException(
            status_code=404,
            detail=f"Circuit '{name}' not found."
        )


# ============================================================
# SIMULATE CIRCUIT
# ============================================================

@app.post("/api/simulate")
def simulate(data: dict):

    try:

        circuit_data = data["circuit"]
        input_values = data["inputs"]

        circuit = Circuit(
            name=circuit_data["name"],
            inputs=circuit_data["inputs"],
            gates=circuit_data["gates"],
            outputs=circuit_data["outputs"]
        )

        simulator = CircuitSimulator(circuit)

        return simulator.simulate(input_values)

    except KeyError as error:

        raise HTTPException(
            status_code=400,
            detail=f"Missing field: {error}"
        )

    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# ============================================================
# TRUTH TABLE
# ============================================================

@app.post("/api/truth-table")
def truth_table(data: dict):

    try:

        circuit_data = data["circuit"]

        circuit = Circuit(
            name=circuit_data["name"],
            inputs=circuit_data["inputs"],
            gates=circuit_data["gates"],
            outputs=circuit_data["outputs"]
        )

        generator = TruthTableGenerator(circuit)

        rows = generator.generate()

        return {
            "circuit": circuit.name,
            "inputs": circuit.inputs,
            "rows": rows,
            "total_combinations": len(rows)
        }

    except KeyError as error:

        raise HTTPException(
            status_code=400,
            detail=f"Missing field: {error}"
        )

    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# ============================================================
# SAMPLE CIRCUITS
# ============================================================

@app.get("/api/samples")
def sample_circuits():

    circuits = [
        create_and_gate(),
        create_half_adder(),
        create_full_adder(),
        create_2_to_1_mux()
    ]

    result = []

    for circuit in circuits:

        result.append({
            "name": circuit.name,
            "inputs": circuit.inputs,
            "gates": circuit.gates,
            "outputs": circuit.outputs
        })

    return {
        "samples": result
    }


# ============================================================
# SAVE ALL SAMPLE CIRCUITS
# ============================================================

@app.post("/api/samples/save")
def save_sample_circuits():

    circuits = [
        create_and_gate(),
        create_half_adder(),
        create_full_adder(),
        create_2_to_1_mux()
    ]

    saved = []

    for circuit in circuits:

        path = repository.save(circuit)

        saved.append({
            "name": circuit.name,
            "path": str(path)
        })

    return {
        "status": "saved",
        "count": len(saved),
        "circuits": saved
    }


# ============================================================
# PROJECT STATUS
# ============================================================

@app.get("/api/status")
def project_status():

    return {
        "project": "Programmable Logic Circuit Repository",
        "version": "1.0.0",
        "logic_gates": [
            "AND",
            "OR",
            "NOT",
            "NAND",
            "NOR",
            "XOR",
            "XNOR"
        ],
        "features": [
            "Circuit Schema",
            "Circuit Evaluation",
            "Save and Load",
            "Truth Table Generation",
            "Truth Table Validation",
            "Circuit Simulation",
            "Intermediate State Tracking",
            "Sample Circuit Designs",
            "Automated Test Cases"
        ],
        "sample_circuits": [
            "AND Gate",
            "Half Adder",
            "Full Adder",
            "2:1 Multiplexer"
        ]
    }