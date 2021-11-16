visits = {
    '미국': {'LA', '뉴욕'},
    '일본': {'도쿄'}
}

visits['프랑스'] = {'파리'}

print(visits)

##############################################################


from collections import defaultdict


def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError as e:
        print(e)
        raise


pictures = defaultdict(open_picture)




class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()