import random

num_rectangles = random.randint(10, 50)
rectangles_dict = {}
rectangles_list = []


def create_rectangles_list():
    for i in range(num_rectangles):
        rect_width = random.randint(2, 9)
        rect_height = random.randint(rect_width, 9)
        rect_enclosed_area = (rect_width - 1) * (rect_height - 1)

        rectangles_dict[i] = (rect_enclosed_area, rect_width, rect_height)

    sorted_rectangles_dict = sorted(rectangles_dict.values(), reverse=True)

    for item in sorted_rectangles_dict:
        rectangles_list.append((item[1], item[2]))

    print(rectangles_list)


create_rectangles_list()
