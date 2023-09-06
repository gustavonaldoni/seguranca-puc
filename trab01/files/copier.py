import sys
import re


class FileCopier:
    def _generate_default_file_path(self, file_path: str):
        for i in range(len(file_path))[::-1]:
            if file_path[i] == '.':
                start_index = i
                break

        file_extension = file_path[start_index+1:]

        result = file_path[:start_index]
        result = f'{result}_safecopy.{file_extension}'

        return result

    def safe_copy(self, file_path: str, resulting_file_path: str = 'DEFAULT'):
        if resulting_file_path == 'DEFAULT':
            resulting_file_path = self._generate_default_file_path(file_path)

        with open(file_path, mode='rb') as initial_file, open(resulting_file_path, mode='wb') as resulting_file:
            character = initial_file.read(1)

            while character:
                correct_character = 0xff & character[0]
                correct_character = correct_character.to_bytes(
                    1, sys.byteorder)

                resulting_file.write(correct_character)

                character = initial_file.read(1)
