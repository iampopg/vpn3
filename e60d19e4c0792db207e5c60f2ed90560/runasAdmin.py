import ctypes
commands = u'cd vpn3'
ctypes.windll.shell32.ShellExecuteW(
        None,
        u"runas",
        u"cmd.exe",
        commands,
        None,
        1
    )