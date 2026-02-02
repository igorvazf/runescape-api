def is_positive_int(value: int, name: str) -> None:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    
    if value <= 0:
        raise ValueError(f"{name} must be a positive integer")

def is_non_empty_str(value: str, name: str) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string")
    
    if not value:
        raise ValueError(f"{name} must not be empty")

def is_boolean(value: bool, name: str) -> None:
    if not isinstance(value, bool):
        raise TypeError(f"{name} must be bool")