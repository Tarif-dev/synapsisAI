"use client";

import { Sandpack } from "@codesandbox/sandpack-react";

export default function ComponentPreview({ code }: { code: string }) {

  // Remove default export
  const fixedCode = code.replace(
    /export default function (\w+)/,
    "function $1"
  );

  // Extract component name
  const match = code.match(/export default function (\w+)/);
  const componentName = match ? match[1] : "GeneratedComponent";

  const wrappedCode = `
import React from "react";

${fixedCode}

export default function App() {
  return (
    <div style={{ padding: 20 }}>
      <${componentName} />
    </div>
  );
}
`;

  return (
    <div className="h-[500px] border rounded-xl overflow-hidden bg-white">
      <Sandpack
        template="react"
        files={{
          "/App.js": wrappedCode,
        }}
        options={{
          showTabs: false,
          showNavigator: false,
        }}
      />
    </div>
  );
}