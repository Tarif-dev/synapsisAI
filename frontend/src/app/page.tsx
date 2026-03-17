"use client";

import { useState } from "react";
import { generateComponent } from "@/lib/generateComponent";
import CodeEditor from "@/components/CodeEditor";
import ComponentPreview from "@/components/ComponentPreview";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [code, setCode] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    const result = await generateComponent(prompt);
    setCode(result);
    setLoading(false);
  };

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <h1 className="text-3xl font-bold">Synapsis AI</h1>

      {/* Prompt Bar */}
      <div className="flex gap-2">
        <input
          className="flex-1 border p-3 rounded-lg"
          placeholder="Describe your component..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <button
          onClick={handleGenerate}
          className="px-4 py-2 bg-black text-white rounded-lg"
        >
          {loading ? "⚡ Generating..." : "Generate"}
        </button>
      </div>

      {/* Workspace */}
      <div className="grid grid-cols-2 gap-6 h-150">
        {/* Code Editor */}
        <div className="bg-[#0d1117] rounded-xl p-2 border border-gray-800">
          <CodeEditor code={code} setCode={setCode} />
        </div>

        {/* Live Preview */}
        <div className="bg-[#0d1117] rounded-xl p-2 border border-gray-800">
          <ComponentPreview code={code} />
        </div>
      </div>
    </div>
  );
}
