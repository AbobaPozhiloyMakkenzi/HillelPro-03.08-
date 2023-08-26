import functools

# TASK1


def reverse_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reverse = ""
        if isinstance(args[0], str):
            for i in args[0]:
                reverse = i + reverse
        else:
            return None
        return reverse

    return wrapper


# TARGET FUNCTIONS


@reverse_string
def get_university_name(data) -> str:
    return data


@reverse_string
def get_university_founding_year(data) -> int:
    return data


# TEST OUPUT
print(
    get_university_name("Oles` Honchar Dnipro National University"),
    get_university_founding_year(1978),
    sep="\n",
)

# TASK2

# MODIFY THIS DECORATOR


def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result[target_key] = replace_with * len(result[target_key])
            return result

        return wrapper

    return decorator


# TARGET FUNCTIONS


@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
