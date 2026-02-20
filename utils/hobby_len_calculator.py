from typing import List

def get_longest_hobby(hobbies_list: List[str]) -> str:
    return max(hobbies_list, key=len)
