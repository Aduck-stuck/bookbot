def get_book_text(path):
    with open(path) as f:
        booktext = f.read()
    return booktext

def get_num_words(path):
    count_text = " "
    count_text = get_book_text(path)
    total = count_text.split()
    print(f"Found {len(total)} total words")

def text_count_characters(path):
    booktext = get_book_text(path)
    final_count = {}
    lower_case_booktext = booktext.lower()
    for ch in lower_case_booktext:
        if ch in final_count:
            final_count[ch] += 1
        else:
            final_count[ch] = 1
    return final_count

def sort_textcount(path):
    sort_list = []
    for x, y in text_count_characters(path).items():
        if x.isalpha():
            sort_list.append({"char" : x, "num" : y})
    sort_list.sort(key=lambda item: item["num"], reverse=True)
    for a in sort_list:
        print(f'{a["char"]}: {a["num"]}')