# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger
import traverse
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.client_new
def new_client(client):
    #logger.warning(type(client.wid))
    #logger.warning(client.wid)
    if "stremio" in client.name.lower() :
        out=subprocess.run(["xset","s","off"],capture_output=True)
        #logger.warning(out)
@hook.subscribe.client_killed
def client_killed(client):
    if "stremio" in client.name.lower() :
        subprocess.run(["xset", "s", "on"])


myBrowser = "google-chrome"       # My browser of choice

mod = "mod4"
terminal = guess_terminal()

keys = [
    #
    Key(["mod1"], "Space", lazy.spawn('rofi -show combi -modes combi -combi-modi "drun,run"'), desc="rofi modi"),
    Key([mod,"shift"], "c", lazy.spawn("google-chrome"), desc='Web browser'),
    Key(["mod1"], "a", lazy.spawn('rofi -show window'), desc="Show All Windows"),

    #bindsym Mod1+Space exec rofi -show combi -modes combi -combi-modi "drun,run"


    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.function(traverse.down), desc="Move focus down"),
    Key([mod], "Up", lazy.function(traverse.up), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # move current window to the top of the stack 
    Key([mod], "Return", lazy.layout.swap_main(), desc="Move window to the top of the stack"),
    #Focus Next Monitor
    Key([mod], 'l', lazy.next_screen(), desc='Next monitor'),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Down", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "control"], "Up", lazy.layout.grow(), desc="Grow window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    #Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod],"f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control","shift"], "q", lazy.spawn("shutdown now"), desc="Shutdown"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Volume Control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc='Volume Mute'),
    
    Key([mod], "h", lazy.hide_show_bar(), desc="hide show bars"),
    Key(["mod1","shift","control"], "v", lazy.spawn("rofi-copyq"), desc="clipboard manager"),


    
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )
darkGray='#282738'

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

groups = [
    # Screen affinity here is used to make
    # sure the groups startup on the right screens
    Group(name="a", screen_affinity=0,label="󰏃"),
    Group(name="s", screen_affinity=0, label="󰏃"),
    Group(name="d", screen_affinity=0,label="󰏃"),
    Group(name="1", screen_affinity=1,label="󰏃"),
    Group(name="2", screen_affinity=1,label="󰏃"),
    Group(name="3", screen_affinity=1,label="󰏃"),
]
groupbox1 = widget.GroupBox(
        visible_groups=['1', '2', '3'],
        fontsize=24,
        borderwidth=3,
        highlight_method='block',
        active='#CAA9E0',
        block_highlight_text_color="#91B1F0",
        highlight_color='#4B427E',
        inactive='353446',
        foreground='#4B427E',
        background=darkGray,
        this_current_screen_border='#353446',
        this_screen_border='#353446',
        other_current_screen_border='#353446',
        other_screen_border='#353446',
        urgent_border='#353446',
        rounded=True,
        disable_drag=True,

        )
groupbox2 = widget.GroupBox(visible_groups=['a', 's', 'd'])

def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in '123':
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()

    return _inner

def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        if name in "123":
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        else:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()

    return _inner

for i in groups:
    keys.append(Key([mod, "shift"], i.name, lazy.function(go_to_group_and_move_window(i.name))))

for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))

layouts = [
    layout.MonadTall(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

getVol = "pactl get-sink-volume  @DEFAULT_SINK@ | awk '{print $5}'"
toggMute = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
getMute = "pactl get-sink-mute @DEFAULT_SINK@"
checkMuteString = 'Mute: yes'
screens = [
    Screen(
        wallpaper="~/Pictures/wallpapers/Simon-THE_ELECTRIC_STATE.jpg",
        wallpaper_mode='fill',
        bottom=bar.Bar(
            [
                groupbox2,
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Volume(
                    font='JetBrainsMono Nerd Font',
                    theme_path='~/.config/qtile/assets/Volume/',
                    emoji=True,
                    fontsize=13,
                    background='#353446',
                    get_volume_command=getVol,
                    mute_command=toggMute,
                    check_mute_command=getMute,
                    check_mute_string=checkMuteString
                ),
                widget.Volume(
                    font='JetBrains Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    fontsize=13,
                    get_volume_command=getVol,
                    mute_command=toggMute,
                    check_mute_command=getMute,
                    check_mute_string=checkMuteString
                ),

                widget.BatteryIcon(
                    theme_path='~/.config/qtile/assets/Battery/',
                    background='#353446',
                    scale=1,
                ),
                widget.Battery(
                    font='JetBrains Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    format='{percent:2.0%}',
                    fontsize=13,
                ),
                widget.Image(
                    filename='~/.config/qtile/assets/3.png',
                ),

                widget.Clock(
                    format='%I:%M %p',
                    background=darkGray,
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),

                

                # widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            border_color = darkGray,
            border_width = [0,0,0,0],
            margin = [0,0,0,0],
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        x=0,y=1080
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    Screen(
        wallpaper="~/Pictures/wallpapers/Simon-THE_ELECTRIC_STATE.jpg",
        wallpaper_mode='fill',
        top=bar.Bar(
          [
              widget.Image(
                    filename='~/.config/qtile/assets/3.png',
                ),
              groupbox1,
            #   widget.WindowName(),
            #   widget.Clock()
          ],
          30,
          background=darkGray
      ),
        x=0,y=0)
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="copyq"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
