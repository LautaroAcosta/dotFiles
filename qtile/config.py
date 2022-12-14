
#Catppuccin Colors
blue = '#89B4F4'
background = '#1e1e2e'
text = '#cdd6f4'
red = '#f38ba8'
yellow = '#f9e2af'
green = '#a6e3a1'


from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty"
flameshot = "flameshot gui --clipboard"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn('rofi -show drun'), desc="Spawn a command using a prompt widget"),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer sset Master,0 5%-')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer sset Master,0 5%+')),
    # Key([mod], "s", lazy.spawn('~/Programs/Bash/flame.sh')),
    Key([mod], "s", lazy.spawn(flameshot)),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [

            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )


layout_defaults = dict(
    border_focus=blue,
    border_normal=background,
    # border_focus_stack=c_alt,
    # border_normal_stack=c_bgn,
    grow_amount=10,
    margin = 2,
)

layouts = [
    layout.Columns(fair = True, **layout_defaults),
    layout.Max(fair=True, **layout_defaults),
    # layout.Stack(num_stacks=2),
    layout.Bsp(fair=True, **layout_defaults),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    layout.VerticalTile(fair=True, **layout_defaults),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Fira Code Nerd Font",
    fontsize=12,
    padding=3,
    foreground = text
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper ='~/Pictures/wallhaven-yxmm3g.png',
        # wallpaper ='~/Pictures/wallhaven-vqgxq8.jpg',
        # wallpaper ='~/Pictures/wallhaven-kxw9o1.png',
        # wallpaper ='~/Pictures/wallhaven-3l9z69.png',
        # wallpaper = '~/Pictures/wallhaven-7pgy5y.png',
        wallpaper_mode='default',
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.7),
                widget.GroupBox(highlight_method='block', foreground=green, active=text, ),
                widget.Prompt(),
                widget.WindowName(max_chars=15),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Pomodoro(color_inactive=blue, color_active=green, color_break=yellow),
                widget.Volume(),
                widget.DF(visible_on_warn=False),
                widget.Net(interface='wlx1caff768f339',format='??? {up} ??? {down}'),
                widget.OpenWeather(app_key='8f764bacadc847395394ff30507a886c',cityid="3435217",language='es', format=' {temp} ??{units_temperature}, {icon}'),
                widget.Clock(format="%a, %b %d %H:%M %p", foreground=blue),
            ],
            22,
            border_width=[2, 0, 2, 0],  
            opacity= 0.3,
        ),
    ),
     Screen(
        wallpaper ='~/Pictures/wallhaven-yxmm3g.png',
        # wallpaper ='~/Pictures/wallhaven-vqgxq8.jpg',
        # wallpaper ='~/Pictures/wallhaven-kxw9o1.png',
        # wallpaper ='~/Pictures/wallhaven-3l9z69.png',
        # wallpaper = '~/Pictures/wallhaven-7pgy5y.png',
        wallpaper_mode='default',
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.7),
                widget.GroupBox(highlight_method='block', foreground=green, active=text, ),
                widget.Prompt(),
                widget.WindowName(max_chars=15),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Volume(),
                widget.DF(visible_on_warn=False),
                widget.OpenWeather(app_key='8f764bacadc847395394ff30507a886c',cityid="3435217",language='es', format=' {temp} ??{units_temperature}, {icon}'),
                widget.Clock(format="%a, %b %d %H:%M %p", foreground=blue),
            ],
            22,
            border_width=[2, 0, 2, 0],  
            opacity= 0.3,
        ),
    ),

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
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
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
