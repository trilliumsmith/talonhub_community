from talon import Context, Module, actions

mod = Module()
global_ctx = Context()
ctx = Context()
ctx.matches = """
code.language: css
code.language: scss
"""

mod.list("css_at_rule", desc="List of CSS @rules")
mod.list("css_unit", desc="List of CSS units")
mod.list("css_global_value", desc="CSS-wide values")

global_ctx.lists["self.css_unit"] = {
    # distance (length)
    "char": "ch",
    "em": "em",
    "rem": "rem",
    "pixels": "px",
    "points": "pt",
    "view height": "vh",
    "view width": "vw",
    # angle
    "degrees": "deg",
    "radians": "rad",
    "turn": "turn",
    # duration (time)
    "seconds": "s",
    "millis": "ms",
    # resolution
    "dots per pixel": "dppx",
    # flexible length (flex) - grid
    "fraction": "fr",
}

global_ctx.lists["self.css_at_rule"] = {
    # regular
    "charset": "charset",
    "import": "import",
    "namespace": "namespace",
    # conditional group
    "media": "media",
    "supports": "supports",
    # other nested
    "page": "page",
    "font face": "font-face",
    "keyframes": "keyframes",
    # CSS Modules
    "value": "value",
}

global_ctx.lists["self.css_global_value"] = ["initial", "inherit", "unset", "revert"]

ctx.lists["user.code_common_function"] = {
    # reference
    "attribute": "attr",
    "env": "env",
    "url": "url",
    "var": "var",
    "variable": "var",
    # mathematical
    "calc": "calc",
    "calculate": "calc",
    "clamp": "clamp",
    "max": "max",
    "min": "min",
    # color
    "HSL": "hsl",
    "hue sat light": "hsl",
    "HSLA": "hsla",
    "lab": "lab",
    "LCH": "lch",
    "RGB": "rgb",
    "red green blue": "rgb",
    "RGBA": "rgba",
    "color": "color",
    # image functions
    "linear gradient": "linear-gradient",
    # counter functions
    "counter": "counter",
    "counters": "counters",
    "symbols": "symbols",
    # filter
    "blur": "blur",
    "brightness": "brightness",
    "contrast": "contrast",
    "drop shadow": "drop-shadow",
    "grayscale": "grayscale",
    "hue rotate": "hue-rotate",
    "invert": "invert",
    "opacity": "opacity",
    "saturate": "saturate",
    "sepia": "sepia",
    # grid
    "fit content": "fit-content",
    "min max": "minmax",
    "repeat": "repeat",
    # transform
    "matrix": "matrix",
    "rotate": "rotate",
    "scale": "scale",
    "skew": "skew",
    "translate": "translate",
}


@ctx.action_class("user")
class UserActions:
    def code_operator_addition(self):
        actions.insert(" + ")

    def code_operator_subtraction(self):
        actions.insert(" - ")

    def code_operator_multiplication(self):
        actions.insert(" * ")

    def code_operator_division(self):
        actions.insert(" / ")

    def code_operator_and(self):
        actions.insert(" and ")

    def code_operator_or(self):
        actions.insert(" or ")

    def code_operator_greater_than(self):
        actions.insert(" > ")

    def code_operator_greater_than_or_equal_to(self):
        actions.insert(" >= ")

    def code_operator_less_than(self):
        actions.insert(" < ")

    def code_operator_less_than_or_equal_to(self):
        actions.insert(" <= ")

    def code_import(self):
        actions.insert("@import ")

    def code_insert_function(text: str, selection: str):
        actions.user.paste(f"{text}({selection})")
        actions.edit.left()
