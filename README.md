### **Chicago Lobbyist Database Analyzer**
#### *Analyze and manage lobbyist data using SQLite and Python.*

---

## **Table of Contents**
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Database Structure](#database-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## **Description**
The Chicago Lobbyist Database Analyzer is a Python-based application that allows users to analyze and retrieve information about lobbyists, clients, and employers in Chicago. The program utilizes SQLite to execute queries and retrieve key statistics related to lobbyists, their compensation, and their employment history. Users can perform searches, retrieve lobbyist details, register lobbyists for specific years, and update records.

---

## **Features**
- Retrieve general statistics about lobbyists, employers, and clients.
- Search for lobbyists based on name patterns.
- Display detailed information about specific lobbyists.
- Find the top N lobbyists by compensation for a given year.
- Register a lobbyist for a particular year.
- Set or update a lobbyist’s salutation.

---

## **Installation**
### **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.x
- SQLite3

### **Clone the Repository**
```bash
git clone https://github.com/yourusername/chicago-lobbyist-analyzer.git
cd chicago-lobbyist-analyzer
```

### **Prepare the Database**
Ensure the SQLite database file (`Chicago_Lobbyists.db`) is present in the project directory.

---

## **Usage**
Run the program using:
```bash
python main.py
```
The program will display an interactive terminal-based interface, where you can enter numerical commands to perform different queries.

---

## **Commands**
| Command | Description |
|---------|------------|
| `1` | Search for lobbyists based on name patterns. |
| `2` | Display detailed information of a lobbyist based on ID. |
| `3` | Show top N lobbyists for a given year. |
| `4` | Register a lobbyist for a given year. |
| `5` | Set or update a lobbyist’s salutation. |
| `x` | Exit the application. |

---

## **Database Structure**
The application interacts with an SQLite database consisting of the following key tables:

- **`LobbyistInfo`**: Contains details about lobbyists, including names and contact information.
- **`EmployerInfo`**: Stores employer details linked to lobbyists.
- **`ClientInfo`**: Contains information on clients associated with lobbyists.
- **`Compensation`**: Stores data on lobbyist compensation and associated clients.
- **`LobbyistYears`**: Tracks the years in which lobbyists were registered.
- **`LobbyistAndEmployer`**: Maps lobbyists to their employers.

---

## **Technologies Used**
- **Python**: Core programming language.
- **SQLite3**: Database for efficient data queries.

---

## **Future Improvements**
- Implement a web-based or GUI interface.
- Add real-time lobbyist data (if available).
- Optimize queries for better performance on large datasets.

---

## **Contributing**
Contributions are welcome! If you’d like to improve this project:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

