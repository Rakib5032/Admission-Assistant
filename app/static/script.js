const sendBtn =
    document.getElementById("send-btn")

const questionInput =
    document.getElementById("question-input")

const chatContainer =
    document.getElementById("chat-container")

function scrollToButtom() {
    chatContainer.scrollTop = chatContainer.scrollHeight
}


function createMessage(text, type) {
    const message = document.createElement('div')
    message.classList.add("message", type)
    message.textContent = text
    console.log(message)
    return message
}

questionInput.addEventListener(
    "keydown",
    function(event) {
        if (
            event.key === "Enter" && !event.shiftKey
        ) {
            event.preventDefault()
            sendBtn.click()
        }
    }
)

sendBtn.addEventListener(
    "click",
    async()=>{
        const question = questionInput.value.trim()

        if(!question){
            return;
        }

        const userMessage = createMessage(
            question, 
            "user-message"
        )

        chatContainer.appendChild(userMessage)
        
        const aiMessage = createMessage(
            "Thinking...",
            "ai-message"
        )
        chatContainer.appendChild(aiMessage)

        questionInput.value=""

        scrollToButtom()

        sendBtn.disabled = true
        sendBtn.innerText="Sending..."


        try{
            const response=await fetch(
                "/ask",
                {
                    method:"POST",
                    headers:{
                        "content-type":"application/json"
                    },

                    body:JSON.stringify({
                        query:question
                    })
                }
            )

            const data = await response.json()

            if(data.success){
                aiMessage.textContent=data.answer
                console.log(data)
            }
            else{
                aiMessage.textContent="❌ "+data.message
                console.log(data)
            }

        }
        catch(error){
            console.log(error)
            aiMessage.textContent= "❌ Something went wrong"
        }

        finally{
            sendBtn.disabled=false
            sendBtn.innerText="Send"

            scrollToButtom()
        }
    }
)