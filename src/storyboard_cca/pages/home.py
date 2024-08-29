import dash
import dash_bootstrap_components as dbc
import storyboard

dash.register_page(
    __name__,
    path="/home",
    title="Home - Climate Change Adaptation Studies",
)


def layout():
    return storyboard.Page(
        header=storyboard.features.BannerImage(
            title="Climate Change Adaptation Studies",
            image=storyboard.placeholders.get_image(),
        ),
        children=[
            storyboard.GridContainer(
                dbc.Col(
                    storyboard.markdown.from_file("text/home/introduction"),
                    width=8,
                ),
                dbc.Col(
                    storyboard.features.LinksBin.from_csv(
                        "text/home/links",
                        title="Learn More",
                    ),
                    width=4,
                ),
            ),
            storyboard.features.ScrollBy(
                left=storyboard.placeholders.get_image(
                    style={
                        "height": "100%",
                        "object-fit": "cover",
                    }
                ),
                right=storyboard.placeholders.LoremIpsum(20),
            ),
            storyboard.features.ScrollBy(
                right=storyboard.placeholders.get_image(
                    style={
                        "height": "100%",
                        "object-fit": "cover",
                    }
                ),
                left=storyboard.placeholders.LoremIpsum(20),
                height_limit="50vh",
            ),
            storyboard.features.ScrollBy(
                left=storyboard.placeholders.get_image(
                    style={
                        "height": "100%",
                        "object-fit": "cover",
                    }
                ),
                right=storyboard.placeholders.LoremIpsum(20),
                height_limit="50vh",
            ),
            storyboard.GridContainer(
                dbc.Row(storyboard.markdown.from_file("text/home/baseline_conditions")),
                dbc.Row(storyboard.table.from_file("text/home/dcr_results")),
            ),
        ],
    )
