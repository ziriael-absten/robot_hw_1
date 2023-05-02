class ContextManager:

    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Error occurred: {exc_type}, {exc_value}")
        print("=" * 10)
        return True



with ContextManager():
    print("Hello world! ")
