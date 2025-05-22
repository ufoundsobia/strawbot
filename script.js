// Send message when 'Enter' key is pressed
document.getElementById("user-input").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
      event.preventDefault(); // Prevent form submission (if wrapped in a form)
      sendMessage();
    }
  });
  
  // Send message when the button is clicked
  document.getElementById("send-btn").addEventListener("click", function() {
    sendMessage();
  });
  
  function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput) {
      // Display user message
      displayMessage(userInput, "user-msg");
  
      // Send message to Rasa API and get response
      fetch("http://localhost:5005/webhooks/rest/webhook", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          sender: "user",
          message: userInput,
        }),
      })
      .then((response) => response.json())
      .then((data) => {
        const botMessage = data[0]?.text || "Sorry, I didn't get that.";
        // Display bot response
        displayMessage(botMessage, "bot-msg");
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  
      // Clear input field
      document.getElementById("user-input").value = "";
    }
  }
  
  function displayMessage(message, className) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", className);
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
  
    // Scroll to bottom of chat box
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  