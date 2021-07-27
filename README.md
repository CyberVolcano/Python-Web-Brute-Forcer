# Python-Web-Brute-Forcer
A simple web brute forcing tool

# About This Tool

This is a guide to the Python Web Brute Forcing tool I made:

To run this program, it requires the following:

Program Flags | What They Do
--------------|--------------
--users	  | A file containing a set of values to be brute forced with (ex. admin, administrator, root...)
--passwords	  | A file containing a set of values to be brute forced with (ex. password, 12345678, toor...)
--url		  | The URL you are sending your attack to (ex. https://www.example.com/)
--payload 	  | The data that is sent in the request along with brackets to indicate what to replace (ex. "username=[]&password=pass")
--request 	  | A file containing the web request headers


#### Q: How do I get the request headers & request payload?
#### A: Opening up inspect element and looking at the web request allows you to copy the request headers and data
 ![image](https://github.com/CyberVolcano/Python-Web-Brute-Forcer/blob/main/screenshots/Pasted%20image%2020210726150353.png)
 
 #### Q: How does this program work?
#### A: First it takes the request headers from a post or get request, then it parses them into a dictionary and which then gets sent off with the request library
 
 Authors Note: If you are brute forcing a target and only need to use one set of values use the "usernames" flag.
