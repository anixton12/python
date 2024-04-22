class Television:
    # Class constants
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializes the Television object with default settings."""
        self.__status: bool = False  # TV is initially off
        self.__muted: bool = False   # TV is initially unmuted
        self.__volume: int = Television.MIN_VOLUME  # Start at minimum volume
        self.__channel: int = Television.MIN_CHANNEL  # Start at minimum channel

    def power(self) -> None:
        """Toggle the power status of the TV (on/off)."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the muted status on if the TV is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel by one, looping back to MIN_CHANNEL at MAX_CHANNEL."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the channel by one, looping back to MAX_CHANNEL at MIN_CHANNEL."""
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by one unless it is at MAX_VOLUME. Unmutes if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by one unless it is at MIN_VOLUME. Unmutes if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Returns a formatted string of the current status, channel, and volume of the TV."""
        volume_display = '0' if self.__muted else self.__volume
        return f"Power={'True' if self.__status else 'False'}, Channel={self.__channel}, Volume={volume_display}"

    tv = Television()
    print(tv)  # Should print the initial status, channel and volume.
