"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    try:
        if line1 == line2:
            return IDENTICAL
        lent = [i for i in range(len(line1)) if line1[i] != line2[i]]
        return lent[0]
    except IndexError:
        if len(line1) > len(line2):
            indx = list(range(len(line1)))
        elif len(line2) > len(line1):
            indx = list(range(len(line2)))
        return indx[-1]
print(singleline_diff('a', 'b'))
print(singleline_diff('abc', 'abcd'))



def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """

    print(idx)
    if idx < 0:
        return ""
    elif len(line1) > len(line2) and idx > len(line2):
        return ""
    elif len(line2) > len(line1) and idx > len(line1):
        return ""
    return (line1 + '\n' + "=" * idx +  '^\n' + line2) + '\n'

#print(singleline_diff_format('Python is fast!!!', 'Python is fun!!!', 11))

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines_list = []
    with open(filename, 'rt', encoding = 'utf-8') as readit:
        for line in readit:
            lines_list.append(line.rstrip())

    return lines_list

#print(get_file_lines("README.md"))


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename1, 'rt', encoding = 'utf-8') as file1:
        get_file_lines(file1)
    with open(filename2, 'rt', encoding = 'utf-8') as file2:
        get_file_lines(file2)

    if file1 == file2:
        return "No differences\n"
    else:
        idx = singleline_diff(file1, file2)
        return singleline_diff_format(file1, file2, idx)