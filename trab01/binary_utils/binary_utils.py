import sys
import os


class BinaryUtils:
    def _generate_default_file_path(self, file_path: str):
        for i in range(len(file_path))[::-1]:
            if file_path[i] == '.':
                start_index = i
                break

        file_extension = file_path[start_index+1:]

        result = file_path[:start_index]
        result = f'{result}_safecopy.{file_extension}'

        return result

    def safe_copy(self, file_path: str, resulting_file_path: str = 'DEFAULT', start: int = 0, end: int = 0):
        file_size = os.path.getsize(file_path)

        if start < 0 or start > end:
            return False

        if end < start or end >= file_size:
            return False

        if resulting_file_path == 'DEFAULT':
            resulting_file_path = self._generate_default_file_path(file_path)

        if end == 0:
            end = file_size - 1

        with open(file_path, mode='rb') as initial_file, open(resulting_file_path, mode='wb') as resulting_file:
            character = initial_file.read(1)
            current = 0

            while character:
                if current >= start and current <= end:
                    correct_character = 0xff & character[0]
                    correct_character = correct_character.to_bytes(
                        1, sys.byteorder)

                    resulting_file.write(correct_character)

                character = initial_file.read(1)
                current += 1

        return True

    def _write_beggining(self, file_path: str, text: bytes) -> bool:
        file_size = os.path.getsize(file_path)

        with open(file_path, mode='rb+') as file:
            characters_copy = file.read(file_size)
            file.seek(-file_size, 1)

            for character in text:
                correct_character = character.to_bytes(1, sys.byteorder)
                file.write(correct_character)

            for character in characters_copy:
                correct_character = 0xff & character
                correct_character = correct_character.to_bytes(
                    1, sys.byteorder)

                file.write(correct_character)

            return True

    def _write_middle(self, file_path: str, text: bytes, position: int) -> bool:
        with open(file_path, mode='rb+') as file:
            file.seek(position, 0)

            for character in text:
                correct_character = 0xff & character
                correct_character = correct_character.to_bytes(
                    1, sys.byteorder)

                file.write(correct_character)
        
        return True

    def _write_end(self, file_path: str, text: bytes) -> bool:
        file_size = os.path.getsize(file_path)

        with open(file_path, mode='rb+') as file:
            file.seek(file_size, 0)

            for character in text:
                correct_character = 0xff & character
                correct_character = correct_character.to_bytes(
                    1, sys.byteorder)

                file.write(correct_character)
        
        return True

    def write(self, file_path: str, text: bytes, position: int) -> bool:
        file_size = os.path.getsize(file_path)
        text_size = len(text)

        if position < -text_size:
            return False

        if position < 0 and abs(position) == text_size:
            self._write_beggining(file_path, text)
            return True
        
        if position >= 0 and position < file_size:
            self._write_middle(file_path, text, position)
            return True
        
        if position >= file_size:
            self._write_end(file_path, text)
            return True
