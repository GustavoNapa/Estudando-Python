def count_substring(string, sub_string):
    return  sum([1 if string[idx:].find(sub_string) == 0 else 0 for idx,i in enumerate(string)])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)