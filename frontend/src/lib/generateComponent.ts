import axios from 'axios'

export async function generateComponent(prompt:string) {
    const res = await axios.post("http://127.0.0.1:8000/generate",{
        prompt,
    })

    return res.data.code
}