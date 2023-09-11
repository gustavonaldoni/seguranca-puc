import sys
import os

DEFAULT_PATH = 'DEFAULT_PATH'
DEFAULT_WRITE_MODE = 'wb'
FILE_SIZE = 0


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

    def _get_correct_byte(self, byte: bytes | int) -> bytes:
        """
        Returns the copy of a byte or integer bit to bit.
        """
        if isinstance(byte, int):
            correct_byte = 0xFF & byte
        elif isinstance(byte, bytes):
            correct_byte = 0xFF & byte[0]
        else:
            raise TypeError('<byte> argument must be of type <bytes> or <int>')

        correct_byte = correct_byte.to_bytes(1, sys.byteorder)
        return correct_byte

    def save_bytes_to_file(self, file_path: str, text: bytes):
        """
        Save the text passed as bytes string to a file,
        bit to bit. If the file exists it is overwritten.
        """
        with open(file_path, mode='wb') as file:
            for character in text:
                correct_character = character.to_bytes(1, sys.byteorder)
                file.write(correct_character)

    def safe_copy_part(self, file_path: str, start: int, end: int, resulting_file_path: str = DEFAULT_PATH, write_mode: str = DEFAULT_WRITE_MODE):
        """
        Copies a file bit to bit from start to end indexes.
        """

        file_size = os.path.getsize(file_path)

        if start < 0:
            raise IndexError("The start index must be a positive integer.")

        if start > end:
            raise IndexError(
                "The start index cannot be greater than the end index.")

        if end >= file_size:
            raise IndexError("The end index must be less than que file size.")

        if resulting_file_path == DEFAULT_PATH:
            resulting_file_path = self._generate_default_file_path(file_path)

        if end == FILE_SIZE:
            end = file_size - 1

        with open(file_path, mode='rb') as initial_file, open(resulting_file_path, mode=write_mode) as resulting_file:
            initial_file.seek(start, 0)

            character = initial_file.read(1)
            current = start

            while character:
                if current >= start and current <= end:
                    correct_character = self._get_correct_byte(character)

                    resulting_file.write(correct_character)

                character = initial_file.read(1)
                current += 1

        return True

    def safe_copy(self, file_path: str, resulting_file_path: str = DEFAULT_PATH) -> bool:
        """
        Copies an entire file bit to bit.
        """

        return self.safe_copy_part(file_path, 0, FILE_SIZE, resulting_file_path)

    def _write_beggining(self, file_path: str, text: bytes) -> bool:
        file_size = os.path.getsize(file_path)

        with open(file_path, mode='rb+') as file:
            characters_copy = file.read(file_size)
            file.seek(-file_size, 1)

            for character in text:
                correct_character = self._get_correct_byte(character)
                file.write(correct_character)

            for character in characters_copy:
                correct_character = self._get_correct_byte(character)
                file.write(correct_character)

            return True

    def _write_middle(self, file_path: str, text: bytes, position: int) -> bool:
        with open(file_path, mode='rb+') as file:
            file.seek(position, 0)

            for character in text:
                correct_character = self._get_correct_byte(character)
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
        """
        Writes to a file the entire binary 
        text on the given position. Can append text
        to the beggining, using negative position, 
        or to the end of the file.
        """
        file_size = os.path.getsize(file_path)
        text_size = len(text)

        if position < -text_size:
            raise IndexError(
                'Your text cannot fill the entire beggining of the file.')

        if position < 0 and abs(position) == text_size:
            self._write_beggining(file_path, text)
            return True

        if position >= 0 and position < file_size:
            self._write_middle(file_path, text, position)
            return True

        if position >= file_size:
            self._write_end(file_path, text)
            return True

    def _diff_same_size(self, file_path1: str, file_path2: str) -> bytes:
        diff = bytearray()

        with open(file_path1, mode='rb') as file1, open(file_path2, mode='rb') as file2:
            character1 = file1.read(1)
            character2 = file2.read(1)

            while character1 and character2:
                if character1 != character2:
                    correct_character = self._get_correct_byte(character2)
                    diff.append(ord(correct_character))

                character1 = file1.read(1)
                character2 = file2.read(1)

        return bytes(diff)

    def _diff_different_size(self, file_path1: str, file_path2: str) -> bytes:
        diff = bytearray()

        file1_size = os.path.getsize(file_path1)
        file2_size = os.path.getsize(file_path2)

        if file1_size > file2_size:
            with open(file_path1, mode='rb') as file1, open(file_path2, mode='rb') as file2:
                character1 = file1.read(1)
                character2 = file2.read(1)

                while character2:
                    if character1 != character2:
                        correct_character = self._get_correct_byte(character2)
                        diff.append(ord(correct_character))

                    character1 = file1.read(1)
                    character2 = file2.read(1)

        else:
            with open(file_path1, mode='rb') as file1, open(file_path2, mode='rb') as file2:
                character1 = file1.read(1)
                character2 = file2.read(1)

                while character1:
                    if character1 != character2:
                        correct_character = self._get_correct_byte(character2)
                        diff.append(ord(correct_character))

                    character1 = file1.read(1)
                    character2 = file2.read(1)

                while character2:
                    correct_character = self._get_correct_byte(character2)
                    diff.append(ord(correct_character))

                    character2 = file2.read(1)

        return bytes(diff)

    def diff(self, file_path1: str, file_path2: str) -> bytes:
        """
        Returns the bytes difference of the second file when compared
        to the first file.
        """
        file1_size = os.path.getsize(file_path1)
        file2_size = os.path.getsize(file_path2)

        if file1_size == file2_size:
            return self._diff_same_size(file_path1, file_path2)

        return self._diff_different_size(file_path1, file_path2)
