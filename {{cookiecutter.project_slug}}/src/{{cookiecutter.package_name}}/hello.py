def hello_world(name: str = "World") -> str:
    """Main entry point for the package.

    Parameters:
        name(str): The name to say hello to.

    Returns:
        str: The string "Hello, {name}!"

    Examples:
        # default
        >>> hello_world()
        "Hello, World!"

        # with name argument
        >>> hello_world("John")
        "Hello, John!"
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello_world())
