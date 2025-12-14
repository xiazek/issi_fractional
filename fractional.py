import math
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Fractional:
    """
    Represents a rational number (fraction) with integer numerator and denominator.
    The fraction is always stored in normalized form:
    - The denominator is always positive.
    - The numerator and denominator are divided by their greatest common divisor.
    - Original values before normalization are stored in original_x and original_y.

    Args:
        x: Numerator of the fraction
        y: Denominator of the fraction
        normalize_original: If True, applies GCD normalization to original values. Default is False.

    Supports arithmetic and comparison operations with other Fractional objects and integers.
    Raises ValueError if denominator is zero.
    """

    x: int
    y: int
    normalize_original: bool = False
    original_x: int = field(init=False)
    original_y: int = field(init=False)

    def __post_init__(self):
        if self.y == 0:
            raise ValueError("Denominator cannot be zero.")
        # Move any minus sign from denominator to numerator
        x, y = self.x, self.y
        if y < 0:
            x = -x
            y = -y
        # Keep originals for string representation by default
        orig_x, orig_y = x, y
        # Always normalize internal representation for math/repr/comparisons
        norm_x, norm_y = self._find_gcd(x, y)
        # If requested, also normalize the "original" pair so str() shows reduced form
        if self.normalize_original:
            orig_x, orig_y = norm_x, norm_y
        # Set attributes
        object.__setattr__(self, 'original_x', orig_x)
        object.__setattr__(self, 'original_y', orig_y)
        object.__setattr__(self, 'x', norm_x)
        object.__setattr__(self, 'y', norm_y)

    @staticmethod
    def _find_gcd(x: int, y: int) -> tuple[int, int]:
        """
        Apply GCD normalization to x and y.

        Args:
            x: Numerator
            y: Denominator

        Returns:
            A tuple of (x // gcd, y // gcd)

        Example:
            _find_gcd(6, 8) returns (3, 4)
        """
        gcd = math.gcd(x, y)
        return x // gcd, y // gcd

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
        return f"{self.original_x}/{self.original_y}"

    def __add__(self, other):
        """
        Add another Fractional or integer to this Fractional and return the result as a new normalized Fractional.
        The result will be in reduced form (GCD applied to both internal and display values).
        """
        if isinstance(other, Fractional):
            num = self.x * other.y + other.x * self.y
            denom = self.y * other.y
            return Fractional(num, denom, normalize_original=True)
        elif isinstance(other, int):
            return Fractional(self.x + other * self.y, self.y, normalize_original=True)
        return NotImplemented

    def __radd__(self, other):
        """
        Add this Fractional to an integer (right-hand side) and return the result as a new normalized Fractional.
        The result will be in reduced form (GCD applied to both internal and display values).
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Subtract another Fractional or integer from this Fractional and return the result as a new normalized Fractional.
        The result will be in reduced form (GCD applied to both internal and display values).
        """
        if isinstance(other, Fractional):
            num = self.x * other.y - other.x * self.y
            denom = self.y * other.y
            return Fractional(num, denom, normalize_original=True)
        elif isinstance(other, int):
            return Fractional(self.x - other * self.y, self.y, normalize_original=True)
        return NotImplemented

    def __rsub__(self, other):
        """
        Subtract this Fractional from an integer (right-hand side) and return the result as a new Fractional.
        Note: Unlike other operations, the result's display form is not normalized.
        """
        if isinstance(other, int):
            return Fractional(other * self.y - self.x, self.y)
        return NotImplemented

    def __mul__(self, other):
        """
        Multiply this Fractional by another Fractional or integer and return the result as a new normalized Fractional.
        The result will be in reduced form (GCD applied to both internal and display values).
        """
        if isinstance(other, Fractional):
            return Fractional(self.x * other.x, self.y * other.y, normalize_original=True)
        elif isinstance(other, int):
            return Fractional(self.x * other, self.y, normalize_original=True)
        return NotImplemented

    def __rmul__(self, other):
        """
        Multiply an integer by this Fractional (right-hand side) and return the result as a new normalized Fractional.
        The result will be in reduced form (GCD applied to both internal and display values).
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Divide this Fractional by another Fractional or integer and return the result as a new normalized Fractional.
        The result will be in reduced form (GCD applied to both internal and display values).
        Raises ZeroDivisionError if dividing by zero Fractional or integer.
        """
        if isinstance(other, Fractional):
            if other.x == 0:
                raise ZeroDivisionError("Cannot divide by zero Fractional.")
            return Fractional(self.x * other.y, self.y * other.x, normalize_original=True)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero integer.")
            return Fractional(self.x, self.y * other, normalize_original=True)
        return NotImplemented

    def __rtruediv__(self, other):
        """
        Divide an integer by this Fractional (right-hand side) and return the result as a new Fractional.
        Note: Unlike other operations, the result's display form is not normalized.
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

    def __hash__(self) -> int:
        if self.y == 1:
            return hash(self.x)         # to be consistent with int equality
        return hash((self.x, self.y))