class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


def parse_line(line):
    try:
        idx = 0
        for ch in line:
            if not ch.isdigit():
                idx += 1
            else:
                break
        score = (float)(line[idx:])
        name = line[:idx].strip().replace("\t", " ")
        return name, score
    except Exception as ex:
        raise BadLine(line)


def read_data(filename):
    students_data = {}
    try:
        data_file = open(filename, "rt")
        line = data_file.readline()
        if line == "":
            raise FileEmpty(f"File {filename} is empty")
        while line != "":
            # line = line.strip()

            name, score = parse_line(line)
            if name not in students_data:
                students_data[name] = score
            else:
                students_data[name] += score

            line = data_file.readline()

        sorted_data = dict(sorted(students_data.items()))
        return sorted_data

    except OSError:
        raise StudentsDataException("Something went wrong with the file")


if __name__ == "__main__":

    try:
        filename = input("Enter the filename to read: ")
        sorted_data = read_data(filename)
        for name, score in sorted_data.items():
            print(name, "\t", score)
    except StudentsDataException as ex:
        print(ex)
        print("Something when wrong, please read the error, correct and try again")
