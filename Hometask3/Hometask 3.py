from pathlib import Path

link2 = Path("rockyou.txt").absolute()


def foo(link):
    results = []
    search_topic = (
        input("What word would you like to search for?").lower().strip()
    )
    with open(link, "r", encoding="utf-8", errors="ignore") as file:
        for i in file.readlines():
            if f"{search_topic}" in i:
                if input(f"do you want to save that? {i}") == "yes":
                    results.append(i)
                    if input("continue?") != "yes":
                        break
                else:
                    pass

        if len(results) <= 0:
            return "no matches found "

    return results, len(results)


print(foo(link2))
