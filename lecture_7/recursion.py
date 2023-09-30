from rich import print

tree = {
   1: {
       'first_inner': {
            1: 'text',
            2: 'text',
            3: 'text',
        },
    },
   2: {
       'second_inner': {
          'second_2_inner':  {
               'second_3_inner_1': {
                    1: 'folder',
                    2: 'folder',
                    3: 'target_folder',
                },
                2: [1, 2, 3]
            }
        }
    },
}

# tree

def rec_find(tree: dict, name: str):
    for key, value in tree.items():
        if isinstance(value, dict):
            print(value, name)
        else:
            if value == name:
                print('FOUND IT')
                break
    # print('smth')

rec_find(tree, 'target_folder')