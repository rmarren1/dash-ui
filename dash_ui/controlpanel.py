import dash_html_components as html
from collections import OrderedDict


class ControlPanel:
    def __init__(self, _id="default_controlpanel_id"):
        self.className = "dui-controlpanel"
        self._id = _id
        self.options = OrderedDict()

    def create_group(self, group, group_title="", group_class=""):
        if group in self.options.keys():
            raise ValueError(
                "The group {:s} already exists in the control panel.")
        option_group_title = html.Strong(
            group_title,
            className="dui-controlpanel-group-title"
        )
        option_group = html.Div(
            className=" ".join(["dui-controlpanel-group", group_class]),
            children=[option_group_title]
        )
        self.options[group] = option_group

    def add_element(self, element, group):
        if group not in self.options.keys():
            raise ValueError(
                "{0} is not an element group. "
                "Add it with ControlPanel.create_group({0})".format(group)
            )
        option = html.Div(
            className="dui-controlpanel-element",
            children=element
        )
        self.options[group].children.append(option)

    def get_component(self):
        control_panel = html.Div(
            className=self.className,
            id=self._id,
            children=[o for o in self.options.values()]
        )
        return html.Div(
            className="dui-controlpanel-wrapper",
            children=control_panel)
