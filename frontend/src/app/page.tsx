"use client";

import { useState } from "react";
import { generateComponent } from "@/lib/generateComponent";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [code , setCode] = useState("")

  const handleGenerate = async()=>{
    const result = await generateComponent(prompt);
    setCode(result);
  }

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-4">
        Synapsis AI component generator
      </h1>

      <textarea className="border p-2 w-full" placeholder="Describe your component ..." value={prompt} onChange={(e)=> setPrompt(e.target.value)}/>

      <button onClick={handleGenerate} className="mt-4 px-4 py-2 bg-black text-white">Generate</button>

      <pre className="mt-6 bg-gray-100 p-4 overflow-auto text-black">{code}</pre>
    </div>
  )
}