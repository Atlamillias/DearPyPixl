from __future__ import annotations
from enum import Enum

from dearpygui import core as idpg

from .tools import Constant, dataclass

# There are a LOT of constants. Using classes to act as
# pseudo-namespaces is generally un-Pythonic. In this case,
# the options are "have lots of classes" or "have lots of modules"
# to contain these. By using classes, the means of lookup are more
# convenient and can be easily modified without an unsightly mess.

# Note: 99% of the constants here return integers (UUID).

# Note: The only reason the dataclasses aren't Enum
# is because the values are important and I'm too lazy
# to type "Enum.value".




AppHandlerRegistry = idpg.mvHandlerRegistry

# A AppHandlerRegistry item must be the parent for
# KeyHandler and MouseHandler items.
@dataclass
class KeyHandler(Constant):
    Down = idpg.add_key_down_handler  # idpg.mvKeyDownHandler | while key is down
    Press = idpg.add_key_press_handler  # idpg.mvKeyPressHandler
    Release = idpg.add_key_release_handler  # idpg.mvKeyReleaseHandler

@dataclass
class MouseHandler(Constant):
    Down =  idpg.add_mouse_down_handler  # idpg.mvMouseDownHandler | while button is down
    Click = idpg.add_mouse_click_handler  #  idpg.mvMouseClickHandler
    DoubleClick = idpg.add_mouse_double_click_handler  # idpg.mvMouseDoubleClickHandler
    Wheel = idpg.add_mouse_wheel_handler  # idpg.mvMouseWheelHandler
    Move = idpg.add_mouse_move_handler  # idpg.mvMouseMoveHandler
    Release = idpg.add_mouse_release_handler  # idpg.mvMouseReleaseHandler
    Drag = idpg.add_mouse_drag_handler  # idpg.mvMouseDragHandler

# A widget item must be the parent for WidgetHandler items.
@dataclass
class WidgetHandler(Constant):
    Activated = idpg.add_activated_handler  # idpg.mvActivatedHandler | while item is active
    Active = idpg.add_active_handler  # idpg.mvActiveHandler
    Clicked = idpg.add_clicked_handler  # idpg.mvClickedHandler
    DeactivatedAfterEdit = idpg.add_deactivated_after_edit_handler  # idpg.mvDeactivatedAfterEditHandler
    Deactivated = idpg.add_deactivated_handler  # idpg.mvDeactivatedHandler
    Edited = idpg.add_edited_handler  # idpg.mvEditedHandler
    Focus = idpg.add_focus_handler  # idpg.mvFocusHandler
    Hover = idpg.add_hover_handler  # idpg.mvHoverHandler
    Resize = idpg.add_resize_handler  # idpg.mvResizeHandler
    ToggledOpen = idpg.add_toggled_open_handler  # idpg.mvToggledOpenHandler
    Visible = idpg.add_visible_handler  # idpg.mvVisibleHandler




@dataclass
class Tool(Constant):  # idpg.show_tool(<tool>)
    About = idpg.mvTool_About
    Debug = idpg.mvTool_Debug
    Doc = idpg.mvTool_Doc
    ItemRegistry = idpg.mvTool_ItemRegistry
    Metrics = idpg.mvTool_Metrics
    Style = idpg.mvTool_Style
    Font = idpg.mvTool_Font




