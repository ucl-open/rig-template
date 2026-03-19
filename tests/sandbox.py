from copier import run_copy
import os

if os.path.exists("./tmp_template"):
    os.remove("./tmp_template")
os.mkdir("./tmp_template")

run_copy("./", "./tmp_template", defaults=True)
