import enum as _enum
from dearpygui import dearpygui as _dearpygui


ANY = -1


class Axis(_enum.IntEnum):
    X = X1 = x = x1 = _dearpygui.mvXAxis
    X2 = x2 = _dearpygui.mvXAxis2
    X3 = x3 = _dearpygui.mvXAxis3
    Y = Y1 = y = y1 = _dearpygui.mvYAxis
    Y2 = y2 = _dearpygui.mvYAxis2
    Y3 = y3 = _dearpygui.mvYAxis3

PlotAxis = Axis


class ColorEdit(_enum.IntEnum):
    ALPHA_PREVIEW_NONE = _dearpygui.mvColorEdit_AlphaPreviewNone  # 0
    ALPHA_PREVIEW = _dearpygui.mvColorEdit_AlphaPreview  # 131072
    ALPHA_PREVIEW_HALF = _dearpygui.mvColorEdit_AlphaPreviewHalf  # 262144
    UINT_8 = _dearpygui.mvColorEdit_uint8  # 8388608
    FLOAT = _dearpygui.mvColorEdit_float  # 16777216
    RGB = _dearpygui.mvColorEdit_rgb  # 1048576
    HSV = _dearpygui.mvColorEdit_hsv  # 2097152
    HEX = _dearpygui.mvColorEdit_hex  # 4194304
    INPUT_RGB = _dearpygui.mvColorEdit_input_rgb  # 134217728
    INPUT_HSV = _dearpygui.mvColorEdit_input_hsv  # 268435456


class ColorFormat(_enum.IntEnum):
    RGBA = _dearpygui.mvFormat_Float_rgba  # 0
    RGB = _dearpygui.mvFormat_Float_rgb  # 1


class ColorPicker(_enum.IntEnum):
    BAR = _dearpygui.mvColorPicker_bar  # 33554432
    WHEEL = _dearpygui.mvColorPicker_wheel  # 67108864


class ComboHeight(_enum.IntEnum):
    SMALL = _dearpygui.mvComboHeight_Small  # 0
    REGULAR = _dearpygui.mvComboHeight_Regular  # 1
    LARGE = _dearpygui.mvComboHeight_Large  # 2
    LARGEST = _dearpygui.mvComboHeight_Largest  # 3


class CullMode(_enum.IntEnum):
    NONE = _dearpygui.mvCullMode_None  # 0
    BACK = _dearpygui.mvCullMode_Back  # 1
    FRONT = _dearpygui.mvCullMode_Front  # 2


class DatePickerLevel(_enum.IntEnum):
    DAY = _dearpygui.mvDatePickerLevel_Day  # 0
    MONTH = _dearpygui.mvDatePickerLevel_Month  # 1
    YEAR = _dearpygui.mvDatePickerLevel_Year  # 2


class Dir(_enum.IntEnum):
    NONE = _dearpygui.mvDir_None  # -1
    LEFT = _dearpygui.mvDir_Left  # 0
    RIGHT = _dearpygui.mvDir_Right  # 1
    UP = _dearpygui.mvDir_Up  # 2
    DOWN = _dearpygui.mvDir_Down  # 3


class FontRangeHint(_enum.IntEnum):
    DEFAULT = _dearpygui.mvFontRangeHint_Default  # 0
    JAPANESE = _dearpygui.mvFontRangeHint_Japanese  # 1
    KOREAN = _dearpygui.mvFontRangeHint_Korean  # 2
    CHINESE_FULL = _dearpygui.mvFontRangeHint_Chinese_Full  # 3
    CHINESE_SIMPLIFIED_COMMON = _dearpygui.mvFontRangeHint_Chinese_Simplified_Common  # 4
    CYRILLIC = _dearpygui.mvFontRangeHint_Cyrillic  # 5
    THAI = _dearpygui.mvFontRangeHint_Thai  # 6
    VIETNAMESE = _dearpygui.mvFontRangeHint_Vietnamese  # 7


class GraphicsBackend(_enum.IntEnum):
    D3D11 = _dearpygui.mvGraphicsBackend_D3D11  # 0
    D3D12 = _dearpygui.mvGraphicsBackend_D3D12  # 1
    VULKAN = _dearpygui.mvGraphicsBackend_VULKAN  # 2
    METAL = _dearpygui.mvGraphicsBackend_METAL  # 3
    OPENGL = _dearpygui.mvGraphicsBackend_OPENGL  # 4