@dataclass
class KeyCode(Constant):
    Key0 = idpg.mvKey_0
    Key1 = idpg.mvKey_1
    Key2 = idpg.mvKey_2
    Key3 = idpg.mvKey_3
    Key4 = idpg.mvKey_4
    Key5 = idpg.mvKey_5
    Key6 = idpg.mvKey_6
    Key7 = idpg.mvKey_7
    Key8 = idpg.mvKey_8
    Key9 = idpg.mvKey_9
    Num0 = idpg.mvKey_NumPad0
    Num1 = idpg.mvKey_NumPad1
    Num2 = idpg.mvKey_NumPad2
    Num3 = idpg.mvKey_NumPad3
    Num4 = idpg.mvKey_NumPad4
    Num5 = idpg.mvKey_NumPad5
    Num6 = idpg.mvKey_NumPad6
    Num7 = idpg.mvKey_NumPad7
    Num8 = idpg.mvKey_NumPad8
    Num9 = idpg.mvKey_NumPad9
    A = idpg.mvKey_A
    B = idpg.mvKey_B
    C = idpg.mvKey_C
    D = idpg.mvKey_D
    E = idpg.mvKey_E
    F = idpg.mvKey_F
    G = idpg.mvKey_G
    H = idpg.mvKey_H
    I = idpg.mvKey_I
    J = idpg.mvKey_J
    K = idpg.mvKey_K
    L = idpg.mvKey_L
    M = idpg.mvKey_M
    N = idpg.mvKey_N
    O = idpg.mvKey_O
    P = idpg.mvKey_P
    Q = idpg.mvKey_Q
    R = idpg.mvKey_R
    S = idpg.mvKey_S
    T = idpg.mvKey_T
    U = idpg.mvKey_U
    V = idpg.mvKey_V
    W = idpg.mvKey_W
    X = idpg.mvKey_X
    Y = idpg.mvKey_Y
    Z = idpg.mvKey_Z
    F1 = idpg.mvKey_F1
    F2 = idpg.mvKey_F2
    F3 = idpg.mvKey_F3
    F4 = idpg.mvKey_F4
    F5 = idpg.mvKey_F5
    F6 = idpg.mvKey_F6
    F7 = idpg.mvKey_F7
    F8 = idpg.mvKey_F8
    F9 = idpg.mvKey_F9
    F10 = idpg.mvKey_F10
    F11 = idpg.mvKey_F11
    F12 = idpg.mvKey_F12
    F13 = idpg.mvKey_F13
    F14 = idpg.mvKey_F14
    F15 = idpg.mvKey_F15
    F16 = idpg.mvKey_F16
    F17 = idpg.mvKey_F17
    F18 = idpg.mvKey_F18
    F19 = idpg.mvKey_F19
    F20 = idpg.mvKey_F20
    F21 = idpg.mvKey_F21
    F22 = idpg.mvKey_F22
    F23 = idpg.mvKey_F23
    F24 = idpg.mvKey_F24
    Up = idpg.mvKey_Up
    Left = idpg.mvKey_Left
    Down = idpg.mvKey_Down
    Right = idpg.mvKey_Right
    Add = idpg.mvKey_Add
    Divide = idpg.mvKey_Divide
    Plus = idpg.mvKey_Plus
    Minus = idpg.mvKey_Minus
    Multiply = idpg.mvKey_Multiply
    Subtract = idpg.mvKey_Subtract
    Alt = idpg.mvKey_Alt
    Apps = idpg.mvKey_Apps
    Back = idpg.mvKey_Back
    Backslash = idpg.mvKey_Backslash
    Browser_Back = idpg.mvKey_Browser_Back
    Browser_Favorites = idpg.mvKey_Browser_Favorites
    Browser_Forward = idpg.mvKey_Browser_Forward
    Browser_Home = idpg.mvKey_Browser_Home
    Browser_Refresh = idpg.mvKey_Browser_Refresh
    Browser_Search = idpg.mvKey_Browser_Search
    Browser_Stop = idpg.mvKey_Browser_Stop
    Caps_Lock = idpg.mvKey_Capital
    Clear = idpg.mvKey_Clear
    Close_Brace = idpg.mvKey_Close_Brace
    Colon = idpg.mvKey_Colon
    Comma = idpg.mvKey_Comma
    Control = idpg.mvKey_Control
    Decimal = idpg.mvKey_Decimal
    Delete = idpg.mvKey_Delete
    End = idpg.mvKey_End
    Escape = idpg.mvKey_Escape
    Execute = idpg.mvKey_Execute
    Help = idpg.mvKey_Help
    Home = idpg.mvKey_Home
    Insert = idpg.mvKey_Insert
    L_Control = idpg.mvKey_LControl
    L_Menu = idpg.mvKey_LMenu
    L_Shift = idpg.mvKey_LShift
    L_Win = idpg.mvKey_LWin
    Next = idpg.mvKey_Next
    Num_Lock = idpg.mvKey_NumLock
    Open_Brace = idpg.mvKey_Open_Brace
    Pause = idpg.mvKey_Pause
    Period = idpg.mvKey_Period
    Print = idpg.mvKey_Print
    Print_Screen = idpg.mvKey_PrintScreen
    Prior = idpg.mvKey_Prior
    Quote = idpg.mvKey_Quote
    R_Control = idpg.mvKey_RControl
    R_Menu = idpg.mvKey_RMenu
    R_Shift = idpg.mvKey_RShift
    R_Win = idpg.mvKey_RWin
    Return = idpg.mvKey_Return
    Scroll_Lock = idpg.mvKey_ScrollLock
    Select = idpg.mvKey_Select
    Separator = idpg.mvKey_Separator
    Shift = idpg.mvKey_Shift
    Slash = idpg.mvKey_Slash
    Sleep = idpg.mvKey_Sleep
    Spacebar = idpg.mvKey_Spacebar
    Tab = idpg.mvKey_Tab
    Tilde = idpg.mvKey_Tilde
    Launch_App1 = idpg.mvKey_Launch_App1
    Launch_App2 = idpg.mvKey_Launch_App2
    Launch_Mail = idpg.mvKey_Launch_Mail
    Launch_Media_Select = idpg.mvKey_Launch_Media_Select
    Next_Track = idpg.mvKey_Media_Next_Track
    Play_Pause = idpg.mvKey_Media_Play_Pause
    Prev_Track = idpg.mvKey_Media_Prev_Track
    Stop = idpg.mvKey_Media_Stop
    Vol_Down = idpg.mvKey_Volume_Down
    Vol_Mute = idpg.mvKey_Volume_Mute
    Vol_Up = idpg.mvKey_Volume_Up

