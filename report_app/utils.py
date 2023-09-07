import random

def generate_color():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)

    return f'#{hex(r)}{hex(g)}{hex(b)}'

def get_random_colors(n):
    # 100 notably different colors
    colors = [
        "#FF5733", "#33FF57", "#5733FF", "#FFFF33", "#33FFFF",
        "#FF3333", "#33FF33", "#3333FF", "#FF3366", "#66FF33",
        "#3366FF", "#FF9933", "#33FF99", "#9933FF", "#FF33CC",
        "#CCFF33", "#33CCFF", "#FF3399", "#99FF33", "#3399FF",
        "#FF6633", "#33FF66", "#6633FF", "#FF33FF", "#FF9966",
        "#66FF99", "#9966FF", "#FFCC33", "#33FFCC", "#CC33FF",
        "#FF3399", "#99FF33", "#3399FF", "#FF6633", "#33FF66",
        "#6633FF", "#FF33FF", "#FF9966", "#66FF99", "#9966FF",
        "#FFCC33", "#33FFCC", "#CC33FF", "#FF33FF", "#FF9966",
        "#66FF99", "#9966FF", "#FFCC33", "#33FFCC", "#CC33FF",
        "#FF3399", "#99FF33", "#3399FF", "#FF6633", "#33FF66",
        "#6633FF", "#FF33FF", "#FF9966", "#66FF99", "#9966FF",
        "#FFCC33", "#33FFCC", "#CC33FF", "#FF33FF", "#FF9966",
        "#66FF99", "#9966FF", "#FFCC33", "#33FFCC", "#CC33FF",
        "#FF3399", "#99FF33", "#3399FF", "#FF6633", "#33FF66",
        "#6633FF", "#FF33FF", "#FF9966", "#66FF99", "#9966FF",
        "#FFCC33", "#33FFCC", "#CC33FF", "#FF33FF", "#FF9966",
        "#66FF99", "#9966FF", "#FFCC33", "#33FFCC", "#CC33FF",
        "#FF3399", "#99FF33", "#3399FF", "#FF6633", "#33FF66",
        "#6633FF", "#FF33FF", "#FF9966", "#66FF99", "#9966FF",
        "#FFCC33", "#33FFCC", "#CC33FF", "#FF33FF", "#FF9966",
        "#66FF99", "#9966FF", "#FFCC33", "#33FFCC", "#CC33FF",
    ]
    # if there are needed more than 100 colors, more  colors (not neccesarily notably different) will be generated
    if (n > 100):
        for i in range(n - 100):
            new_color = generate_color()
            while new_color in colors:
                new_color = generate_color()
        
            colors.append(new_color)
            
    return colors[:n+1]  

