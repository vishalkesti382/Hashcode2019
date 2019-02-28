import pandas as pd
dft = pd.read_csv('1.csv')
subset = dft[['id', 'cs', 'ori']]
dataframes = [tuple(x) for x in subset.values]


horizontal = []
vertical = []
fn = len
slideshow = []


def seperator(df):
    for d in df:
        if d[2] == 'H':
            horizontal.append(d)
        if d[2] == 'V':
            vertical.append(d)

    horizontal.sort(key=lambda x: x[1], reverse=True)
    vertical.sort(key=lambda x: x[1], reverse=True)

    if fn(vertical) % 2 != 0:
        vertical.pop(fn(vertical) - 1)
    pass


def vertical_slides(vertical):
    slides = []
    j = 0
    length = int(fn(vertical) / 2)

    for i in range(length):
        val1 = vertical[j]
        val2 = vertical[j+1]
        mean = (val1[1] + val2[1]) / 2
        t = ((str(val1[0])+' '+str(val2[0])), mean)
        j += 2
        slides.append(t)

    return slides


def merging_slides(hlist, vlist):
    slide_list = []

    total = int(fn(hlist) + fn(vlist))

    slide_list.extend(hlist)
    slide_list.extend(vlist)
    slide_list.sort(key=lambda x: x[1])
    return slide_list


def update_slideshow(slideshow):
    slides = []
    for t in slideshow:
        slides.append(t[0])

    with open('1.txt', 'w') as f:
        f.write("%s\n" % str(len(slides)))
        for item in slides:
            f.write("%s\n" % item)
    return slides


if __name__ == '__main__':
    seperator(dataframes)
    v_slides = vertical_slides(vertical)
    h_slides = horizontal
    slideshow = merging_slides(h_slides, v_slides)
    print(slideshow)
    slideshow_slides = update_slideshow(slideshow)
    print(slideshow_slides)
