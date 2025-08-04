const base_url = "http://localhost:4000";

async function getAIResponse(prompt) {
    try {
        const response = await fetch(`${base_url}/api/v1/ollama/ask`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                prompt: prompt.prompt, 
                user: 'user1', 
                model: 'deepseek-r1:1.5b' 
            })
        });
        
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status}`);
        }
        
        const data = await response.json();
        return { response: data.response || data }; // Return in expected format
    } catch (error) {
        console.error("API error:", error);
        return { response: 'Error getting response from AI' };
    }
}

export { getAIResponse };