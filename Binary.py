"""Binary Stuff."""


write_to_file = lambda file_name, text : open(file_name, "w+").write(text)


text_to_binary = lambda text : "".join([bin(ord(i))[2:] for i in list(text)])


if __name__ == "__main__":
    write_to_file(input("What is the target file?: "), text_to_binary(
        input("What do you want to convert to binary?: ")))
