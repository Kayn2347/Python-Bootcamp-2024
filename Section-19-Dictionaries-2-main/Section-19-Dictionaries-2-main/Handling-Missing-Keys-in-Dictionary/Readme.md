# Handling Missing Keys in Dictionary

items = {
    "computer" : 10,
    "printer" : 8,
    "mouse" : 15,
    "webcam" : 12,
    "router" : 10,
}

# quantity = items.get("microphone", 11)
# print(f"Number of items in the sore: {quantity}")
# print(items)


quantity = items.setdefault("computer", 11)
print(f"Number of items in the sore: {quantity}")
print(items)


