# test_diskutility.py
"""
Tests for DiskUtility module.
"""

import unittest
from diskutility import DiskUtility

class TestDiskUtility(unittest.TestCase):
    """Test cases for DiskUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DiskUtility()
        self.assertIsInstance(instance, DiskUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DiskUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
