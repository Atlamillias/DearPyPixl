import enum
from dearpygui import dearpygui


class Platform(enum.IntEnum):
    WINDOWS =  dearpygui.mvPlatform_Windows   # 0
    MAC     =  dearpygui.mvPlatform_Apple     # 1
    LINUX   =  dearpygui.mvPlatform_Linux     # 2
    OTHER   = -1

    @classmethod
    def _missing_(cls, value: object):
        if isinstance(value, int):
            return cls.OTHER
        return None


class MouseInput(enum.IntEnum):
    ANY    = -1
    LEFT   = dearpygui.mvMouseButton_Left    # 0
    L      = LEFT
    RIGHT  = dearpygui.mvMouseButton_Right   # 1
    R      = RIGHT
    MIDDLE = dearpygui.mvMouseButton_Middle  # 2
    M      = MIDDLE
    X1     = dearpygui.mvMouseButton_X1      # 3
    X2     = dearpygui.mvMouseButton_X2      # 4


class KeyInput(enum.IntEnum):
    ANY              = -1
    BREAK            = 3
    BACKSPACE        = 8
    TAB              = 9
    CLEAR            = 12
    RETURN           = 13
    ENTER            = RETURN
    SHIFT            = 16
    CTRL             = 17
    ALT              = 18
    PAUSE            = 19
    CAPS_LOCK        = 20
    ESC              = 27
    SPACEBAR         = 32
    SPACE            = SPACEBAR
    PAGE_UP          = 33
    PAGE_DN          = 34
    END              = 35
    HOME             = 36
    ARROW_LEFT       = 37
    ARROW_RIGHT      = 38
    ARROW_UP         = 39
    ARROW_DN         = 40
    SELECT           = 41
    PRINT            = 42
    EXEC             = 43
    PRINTSCREEN      = 44
    PRTSCR           = PRINTSCREEN
    INSERT           = 45
    INS              = INSERT
    DELETE           = 46
    DEL              = DELETE
    HELP             = 47
    DIGIT_0          = 48
    DIGIT_1          = 49
    DIGIT_2          = 50
    DIGIT_3          = 51
    DIGIT_4          = 52
    DIGIT_5          = 53
    DIGIT_6          = 54
    DIGIT_7          = 55
    DIGIT_8          = 56
    DIGIT_9          = 57
    A                = 65
    B                = 66
    C                = 67
    D                = 68
    E                = 69
    F                = 70
    G                = 71
    H                = 72
    I                = 73
    J                = 74
    K                = 75
    L                = 76
    M                = 77
    N                = 78
    O                = 79
    P                = 80
    Q                = 81
    R                = 82
    S                = 83
    T                = 84
    U                = 85
    V                = 86
    W                = 87
    X                = 88
    Y                = 89
    Z                = 90
    L_META           = 91
    R_META           = 92
    L_WIN            = L_META
    R_WIN            = R_META
    APPS             = 93
    SLEEP            = 95
    NUMPAD_0         = 96
    NUMPAD_1         = 97
    NUMPAD_2         = 98
    NUMPAD_3         = 99
    NUMPAD_4         = 100
    NUMPAD_5         = 101
    NUMPAD_6         = 102
    NUMPAD_7         = 103
    NUMPAD_8         = 104
    NUMPAD_9         = 105
    NUMPAD_MUL       = 106
    NUMPAD_ADD       = 107
    NUMPAD_SEP       = 108
    NUMPAD_SUB       = 109
    NUMPAD_DEC       = 110
    NUMPAD_DIV       = 111
    F1               = 112
    F2               = 113
    F3               = 114
    F4               = 115
    F5               = 116
    F6               = 117
    F7               = 118
    F8               = 119
    F9               = 120
    F10              = 121
    F11              = 122
    F12              = 123
    F13              = 124
    F14              = 125
    F15              = 126
    F16              = 127
    F17              = 128
    F18              = 129
    F19              = 130
    F20              = 131
    F21              = 132
    F22              = 133
    F23              = 134
    F24              = 135
    NUM_LOCK         = 144
    SCR_LOCK         = 145
    L_SHIFT          = 160
    R_SHIFT          = 161
    L_CTRL           = 162
    R_CTRL           = 163
    L_MENU           = 164
    R_MENU           = 165
    BROWSER_BACK     = 166
    BROWSER_FORWARD  = 167
    BROWSER_REFRESH  = 168
    BROWSER_STOP     = 169
    BROWSER_SEARCH   = 170
    BROWSER_FAVS     = 171
    BROWSER_HOME     = 172
    VOL_MUTE         = 173
    VOL_DN           = 174
    VOL_UP           = 175
    MEDIA_TRACK_NEXT = 176
    MEDIA_TRACK_PREV = 177
    MEDIA_STOP       = 178
    MEDIA_PLAY       = 179
    MEDIA_PAUSE      = MEDIA_PLAY
    LAUNCH_MAIL      = 180
    MEDIA_SELECT     = 181
    LAUNCH_APP1      = 182
    LAUNCH_APP2      = 183
    SEMICOLON        = 186
    PLUS             = 187
    COMMA            = 188
    MINUS            = 189
    PERIOD           = 190
    FORWARD_SLASH    = 191
    TILDE            = 192  # ~
    BRACKET_OPEN     = 219  # [
    BACKSLASH        = 220  #
    BRACKET_CLOSE    = 221
    QUOTE            = 222
    INTL_BACKSLASH   = 226  # \
    UNIDENTIFIED     = 255


class ThemeCategory(enum.IntEnum):
    CORE = dearpygui.mvThemeCat_Core   # 0
    PLOT = dearpygui.mvThemeCat_Plots  # 1
    NODE = dearpygui.mvThemeCat_Nodes  # 2


class NodeAttrIO(enum.IntEnum):
    INPUT  = dearpygui.mvNode_Attr_Input
    OUTPUT = dearpygui.mvNode_Attr_Output
    STATIC = dearpygui.mvNode_Attr_Static


class NodeMMapLoc(enum.IntEnum):
    LOWER_LEFT  = dearpygui.mvNodeMiniMap_Location_BottomLeft
    LOWER_RIGHT = dearpygui.mvNodeMiniMap_Location_BottomRight
    UPPER_RIGHT = dearpygui.mvNodeMiniMap_Location_TopRight
    UPPER_LEFT  = dearpygui.mvNodeMiniMap_Location_TopLeft
