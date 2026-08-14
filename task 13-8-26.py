s = input()

for ch in s:
    if s.count(ch) > 1:
        print(ch, "is repeating", s.count(ch), "times")
        s = s.replace(ch, '', 1)
s = input()

checked = []

for ch in s:
    if ch not in checked:
        checked.append(ch)

        if s.count(ch) > 1:
            print(ch, "is repeating", s.count(ch), "times")

            index = []
            for i in range(len(s)):
                if s[i] == ch:
                    index.append(i)

            print("index =", index)
