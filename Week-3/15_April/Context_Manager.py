# Context Manager

class ContextManager:
    def __enter__(self):
        print("Entering the Block")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the Block")

# Using the context manager
with ContextManager() as cm:
    print("Inside the Block")
