"use client";

import { Sandpack } from "@codesandbox/sandpack-react";

export default function ComponentPreview({ code }: { code: string }) {
  return (
    <div className="h-125 border rounded-lg overflow-hidden">
      <Sandpack
        template="react"
        files={{
          "/App.js": code,
        }}
        options={{
          showNavigator: false,
          showTabs: false,
        }}
      />
    </div>
  );
}