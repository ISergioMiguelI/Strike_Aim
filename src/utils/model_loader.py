import pyassimp
import pywavefront

class ModelLoader:
    @staticmethod
    def load_model(path):
        try:
            scene = pyassimp.load(path)
            return scene
        except Exception as e:
            print(f"Erro ao carregar modelo: {e}")
            return None

    @staticmethod
    def release_model(scene):
        if scene:
            pyassimp.release(scene)