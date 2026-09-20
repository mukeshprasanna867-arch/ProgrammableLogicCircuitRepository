"""
Truth Table Validator
EC2201 - Digital System Design and Microprocessor
"""

from backend.truth_table import TruthTableGenerator


class TruthTableValidator:

    def __init__(self, circuit, expected_rows):
        self.circuit = circuit
        self.expected_rows = expected_rows

    def validate(self):
        """Compare generated truth table with expected results."""

        generator = TruthTableGenerator(self.circuit)
        actual_rows = generator.generate()

        passed = 0
        failed = 0
        results = []

        if len(actual_rows) != len(self.expected_rows):
            return {
                "status": "INVALID",
                "total": len(self.expected_rows),
                "passed": 0,
                "failed": len(self.expected_rows),
                "results": [],
                "error": (
                    "Expected and generated row counts "
                    "do not match."
                )
            }

        for index, (actual, expected) in enumerate(
            zip(actual_rows, self.expected_rows),
            start=1
        ):
            is_match = actual == expected

            if is_match:
                passed += 1
            else:
                failed += 1

            results.append({
                "case": index,
                "expected": expected,
                "actual": actual,
                "passed": is_match
            })

        status = "VALID" if failed == 0 else "INVALID"

        return {
            "status": status,
            "total": len(actual_rows),
            "passed": passed,
            "failed": failed,
            "results": results
        }

    def print_report(self):
        """Print validation results."""

        report = self.validate()

        print()
        print("=" * 50)
        print("TRUTH TABLE VALIDATION")
        print("=" * 50)

        print("Circuit:", self.circuit.name)
        print("Total Cases:", report["total"])
        print("Passed:", report["passed"])
        print("Failed:", report["failed"])

        print("-" * 50)

        for result in report["results"]:
            status = "PASS" if result["passed"] else "FAIL"

            print(
                f"Case {result['case']:02d}: {status}"
            )

            if not result["passed"]:
                print(
                    "  Expected:",
                    result["expected"]
                )
                print(
                    "  Actual:",
                    result["actual"]
                )

        print("-" * 50)

        if report["status"] == "VALID":
            print("STATUS: VALID")
        else:
            print("STATUS: INVALID")

        print("=" * 50)

        return report