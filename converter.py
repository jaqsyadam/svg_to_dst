import subprocess
import os


def convert_svg_to_dst(svg_path: str, dst_path: str) -> None:
    """
    Конвертирует SVG-файл в DST с использованием Inkscape и Ink/Stitch.
    """
    try:
        # Проверяем, существует ли исходный SVG-файл
        if not os.path.exists(svg_path):
            raise FileNotFoundError(f"Файл {svg_path} не найден.")

        # Команда для конвертации через Inkscape (Ink/Stitch)
        command = [
            "inkscape",
            svg_path,
            "--export-filename", dst_path,
            "--export-type=dst"
        ]

        # Выполняем команду
        subprocess.run(command, check=True)

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Ошибка: {e}")

    except subprocess.CalledProcessError:
        raise RuntimeError(
            "Ошибка при выполнении команды Inkscape. Проверьте корректность SVG-файла и установку Ink/Stitch.")

    except Exception as e:
        raise RuntimeError(f"Произошла непредвиденная ошибка: {e}")