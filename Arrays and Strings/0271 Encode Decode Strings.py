def encode(strs: list[str]) -> str:
    if strs == []:
        return ""
    elif strs == [""]:
        return "case2"
    si = ""
    for i in range(len(strs) -1):
        si += strs[i]
        si += "."
    si += strs[-1]
    return si


def decode(s: str) -> list[str]:
    if s == "":
        return []
    elif s == "case2":
        return [""]
    return s.split(".")

