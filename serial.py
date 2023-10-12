"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Make a new serial generator, starting at start."""
        self.start = self.next = start

    def __repr__(self):
        """show representation of object"""
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
         """generates the next serial number in the sequence"""
         new_serial = self.next
         self.next += 1
         return new_serial
    
    def reset(self):
        """reset next counter to start"""
        self.next = self.start
         


