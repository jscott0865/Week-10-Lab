# equipment_main.py
# Author: Jackson Scott

from equipment_bot import EquipmentAssistant
from equipment_tool import EquipmentCatalog

INVENTORY = {
    "kayak": "$35/day",
    "tent": "$25/day",
    "paddleboard": "$30/day",
}

catalog = EquipmentCatalog(INVENTORY)
assistant = EquipmentAssistant(
    "Ultron",
    "You help customers check gear pricing and availability for Bayside Rentals",
    catalog,
)
print("Type a message, or type quit to stop")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")
print(f"Messages in this conversation: {len(assistant.history)}")
