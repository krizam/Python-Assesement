def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def count_keyword(lines, keyword):
    count = 0
    for line in lines:
        count += line.lower().count(keyword.lower())
    return count

def main():
    filename = "Task-2/financial_report.txt"
    try:
        lines = read_file(filename)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    while True:
        keyword = input("Enter a keyword to search (or 'exit' to quit): ").strip()
        if keyword.lower() == 'exit':
            break
        
        occurrences = count_keyword(lines, keyword)
        print(f"The keyword '{keyword}' appears {occurrences} time(s) in the report.")

if __name__ == '__main__':
    main()