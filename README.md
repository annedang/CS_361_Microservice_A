# CS_361_Microservice_A


How to programmatically REQUEST data:
	• The sender (client) will use the ZeroMQ REQ socket to connect with the server at localhost:5556. Then it will put out a request with the string “[start time], [duration]”. After that it will wait for a response from the server. Once it receives the response it will process the information that it received.
	• Here is an example call:
		context = zmq.Context()
		socket = contex.socket(zmq.REQ)
		socket.connect(“tcp://localhost:5556”)
		start_time = "09:45:33"
		duration = "120"
		socket.send_string(f"{start_time}, {duration}")
		reply = socket.recv()
	
How to programmatically RECEIVE data:
	• Once the receiver (server) is initiated it will be listening to the ZeroMQ REP socket for a request. Once it receives the request it will decode and process it (socket.recv) before sending back a response.
	• Here is an example call:
		context = zmq.Context()
		socket = context.socket(zmq.REP)
		socket.bind(“tcp://*:5556”)
		message_received = socket.recv()
		message_str = message_received.decode()
		reply = f"Elapsed Time: {elapsed_time:.2f}, Remaining Time: {remaining_time:.2f}"
 socket.send_string(reply) ![image](https://github.com/user-attachments/assets/b3927b31-0c71-4b57-a6e2-40aeaa86f3b7)

