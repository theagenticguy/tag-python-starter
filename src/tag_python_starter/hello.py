def hello_world(name: str = "World") -> str:
    """Main entry point for the package.

    Parameters:
        name (str): The name to say hello to.

    Returns:
        str: The string "Hello, {name}!"

    Example:
        # Default usage
        ```python
        hello_world()
        "Hello, World!"
        ```

        # With name argument
        ```python
        hello_world("John")
        "Hello, John!"
        ```
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello_world())
