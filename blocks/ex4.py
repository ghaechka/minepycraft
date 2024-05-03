from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

# Получение текущих координат игрока
x, y, z = mc.player.getPos()

# Размеры поля
width = 10  # ширина поля
length = 5  # длина поля

# Создание поля вспаханной земли
for i in range(width):
    for j in range(length):
        # Устанавливаем блок вспаханной земли (тип блока 60) немного ниже уровня ног игрока
        mc.setBlock(x + i + 1, y - 1, z + j + 1, block.FARMLAND.id)
