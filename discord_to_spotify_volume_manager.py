import time
from pycaw.pycaw import AudioUtilities, IAudioMeterInformation, ISimpleAudioVolume

VOLUME_THRESHOLD = 0.3   # Threshold for Discord volume
INCREMENT        = 0.01  # Increment for adjusting volume
MAX_VOLUME       = 1.0   # Maximum volume
MIN_VOLUME       = 0.1   # Minimum volume
VOLUME_LIST_SIZE = 20    # Size of volume history list

def set_spotify_volume(volume):
    '''
    Set the volume of the Spotify app.

    Args:
        volume (float): The volume level to set, ranging from 0 to 1.
    '''
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe":
            volume_interface.SetMasterVolume(volume, None)

def get_discord_volume():
    '''
    Get the volume of the Discord App (All Processes combined)
    '''
    sessions = AudioUtilities.GetAllSessions()
    sum_volume = 0
    for session in sessions:
        volume = session._ctl.QueryInterface(IAudioMeterInformation)
        if session.Process and session.Process.name() == "Discord.exe":
            sum_volume += volume.GetPeakValue()
    return sum_volume

def measure_volume_continuously(interval=0.01):
    '''
    Measures Discord volume and adjusts Spotify volume accordingly
    '''
    volume_list = [0] * VOLUME_LIST_SIZE
    volume = MAX_VOLUME
    while True:
        try:
            discord_volume = get_discord_volume()
            volume_list.pop(0)
            volume_list.append(discord_volume)
            volume_sum = sum(volume_list)
            if volume_sum > VOLUME_THRESHOLD:
                volume = MIN_VOLUME
            else:
                volume = min(MAX_VOLUME, volume + INCREMENT)
            set_spotify_volume(volume)
            time.sleep(interval)
        except Exception as e:
            print("Error:", e)
            time.sleep(1)

measure_volume_continuously()
