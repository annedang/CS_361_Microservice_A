# client 
# TEST PROGRAM
import zmq
import datetime

def initiate_checkin():
    """ Returns the current time"""
    
    return datetime.datetime.now().strftime('%H:%M:%S')


def get_duration_input():
    """ Gets and returns check in window duration from user."""
    
    duration = input("Enter the duration in minutes (ex. 120): ")
    return duration


def small_test_program():
    """ Sends request to server with check-in time and duration. """
    context = zmq.Context()                 # Required for ZeroMQ to set up env
    socket = context.socket(zmq.REQ)        # Request Socket
    socket.connect("tcp://localhost:5556")  # Connect to remote socket
    
    start_time = initiate_checkin()
    print(f"Check in Started at {start_time}")

    duration = get_duration_input()
    
    # Sending the Message
    print(f"Sending a request...")
    print(f"Check-In Time: {start_time}, Duration: {duration}")
    socket.send_string(f"{start_time}, {duration}")

    # Receiving the Reply
    reply = socket.recv()
    print(f"Response from Server: {reply.decode()}")

if __name__ == "__main__":
    small_test_program()