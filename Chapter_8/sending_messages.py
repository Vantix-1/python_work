# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# -Write a function called send_messages() that prints each text message
# -and moves each message to a new list called sent_messages as it’s printed.
# -After calling the function, print both of your lists to make sure the messages were moved correctly.

text_messages = ['hi','hello','how are you']
sent_messages = []
def show_messages(messages):
    """Shows a list of messages"""
    for message in messages:
        print(message)
print("Original Messages:")
show_messages(text_messages)

def send_messages(messages):
    """Sends all messages and moves them to sent messages"""
    while messages:
        current_message = messages.pop()
        print(f"Sending Message: {current_message}")
        sent_messages.append(current_message)
print("\nSending messages:----")
send_messages(text_messages)

print("\n--- Results ---")
print(f"Original list (text_messages): {text_messages}")
print(f"Sent list (sent_messages): {sent_messages}")