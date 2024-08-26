import dash
import widgets

dash.register_page(__name__, path="/home/", redirect_from=["/home"])


def layout():
    return widgets.layout.LayoutCCA(
        header=widgets.features.TitleImageOverlay(
            title="Climate Change Adaptation Studies",
            image=widgets.placeholders.PlaceholderImage(),
        ),
        children=[
            widgets.markdown.from_file("home/introduction"),
            widgets.tables.from_file("home/dcr_results"),
        ],
    )
