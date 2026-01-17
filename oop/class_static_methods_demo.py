class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without needing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Accesses class attribute before performing multiplication."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
