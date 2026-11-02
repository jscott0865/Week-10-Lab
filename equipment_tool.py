# equipment_tool.py
# Author: Jackson Scott


class EquipmentCatalog:
    """A tool that knows which rental gear is available and daily rates."""

    def __init__(self, inventory):
        """Store the inventory and daily prices."""
        self.inventory = inventory

    def find_item(self, text):
        """Return first known item in text or none"""
        for item in self.inventory:
            if item in text.lower():
                return item
            return None

    def get_details(self, item):
        """Return the details/rate for an item, unless it is unknown"""
        if item in self.inventory:
            return self.inventory[item]
        return None
