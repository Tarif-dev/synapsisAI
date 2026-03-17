def generate_react_component(ui_schema) : 
    component_name = ui_schema["componentName"]

    jsx_elements = []

    for element in ui_schema["elements"]:
        if element["type"] == "image":
            jsx_elements.append(
                '<img src="/placeholder.png" className="w-full rounded-lg" />'
            )

        if element["type"] == "text":
            jsx_elements.append(
                '<p className="text-lg font-semibold">Sample Text</p>'
            )

        if element["type"] == "button":
            jsx_elements.append(
                '<button className="px-4 py-2 bg-black text-white rounded-lg">Click</button>'
            )

    jsx_body = "\n".join(jsx_elements)

    return f"""
export default function {component_name}() {{
  return (
    <div className="p-4 rounded-xl shadow-lg bg-white space-y-3">
      {jsx_body}
    </div>
  );
}}
"""