import pygame
import time

# Function to play the correct audio for the chosen response
def play_audio(file_path):
    print(f"Attempting to play {file_path}")

    # Initialize pygame mixer for playing audio
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Error initializing mixer: {e}")
        return

    try:
        # Load the audio as a Sound object
        sound = pygame.mixer.Sound(file_path)

        # Set the volume to maximum
        sound.set_volume(1.0)

        # Play the sound
        sound.play()

        # Wait for the sound to finish
        time.sleep(sound.get_length())

        print(f"Played {file_path}")
    except pygame.error as err:
        print(f"Error playing audio: {err}")
        return

    print("Audio playback finished")