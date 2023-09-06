from files.copier import FileCopier

if __name__ == '__main__':
    file_copier = FileCopier()
    file_copier.safe_copy('./image01.jpeg')
    file_copier.safe_copy('./file01.pdf')