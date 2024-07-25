from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
    ErrorModule(e)

Title("Obfuscator Tool (Paid)")

try:
    print(f"{INFO} still deciding if i can even code this")
    print(f"{INFO} The tool would be paid and can be purchased on discord\n")
    webbrowser.open_new_tab(f"https://{discord_server}")
    Continue()
    Reset()
except Exception as e:
    Error(e)
