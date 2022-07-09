import traceback
from re import match

from vk import Vk


def get_results(comments_list: list):
    results = dict()
    if input("1 - Искомые категории; 2 - Регулярные выражения: ") == "1":
        words = input("Перечислите искомые категории через запятую: ").lower().split(',')
        words = list(map(lambda word: word.strip(), words))
        for comment in comments_list:
            for word in words:
                if word == comment["text"].lower():
                    if word not in results.keys():
                        results[word] = 0
                    results[word] += 1
    else:
        regexs = input("Перечислите регулярные выражения в кавычках через запятую: ").split(',')
        regexs = list(map(lambda regex: regex.strip()[1:-1], regexs))
        for comment in comments_list:
            for regex in regexs:
                if match(regex, comment["text"].lower()):
                    if regex not in results.keys():
                        results[regex] = 0
                    results[regex] += 1
    return results


if __name__ == "__main__":
    video_id = input("Ввод id видео: ")
    try:
        comments = Vk().get_comments(video_id)
        results = get_results(comments)
        print(results)
    except Exception as err:
        print(f"{err.__class__.__name__}: {err}")
        traceback.print_tb(err.__traceback__)
