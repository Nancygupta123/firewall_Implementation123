ADVANCED FIREWALL PROJECT This is a web application designed to manage incoming and outgoing network traffic using predefined rules. FUNCTIONALITY:

Login Authentication: Provides secure access to the application.
Whitelists and Blacklists Management: Allows users to manage lists of allowed and blocked entities.
Rule Management: Facilitates adding, moving, and removing rules between whitelists and blacklists.
Packet Validation: Checks the validity of network packets based on configured rules.
OBJECTIVES:

Design Patterns • Strategy, Factory, and Singleton Patterns: Implemented for efficient rule handling and scalability.

Network Traffic Filtering • IP Addresses, Ports, and Protocols: Implements strategies for filtering traffic based on these parameters.

User Interface • Rule Management Interface: Provides a user-friendly web interface for setting rules and monitoring network traffic.

SOFTWARE REQUIREMENTS: • Python 3.12 or later: Core programming language. • Flask: Web framework for building the application.

INSTALLATION: Step 1: First, we must install the dependencies:

Step 2: we must run the application:

Step 3: Usage, we must access this on

Logging In:

Use the default admin credentials: o Username: admin o Password: password
Navigating the Application: 3. Use the home page to manage rules, display lists, and check packets.

• Firewall/: Contains core application files. o init.py: Initialization file. o strategy_factory.py: Implements strategy and factory patterns. o ip_filter.py: Handles IP filtering logic. o settings.py: Configuration settings. • templates/: HTML templates for the web interface. o index.html: Main page template. o home.html, set_rules.html, display_lists.html, check_packet.html: Specific page templates. • static/: Static files like CSS for styling. o style.css: CSS stylesheets. • app.py: Entry point for running the Flask application. • requirements.txt: Lists all dependencies required for the project.

STEPS TO COMPLETE PROJECT:

Step 1: Set Up Configuration Settings (Singleton Pattern) • Purpose: Ensure only one instance of the settings exists. • File: config/settings.py

Step 2: Define the Base Strategy (Strategy Pattern) • Purpose: Create an abstract base class for filtering network traffic. • File: firewall/base_strategy.py

Step 3: Implement IP Filter Strategy • Purpose: Filter network traffic based on IP addresses. • File: firewall/ip_filter.py

Step 4: Implement Port Filter Strategy • Purpose: Filter network traffic based on ports. • File: firewall/port_filter.py

Step 5: Implement Protocol Filter Strategy • Purpose: Filter network traffic based on protocols. • File: firewall/protocol_filter.py

Step 6: Create the Strategy Factory (Factory Pattern) • Purpose: Create instances of different firewall strategies. • File: firewall/strategy_factory.py

Step 7: Combine Everything in the Main File • Purpose: Use the strategies for filtering network traffic. • File: main.py

![image](https://github.com/user-attachments/assets/527c5128-380f-4384-9736-7669a20e841f)


WORKING:

Firstly run the app.py file image
![image](https://github.com/user-attachments/assets/fec8800a-808e-4da7-af7c-245a7c2e1180)
Step 2 click on Running on http://127.0.0.1:5000 
![image](https://github.com/user-attachments/assets/d0840920-7e04-47c8-a3b8-5dbf5e8391c2)


Step 3 Login: username – admin password- password (you can do following things mentioned there) 
![image](https://github.com/user-attachments/assets/432c94e4-dd84-44c9-8c0d-df322af7b4fb)


Step 4: after setting rules and IP’s we will check for the packets: 
![image](https://github.com/user-attachments/assets/6007ea3c-68e4-4cce-a7bb-f189368ec8ef)