class NodeAttr(_enum.IntEnum):
    INPUT = _dearpygui.mvNode_Attr_Input  # 0
    OUTPUT = _dearpygui.mvNode_Attr_Output  # 1
    STATIC = _dearpygui.mvNode_Attr_Static  # 2


class NodeMiniMapLocation(_enum.IntEnum):
    BOTTOM_LEFT = _dearpygui.mvNodeMiniMap_Location_BottomLeft  # 0
    BOTTOM_RIGHT = _dearpygui.mvNodeMiniMap_Location_BottomRight  # 1
    TOP_LEFT = _dearpygui.mvNodeMiniMap_Location_TopLeft  # 2
    TOP_RIGHT = _dearpygui.mvNodeMiniMap_Location_TopRight  # 3


class NodePinShape(_enum.IntEnum):
    CIRCLE = _dearpygui.mvNode_PinShape_Circle  # 0
    CIRCLE_FILLED = _dearpygui.mvNode_PinShape_CircleFilled  # 1
    TRIANGLE = _dearpygui.mvNode_PinShape_Triangle  # 2
    TRIANGLE_FILLED = _dearpygui.mvNode_PinShape_TriangleFilled  # 3
    QUAD = _dearpygui.mvNode_PinShape_Quad  # 4
    QUAD_FILLED = _dearpygui.mvNode_PinShape_QuadFilled  # 5


class Platform(_enum.IntEnum):
    WINDOWS = _dearpygui.mvPlatform_Windows  # 0
    APPLE = _dearpygui.mvPlatform_Apple  # 1
    LINUX = _dearpygui.mvPlatform_Linux  # 2


class PlotBin(_enum.IntEnum):
    SQRT = _dearpygui.mvPlotBin_Sqrt  # -1
    STURGES = _dearpygui.mvPlotBin_Sturges  # -2
    RICE = _dearpygui.mvPlotBin_Rice  # -3
    SCOTT = _dearpygui.mvPlotBin_Scott  # -4


class PlotColorMap(_enum.IntEnum):
    DEFAULT = _dearpygui.mvPlotColormap_Default  # 0
    DEEP = _dearpygui.mvPlotColormap_Deep  # 0
    DARK = _dearpygui.mvPlotColormap_Dark  # 1
    PASTEL = _dearpygui.mvPlotColormap_Pastel  # 2
    PAIRED = _dearpygui.mvPlotColormap_Paired  # 3
    VIRIDIS = _dearpygui.mvPlotColormap_Viridis  # 4
    PLASMA = _dearpygui.mvPlotColormap_Plasma  # 5
    HOT = _dearpygui.mvPlotColormap_Hot  # 6
    COOL = _dearpygui.mvPlotColormap_Cool  # 7
    PINK = _dearpygui.mvPlotColormap_Pink  # 8
    JET = _dearpygui.mvPlotColormap_Jet  # 9
    TWILIGHT = _dearpygui.mvPlotColormap_Twilight  # 10
    RdBu = _dearpygui.mvPlotColormap_RdBu  # 11
    BrBG = _dearpygui.mvPlotColormap_BrBG  # 12
    PiYG = _dearpygui.mvPlotColormap_PiYG  # 13
    SPECTRAL = _dearpygui.mvPlotColormap_Spectral  # 14
    GREYS = _dearpygui.mvPlotColormap_Greys  # 15


class PlotLocation(_enum.IntEnum):
    CENTER = C = _dearpygui.mvPlot_Location_Center  # 0
    NORTH = N = _dearpygui.mvPlot_Location_North  # 1
    SOUTH = S = _dearpygui.mvPlot_Location_South  # 2
    WEST = W = _dearpygui.mvPlot_Location_West  # 4
    EAST = E = _dearpygui.mvPlot_Location_East  # 8
    NORTHWEST = NW = _dearpygui.mvPlot_Location_NorthWest  # 5
    NORTHEAST = NE = _dearpygui.mvPlot_Location_NorthEast  # 9
    SOUTHWEST = SW = _dearpygui.mvPlot_Location_SouthWest  # 6
    SOUTHEAST = SE = _dearpygui.mvPlot_Location_SouthEast  # 10


