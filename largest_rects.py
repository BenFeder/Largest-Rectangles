rectangles_dict = {}
rectangles_list = []


def create_rectangles_list():
    for i in range(2, 10):
        rect_width = i
        for j in range(i, 10):
            rect_height = j
            rect_enclosed_area = (rect_width - 1) * (rect_height - 1)

            rectangles_dict[(i, j)] = (
                rect_enclosed_area, rect_width, rect_height)

    sorted_rectangles_dict = sorted(
        rectangles_dict.keys(), key=lambda a: rectangles_dict[a], reverse=True)

    print(sorted_rectangles_dict)


create_rectangles_list()
