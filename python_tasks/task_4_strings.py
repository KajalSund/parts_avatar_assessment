# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    sku = sku_string.replace('-', ' ')
    return sku.title()

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"