class PlotMarker(_enum.IntEnum):
    NONE = _dearpygui.mvPlotMarker_None  # -1
    CIRCLE = _dearpygui.mvPlotMarker_Circle  # 0
    SQUARE = _dearpygui.mvPlotMarker_Square  # 1
    DIAMOND = _dearpygui.mvPlotMarker_Diamond  # 2
    UP = _dearpygui.mvPlotMarker_Up  # 3
    DOWN = _dearpygui.mvPlotMarker_Down  # 4
    LEFT = _dearpygui.mvPlotMarker_Left  # 5
    RIGHT = _dearpygui.mvPlotMarker_Right  # 6
    CROSS = _dearpygui.mvPlotMarker_Cross  # 7
    PLUS = _dearpygui.mvPlotMarker_Plus  # 8
    ASTERISK = _dearpygui.mvPlotMarker_Asterisk  # 9


class PlotScale(_enum.IntEnum):
    LINEAR = _dearpygui.mvPlotScale_Linear  # 0
    TIME = _dearpygui.mvPlotScale_Time  # 1
    LOG_10 = _dearpygui.mvPlotScale_Log10  # 2
    SYM_LOG = _dearpygui.mvPlotScale_SymLog  # 3


class ReservedUUID(_enum.IntEnum):
    UUID_0 = _dearpygui.mvReservedUUID_0  # 10
    UUID_1 = _dearpygui.mvReservedUUID_1  # 11
    UUID_2 = _dearpygui.mvReservedUUID_2  # 12
    UUID_3 = _dearpygui.mvReservedUUID_3  # 13
    UUID_4 = _dearpygui.mvReservedUUID_4  # 14
    UUID_5 = _dearpygui.mvReservedUUID_5  # 15
    UUID_6 = _dearpygui.mvReservedUUID_6  # 16
    UUID_7 = _dearpygui.mvReservedUUID_7  # 17
    UUID_8 = _dearpygui.mvReservedUUID_8  # 18
    UUID_9 = _dearpygui.mvReservedUUID_9  # 19
    UUID_10 = _dearpygui.mvReservedUUID_10  # 20


class TabOrder(_enum.IntEnum):
    REORDERABLE = _dearpygui.mvTabOrder_Reorderable  # 0
    FIXED = _dearpygui.mvTabOrder_Fixed  # 1
    LEADING = _dearpygui.mvTabOrder_Leading  # 2
    TRAILING = _dearpygui.mvTabOrder_Trailing  # 3


class TablePolicy(_enum.IntEnum):
    FIXED_FIT = _dearpygui.mvTable_SizingFixedFit  # 8192
    FIXED_SAME = _dearpygui.mvTable_SizingFixedSame  # 16384
    STRETCH_PROP = _dearpygui.mvTable_SizingStretchProp  # 24576
    STRETCH_SAME = _dearpygui.mvTable_SizingStretchSame  # 32768


class ThemeCategory(_enum.IntEnum):
    CORE = _dearpygui.mvThemeCat_Core  # 0
    PLOTS = PLOT = _dearpygui.mvThemeCat_Plots  # 1
    NODES = NODE = _dearpygui.mvThemeCat_Nodes  # 2


class TimeUnit(_enum.IntEnum):
    us = MICROSECOND = _dearpygui.mvTimeUnit_Us  # 0
    ms = MILLISECOND = _dearpygui.mvTimeUnit_Ms  # 1
    s = SECOND = _dearpygui.mvTimeUnit_S  # 2
    min = MINUTE = _dearpygui.mvTimeUnit_Min  # 3
    hr = HOUR = _dearpygui.mvTimeUnit_Hr  # 4
    day = DAY = _dearpygui.mvTimeUnit_Day  # 5
    mo = MONTH = _dearpygui.mvTimeUnit_Mo  # 6
    yr = YEAR = _dearpygui.mvTimeUnit_Yr  # 7


