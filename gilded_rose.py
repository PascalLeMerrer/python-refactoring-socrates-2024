# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_item_quality(item)


def update_item_quality(item):
    if item.name == "Aged Brie":
        increase_quality(item)

    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        increase_backstage_pass_quality(item)
    else:
        decrease_quality(item)

    if item.name != "Sulfuras, Hand of Ragnaros":
        item.sell_in = item.sell_in - 1
    if item.sell_in >= 0:
        return
    if item.name == "Aged Brie":
        increase_quality(item)
        return
    if item.name == "Backstage passes to a TAFKAL80ETC concert":
        item.quality = 0
        return
    decrease_quality(item)
    if item.name == "Conjured Mana Cake":
        decrease_quality(item)



def increase_backstage_pass_quality(item):
    increase_quality(item)
    if item.quality < 50:
        if item.sell_in < 11:
            increase_quality(item)
        if item.sell_in < 6:
            increase_quality(item)


def decrease_quality(item):
    if item.quality > 0:
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = item.quality - 1


def increase_quality(item):
    if item.quality < 50:
        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
