import sys
#from PySquashfsImage import SquashFsImage

class FirmwarePart:
    def __init__(self, name, offset, size, type=""):
        self.name = name
        self.offset = offset
        self. size = size
        self.type = type

firmware_parts = [
    FirmwarePart("uImage_header", 0x39000, 0x40, "header"),
    FirmwarePart("uImage_kernel", 0x39040, 0x377B, "kernel"),
    FirmwarePart("squashfs_0", 0x23B000, 0x180000, "squashfs"),
    FirmwarePart("squashfs_1", 0x438000, 0x3E917C, "squashfs"),
    FirmwarePart("JFFS2_0", 0x3BB000, 0x181C4, "jffs2"),
    FirmwarePart("JFFS2_1", 0x3D392C, 0x7908, "jffs2"),
    FirmwarePart("JFFS2_3", 0x3DBAA4, 0x3F18, "jffs2"),
    FirmwarePart("JFFS2_4", 0x3DF9BC, 0x58644, "jffs2")
]


if len(sys.argv) <= 2:
    print("usage: extract.py unpack 'file'")
    sys.exit()

if sys.argv[1] == "unpack":
    inF = open(sys.argv[2], "rb")
    for part in firmware_parts:
        outF = open("./img/" + part.name + ".img", "wb")
        inF.seek(part.offset)
        data = inF.read(part.size)
        outF.write(data)
        outF.close()
        print(f"Wrote {part.name}: {hex(len(data))} bytes")
    '''
    for part in firmware_parts:
        if part.type == "squashfs":
            print(part.name)
            image = SquashFsImage("./img/" + part.name + ".img")
            for i in image.root.findAll():
                #path = i.getName()
                print(i.getPath())
                print(i.getContent())
                #with open(path, 'wb') as f:
                #    print(f"Saving File: {i.getName()}")
                #    f.write(i.getContent())
                '''