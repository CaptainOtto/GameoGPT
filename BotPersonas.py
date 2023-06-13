
@dataclass
class BotBase:
    name: str
    greetMessage: str = "Hello, I am a bot. I am here to help you."
    focusAreas: str

@dataclass
class Unrealabot(BotBase):
    name: str = "Unrealabout"
    greetMessage: str = "Hello, I am Unrealabot. I love to help with questions related to Unreal Engine 4 & 5."
    focusAreas: str = "Unreal Engine 4 and Unreal Engine 5"
