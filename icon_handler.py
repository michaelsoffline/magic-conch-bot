from PIL import Image
from StreamDeck.ImageHelpers import PILHelper
from utils import resource_path

def update_button_icon(deck, key, icon_path):
    # Open the icon image
    icon_image = Image.open(icon_path)

    # Resize the image to the correct size for the Stream Deck (72 x 72 px)
    deck_icon = PILHelper.create_scaled_image(deck, icon_image, margins=[0, 0, 0, 0])

    # Convert the PIL image to raw bytes for Stream Deck
    deck.set_key_image(key, PILHelper.to_native_format(deck, deck_icon))