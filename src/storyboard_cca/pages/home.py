import dash
import storyboard

dash.register_page(
    __name__,
    path="/home",
    title="Home - Climate Change Adaptation Studies",
)


def layout():
    return storyboard.Page(
        header=storyboard.features.TitleImageOverlay(
            title="Climate Change Adaptation Studies",
            image=storyboard.placeholders.get_image(),
        ),
        children=[
            storyboard.markdown.from_file("text/home/introduction"),
            storyboard.table.from_file("text/home/dcr_results"),
        ],
    )
