# Programmable Logic Circuit Repository

## EC2201 – Digital System Design and Microprocessor

### Unit IV – Memory and Programmable Logic Devices

**Project Level:** Intermediate

---

## 1. Project Overview

Programmable Logic Circuit Repository is a software-based digital logic
simulation and repository system.

The system allows users to define, store, load, simulate and validate
programmable digital logic circuits.

The project demonstrates digital-system concepts using a reproducible
software model and synthetic circuit data.

---

## 2. Problem Statement

Digital logic circuits are commonly designed and tested using individual
tools. A repository-based system can provide a structured way to store
circuit definitions and verify their behavior.

This project provides a software solution where digital circuits can be:

- Defined using a standard circuit schema
- Stored as JSON designs
- Loaded from the repository
- Simulated using binary inputs
- Evaluated gate by gate
- Displayed using visual logic-gate diagrams
- Verified using truth tables
- Tested using normal and fault test cases

---

## 3. Objectives

The main objectives are:

1. Define a reusable circuit schema.
2. Implement standard digital logic gates.
3. Implement circuit evaluation.
4. Store circuit designs using JSON.
5. Load saved circuit designs.
6. Generate truth tables.
7. Validate circuit outputs.
8. Simulate circuits visually.
9. Display intermediate gate states.
10. Test normal and fault conditions.

---

## 4. Supported Logic Gates

The system supports seven standard logic gates:

- AND
- OR
- NOT
- NAND
- NOR
- XOR
- XNOR

---

## 5. Circuit Schema

Each circuit contains:

```text
Circuit
├── name
├── inputs
├── gates
└── outputs