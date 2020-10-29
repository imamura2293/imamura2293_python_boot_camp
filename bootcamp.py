2 + 2

3 - 8
6 * 9
8 / 2
5 % 2

width = 60
height = 90
width * height

"Hello world"

"Monty Python's Flying Circus"

["Hello", 3]

# ここはコメント文
a = 1


def add(a, b):
    return a + b


add(1, 3)

round(10.4)


def fizzbuzz(num):
    retrun
    num


print(fizzbuzz(4))


def fizzbuzz(num):
    return num


for num in range(1, 101):
    print(fizzbuzz(num))


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
    for num in ramge(1, 101):
        print(fizzbuzz(num))


n1 = 100
s1 = "hello"
l1 = [1, 2, 3]
type(n1)

type(s1)
tupe(l1)

isinstance(n1, int)

isinstance(s2, str)

isinstance(li, list)

import.collections.abc

isinstanve(s1, collection.abc.Sequence)

isinstance(l1, collection.abc.Sequence)

# 3


2 + 2

3 - 8

6 * 9
8 / 2
5 % 2
5 ** 2

10 / 3
10 / 4
-10 / 4

10 // 3
10 // 4
-10 // 4

5.0
5.0 + 5.2
10.2 + 8

"Hello,World"

"Hello,World"

print("I\"m Hiroki)

print("Hello\nworld"))


print("I'm Hiroki")

"""foo
    bar
    baz
    """

"Mt." + "Fuji"

"spam" * 5

"python"[1]

"python"[:3]
"python"[4:]

len("pyhon")

"t" in "python"

"k" in "python"

"th" in "python"

"pain-au-chocolate".split("-")

"-".join(["pain", "de", "campagne"])

["spam", "egg", 0.5]

['spam'] * 5

['spam', 'ham', 'egg'][0]

['spam', 'ham', 'egg'][1:]

len(['spam', 'ham', 'egg'])

'ham' in ['spam', 'ham', 'egg']

for animal in ["cat", "dog", "snake"]:
    print(animal)

animals = ["cat", "dog", "snake"]
animals.append("elepahant")
animals

ret = []
for animal in animals:
    ret.append(len(animal))

    ret

[len(animal) for animal in animals]

dog, cat = ["dog", "cat"]
dog
cat

("spam", "ham", 4)

("spam", "ham") + ("egg",)
("spam",) * 5
("spam", "ham", "egg")[0]
("spam", "ham", "egg")[1:]

len(("spam", "ham", "egg"))

"ham" in ("spam", "ham", "egg")

("spam",)
("spam")

"dog", "cat"


def head_splitter(seq):
    return seq[0], seq[1:]


...
head, tail = head_splitter(['head', 'body', 'tail'])
head

tail


def bad_implementation():
    return 'username', 'user_password', 'user_id', 'user_permission1', 'user_permission2'


user_info = {'user_name': 'taro', 'last_name': 'Yamada'}
user_info

user_info['user_name']
user_info['first_name'] = 'Taro'
user_info
'user_name' in user_info
'bio' in user_info

user_info['bio']

user_info.get('user_name')
bio = user_info.get('bio')
print(bio)

user_info.get('bio', '')

user_info = {'user_name': 'taro', 'last_name': 'Yamada'}
for key in user_info:
    print(key)
    print(user_info[key])

d = {'foo': 'spam', 'bar': 'ham'}
for key, value in d.items():
    print(key, value)

{'spam', 'ham'}
{'spam', 'spam', 'spam'}

unique_users = {'dog', 'cat'}
unique_users.add('snake')
unique_users

len(unique_users)
unique_users.add('snake')
unique_users.add('snake')
unique_users.add('snake')
len(unique_users)

allowed_permissions = {'edit', 'view'}
requested_permissions = {'view', 'delete'}
allowed_permissions & requested_permissions

editor = {'edit', 'comment'}
reviewer = {'comment', 'approve'}
editor | reviewer
