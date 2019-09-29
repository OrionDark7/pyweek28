import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name = "O2 Space Salvage",
    options = {"build_exe":{"packages":["pygame"], "include_files":[]}},
    description = "O2 Space Salvage - Post-Mortem Update 3",
    version = "PM 3",
    executables = executables
)
