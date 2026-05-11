# test_objectpool.py
"""
Tests for ObjectPool module.
"""

import unittest
from objectpool import ObjectPool

class TestObjectPool(unittest.TestCase):
    """Test cases for ObjectPool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ObjectPool()
        self.assertIsInstance(instance, ObjectPool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ObjectPool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
