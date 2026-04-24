import enum
from dearpygui import _dearpygui


class mvNodePinShape(enum.IntEnum):
    CIRCLE = _dearpygui.mvNode_PinShape_Circle
    CIRCLE_FILLED = _dearpygui.mvNode_PinShape_CircleFilled
    QUAD = _dearpygui.mvNode_PinShape_Quad
    QUAD_FILLED = _dearpygui.mvNode_PinShape_QuadFilled
    TRIANGLE = _dearpygui.mvNode_PinShape_Triangle
    TRIANGLE_FILLED = _dearpygui.mvNode_PinShape_TriangleFilled

mvNode_PinShape_Circle = mvNodePinShape.CIRCLE
mvNode_PinShape_CircleFilled = mvNodePinShape.CIRCLE_FILLED
mvNode_PinShape_Quad = mvNodePinShape.QUAD
mvNode_PinShape_QuadFilled = mvNodePinShape.QUAD_FILLED
mvNode_PinShape_Triangle = mvNodePinShape.TRIANGLE
mvNode_PinShape_TriangleFilled = mvNodePinShape.TRIANGLE_FILLED


class mvNodeAttr(enum.IntEnum):
    INPUT  = _dearpygui.mvNode_Attr_Input
    OUTPUT = _dearpygui.mvNode_Attr_Output
    STATIC = _dearpygui.mvNode_Attr_Static

mvNode_Attr_Input = mvNodeAttr.INPUT
mvNode_Attr_Output = mvNodeAttr.OUTPUT
mvNode_Attr_Static = mvNodeAttr.STATIC


class mvTableSizing(enum.IntEnum):
    FIXED_FIT = _dearpygui.mvTable_SizingFixedFit
    FIXED_SAME = _dearpygui.mvTable_SizingFixedSame
    STRETCH_PROP = _dearpygui.mvTable_SizingStretchProp
    STRETCH_SAME = _dearpygui.mvTable_SizingStretchSame

mvTable_SizingFixedFit = mvTableSizing.FIXED_FIT
mvTable_SizingFixedSame = mvTableSizing.FIXED_SAME
mvTable_SizingStretchProp = mvTableSizing.STRETCH_PROP
mvTable_SizingStretchSame = mvTableSizing.STRETCH_SAME




# [ input codes ]

class _CodeMapEnumType(enum.EnumMeta):
    def __getitem__(self, name: str):
        key = name.upper().replace(" ", "_").replace("-", "_")
        try:
            return self._member_map_[key]
        except KeyError:
            raise KeyError(name) from None


class KeyCode(enum.IntEnum, metaclass=_CodeMapEnumType):
    """Contains all possible values for handler and input key arguments."""
    MOD_DISABLED = _dearpygui.mvKey_ModDisabled  # -1
    NONE = ANY = _dearpygui.mvKey_None  # 0  <default value>
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
    S = _dearpygui.mvKey_S  # 564
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

mvKey = KeyCode
mvKey.EQUAL._add_alias_('=')
mvKey.SEMICOLON._add_alias_(';')
mvKey.GRAVE_ACCENT._add_alias_('`')
mvKey.APOSTROPHE._add_alias_('\'')

