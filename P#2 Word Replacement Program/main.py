def replace_world():
    str = "Hi, i am george and hi hi hi"
    word_to_replace = input("Enter the word to replace: ")  # შეგყვავს სიტყვა, რომლის შეცვლაც გვსურს
    word_repacement = input("Enter the word replacement: ")  # შეგყვავს სიტყვა, რომლითაც უნდა შევცვალოთ სიტყვა
    print(str.replace(word_to_replace, word_repacement))  # ვიყენებთ replace ფუნქციას

replace_world()