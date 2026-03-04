class Greeter:

    def greet(self, name):
        return f"Hello, {name}!"

    def greet_loud(self, name):
        return f"HELLO, {name.upper()}!"

    def greet_formal(self, name):
        return f"Good day, {name}."

# This comment is to trigger the Jenkins pipeline with a commit.