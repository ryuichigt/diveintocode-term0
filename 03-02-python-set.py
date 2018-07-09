course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}


def find_person(want_to_find_person):
    """
    受講生がどのコースに在籍しているかを出力する。
    まずはフローチャートを書いて、どのようにアルゴリズムを解いていくか考えてみましょう。
    """
    # ここにコードを書いてみる
    course_person = [set(i) for i in course_dict.values()]
    for course,person in zip(list(course_dict),course_person):
        find_persons = person & set(want_to_find_person)

        if len(find_persons) == 2:
            print(course + "に{}は在籍しています。".format(find_persons))

        elif len(find_persons) == 1:
            print(course + "に{}のみ在籍しています。".format(find_persons))

        else:
            print(course + "に{}は在籍していません。".format(want_to_find_person))




def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()