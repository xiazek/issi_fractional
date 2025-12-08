import math
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Fractional:
    """
    Represents a rational number (fraction) with integer numerator and denominator.
    The fraction is always stored in normalized form:
    - The denominator is always positive.
    - The numerator and denominator are divided by their greatest common divisor.
    Supports arithmetic and comparison operations with other Fractional objects and integers.
    Raises ValueError if denominator is zero.
    """

    x: int
    y: int

    def __post_init__(self):
        if self.y == 0:
            raise ValueError("Denominator cannot be zero.")
        # Normalize sign
        x, y = self.x, self.y
        if y < 0:
            x = -x
            y = -y
        # skracamy ułamek dzieląc przez największy wspólny dzielnik
        gcd = math.gcd(x, y)
        object.__setattr__(self, 'x', x // gcd)
        object.__setattr__(self, 'y', y // gcd)

    def __repr__(self) -> str:
        """
        Return the developer-friendly string representation of the Fractional object.
        Example: Fractional(1, 2)
        """
        return f"Fractional({self.x}, {self.y})"

    def __str__(self):
        """
        Return the user-friendly string representation of the Fractional object.
        Example: '1/2'
        """
        return f"{self.x}/{self.y}"

    def __add__(self, other):
        """
        Add another Fractional or integer to this Fractional and return the result as a new Fractional.
        """
        if isinstance(other, Fractional):
            num = self.x * other.y + other.x * self.y
            denom = self.y * other.y
            return Fractional(num, denom)
        elif isinstance(other, int):
            return Fractional(self.x + other * self.y, self.y)
        return NotImplemented

    def __radd__(self, other):
        """
        Add this Fractional to an integer (right-hand side) and return the result as a new Fractional.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Subtract another Fractional or integer from this Fractional and return the result as a new Fractional.
        """
        if isinstance(other, Fractional):
            num = self.x * other.y - other.x * self.y
            denom = self.y * other.y
            return Fractional(num, denom)
        elif isinstance(other, int):
            return Fractional(self.x - other * self.y, self.y)
        return NotImplemented

    def __rsub__(self, other):
        """
        Subtract this Fractional from an integer (right-hand side) and return the result as a new Fractional.
        """
        if isinstance(other, int):
            return Fractional(other * self.y - self.x, self.y)
        return NotImplemented

    def __mul__(self, other):
        """
        Multiply this Fractional by another Fractional or integer and return the result as a new Fractional.
        """
        if isinstance(other, Fractional):
            return Fractional(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Fractional(self.x * other, self.y)
        return NotImplemented

    def __rmul__(self, other):
        """
        Multiply an integer by this Fractional (right-hand side) and return the result as a new Fractional.
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Divide this Fractional by another Fractional or integer and return the result as a new Fractional.
        Raises ZeroDivisionError if dividing by zero Fractional or integer.
        """
        if isinstance(other, Fractional):
            if other.x == 0:
                raise ZeroDivisionError("Cannot divide by zero Fractional.")
            return Fractional(self.x * other.y, self.y * other.x)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero integer.")
            return Fractional(self.x, self.y * other)
        return NotImplemented

    def __rtruediv__(self, other):
        """
        Divide an integer by this Fractional (right-hand side) and return the result as a new Fractional.
        Raises ZeroDivisionError if dividing by zero Fractional.
        """
        if isinstance(other, int):
            if self.x == 0:
                raise ZeroDivisionError("Cannot divide by zero Fractional.")
            return Fractional(other * self.y, self.x)
        return NotImplemented

    def __eq__(self, other):
        """
        Check if this Fractional is equal to another Fractional or integer.
        """
        if isinstance(other, Fractional):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, int):
            return self.x == other and self.y == 1
        return NotImplemented

    def __lt__(self, other):
        """
        Check if this Fractional is less than another Fractional or integer.
        """
        if isinstance(other, Fractional):
            return self.x * other.y < other.x * self.y
        elif isinstance(other, int):
            return self.x < other * self.y
        return NotImplemented

    def __le__(self, other):
        """
        Check if this Fractional is less than or equal to another Fractional or integer.
        """
        if isinstance(other, Fractional):
            return self.x * other.y <= other.x * self.y
        elif isinstance(other, int):
            return self.x <= other * self.y
        return NotImplemented

    def __gt__(self, other):
        """
        Check if this Fractional is greater than another Fractional or integer.
        """
        if isinstance(other, Fractional):
            return self.x * other.y > other.x * self.y
        elif isinstance(other, int):
            return self.x > other * self.y
        return NotImplemented

    def __ge__(self, other):
        """
        Check if this Fractional is greater than or equal to another Fractional or integer.
        """
        if isinstance(other, Fractional):
            return self.x * other.y >= other.x * self.y
        elif isinstance(other, int):
            return self.x >= other * self.y
        return NotImplemented
