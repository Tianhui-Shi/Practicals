from programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby,python,visual_basic]

    for l in languages:
        if l.is_dynamtic():
            print(l.name)



if __name__ == '__main__':
    main()