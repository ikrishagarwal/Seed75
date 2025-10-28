import board
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.rotary_encoder import RotaryEncoderHandler

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    column_pins=[board.GP0, board.GP1, board.GP15, board.GP14, board.GP13, board.GP12, board.GP11,
                 board.GP10, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3],
    row_pins=[board.GP17, board.GP18, board.GP19,
              board.GP20, board.GP21, board.GP22],
    value_when_pressed=False,
)

# Define Keymap (needs fixes)
keyboard.keymap = [
    [
        # Row 1
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCR,
        # Row 2
        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
        # Row 3
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,
        # Row 4
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.DEL, KC.NO,
        # Row 5
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.END,
        # Row 6
        KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN,
        # Row 7
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.SLCK, KC.PAUS, KC.INS, KC.HOME, KC.PGUP,
    ],
]

encoder = RotaryEncoderHandler(pin_a=board.GP2, pin_b=board.GP16)
encoder.rotation_cw = KC.VOLU  # Volume Up
encoder.rotation_ccw = KC.VOLD  # Volume Down
keyboard.modules.append(encoder)

if __name__ == '__main__':
  keyboard.go()
