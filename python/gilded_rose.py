"""
gilded_rose.py
A. Chen
Updated: 2025-03-20

Has GildedRose class and Item class
"""

# -*- coding: utf-8 -*-

class GildedRose(object):
    NORMAL_QUALITY_DECREASE = 1


    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            
            # items that just decrease by value everyday, no special rules
            is_normal_item = True

            # Sulfuras is never changed
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # decrease/increase quality
            if item.name == "Aged Brie":
                is_normal_item = False
                if item.quality < 50:
                    item.quality = item.quality + 1
            
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                is_normal_item = False
                if item.sell_in < 6:
                    item.quality = item.quality + 3
                elif item.sell_in < 11:
                    item.quality = item.quality + 2
                else:
                    item.quality = item.quality + 1
                # can't have quality > 50
                if item.quality > 50:
                    item.quality = 50
            
            if item.name == "Conjured Mana Cake":
                is_normal_item = False
                item.quality = item.quality - 2 * self.NORMAL_QUALITY_DECREASE
            
            if is_normal_item:
                item.quality = item.quality - self.NORMAL_QUALITY_DECREASE
            
            # all item sell_in decrease
            item.sell_in = item.sell_in - 1

            # handle items that have negative sell_in
            if item.sell_in < 0:
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = item.quality - item.quality
                
                if item.name == "Conjured Mana Cake":
                    item.quality = item.quality - 2 * self.NORMAL_QUALITY_DECREASE

                if is_normal_item:
                    item.quality = item.quality - self.NORMAL_QUALITY_DECREASE
            
            # quality is never negative
            if item.quality < 0:
                item.quality = 0


# Item class should not be changed
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
