The Western Governors University Parcel Service (WGUPS) is tasked with creating an effective routing and delivery plan for their Daily Local Deliveries (DLD). Currently, packages are not consistently reaching their destinations by the promised deadlines. The DLD route in Salt Lake City utilizes three trucks, two drivers, and handles an average of 40 packages each day. Each package comes with unique specifications and delivery requirements.

Your goal is to develop an algorithm, write the necessary code, and propose a solution to ensure that all 40 packages (as detailed in the attached "WGUPS Package File") are delivered punctually while adhering to their requirements, and keeping the total distance traveled by both trucks under 140 miles. Delivery locations are illustrated in the accompanying "Salt Lake City Downtown Map," and distances to these locations are provided in the "WGUPS Distance Table." The program should be designed for this specific locale but also adaptable for future use in other cities where WGU operates. Comprehensive comments are needed to enhance code clarity and justify the decisions made during development.

It's crucial for the supervisor to have visibility into the progress of each truck and the status of its packages, based on any of the variables listed in the "WGUPS Package File," including which packages have been delivered and the corresponding delivery times.

ASSUMPTIONS
Each truck can carry a maximum of 16 packages, and every package has a unique ID.
Trucks operate at an average speed of 18 miles per hour and do not require fuel stops.
There are no traffic incidents.
Three trucks and two drivers are available for the deliveries, with drivers assigned to the same truck throughout the service.
Drivers commence their route no earlier than 8:00 a.m., fully loaded, and may return to the hub for additional packages if necessary.
Delivery and loading times are negligible, meaning no time is lost during these activities, as it's included in the truck's average speed.
Only one special note can accompany a package.
The address for package #9, located at the Third District Juvenile Court, is incorrect and will be updated at 10:20 a.m. WGUPS is aware of this error but will not know the correct address (410 S State St., Salt Lake City, UT 84111) until that time.
Distances in the WGUPS Distance Table are consistent, regardless of the travel direction.
The day concludes when all 40 packages are delivered.
REQUIREMENTS
A. Identify a self-adjusting algorithm (e.g., "Nearest Neighbor algorithm," "Greedy algorithm") utilized in the program to handle package deliveries.

B. Provide a program overview that includes:

A pseudocode explanation of the algorithm’s logic.
A description of the programming environment used for the Python application.
An evaluation of the space-time complexity for each major segment of the program, including the overall complexity using big-O notation.
An analysis of how the solution can scale and adapt to an increasing number of packages.
A discussion on the efficiency and maintainability of the software.
An assessment of the strengths and weaknesses of the self-adjusting data structures (e.g., hash tables).
C. Write a functioning program to ensure all packages are delivered, meeting all outlined requirements, using the provided "Salt Lake City Downtown Map," "WGUPS Distance Table," and "WGUPS Package File."

Include a comment at the top of a file named “main.py” that lists your first name, last name, and student ID.
Incorporate comments throughout your code to clarify the process and program flow.
D. Identify a self-adjusting data structure, such as a hash table, suitable for use with the identified algorithm in part A for storing package data.

Explain how your chosen data structure manages the relationships between the data points stored.
E. Develop a hash table without using additional libraries or classes, including an insertion function that accepts:

Package ID number
Delivery address
Delivery deadline
Delivery city
Delivery zip code
Package weight
Delivery status (e.g., delivered, en route)
F. Create a lookup function that takes the following components as input and returns the associated data elements:

Package ID number
Delivery address
Delivery deadline
Delivery city
Delivery zip code
Package weight
Delivery status (e.g., "at the hub," "en route," or "delivered"), along with the delivery time.
G. Provide a user interface that allows the status and information (as outlined in part F) of any package to be viewed at any time, along with the total mileage traveled by all trucks.

Include screenshots displaying the status of all packages between 8:35 a.m. and 9:25 a.m.
Include screenshots showing the status of all packages between 9:35 a.m. and 10:25 a.m.
Include screenshots revealing the status of all packages between 12:03 p.m. and 1:12 p.m.
H. Provide screenshots demonstrating the successful execution of the code, free of runtime errors or warnings, which includes the total mileage traveled by all trucks.

I. Justify the core algorithm identified in part A and utilized in the solution by:

Describing at least two strengths of the employed algorithm.
Verifying that the algorithm satisfies all requirements outlined in the scenario.
Identifying two alternative algorithms, distinct from the one used in the solution, that would meet the scenario requirements. a. Explain how each of the alternative algorithms differs from the one implemented in the solution.
J. Reflect on what you would do differently if you were to repeat this project, aside from the two algorithms identified in I3.

K. Justify the data structure identified in part D by:

Verifying that the chosen data structure meets all scenario requirements. a. Explain how the time required for the lookup function changes with variations in the number of packages. b. Explain how the space usage of the data structure is affected by changes in the number of packages. c. Describe how an increase in the number of trucks or cities would impact the lookup time and space usage of the data structure.
Identify two other data structures that could fulfill the same requirements of the scenario. a. Describe how each identified data structure differs from the one used in the solution.
L. Acknowledge sources with in-text citations and references for any content that is quoted, paraphrased, or summarized.

M. Ensure that your submission demonstrates professional communication in both content and presentation.
