from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Начальные координаты
x, y, z = 10, 11, 12
width = 10  # Ширина стены

# Создание стены из камня
for i in range(width):
    mc.setBlock(x + i, y, z, 1)
