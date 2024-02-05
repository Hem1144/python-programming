def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    if lang in greetings:
        message = f"{greetings[lang]} {name}!"
        print(message)
    else:
        print("Invalid language.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provide a personal greeting.")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of person to greet.",
    )

    parser.add_argument(
        "-l",
        "--language",
        metavar="lang",
        required=True,
        choices=["English", "Spanish", "German"],
        help="The language of the greeting.",
    )

    args = parser.parse_args()

    hello(args.name, args.language)
