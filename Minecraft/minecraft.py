from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getPos()
print(x, y, z)
mc.setBlock(x, y-1, z, 56)
    

