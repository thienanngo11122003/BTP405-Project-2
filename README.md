# BTP405-Project-2


•	Software product:

For (target customer): Food enthusiasts and restaurant owners seeking a streamlined and efficient solution for managing reservations and optimizing dining experiences.

Who (statement of the need or opportunity): Encounter challenges in coordinating reservations, managing booking availability, and enhancing customer satisfaction in the dining process.

The (product name) is a (product category): The RaaS (Restaurant as a Service) platform is a cloud-based application for simplifying restaurant reservation management.

That (key benefit, compelling reason to buy): Empowers users to effortlessly make, manage, and cancel reservations online, while providing restaurant staff with intuitive tools for managing booking availability, customer information, and receiving real-time notifications.

Unlike (primary competitive alternative): Traditional phone-based reservation systems or manual booking processes that often lead to inefficiency, errors, and customer dissatisfaction.

Our product (statement of primary differentiation): Distinguishes itself by adopting a microservices architecture for scalability and flexibility, prioritizing security and privacy through robust encryption and authentication mechanisms, and embracing Agile methodologies to ensure continuous improvement and alignment with user needs.

•	Agile software engineering:

 <img width="426" alt="image" src="https://github.com/thienanngo11122003/BTP405-Project-2/assets/132942173/b718a674-0535-41cf-ae0f-2a97bef20632">

<img width="468" alt="image" src="https://github.com/thienanngo11122003/BTP405-Project-2/assets/132942173/f61daedd-5b03-40db-bed6-ecc481406000">

<img width="468" alt="image" src="https://github.com/thienanngo11122003/BTP405-Project-2/assets/132942173/c64222ee-ab02-4ba8-958c-7400da5d5f1d">

<img width="468" alt="image" src="https://github.com/thienanngo11122003/BTP405-Project-2/assets/132942173/8b30735a-dfa5-4159-871e-072200dcfa60">

<img width="468" alt="image" src="https://github.com/thienanngo11122003/BTP405-Project-2/assets/132942173/5210893b-4fad-4c57-adb5-eb9e2c30199f">

<img width="468" alt="image" src="https://github.com/thienanngo11122003/BTP405-Project-2/assets/132942173/99263caa-f955-4559-a63e-e3191b6c63fc">




 
 
  
•	Features, scenarios, and stories:

-	Customer Persona:
Name: Mark Johnson
Occupation: Sales Executive
Scenario: Mark, a sales executive, plans to take his family out for dinner on Saturday night. He quickly checks the restaurant reservation system on his phone during a break at work to find a nearby restaurant with available tables for four people at 7:00 PM.

-	Restaurant Manager Persona:
Name: Emily Parker
Occupation: Restaurant Manager
Scenario: Emily, the restaurant manager, receives an alert on her tablet notifying her of a last-minute cancellation for a large party reservation. She quickly updates the table availability on the reservation system and assigns the vacant table to a waiting group, ensuring efficient utilization of seating capacity.

-	 Kitchen Staff Persona:
Name: Carlos Martinez
Occupation: Head Chef
Scenario: Carlos, the head chef, receives a notification on his kitchen display screen informing him of a new order for a vegetarian pasta dish with gluten-free options. He quickly prepares the customized dish according to the specifications provided by the customer through the reservation system.

-	Customer Support Persona:
Name: Jessica Brown
Occupation: Customer Support Representative
Scenario: Jessica, a customer support representative, receives a chat request from a user experiencing difficulty modifying their reservation online. Using the reservation system's integrated chat feature, Jessica guides the user through the process step-by-step, resolving the issue and ensuring a smooth customer experience

•	Software Architecture:
The restaurant reservation system is structured as a collection of loosely coupled microservices, each responsible for specific functionalities, such as user authentication, reservation management, and notification handling. This architecture enhances scalability and maintainability by allowing independent deployment and scaling of individual services.

Security Layers:
Security measures are implemented at multiple layers of the architecture to ensure the protection of user data and system integrity. This includes network security, authentication, authorization, and data encryption. Access to sensitive information, such as user profiles and reservation details, is restricted based on user roles and permissions, ensuring compliance with data protection regulations.

Scalability:
The system is designed to handle a large volume of concurrent users and reservations by leveraging cloud-based services for horizontal scaling. Elastic compute resources automatically provision and scale compute instances based on demand, while load balancers distribute incoming traffic across multiple instances of microservices, ensuring optimal performance and availability during peak usage periods.

Interoperability:
The use of standardized protocols and data formats facilitates interoperability with existing restaurant management systems and third-party applications. RESTful APIs are provided to enable seamless integration with external systems, allowing for the exchange of reservation data, user information, and other system functionalities. This promotes collaboration and interoperability with various stakeholders in the restaurant industry.


