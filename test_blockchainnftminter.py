# test_blockchainnftminter.py
"""
Tests for BlockchainNFTMinter module.
"""

import unittest
from blockchainnftminter import BlockchainNFTMinter

class TestBlockchainNFTMinter(unittest.TestCase):
    """Test cases for BlockchainNFTMinter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNFTMinter()
        self.assertIsInstance(instance, BlockchainNFTMinter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNFTMinter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
