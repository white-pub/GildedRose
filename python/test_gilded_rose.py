"""
test_gilded_rose.py
A. Chen
Updated: 2025-03-20

Has unit tests.
"""

# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    
    # make sure the update method don't change item.name
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item(self):
        items = [Item("+5 Dexterity Vest", 10, 5), Item("bread", 8, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

        self.assertEqual(7, items[1].sell_in)
        self.assertEqual(1, items[1].quality)    

    def test_normal_item_pass_sell_day(self):
        items = [Item("+5 Dexterity Vest", 0, 5), Item("bread", -3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(3, items[0].quality)      

        self.assertEqual(-4, items[1].sell_in)
        self.assertEqual(4, items[1].quality)
    
    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 24, 30), 
                 Item("Backstage passes to a TAFKAL80ETC concert", 10, 30),
                 Item("Backstage passes to a TAFKAL80ETC concert", 4, 30),
                 Item("Backstage passes to a TAFKAL80ETC concert", 0, 30),
                 Item("Backstage passes to a TAFKAL80ETC concert", -2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].sell_in)
        self.assertEqual(31, items[0].quality)

        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(32, items[1].quality)

        self.assertEqual(3, items[2].sell_in)
        self.assertEqual(33, items[2].quality)

        self.assertEqual(-1, items[3].sell_in)
        self.assertEqual(0, items[3].quality)        
        
        self.assertEqual(-3, items[4].sell_in)
        self.assertEqual(0, items[4].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 24, 30), 
                 Item("Aged Brie", -3, 30),
                 Item("Aged Brie", 24, 49),
                 Item("Aged Brie", 24, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].sell_in)
        self.assertEqual(31, items[0].quality)

        self.assertEqual(-4, items[1].sell_in)
        self.assertEqual(31, items[1].quality)

        self.assertEqual(23, items[2].sell_in)
        self.assertEqual(50, items[2].quality)

        self.assertEqual(23, items[3].sell_in)
        self.assertEqual(50, items[3].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 24, 80), 
                 Item("Sulfuras, Hand of Ragnaros", 1, 80),
                 Item("Sulfuras, Hand of Ragnaros", 0, 80),
                 Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(24, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

        self.assertEqual(1, items[1].sell_in)
        self.assertEqual(80, items[1].quality)

        self.assertEqual(0, items[2].sell_in)
        self.assertEqual(80, items[2].quality)

        self.assertEqual(-1, items[3].sell_in)
        self.assertEqual(80, items[3].quality)

    def test_conjured(self):
        items = [Item("Conjured Mana Cake", 24, 50), 
                 Item("Conjured Mana Cake", 1, 20),
                 Item("Conjured Mana Cake", 0, 20),
                 Item("Conjured Mana Cake", -1, 20),
                 Item("Conjured Mana Cake", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].sell_in)
        self.assertEqual(48, items[0].quality)

        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(18, items[1].quality)

        self.assertEqual(-1, items[2].sell_in)
        self.assertEqual(16, items[2].quality)

        self.assertEqual(-2, items[3].sell_in)
        self.assertEqual(16, items[3].quality)
        
        self.assertEqual(-2, items[4].sell_in)
        self.assertEqual(0, items[4].quality)
        
if __name__ == '__main__':
    unittest.main()
