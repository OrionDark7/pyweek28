from distutils.core import setup
import cx_Freeze

execu = [cx_Freeze.Executable("./main.py", base="WIN32GUI")]

cx_Freeze.setup(
    name = "The Infinite Tower",
    version = "1.0",
    options = {"build_exe": {"packages": ["pygame", "random", "sys"]}},
    executables = execu
)
