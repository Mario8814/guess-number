import random


def play_game():
    print("我已经想好了一个 1 到 100 之间的数字,你有 8 次机会。")

    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 8

    while attempts < max_attempts:
        guess = input("请输入你猜的数字: ")

        # 检查输入是不是有效的整数
        if not guess.isdigit():
            print("请输入有效的整数哦!")
            continue

        attempts += 1
        guess = int(guess)
        remaining = max_attempts - attempts

        if guess < target:
            print(f"太小了,再大一点!还剩 {remaining} 次机会。")
        elif guess > target:
            print(f"太大了,再小一点!还剩 {remaining} 次机会。")
        else:
            print(f"恭喜!你猜对了,就是 {target}!")
            print(f"你一共猜了 {attempts} 次。")
            return

    # 循环结束还没猜对,说明 8 次机会用完了
    print(f"很遗憾,机会用完了。正确答案是 {target}。")


def main():
    print("欢迎来玩猜数字游戏!")

    while True:
        play_game()

        again = input("还要再来一局吗? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("感谢游玩,再见!")
            break


if __name__ == "__main__":
    main()
