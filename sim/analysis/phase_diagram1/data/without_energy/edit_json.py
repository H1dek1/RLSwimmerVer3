#!/usr/bin/env python3

import json

def main():
    file_object = open('b.json', 'r')
    data = json.load(file_object)
    
    editted_data = dict()
    editted_data['name'] = data.pop('name')
    editted_data['data'] = data.copy()
    print(data.keys())
    print(editted_data['data'].keys())

    with open('b_editted.json', mode='wt', encoding='utf-8') as f:
        json.dump(editted_data, f, ensure_ascii=False, indent=2)
        



if __name__ == '__main__':
    main()
