import requests
import markdown

class AgriculturalChatbot:
    def __init__(self):
        self.history = []
        self.model_url = "http://localhost:11434/api/generate"
        self.model_name = "llama3.2:1b"

    def get_response(self, user_input):
        try:
            # Create the prompt with conversation history
            prompt = "You are a helpful agriculture assistant.\n"
            for msg in self.history:
                prompt += f"Human: {msg['user']}\nAssistant: {msg['bot']}\n"
            prompt += f"Human: {user_input}\nAssistant:"

            # Make the API request
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            }

            res = requests.post(self.model_url, json=payload)
            res.raise_for_status()
            bot_reply = res.json().get("response", "").strip()
            
            # Store the conversation
            self.history.append({"user": user_input, "bot": bot_reply})
            
            # Format the response with proper bullet points and paragraphs
            formatted_response = bot_reply.replace('\n', '<br>')
            
            # Convert bullet points to HTML list
            if '•' in formatted_response:
                lines = formatted_response.split('<br>')
                formatted_lines = []
                in_list = False
                
                for line in lines:
                    if line.strip().startswith('•'):
                        if not in_list:
                            formatted_lines.append('<ul>')
                            in_list = True
                        formatted_lines.append(f'<li>{line.strip()[1:].strip()}</li>')
                    else:
                        if in_list:
                            formatted_lines.append('</ul>')
                            in_list = False
                        formatted_lines.append(f'<p>{line.strip()}</p>')
                
                if in_list:
                    formatted_lines.append('</ul>')
                
                formatted_response = ''.join(formatted_lines)
            
            return formatted_response
        except Exception as e:
            return f"Error: {str(e)}"

# Create an instance that app.py can import
chatbot_instance = AgriculturalChatbot()
