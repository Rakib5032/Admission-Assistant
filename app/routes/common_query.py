query = {

    "hi":
    "👋 Hello! How can I help you today?",

    "hello":
    "👋 Hello! How can I help you today?",

    "hey":
    "👋 Hello! How can I help you today?",

    "good morning":
    "☀️ Good morning! How can I help you today?",

    "good afternoon":
    "🌤️ Good afternoon! How can I help you today?",

    "good evening":
    "🌙 Good evening! How can I help you today?",

    "how are you":
    "😄 I'm doing well! How can I help you today?",

    "how are u":
    "😄 I'm doing well! How can I help you today?",

    "how r u":
    "😄 I'm doing well! How can I help you today?",

    "who are you":
    "🤖 I am the DIU Admission Assistant.",

    "what are you":
    "🎓 I am a chatbot designed to help with DIU information.",

    "who made you":
    "🛠️ I was built to assist with DIU admission queries.",

    "what can you do":
    "📚 I can answer questions about admissions, departments, credits, fees and scholarships.",

    "help":
    "❓ Ask me anything related to DIU admissions.",
    
    "help me":
    "❓ Ask me anything related to DIU admissions.",

    "thanks":
    "😊 You're welcome!",

    "thank you":
    "😊 You're welcome!",

    "thx":
    "😊 You're welcome!",
    
    "thnx":
    "😊 You're welcome!",

    "ok":
    "👍 Alright!",

    "bye":
    "👋 Goodbye! Have a great day!",

    "see you":
    "👋 See you again!",

    "goodbye":
    "👋 Goodbye!",

    "nice":
    "😄 Glad you liked it!",

    "awesome":
    "✨ Happy to hear that!",

    "great":
    "🎉 That's great!",
}


toall_keywords = [
    "hi",
    
    "hello",
    
    "hey",

    "toall",

    "start",

    "begin",

    "help",

    "admission",

    "apply",

    "get started",

    "new here",

    "start admission",

    "guide me",

    "i need help",
    
    "need help",

    "where do i start"

]

to_all = (
    " To guide you better, please share your SSC & HSC results "
    "or the department you're interested in."
)

def common_query(user_query: str):

    answer = query.get(
        user_query,
        ""
    )

    if user_query in toall_keywords:
        
        print(answer)
        
        if answer == "":
            answer = to_all
        else:
            answer += (
                "\n\n" + to_all
            )

    return{
        "success": True if len(answer) > 0 else False,
        "answer": answer
    }