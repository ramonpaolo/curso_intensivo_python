import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

py_styles = LS("#333366", base_style=LCS)

chart = pygal.Bar(style=py_styles, x_label_rotation=45, show_legend=False)

chart._title = "Python Projects"
chart.x_labels = ["httpie", "django", "flask"]

plot_dics = [{
    "value": 16101, "label": "Description of httpie"
    },
    {
        "value": 15028, "label": "Description of django"
    },
    {
        "value": 14798, "label": "Description of flask"
    }
]

chart.add("", plot_dics)
chart.render_to_file("bar_descriptions.svg")