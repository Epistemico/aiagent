from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def testGetFilesInfo():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print()

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print()

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin/' directory:")
    print(result)
    print()

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print()


def testGetFileContent():
    result = get_file_content("calculator", "lorem.txt")
    print(result)

    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print()

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)
    print()


if __name__ == "__main__":
    testGetFilesInfo()
    testGetFileContent()