class Tool(_enum.IntEnum):
    ABOUT = _dearpygui.mvTool_About  # 3
    DEBUG = _dearpygui.mvTool_Debug  # 4
    DOC = _dearpygui.mvTool_Doc  # 5
    ITEM_REGISTRY = _dearpygui.mvTool_ItemRegistry  # 6
    METRICS = _dearpygui.mvTool_Metrics  # 7
    STACK = _dearpygui.mvTool_Stack  # 10
    STYLE = _dearpygui.mvTool_Style  # 8
    FONT = _dearpygui.mvTool_Font  # 9




# [ input codes ]

class _KeymapEnumType(_enum.EnumMeta):
    def __getitem__(self, name: str):
        key = name.upper().replace(" ", "_").replace("-", "_")
        try:
            return self._member_map_[key]
        except KeyError:
            raise KeyError(name) from None


class Key(_enum.IntEnum, metaclass=_KeymapEnumType):
    """Contains all possible values for handler and input *key*
    arguments.

    Note that `MOUSE_*` members are different from mouse button
    constants. These work for key press, release, etc. events.
    """
    MOD_DISABLED = _dearpygui.mvKey_ModDisabled  # -1
    ANY = NONE = _dearpygui.mvKey_None  # 0  <default value>
    CLEAR = _dearpygui.mvKey_Clear  # 12
    PRIOR = _dearpygui.mvKey_Prior  # 33
    NEXT = _dearpygui.mvKey_Next  # 34
    SELECT = SEL = _dearpygui.mvKey_Select  # 41
    EXECUTE = EXEC = _dearpygui.mvKey_Execute  # 43
    HELP = _dearpygui.mvKey_Help  # 47
    L_WIN = _dearpygui.mvKey_LWin  # 91
    R_WIN = _dearpygui.mvKey_RWin  # 92
    APPS = _dearpygui.mvKey_Apps  # 93
    SLEEP = _dearpygui.mvKey_Sleep  # 95
    F25 = _dearpygui.mvKey_F25  # 136
    BROWSER_REFRESH = _dearpygui.mvKey_Browser_Refresh  # 168
    BROWSER_STOP = _dearpygui.mvKey_Browser_Stop  # 169
    BROWSER_SEARCH = _dearpygui.mvKey_Browser_Search  # 170
    BROWSER_FAVORITES = _dearpygui.mvKey_Browser_Favorites  # 171
    BROWSER_HOME = _dearpygui.mvKey_Browser_Home  # 172
    VOLUME_MUTE = VOL_MUTE = _dearpygui.mvKey_Volume_Mute  # 173
    VOLUME_DOWN = VOL_DOWN = VOL_DN = _dearpygui.mvKey_Volume_Down  # 174
    VOLUME_UP = VOL_UP = _dearpygui.mvKey_Volume_Up  # 175
    MEDIA_NEXT_TRACK = NEXT_TRACK = _dearpygui.mvKey_Media_Next_Track  # 176
    MEDIA_PREV_TRACK = PREV_TRACK = _dearpygui.mvKey_Media_Prev_Track  # 177
    MEDIA_STOP = STOP_TRACK = _dearpygui.mvKey_Media_Stop  # 178
    MEDIA_PLAY_PAUSE = PLAY_TRACK = PAUSE_TRACK = _dearpygui.mvKey_Media_Play_Pause  # 179
    LAUNCH_MAIL = _dearpygui.mvKey_Launch_Mail  # 180
    LAUNCH_MEDIA_SELECT = _dearpygui.mvKey_Launch_Media_Select  # 181
    LAUNCH_APP_1 = _dearpygui.mvKey_Launch_App1  # 182
    LAUNCH_APP_2 = _dearpygui.mvKey_Launch_App2  # 183
    COLON = _dearpygui.mvKey_Colon  # 186
    PLUS = _dearpygui.mvKey_Plus  # 187
    TILDE = _dearpygui.mvKey_Tilde  # 192
    QUOTE = _dearpygui.mvKey_Quote  # 222
    TAB = _dearpygui.mvKey_Tab  # 512
    LEFT = LEFT_ARROW = _dearpygui.mvKey_Left  # 513
    RIGHT = RIGHT_ARROW = _dearpygui.mvKey_Right  # 514
    UP = UP_ARROW = _dearpygui.mvKey_Up  # 515
    DOWN = DOWN_ARROW = _dearpygui.mvKey_Down  # 516
    PAGE_UP = PG_UP = PGUP = 517
    PAGE_DOWN = PG_DN = PGDN = 518
    HOME = _dearpygui.mvKey_Home  # 519
    END = _dearpygui.mvKey_End  # 520
    INSERT = INS = _dearpygui.mvKey_Insert  # 521
    DELETE = DEL = _dearpygui.mvKey_Delete  # 522
    BACK = BACKSPACE = _dearpygui.mvKey_Back  # 523
    SPACEBAR = SPACE = _dearpygui.mvKey_Spacebar  # 524
    RETURN = ENTER = _dearpygui.mvKey_Return  # 525
    ESCAPE = ESC = _dearpygui.mvKey_Escape  # 526
    L_CONTROL = L_CTRL = LCONTROL = LCTRL = _dearpygui.mvKey_LControl  # 527
    L_SHIFT = LSHIFT = _dearpygui.mvKey_LShift  # 528
    L_ALT = LALT = _dearpygui.mvKey_LAlt  # 529
    L_SUPER = LSUPER = 530
    R_CONTROL = RCONTROL = R_CTRL = RCTRL = _dearpygui.mvKey_RControl  # 531
    R_SHIFT = RSHIFT = _dearpygui.mvKey_RShift  # 532
    R_ALT = RALT = _dearpygui.mvKey_RAlt  # 533
    R_SUPER = RSUPER = 534
    MENU = _dearpygui.mvKey_Menu  # 535
    DIGIT_0 = _dearpygui.mvKey_0  # 536
    DIGIT_1 = _dearpygui.mvKey_1  # 537
    DIGIT_2 = _dearpygui.mvKey_2  # 538
    DIGIT_3 = _dearpygui.mvKey_3  # 539
    DIGIT_4 = _dearpygui.mvKey_4  # 540
    DIGIT_5 = _dearpygui.mvKey_5  # 541
    DIGIT_6 = _dearpygui.mvKey_6  # 542
    DIGIT_7 = _dearpygui.mvKey_7  # 543
    DIGIT_8 = _dearpygui.mvKey_8  # 544
    DIGIT_9 = _dearpygui.mvKey_9  # 545
    A = _dearpygui.mvKey_A  # 546
    B = _dearpygui.mvKey_B  # 547
    C = _dearpygui.mvKey_C  # 548
    D = _dearpygui.mvKey_D  # 549
    E = _dearpygui.mvKey_E  # 550
    F = _dearpygui.mvKey_F  # 551
    G = _dearpygui.mvKey_G  # 552
    H = _dearpygui.mvKey_H  # 553
    I = _dearpygui.mvKey_I  # 554
    J = _dearpygui.mvKey_J  # 555
    K = _dearpygui.mvKey_K  # 556
    L = _dearpygui.mvKey_L  # 557
    M = _dearpygui.mvKey_M  # 558
    N = _dearpygui.mvKey_N  # 559
    O = _dearpygui.mvKey_O  # 560
    P = _dearpygui.mvKey_P  # 561
    Q = _dearpygui.mvKey_Q  # 562
    R = _dearpygui.mvKey_R  # 563
    s = _dearpygui.mvKey_S  # 564
    T = _dearpygui.mvKey_T  # 565
    U = _dearpygui.mvKey_U  # 566
    V = _dearpygui.mvKey_V  # 567
    W = _dearpygui.mvKey_W  # 568
    X = _dearpygui.mvKey_X  # 569
    Y = _dearpygui.mvKey_Y  # 570
    Z = _dearpygui.mvKey_Z  # 571
    F1 = _dearpygui.mvKey_F1  # 572
    F2 = _dearpygui.mvKey_F2  # 573
    F3 = _dearpygui.mvKey_F3  # 574
    F4 = _dearpygui.mvKey_F4  # 575
    F5 = _dearpygui.mvKey_F5  # 576
    F6 = _dearpygui.mvKey_F6  # 577
    F7 = _dearpygui.mvKey_F7  # 578
    F8 = _dearpygui.mvKey_F8  # 579
    F9 = _dearpygui.mvKey_F9  # 580
    F10 = _dearpygui.mvKey_F10  # 581
    F11 = _dearpygui.mvKey_F11  # 582
    F12 = _dearpygui.mvKey_F12  # 583
    F13 = _dearpygui.mvKey_F13  # 584
    F14 = _dearpygui.mvKey_F14  # 585
    F15 = _dearpygui.mvKey_F15  # 586
    F16 = _dearpygui.mvKey_F16  # 587
    F17 = _dearpygui.mvKey_F17  # 588
    F18 = _dearpygui.mvKey_F18  # 589
    F19 = _dearpygui.mvKey_F19  # 590
    F20 = _dearpygui.mvKey_F20  # 591
    F21 = _dearpygui.mvKey_F21  # 592
    F22 = _dearpygui.mvKey_F22  # 593
    F23 = _dearpygui.mvKey_F23  # 594
    F24 = _dearpygui.mvKey_F24  # 595
    APOSTROPHE = 596
    COMMA = _dearpygui.mvKey_Comma  # 597
    MINUS = _dearpygui.mvKey_Minus  # 598
    PERIOD = _dearpygui.mvKey_Period  # 599
    SLASH = FORWARD_SLASH = _dearpygui.mvKey_Slash  # 600
    SEMICOLON = 601
    EQUAL = 602
    OPEN_BRACE = _dearpygui.mvKey_Open_Brace  # 603
    BACKSLASH = BACK_SLASH = _dearpygui.mvKey_Backslash  # 604
    CLOSE_BRACE = _dearpygui.mvKey_Close_Brace  # 605
    GRAVE_ACCENT = ACCENT = 606
    CAPS_LOCK = CAPS = CAPS_LCK = CAPSLCK = _dearpygui.mvKey_CapsLock  # 607
    SCROLL_LOCK = SCRLCK = SCR_LCK = _dearpygui.mvKey_ScrollLock  # 608
    NUM_LOCK = NUMLCK = NUM_LCK = _dearpygui.mvKey_NumLock  # 609
    PRINT = PRINT_SCREEN = PRT_SCR = PRTSCR = _dearpygui.mvKey_Print  # 610
    PAUSE = _dearpygui.mvKey_Pause  # 611
    NUMPAD_0 = NUM_0 = _dearpygui.mvKey_NumPad0  # 612
    NUMPAD_1 = NUM_1 = _dearpygui.mvKey_NumPad1  # 613
    NUMPAD_2 = NUM_2 = _dearpygui.mvKey_NumPad2  # 614
    NUMPAD_3 = NUM_3 = _dearpygui.mvKey_NumPad3  # 615
    NUMPAD_4 = NUM_4 = _dearpygui.mvKey_NumPad4  # 616
    NUMPAD_5 = NUM_5 = _dearpygui.mvKey_NumPad5  # 617
    NUMPAD_6 = NUM_6 = _dearpygui.mvKey_NumPad6  # 618
    NUMPAD_7 = NUM_7 = _dearpygui.mvKey_NumPad7  # 619
    NUMPAD_8 = NUM_8 = _dearpygui.mvKey_NumPad8  # 620
    NUMPAD_9 = NUM_9 = _dearpygui.mvKey_NumPad9  # 621
    DECIMAL = NUMPAD_DECIMAL = NUM_DECIMAL = _dearpygui.mvKey_Decimal  # 622
    DIVIDE = NUMPAD_DIVIDE = NUM_DIVIDE = _dearpygui.mvKey_Divide  # 623
    MULTIPLY = NUMPAD_MULTIPLY = NUM_MULTIPLY = _dearpygui.mvKey_Multiply  # 624
    SUBTRACT = NUMPAD_SUBTRACT = NUM_SUBTRACT = _dearpygui.mvKey_Subtract  # 625
    ADD = NUMPAD_ADD = NUM_ADD = _dearpygui.mvKey_Add  # 626
    NUMPAD_ENTER = NUM_ENTER = _dearpygui.mvKey_NumPadEnter  # 627
    NUMPAD_EQUAL = NUM_EQUAL = _dearpygui.mvKey_NumPadEqual  # 628
    BROWSER_BACK = _dearpygui.mvKey_Browser_Back  # 629
    BROWSER_FORWARD = _dearpygui.mvKey_Browser_Forward  # 630
    GAMEPAD_START = 631
    GAMEPAD_BACK = 632
    GAMEPAD_FACE_LEFT = 633
    GAMEPAD_FACE_RIGHT = 634
    GAMEPAD_FACE_UP = 635
    GAMEPAD_FACE_DOWN = 636
    GAMEPAD_DPAD_LEFT = 637
    GAMEPAD_DPAD_RIGHT = 638
    GAMEPAD_DPAD_UP = 639
    GAMEPAD_DPAD_DOWN = 640
    GAMEPAD_L1 = 641
    GAMEPAD_R1 = 642
    GAMEPAD_L2 = 643
    GAMEPAD_R2 = 644
    GAMEPAD_L3 = 645
    GAMEPAD_R3 = 646
    GAMEPAD_LSTICK_LEFT = 647
    GAMEPAD_LSTICK_RIGHT = 648
    GAMEPAD_LSTICK_UP = 649
    GAMEPAD_LSTICK_DOWN = 650
    GAMEPAD_RSTICK_LEFT = 651
    GAMEPAD_RSTICK_RIGHT = 652
    GAMEPAD_RSTICK_UP = 653
    GAMEPAD_RSTICK_DOWN = 654
    MOUSE_LEFT = LEFT_CLICK = LMB = 655
    MOUSE_RIGHT = RIGHT_CLICK = RMB = 656
    MOUSE_MIDDLE = MIDDLE_CLICK = MMB = 657
    MOUSE_X1 = 658
    MOUSE_X2 = 659
    MOUSE_WHEEL_X = SCROLL_H = H_SCROLL = 660
    MOUSE_WHEEL_Y = SCROLL_V = V_SCROLL = 661
    MOD_CTRL = _dearpygui.mvKey_ModCtrl  # 4096
    MOD_SHIFT = _dearpygui.mvKey_ModShift  # 8192
    MOD_ALT = _dearpygui.mvKey_ModAlt  # 16384
    MOD_SUPER = _dearpygui.mvKey_ModSuper  # 32768