class Key(Enum):
    Key0 = "0"
    Key1 = "1"
    Key2 = "2"
    Key3 = "3"
    Key4 = "4"
    Key5 = "5"
    Key6 = "6"
    Key7 = "7"
    Key8 = "8"
    Key9 = "9"
    Plus = "+"
    Minus = "-"
    Multiply = "num*"
    Add = "num+"
    Subtract = "num-"
    Divide = "num/"
    Backslash = r"\\"
    Browser_Back = "bback"
    Browser_Favorites = "bfavorites"
    Browser_Forward = "bforward"
    Browser_Home = "bhome"
    Browser_Refresh = "brefresh"
    Browser_Search = "bsearch"
    Browser_Stop = "bstop"
    Close_Brace = "]"
    Colon = ":"
    Comma = ","
    Control = "ctrl"
    Delete = "del"
    Decimal = "num."
    Escape = "esc"
    Execute = "exec"
    Insert = "ins"
    L_Control = "lctrl"
    Open_Brace = "["
    Period = "."
    Print_Screen = "prtscr"
    R_Control = "rctrl"
    Quote = "'"
    Slash = r"/"
    Spacebar = "space"
    Tilde = "~"
    Launch_App1 = "app1"
    Launch_App2 = "app2"
    Launc_hMail = "mail"
    Launch_Media_Select = "mediaselect"
    Next_Track = "nexttrack"
    Play_Pause = "playpause"
    Prev_Track = "prevtrack"
    Stop = "stop"
    Vol_Down = "vol-"
    Vol_Mute = "mute"
    Vol_Up = "vol+"

@dataclass
class Mouse(Constant):
    Left = idpg.mvMouseButton_Left
    Right = idpg.mvMouseButton_Right
    Middle = idpg.mvMouseButton_Middle
    Button1 = idpg.mvMouseButton_X1
    Button2 = idpg.mvMouseButton_X2
