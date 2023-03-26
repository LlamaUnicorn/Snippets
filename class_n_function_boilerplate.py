# VS Code snippets
"""
	"Clean Code Class": {
		"prefix": "cc_class",
		"body": [
		  "class $1:",
		  "    \"\"\"",
		  "    $2",
		  "    \"\"\"",
		  "    def __init__(self, $3: $4):",
		  "        \"\"\"",
		  "        Initialize an instance of the $1 class.",
		  "        ",
		  "        Args:",
		  "        $3 ($4): $5",
		  "        \"\"\"",
		  "        $0"
		],
		"description": "Create a clean code class with docstrings and best practices"
	  },	  
	  
	  "Clean Code Function": {
		"prefix": "cc_func",
		"body": [
			"def $1($2: $3) -> $4:",
			"    \"\"\"",
			"    $5",
			"",
			"    Args:",
			"    $2 ($3): $6",
			"",
			"    Returns:",
			"    $4:",
			"    \"\"\"",
			"    $0"
		  ],
		"description": "Create a function boilerplate with docstrings and type hints"
	  }
"""
def pwr_of_2(x: int) -> int:
    """
    Returns the result of raising the argument to the power of 2.

    Args:
    x (int): The number to be raised to the power of 2.

    Returns:
    int: The result of x raised to the power of 2
    """
    return x ** 2


test_func = pwr_of_2(4)
print(test_func)


class Dog:
    """
    Make a dog
    """
    def __init__(self, name: str):
        """
        Initialize an instance of the Dog class.

        Args:
        name (str): The name of a dog
        """
        self.name = name

    def dog_name(self):
        """Return dog's name"""
        return self.name

    def __str__(self) -> str:
        return self.name


dog1 = Dog("Spot")
print(dog1.dog_name())
