import dash_html_components as html
from collections import OrderedDict


class ControlPanel:
    def __init__(self, _id="default_controlpanel_id"):
        self.className = "dui-controlpanel"
        self._id = _id
        self.options = OrderedDict()
        self.sections = OrderedDict()

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

    def create_section(self, section, defaultOpen=True,
                       section_title="", section_class=""):
        if section in self.options.keys():
            raise ValueError(
                "The section {:s} already exists in the control panel.")
        option_section_title = html.Summary(
            section_title,
            className="dui-controlpanel-section-title",
        )
        option_section = html.Details(
            className=" ".join(["dui-controlpanel-section", section_class]),
            open=defaultOpen,
            children=[option_section_title]
        )
        self.sections[section] = option_section

    def add_groups_to_section(self, section, groups):
        for group in groups:
            if group not in self.options.keys():
                raise ValueError(
                    "{0} is not an element group. "
                    "Add it with ControlPanel.create_group({0})".format(group)
                )
        if section not in self.sections.keys():
            raise ValueError(
                "{0} is not a valid section. "
                "Add it with ControlPanel.create_section({0})".format(section)
            )
        for group in groups:
            self.sections[section].children.append(self.options[group])

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
            children=list(
                (o for o in self.options.values())
                if not self.sections else
                (s for s in self.sections.values())
            )
        )
        return html.Div(
            className="dui-controlpanel-wrapper",
            children=control_panel)
