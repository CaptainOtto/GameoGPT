from game_gen_model import GameGenModel
from api_model import ApiModel

class Models:
    def __init__(self):
        self.game_gen_models = GameGenModel("Unreal Engine", "3D", "Realism", "Survival", "")
        self.api_model = ApiModel()

models = Models()
