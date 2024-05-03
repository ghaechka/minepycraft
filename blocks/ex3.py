from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def build_cube(x, y, z, size, block_type):
    """ Функция для строительства куба заданного размера и типа блока """
    for i in range(size):
        for j in range(size):
            for k in range(size):
                mc.setBlock(x + i, y + j, z + k, block_type)

# Координаты для начала строительства
start_x, start_y, start_z = 10, 11, 12
cube_size = 3  # Размер стороны куба

# Вызов функции для строительства куба из камня
build_cube(start_x, start_y, start_z, cube_size, 1)
