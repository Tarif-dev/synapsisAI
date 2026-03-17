def style_dict_to_inline(style: dict):
    if not style:
        return "{{}}"

    style_string = ", ".join([f'{k}: "{v}"' for k, v in style.items()])
    return "{{ " + style_string + " }}"


def generate_react_component(ui_schema):

    component_name = ui_schema.get("componentName", "GeneratedComponent")
    layout = ui_schema.get("layout", "vertical")
    elements = ui_schema.get("elements", [])
    container_style = ui_schema.get("styles", {})

    jsx_elements = []

    for element in elements:

        el_type = element.get("type")
        style = element.get("style", {})

        if el_type == "image":
            jsx_elements.append(
                f'<img src="{element.get("src", "https://via.placeholder.com/300")}" '
                f'style={style_dict_to_inline(style)} />'
            )

        elif el_type == "text":
            jsx_elements.append(
                f'<p style={style_dict_to_inline(style)}>{element.get("content", "Text")}</p>'
            )

        elif el_type == "button":
            jsx_elements.append(
                f'<button style={style_dict_to_inline(style)}>'
                f'{element.get("content", "Click")}</button>'
            )

    # Layout logic
    if layout == "horizontal":
        layout_style = {
            "display": "flex",
            "gap": "16px",
            "alignItems": "center"
        }
    else:
        layout_style = {
            "display": "flex",
            "flexDirection": "column",
            "gap": "12px"
        }

    final_container_style = {**container_style, **layout_style}

    jsx_body = "\n".join(jsx_elements)

    return f"""
export default function {component_name}() {{
  return (
    <div style={style_dict_to_inline(final_container_style)}>
      {jsx_body}
    </div>
  );
}}
"""