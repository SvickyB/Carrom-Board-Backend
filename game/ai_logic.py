# game/ai_logic.py

import math
import random

def ai_choose_shot(board_state):
    striker_x, striker_y = board_state["striker"]
    pieces = board_state["pieces"]

    if not pieces:
        return None

    closest_piece = min(pieces, key=lambda p: math.hypot(p[0] - striker_x, p[1] - striker_y))

    piece_x, piece_y = closest_piece
    angle = math.atan2(piece_y - striker_y, piece_x - striker_x)
    power = random.uniform(200, 500)

    return {"angle": angle, "power": power}
