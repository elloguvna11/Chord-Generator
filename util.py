import json


CONFIG_FILE = 'assets/config.json'


def load_config() -> dict:
    '''Loads the configuration json file into a python dictionary.'''
    with open(CONFIG_FILE, 'r') as configfile:
        text = configfile.read()
        config_dict = json.loads(text)
        return config_dict


def load_audio_list(config: dict) -> dict:
    '''Parses the config dictionary to load the audio files for each key.'''
    raw_audio_list = config['audio_list']
    parsed_audio_list = {
        key: {
            chord_name: f"assets/audio/{filename}"
            for chord_name, filename in chord_dictionary.items()
        }
        for key, chord_dictionary in raw_audio_list.items()
    }
    return parsed_audio_list