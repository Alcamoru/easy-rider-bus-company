def print_book_info(title, author=None, year=None):
    #  Write your code here
    if author and year:
        print(f'"{title}" was written by {author} in {year}')
    elif author is None and year:
        print(f'"{title}" was written in {year}')
    elif author and year is None:
        print(f'"{title}" was written by {author}')
    else:
        print(f'"{title}"')
