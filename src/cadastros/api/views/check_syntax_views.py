import py_compile
import glob

base = r"c:/Users/vmace/OneDrive/Documentos/Projetos Dev/Cancella Flow/cancella-flow-backend/src/cadastros/api/views"
for p in glob.glob(base + "/*.py"):
    try:
        py_compile.compile(p, doraise=True)
        print("OK:", p)
    except Exception as e:
        print("ERR:", p)
        print(e)
