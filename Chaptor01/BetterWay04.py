# 파이썬에서 u
a = 0b10111011
b = 0xc5f

print('이진수 %d, 십육진수: %d', (a, b))

pantry = [
    ('아보카도', 1.25),
    ('바나나', 2.5),
    ('체리', 15)
]

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))


key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)
# 딕셔너리를 사용함으로써, 여러 형식 지정자에 같은 키를 지정할 수 있어 같은 값을 반복하지 않아도 됨.
new_way = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}
reordered = '%(key)-10s = %(value).2f' % {'value': value, 'key': key}

assert old_way == new_way == reordered


# 딕셔너리는 딕셔너리 키와 콜론 등 형식화 방식이 길어져 시각적으로 더욱 불편
for i, (item, count) in enumerate(pantry):
    before = '#%d: %-10s = %d' % (
        i+1,
        item.title(),
        round(count)
    )

    after = '#%(loop)d: %(item)-10s = %(count)d' % {
        'loop': i+1,
        'item': item.title(),
        'count': round(count)
    }

    assert before == after


a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my String'
formatted = format(b, '^20s')
print('*', formatted, '*')


# 인터폴레이션을 통한 형식 문자열
key = 'my_var'
value = 1.2345
formatted = f'{key} = {value}'
print(formatted)

for i, (item, count) in enumerate(pantry):
    print(f'#{i+1}'
          f'{item.title():<10s} = '
          f'{round(count)}')


places = 3
num = 1.2345
print(f'내가 고른 숫자는 {num:.{places}f}')