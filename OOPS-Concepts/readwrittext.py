with open("demotext", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("demotext", "w") as writer:
        for line in reversed(content):
            writer.write(line)

