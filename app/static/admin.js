const messageBox =
document.getElementById(
    "message"
)

const fileInput =
document.getElementById(
    "pdf"
)

const uploadBtn =
document.querySelector(
    ".upload-btn"
)

const updateBtn =
document.querySelector(
    ".update-btn"
)



function showMessage(text){

    messageBox.style.display =
    "block"

    messageBox.innerText =
    text
}



async function uploadPDF(){

    const file =
    fileInput.files[0]


    if(!file){

        showMessage(
            "Please select PDF"
        )

        return
    }


    let formData =
    new FormData()

    formData.append(
        "file",
        file
    )


    try{

        uploadBtn.disabled =
        true

        uploadBtn.innerText =
        "Uploading..."


        showMessage(
            "Uploading PDF..."
        )


        const response =
        await fetch(
            "/admin/upload",
            {
                method:"POST",
                body:formData
            }
        )

        const data =
        await response.json()

        showMessage(
            data.message
        )


        fileInput.value = ""

    }

    catch(error){

        showMessage(
            "Upload failed"
        )

    }

    finally{

        uploadBtn.disabled =
        false

        uploadBtn.innerText =
        "Upload PDF"

    }

}



async function updateRAG(){

    try{

        updateBtn.disabled =
        true

        updateBtn.innerText =
        "Updating..."


        showMessage(
            "Updating RAG..."
        )


        const response =
        await fetch(
            "/admin/update-rag",
            {
                method:"POST"
            }
        )


        const data =
        await response.json()


        showMessage(
            data.message
        )

    }

    catch(error){

        showMessage(
            "Update failed"
        )

    }

    finally{

        updateBtn.disabled =
        false

        updateBtn.innerText =
        "Update RAG"

    }

}

async function seePDF(){

    try{

        showMessage(
            "Loading PDF..."
        )


        const response =
        await fetch(
            "/admin/seePDF",
            {
                method:"GET"
            }
        )


        const data =
        await response.json()


        console.log(data)

        showMessage(
            data.message
        )

    }

    catch(error){

        showMessage(
            "See PDF failed"
        )

    }

}