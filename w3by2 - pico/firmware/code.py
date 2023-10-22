print("Starting")

import board
import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6) # Cols
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)             # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap
keyboard.keymap = [
    [KC.ESCAPE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.F20, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.MEDIA_PLAY_PAUSE, 
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.HOME,
     KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.PGUP,
     KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.PGDOWN,
     KC.LCTRL, KC.LGUI, KC.LALT, KC.SPACE, KC.APPLICATION, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.LEFT, KC.DOWN, KC.RIGHT]
]

if __name__ == '__main__':
    keyboard.go()
