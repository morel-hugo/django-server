import pygal
from pygal.style import Style

custom_style_line = Style(
    background='transparent',
    foreground='#000000', # Legend x,y
    foreground_strong='#53A0E8', # Strong value and hover value
    opacity_hover='.5',

    colors=('#e5849b', '#e5849b', '#f3d387', '#8fd9b3', '#E89B53'),
    transition='400ms ease-in',
)

custom_style_pie = Style(
    background='transparent',
    #plot_background='transparent',
    transition='400ms ease-in',

)

custom_style_gaug = Style(
    background='transparent',
    plot_background='transparent',
    print_values=False,
    value_font_size=140,
    transition='400ms ease-in',
    colors=('#90a9e7','#90a9e7'),
)


# ------------   Basic_Line   ------------
def basic_line():
    line_chart = pygal.StackedLine(fill=True,show_legend=False, style=custom_style_line,height=400, explicit_size=True,show_y_guides=False)
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('IE',  [10.8, 15.6, 37.7, 25.5,   50, 52.6, 54.7, 44.8, 56.2, 60.6, 50.1])

    return line_chart.render_data_uri()

# ------------   Selid_pie   ------------

def solid_pie():
    pie_chart = pygal.Pie(inner_radius=.75,height=700,style=custom_style_pie,show_legend=False)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)

    return pie_chart.render_data_uri()


# ------------   Solid_Gauge   ------------

def solid_gauge(data):
    gauge = pygal.SolidGauge(inner_radius=0.85, style=custom_style_gaug, show_legend=False, js=[])
    gauge.add('Series 6', data)
    return gauge.render_data_uri()


def func_solid_gauge():
    data = 40
    list_gauge = list()
    for i in range(4):
        list_gauge.append(solid_gauge(data))

    return list_gauge

# -----------------------------------------------------------------










def solid_gauge_fd():
    gauge = pygal.SolidGauge(inner_radius=0.85, style=custom_style_gaug, show_legend=False, js=[])
    gauge.add('Series 6', 27)

    return gauge.render_data_uri()

def solid_gauge_marge():
    gauge = pygal.SolidGauge(inner_radius=0.85, style=custom_style_gaug, show_legend=False, js=[])
    gauge.add('Series 6', 57)

    return gauge.render_data_uri()

def solid_gauge_nt():
    gauge = pygal.SolidGauge(inner_radius=0.85, style=custom_style_gaug, show_legend=False, js=[])
    gauge.add('Series 6', 87)

    return gauge.render_data_uri()
