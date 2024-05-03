from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Координаты для размещения блока
x, y, z = 10, 11, 12

# Установка блока (в данном случае, камня) по координатам x, y, z
mc.setBlock(x, y, z, 1)
