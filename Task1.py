
# Simple Python script that prints a greeting message

def greet(name: str) -> str:
    """Return a personalized greeting."""
    return f"Hello, {name}! 👋"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
