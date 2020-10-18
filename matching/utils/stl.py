import stl
import numpy as np
from stl import mesh

# モデルのx、y、zを得る 単位mm
def find_mins_maxs(obj):
    minx = obj.x.min()
    maxx = obj.x.max()
    miny = obj.y.min()
    maxy = obj.y.max()
    minz = obj.z.min()
    maxz = obj.z.max()
    w1 = maxx - minx
    l1 = maxy - miny
    h1 = maxz - minz
    model = [w1, l1, h1]

    return model

# プリント可能かどうか


def allowprint(printer, model):
    printer2 = printer.copy()
    model2 = model.copy()
    printer2.sort()
    model2.sort()

    for i in range(3):
        if printer2[i] < model2[i]:
            return False

    return True

def canPrint(printer_max_xyz, stl_path):
    m = mesh.Mesh.from_file(stl_path)
    model = find_mins_maxs(m)
    return allowprint(printer_max_xyz, model)
