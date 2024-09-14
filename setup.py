from cx_Freeze import setup, Executable

# Specify the target executable name without extension (it will add .exe automatically on Windows)
executables = [
    Executable("./command_prompt - Copy.py", target_name="command_prompt",icon='.\commandpromptlogo.jpg')
]

setup(
    name="command prompt - test",
    version="1.0",
    description="goofy command prompt",
    executables=executables
)
