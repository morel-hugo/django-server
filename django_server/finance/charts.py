import pygal
from pygal.style import Style

custom_style = Style(
    background='transparent',
    transition='400ms ease-in'
)
  #value_font_size=100,
  #no_data_font_size='100')

custom_style_gaug = Style(
    background='transparent',
    plot_background='transparent',
    print_values=False,
    value_font_size=130,
)


def basic_line():
    line_chart = pygal.Line(show_legend=False,style=custom_style)
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('IE',  [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])

    return line_chart.render_data_uri()


def solid_gauge():
    gauge = pygal.SolidGauge(inner_radius=0.85, style=custom_style_gaug, show_legend=False, js=[])
    gauge.add('Series 6', 77)

    return gauge.render_data_uri()
