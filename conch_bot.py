from StreamDeck.DeviceManager import DeviceManager
from responses import get_random_responses
from audio_handler import play_audio
from icon_handler import update_button_icon
from utils import resource_path

# Global variable for the Stream Deck instance
deck = None

def magic_conch():
    global deck
    # Detect all Stream Deck devices connected to the system
    decks = DeviceManager().enumerate()

    if len(decks) > 0:
        # Use the first detected Stream Deck
        deck = decks[0]

        # Open the Stream Deck for input/output
        deck.open()
        deck.reset()

        print(f"Connected to {deck.deck_type()}")

        # Set Stream Deck brightness to 50
        deck.set_brightness(50)

        def key_change_callback(deck, key, state):
            if state:
                print(f"Button {key} pressed")

                temp_icon_path = resource_path("images/Answer_In_Progress.png")
                update_button_icon(deck, key, temp_icon_path)

                # Get random response from the Magic Conch
                response, audio_file = get_random_responses()

                # Print and play the response
                print(f"Magic Conch: {response}")
                play_audio(audio_file)

                original_icon_path = resource_path("images/Magic_Conch_Icon.png")
                update_button_icon(deck, key, original_icon_path)

        # Set callback for key presses
        deck.set_key_callback(key_change_callback)

        # Keep the app running and listening for key presses
        try:
            while True:
                pass
        except KeyboardInterrupt:
            stop_magic_conch()
    else:
        print("No Stream Deck found!")

def stop_magic_conch():
    global deck
    if deck:
        deck.reset() # Reset the Stream Deck to its default state
        deck.close() # Close the connection
        print("Stream Deck disconnected")