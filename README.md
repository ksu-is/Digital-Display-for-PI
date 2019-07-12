# Digital-Display-for-PI

This is a digital display program that will update and run on a raspberry pi.  It will loop a video and update via a SFTP server.
The program should connect to the file server, login, and check to see if an update is required.  After determining the need to
update, the file should be downloaded and extracted before being ran on a loop with omxplayer.
