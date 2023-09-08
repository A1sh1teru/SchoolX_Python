# from module import greet

x = 42
def outer(y):
    print(f'y in outer before assig: {"y" in locals()}')
    y = 12
    print(f'y in outer after assig: {"y" in locals()}')
    def answer():
        asdas = 12 + y 
        print(f'y in answer: {"y" in locals()}')
        return x
    return answer()

if __name__ == '__main__':
    x = 42
    print(
        f'y in main is exists: {"y" in locals()}'
    )