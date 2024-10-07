from random import choice

from utils import resource_path

responses = {
    "I don't think so." : resource_path("audio/I_Don't_Think_So.mp3"),
    "Maybe someday." : resource_path("audio/Maybe_Someday.mp3"),
    "No." : resource_path("audio/No.mp3"),
    "No.\sass" : resource_path("audio/No_Sass_Ver.mp3"),
    "Try asking again." : resource_path("audio/Try_Asking_Again.mp3"),
    "Yes." : resource_path("audio/Yes.mp3"),
}

# Pulls random response from list of potential responses
def get_random_responses():
    return choice(list(responses.items()))