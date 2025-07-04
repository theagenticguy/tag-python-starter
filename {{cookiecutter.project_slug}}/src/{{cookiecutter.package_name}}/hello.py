def hello_world(name: str = "World") -> str:
    """Main entry point for the package.

    Parameters:
        name: The name to say hello to.

    Returns:
        str: The string "Hello, {name}!"

    Example:
        >>> hello_world()
        "Hello, World!"
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello_world())
