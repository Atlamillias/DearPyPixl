import enum


class Key(enum.Enum):
    ANY = -1
    Break = 3
    Backspace = 8
    Tab = 9
    Clear = 12
    Return = 13
    Enter = 13
    Shift = 16
    Ctrl = 17
    Alt = 18
    Pause = 19
    CapsLock = 20
    Esc = 27
    Spacebar = 32
    PgUp = 33
    PgDn = 34
    End = 35
    Home = 36
    ArrowLeft = 37
    ArrowRight = 38
    ArrowUp = 39
    ArrowDn = 40
    Select = 41
    Print = 42
    Exec = 43
    PrtScr = 44
    Ins = 45
    Del = 46
    Help = 47
    Digit0 = 48
    Digit1 = 49
    Digit2 = 50
    Digit3 = 51
    Digit4 = 52
    Digit5 = 53
    Digit6 = 54
    Digit7 = 55
    Digit8 = 56
    Digit9 = 57
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90
    L_Meta = 91
    R_Meta = 92
    L_Win = 91
    R_Win = 92
    Apps = 93
    Sleep = 95
    Numpad0 = 96
    Numpad1 = 97
    Numpad2 = 98
    Numpad3 = 99
    Numpad4 = 100
    Numpad5 = 101
    Numpad6 = 102
    Numpad7 = 103
    Numpad8 = 104
    Numpad9 = 105
    NumpadMultiply = 106
    NumpadAdd = 107
    NumpadSeparator = 108
    NumpadSubtract = 109
    NumpadDecimal = 110
    NumpadDivide = 111
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123
    F13 = 124
    F14 = 125
    F15 = 126
    F16 = 127
    F17 = 128
    F18 = 129
    F19 = 130
    F20 = 131
    F21 = 132
    F22 = 133
    F23 = 134
    F24 = 135
    NumLock = 144
    ScrollLock = 145
    L_Shift = 160
    R_Shift = 161
    L_Ctrl = 162
    R_Ctrl = 163
    L_Menu = 164
    R_Menu = 165
    BrowserBack = 166
    BrowserForward = 167
    BrowserRefresh = 168
    BrowserStop = 169
    BrowserSearch = 170
    BrowserFavorites = 171
    BrowserHome = 172
    VolMute = 173
    VolDown = 174
    VolUp = 175
    MediaTrackNext = 176
    MediaTrackPrev = 177
    MediaStop = 178
    MediaPlayPause = 179
    LaunchMail = 180
    MediaSelect = 181
    LaunchApp1 = 182
    LaunchApp2 = 183  # calc on Win32
    Semicolon = 186
    Plus = 187
    Comma = 188
    Minus = 189
    Period = 190
    ForwardSlash = 191
    Tilde = 192
    BracketOpen = 219
    Backslash = 220
    BracketClose = 221
    Quote = 222
    IntlBackslash = 226  # \
    UNIDENTIFIED = 255  # FN key is common


class Mouse(enum.Enum):
    ANY = -1
    Left = 0
    Right = 1
    Middle = 2
    Button1 = 3
    Button2 = 4