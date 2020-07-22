# socket_example
Yet another socket server-client with blackjack and hookers.

# config
All settings, both for the client and the server, are stored in the settings.json file, in the corresponding sections. 

The client sends json, which is stored in the ["send"] field to the server. The location of the server is ["ip"] and ["port"].
If ["historyPolitics"]["save"] : "true", the client will write the server's response to ["historyPolitics"]["file"] .

The server, when receiving a request from a client, checks if the client requires the password ["needKey"] and, if so, checks if the received json has a "key" and is equal to the ["key"] field from the settings.
If the password is missing or not invalid, it returns to the client a string from the ["errorMessage"] field.
If the password is good or not needed, the server checks the settings field ["savePolitics"]["save"], if the field is true, it checks if the field "saveAs" exists in the received json, if it exists, it will save the received json to the file "saveAs", if there is no such field - to the file ["savePolitics"]["save"]. Finally the server will send ["returnMessage"] to the client.
If the field ["historyPolitics"]["save"] : "true", the client's request will be saved by the server in the file ["historyPolitics"]["file"].
