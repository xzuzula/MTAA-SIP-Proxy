import sipfullproxy
import socket, SocketServer

HOST, PORT = '0.0.0.0', 5060

if __name__ == "__main__":
	hostname = socket.gethostname()
	ipaddress = socket.gethostbyname(hostname)
	proxyna = sipfullproxy.UDPHandler
	ip_pc = raw_input("Proxy PC IP address (default: %s): " % ipaddress)
	if ip_pc != "":
		ipaddress = ip_pc
	proxyna.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,PORT)
	proxyna.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,PORT)
	proxyna.enable_logging = True
	ip_host = raw_input("HOST IP address (default: %s): " % HOST)
	if ip_host != "":
		HOST = ip_host
	server_port = raw_input("PORT proxy (default: %s): " % PORT)
	if server_port != "":
		PORT = int(server_port)
	server = SocketServer.UDPServer((HOST, PORT), proxyna)
	print("Server started on: %s" % ipaddress + ":" + str(PORT))
	server.serve_forever()
