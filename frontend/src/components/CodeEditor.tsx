"use client";

import { Editor } from "@monaco-editor/react";

export default function CodeEditor({
  code,
  setCode,
}: {
  code: string;
  setCode: (val: string) => void;
}) {
  return(
    <div className="h-125 border rounded-lg overflow-hidden">
        <Editor
            height="100%"
            defaultLanguage="javascript"
            value={code}
            onChange={(value) => setCode(value || "")}
            theme="vs-dark"
            options={{
                fontSize : 14,
                minimap : {enabled : false}
            }}
        />
    </div>
  ) 
}
