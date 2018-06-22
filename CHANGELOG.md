# 0.4.0
* Added `menu` and `menu_height` attributes to `add_graph`, which places `menu`
on top of the graph element with `menu_height`.

# 0.3.1
* Removed 'displayModeBar = False' which was accidentally set in `Grid.add_graph`

# 0.3.0
* Added a `ControlPanel` object. When added, this is a sidebar which holds input components separate from the plot grid.
* Added the function `dash_ui.Layout` which creats the layout from a `Grid` Object and (optionally) a `ControlPanel` object
* Changed the `grid_id` property of `Grid` to `_id` to remove redundancy.

# 0.2.0
Grid elements have a `dui-grid-element` class with which you can style them, and 
arbitrary classes can be added to grid components with the `element_class` argument of 
`add_element`

# 0.1.0
Added: Grid component