mvKey_ModDisabled = mvKey.MOD_DISABLED
mvKey_None = mvKey.NONE; mvKey_None._add_alias_(''); mvKey_None._add_value_alias_(None)
mvKey_Clear = mvKey.CLEAR
mvKey_Prior = mvKey.PRIOR
mvKey_Next = mvKey.NEXT
mvKey_Select = mvKey.SELECT
mvKey_Execute = mvKey.EXECUTE
mvKey_Help = mvKey.HELP
mvKey_LWin = mvKey.L_WIN
mvKey_RWin = mvKey.R_WIN
mvKey_Apps = mvKey.APPS
mvKey_Sleep = mvKey.SLEEP
mvKey_F25 = mvKey.F25
mvKey_Browser_Refresh = mvKey.BROWSER_REFRESH
mvKey_Browser_Stop = mvKey.BROWSER_STOP
mvKey_Browser_Search = mvKey.BROWSER_SEARCH
mvKey_Browser_Favorites = mvKey.BROWSER_FAVORITES
mvKey_Browser_Home = mvKey.BROWSER_HOME
mvKey_Volume_Mute = mvKey.VOLUME_MUTE; mvKey_Volume_Mute._add_alias_("VOL+")
mvKey_Volume_Down = mvKey.VOLUME_DOWN; mvKey_Volume_Down._add_alias_("VOL_")
mvKey_Volume_Up = mvKey.VOLUME_UP; mvKey_Volume_Up._add_alias_("VOL/")
mvKey_Media_Next_Track = mvKey.MEDIA_NEXT_TRACK
mvKey_Media_Prev_Track = mvKey.MEDIA_PREV_TRACK
mvKey_Media_Stop = mvKey.MEDIA_STOP
mvKey_Media_Play_Pause = mvKey.MEDIA_PLAY_PAUSE
mvKey_Launch_Mail = mvKey.LAUNCH_MAIL
mvKey_Launch_Media_Select = mvKey.LAUNCH_MEDIA_SELECT
mvKey_Launch_App1 = mvKey.LAUNCH_APP_1
mvKey_Launch_App2 = mvKey.LAUNCH_APP_2
mvKey_Colon = mvKey.COLON; mvKey_Colon._add_alias_(':')
mvKey_Plus = mvKey.PLUS
mvKey_Tilde = mvKey.TILDE; mvKey_Tilde._add_alias_('~')
mvKey_Quote = mvKey.QUOTE; mvKey_Quote._add_alias_('"')
mvKey_Tab = mvKey.TAB
mvKey_Left = mvKey.LEFT
mvKey_Right = mvKey.RIGHT
mvKey_Up = mvKey.UP
mvKey_Down = mvKey.DOWN
mvKey_Home = mvKey.HOME
mvKey_End = mvKey.END
mvKey_Insert = mvKey.INSERT
mvKey_Delete = mvKey.DELETE
mvKey_Back = mvKey.BACK
mvKey_Spacebar = mvKey.SPACEBAR
mvKey_Return = mvKey.RETURN
mvKey_Escape = mvKey.ESCAPE
mvKey_LControl = mvKey.L_CONTROL
mvKey_LShift = mvKey.L_SHIFT
mvKey_LAlt = mvKey.L_ALT
mvKey_RControl = mvKey.R_CONTROL
mvKey_RShift = mvKey.R_SHIFT
mvKey_RAlt = mvKey.R_ALT
mvKey_Menu = mvKey.MENU
mvKey_0 = mvKey.DIGIT_0; mvKey.DIGIT_0._add_alias_('0')
mvKey_1 = mvKey.DIGIT_1; mvKey.DIGIT_1._add_alias_('1')
mvKey_2 = mvKey.DIGIT_2; mvKey.DIGIT_2._add_alias_('2')
mvKey_3 = mvKey.DIGIT_3; mvKey.DIGIT_3._add_alias_('3')
mvKey_4 = mvKey.DIGIT_4; mvKey.DIGIT_4._add_alias_('4')
mvKey_5 = mvKey.DIGIT_5; mvKey.DIGIT_5._add_alias_('5')
mvKey_6 = mvKey.DIGIT_6; mvKey.DIGIT_6._add_alias_('6')
mvKey_7 = mvKey.DIGIT_7; mvKey.DIGIT_7._add_alias_('7')
mvKey_8 = mvKey.DIGIT_8; mvKey.DIGIT_8._add_alias_('8')
mvKey_9 = mvKey.DIGIT_9; mvKey.DIGIT_9._add_alias_('9')
mvKey_A = mvKey.A
mvKey_B = mvKey.B
mvKey_C = mvKey.C
mvKey_D = mvKey.D
mvKey_E = mvKey.E
mvKey_F = mvKey.F
mvKey_G = mvKey.G
mvKey_H = mvKey.H
mvKey_I = mvKey.I
mvKey_J = mvKey.J
mvKey_K = mvKey.K
mvKey_L = mvKey.L
mvKey_M = mvKey.M
mvKey_N = mvKey.N
mvKey_O = mvKey.O
mvKey_P = mvKey.P
mvKey_Q = mvKey.Q
mvKey_R = mvKey.R
mvKey_S = mvKey.S
mvKey_T = mvKey.T
mvKey_U = mvKey.U
mvKey_V = mvKey.V
mvKey_W = mvKey.W
mvKey_X = mvKey.X
mvKey_Y = mvKey.Y
mvKey_Z = mvKey.Z
mvKey_F1 = mvKey.F1
mvKey_F2 = mvKey.F2
mvKey_F3 = mvKey.F3
mvKey_F4 = mvKey.F4
mvKey_F5 = mvKey.F5
mvKey_F6 = mvKey.F6
mvKey_F7 = mvKey.F7
mvKey_F8 = mvKey.F8
mvKey_F9 = mvKey.F9
mvKey_F10 = mvKey.F10
mvKey_F11 = mvKey.F11
mvKey_F12 = mvKey.F12
mvKey_F13 = mvKey.F13
mvKey_F14 = mvKey.F14
mvKey_F15 = mvKey.F15
mvKey_F16 = mvKey.F16
mvKey_F17 = mvKey.F17
mvKey_F18 = mvKey.F18
mvKey_F19 = mvKey.F19
mvKey_F20 = mvKey.F20
mvKey_F21 = mvKey.F21
mvKey_F22 = mvKey.F22
mvKey_F23 = mvKey.F23
mvKey_F24 = mvKey.F24
mvKey_Comma = mvKey.COMMA; mvKey_Comma._add_alias_(',')
mvKey_Minus = mvKey.MINUS
mvKey_Period = mvKey.PERIOD
mvKey_Slash = mvKey.SLASH
mvKey_Open_Brace = mvKey.OPEN_BRACE; mvKey_Open_Brace._add_alias_('[')
mvKey_Backslash = mvKey.BACKSLASH; mvKey_Backslash._add_alias_('\\')
mvKey_Close_Brace = mvKey.CLOSE_BRACE; mvKey_Close_Brace._add_alias_(']')
mvKey_CapsLock = mvKey.CAPS_LOCK
mvKey_ScrollLock = mvKey.SCROLL_LOCK
mvKey_NumLock = mvKey.NUM_LOCK
mvKey_Print = mvKey.PRINT
mvKey_Pause = mvKey.PAUSE
mvKey_NumPad0 = mvKey.NUMPAD_0
mvKey_NumPad1 = mvKey.NUMPAD_1
mvKey_NumPad2 = mvKey.NUMPAD_2
mvKey_NumPad3 = mvKey.NUMPAD_3
mvKey_NumPad4 = mvKey.NUMPAD_4
mvKey_NumPad5 = mvKey.NUMPAD_5
mvKey_NumPad6 = mvKey.NUMPAD_6
mvKey_NumPad7 = mvKey.NUMPAD_7
mvKey_NumPad8 = mvKey.NUMPAD_8
mvKey_NumPad9 = mvKey.NUMPAD_9
mvKey_Decimal = mvKey.DECIMAL; mvKey_Decimal._add_alias_('.')
mvKey_Divide = mvKey.DIVIDE; mvKey_Divide._add_alias_('/')
mvKey_Multiply = mvKey.MULTIPLY; mvKey_Multiply._add_alias_('*')
mvKey_Subtract = mvKey.SUBTRACT; mvKey_Subtract._add_alias_('-')
mvKey_Add = mvKey.ADD; mvKey_Add._add_alias_('+')
mvKey_NumPadEnter = mvKey.NUMPAD_ENTER
mvKey_NumPadEqual = mvKey.NUMPAD_EQUAL
mvKey_Browser_Back = mvKey.BROWSER_BACK
mvKey_Browser_Forward = mvKey.BROWSER_FORWARD
mvKey_ModCtrl = mvKey.MOD_CTRL
mvKey_ModShift = mvKey.MOD_SHIFT
mvKey_ModAlt = mvKey.MOD_ALT
mvKey_ModSuper = mvKey.MOD_SUPER


class PointerCode(enum.IntEnum, metaclass=_CodeMapEnumType):
    """Contains all possible values for *button* mouse event
    arguments.
    """
    NONE = ANY = -1  # <default value>
    LEFT = L = _dearpygui.mvMouseButton_Left  # 0
    RIGHT = R = _dearpygui.mvMouseButton_Right  # 1
    MIDDLE = M = _dearpygui.mvMouseButton_Middle  # 2
    X1 = _dearpygui.mvMouseButton_X1  # 3
    X2 = _dearpygui.mvMouseButton_X2  # 4

mvMouseButton = PointerCode
mvMouseButton.ANY._add_alias_('')
mvMouseButton.ANY._add_value_alias_(None)

mvMouseButton_Left = mvMouseButton.LEFT
mvMouseButton_Right = mvMouseButton.RIGHT
mvMouseButton_Middle = mvMouseButton.MIDDLE
mvMouseButton_X1 = mvMouseButton.X1
mvMouseButton_X2 = mvMouseButton.X2
