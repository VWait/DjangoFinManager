#Функция walk()
import os

path = "C:\Windows\Web"

for path, dirnames, filenames in os.walk(path):
    print(f"path – {path}")
    print(f"dirnames – {dirnames}")
    print(f"filenames – {filenames}")

#Модуль os.path. Для того, чтобы путь указывался корректно независимо от системы,
# необходимо передать его в качестве аргумента в функцию normpath()
import os

path = os.path.normpath("C:/Windows/Web")

for path, dirnames, filenames in os.walk(path):
    print(f"path – {path}")
    print(f"dirnames – {dirnames}")
    print(f"filenames – {filenames}")

#Функция join()
import os

dir_1 = "Windows"
dir_2 = "Web"
path = os.path.join(dir_1, dir_2)
print(path)

"""Кроме того, с помощью функции isabs() можно
проверить, является ли путь абсолютным. А с помощью
функций isfile(), isdir(), islink() узнаем, ведет
путь к файлу, директории или ссылке"""
import os

path = os.path.normpath("C:\\Windows\\Web")
print(os.path.isabs(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.path.islink(path))




