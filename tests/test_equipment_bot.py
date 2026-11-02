from equipment_bot import EquipmentAssistant
from equipment_tool import EquipmentCatalog


def make_assistant():
    """Build a new assistant with its own tool for each test"""
    catalog = EquipmentCatalog({"kayak": "$35/day", "tent": "$25/day"})
    return EquipmentAssistant("Scout", "Be helpful", catalog)


def test_item_lookup_uses_tool():
    assistant = make_assistant()
    reply = assistant.respond("How much does the kayak cost?")
    assert "kayak" in reply and "$35/day" in reply


def test_missing_item_asks_for_clarification():
    assistant = make_assistant()
    assert "rental details" in assistant.respond("How much is gear?")

def test_reservation_goes_to_human():
    assistant = make_assistant()
    assert "passing you to a human" in assistant.respond(
        "I want to reserve a kayak"
    )


def test_unknown_request_safe_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("What is the weathet today?")
