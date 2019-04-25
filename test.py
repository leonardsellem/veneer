from script import *
import unittest

#INSTANCES
#Marketplaces
veneer = Marketplace()

#Clients
edytta = Client('Edytta Halpirt', 'Private Collection', False, 1000000)
moma = Client('The MOMA', 'New York', True,10000000)

#Artworks
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

#TESTS
class TestListing(unittest.TestCase):
    def test_new_listing(self):
        test_listing = Listing(girl_with_mandolin, 1000000, edytta, veneer)
        self.assertEqual(test_listing.art, girl_with_mandolin)
    def test_add_listing(self):
        test_listing = Listing(girl_with_mandolin, 1000000, edytta, veneer)
        veneer.add_listing(test_listing)
        self.assertIn(test_listing, veneer.listings)
        veneer.remove_listing(test_listing)
    def test_remove_listing(self):
        test_listing = Listing(girl_with_mandolin, 1000000, edytta, veneer)
        veneer.add_listing(test_listing)
        veneer.remove_listing(test_listing)
        self.assertNotIn(test_listing, veneer.listings)

class TestTransaction(unittest.TestCase):
    def test_change_ownership(self):
        edytta.sell_artwork(girl_with_mandolin, 6000000, veneer)
        moma.buy_artwork(girl_with_mandolin, veneer)
        self.assertEqual(girl_with_mandolin.owner,moma)
        moma.sell_artwork(girl_with_mandolin, 6000000, veneer)
        edytta.buy_artwork(girl_with_mandolin, veneer)
    def test_money_transferred(self):
        edytta.sell_artwork(girl_with_mandolin, 6000000, veneer)
        moma.buy_artwork(girl_with_mandolin, veneer)
        self.assertEqual(edytta.wallet,7000000)
        self.assertEqual(moma.wallet,4000000)
        moma.sell_artwork(girl_with_mandolin, 6000000, veneer)
        edytta.buy_artwork(girl_with_mandolin, veneer)

if __name__ == '__main__':
    unittest.main()