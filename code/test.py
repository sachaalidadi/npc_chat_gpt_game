from rembg import new_session,remove
from PIL import Image
from pathlib import Path

here = Path(__file__).parent.resolve()
input_path = Path(here / "sprites" / "down_idle" / "idle_down.png")
# print(input_path)
image = input_path.read_bytes()
# print(image)
output_path = "./sprites/down_idle/idle_down_transparent.png"
input = Image.open(image,session = new_session())
output = remove(input_path)
output.save(output_path)