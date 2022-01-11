#!/usr/bin/env python3

import json

def main():
    first_json = open('b_first.json', 'r')
    first = json.load(first_json)
    second_json = open('b_second.json', 'r')
    second = json.load(second_json)
    print(first.keys())
    print(second.keys())
    for key, value in second.items():
        if key == 'name':
            pass
        else:
            first[key] = value

    print(first.keys())

    with open('b.json', mode='wt', encoding='utf-8') as f:
        json.dump(first, f, ensure_ascii=False, indent=2)
        



if __name__ == '__main__':
    main()