Key.ANY._add_alias_('')
Key.ANY._add_value_alias_(None)
Key.RETURN._add_alias_('\n')
Key.RETURN._add_alias_('\r')
Key.RETURN._add_alias_("\r\n")
Key.DIGIT_0._add_alias_('0')
Key.DIGIT_1._add_alias_('1')
Key.DIGIT_2._add_alias_('2')
Key.DIGIT_3._add_alias_('3')
Key.DIGIT_4._add_alias_('4')
Key.DIGIT_5._add_alias_('5')
Key.DIGIT_6._add_alias_('6')
Key.DIGIT_7._add_alias_('7')
Key.DIGIT_8._add_alias_('8')
Key.DIGIT_9._add_alias_('9')
Key.DECIMAL._add_alias_('.')
Key.EQUAL._add_alias_('=')
Key.ADD._add_alias_('+')
Key.DIVIDE._add_alias_('/')
Key.MULTIPLY._add_alias_('*')
Key.SUBTRACT._add_alias_('-')
Key.COLON._add_alias_(':')
Key.SEMICOLON._add_alias_(';')
Key.TILDE._add_alias_('~')
Key.GRAVE_ACCENT._add_alias_('`')
Key.QUOTE._add_alias_('"')
Key.APOSTROPHE._add_alias_('\'')
Key.TAB._add_alias_('\t')
Key.SPACEBAR._add_alias_(' ')
Key.OPEN_BRACE._add_alias_('[')
Key.BACKSLASH._add_alias_('\\')
Key.CLOSE_BRACE._add_alias_(']')
Key.COMMA._add_alias_(',')
Key.VOLUME_UP._add_alias_("VOL+")
Key.VOLUME_DOWN._add_alias_("VOL_")  # "vol-"
Key.VOLUME_MUTE._add_alias_("VOL/")


class MouseButton(_enum.IntEnum, metaclass=_KeymapEnumType):
    """Contains all possible values for *button* mouse event
    arguments.
    """
    ANY = -1  # <default value>
    LEFT = L = _dearpygui.mvMouseButton_Left  # 0
    RIGHT = R = _dearpygui.mvMouseButton_Right  # 1
    MIDDLE = M = _dearpygui.mvMouseButton_Middle  # 2
    X1 = _dearpygui.mvMouseButton_X1  # 3
    X2 = _dearpygui.mvMouseButton_X2  # 4

MouseButton.ANY._add_alias_('')
MouseButton.ANY._add_value_alias_(None)
