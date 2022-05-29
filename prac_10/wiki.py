import wikipedia as wiki

def main():

    user_input = input("Enter a page title or search phrase or q to quit: ")
    while user_input != 'q':

        try:
            search_page = wiki.page(user_input)
            print("Title: {}".format(search_page.title))
            print(wiki.summary(user_input))
            print("URL: {}".format(search_page.url))
            user_input = input("Enter a page title or search phrase: ")
        except wiki.exceptions.DisambiguationError as ex:
            print(ex.options)
            user_input = input("Enter a page title or search phrase: ")

if __name__ == "__main__":
    main()