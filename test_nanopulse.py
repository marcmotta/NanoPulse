# test_nanopulse.py
"""
Tests for NanoPulse module.
"""

import unittest
from nanopulse import NanoPulse

class TestNanoPulse(unittest.TestCase):
    """Test cases for NanoPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NanoPulse()
        self.assertIsInstance(instance, NanoPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NanoPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
