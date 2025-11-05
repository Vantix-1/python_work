# 8-11. Archived Messages: Start with your work from Exercise 8-10. 
# -Call the function send_messages() with a copy of the list of messages.
# -After calling the function, print both of your lists to show that the original list has retained its messages.

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
send_messages(text_messages[:])

print("\n--- Results ---")
print(f"Original list: {text_messages}")
sent_messages.reverse()
print(f"\nSent list: {sent_messages}")