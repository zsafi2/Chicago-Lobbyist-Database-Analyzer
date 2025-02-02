#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
    
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone


##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   
   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, 
               State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
      
      self._Lobbyist_ID = Lobbyist_ID
      self._Salutation = Salutation
      self._First_Name = First_Name
      self._Middle_Initial = Middle_Initial
      self._Last_Name = Last_Name
      self._Suffix = Suffix
      self._Address_1 = Address_1
      self._Address_2 = Address_2
      self._City = City
      self._State_Initial = State_Initial
      self._Zip_Code = Zip_Code
      self._Country = Country
      self._Email = Email
      self._Phone = Phone
      self._Fax = Fax
      self._Years_Registered = Years_Registered
      self._Employers = Employers
      self._Total_Compensation = Total_Compensation

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def Salutation(self):
      return self._Salutation

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Middle_Initial(self):
      return self._Middle_Initial

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Suffix(self):
      return self._Suffix

   @property
   def Address_1(self):
      return self._Address_1

   @property
   def Address_2(self):
      return self._Address_2

   @property
   def City(self):
      return self._City

   @property
   def State_Initial(self):
      return self._State_Initial

   @property
   def Zip_Code(self):
      return self._Zip_Code

   @property
   def Country(self):
      return self._Country

   @property
   def Email(self):
      return self._Email

   @property
   def Phone(self):
      return self._Phone

   @property
   def Fax(self):
      return self._Fax

   @property
   def Years_Registered(self):
      return self._Years_Registered

   @property
   def Employers(self):
      return self._Employers

   @property
   def Total_Compensation(self):
      return self._Total_Compensation



##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone
      self._Total_Compensation = Total_Compensation
      self._Clients = Clients

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone

   @property
   def Total_Compensation(self):
      return self._Total_Compensation

   @property
   def Clients(self):
      return self._Clients

   

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   
   # sql query to count the total number of lobbyists in our database
   query = "select count(*) from LobbyistInfo;"
   
   # use the datatier class to execute the query and store the result in row
   row = datatier.select_one_row(dbConn, query)
   
   # check if an error occured executing the query otherwise return the number
   if row == None:
      return -1
   
   return row[0]


##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   
   # we do the same process as we did in num_lobbyists function but with different query
   # we want to find the total number of employers this time
   query = "select count(*) from EmployerInfo;"
   
   row = datatier.select_one_row(dbConn, query)
   
   if row == None:
      return -1
   
   return row[0]

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   
   # Again same process different query: total number of clinets
   query = "select count(*) from ClientInfo;"
   row = datatier.select_one_row(dbConn, query)
   
   if row == None:
      return -1
   
   return row[0]

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   
   # query to returns all lobbyists whose first or last name are "like"
   # the pattern. Patterns are based on SQL, which allow the _ and % wildcards.
   query = "select * from LobbyistInfo where First_Name like ? or Last_Name like ? order by Lobbyist_ID asc;"
   rows = datatier.select_n_rows(dbConn, query, [pattern, pattern])
   result = []
   
   if rows:
      # if the result is not empty got through each row 
      for row in rows:
         
         # make an lobbyist obj with the given parameters ID, first name, last name, phone and add to our result list
         lobbyist_obj = Lobbyist(row[0], row[2], row[4], row[13])
         result.append(lobbyist_obj)
   
   return result

   


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):

   # Query to check if a lobbyist Id exist in the data base
   query1 = "select * from LobbyistInfo where Lobbyist_ID = ? order by Lobbyist_ID asc;"         
   
   # Query to calculate the total compensation associated with the given lobbyist ID 
   query2 = "select sum(Compensation_Amount) from Compensation where Lobbyist_ID = ?;"           
   
   # Query to find all the years that the lobbyist has worked using the Lobbyist Id which is passesd as a parameter
   query3 = "select Year from LobbyistYears where Lobbyist_ID = ?;"
   
   # Query to find all the employers that the lobbyist has worked with
   query4 = """
            select distinct Employer_Name from EmployerInfo 
            inner join LobbyistAndEmployer on LobbyistAndEmployer.Employer_ID =  EmployerInfo.Employer_ID
            inner join LobbyistYears on LobbyistYears.Lobbyist_ID = LobbyistAndEmployer.Lobbyist_ID
            where LobbyistAndEmployer.Lobbyist_ID = ?
            order by EmployerInfo.Employer_Name asc;
            """
   
   # Retrieve all the data using these queries from the data tier passing lobbyist Id as a parameter
   row1 = datatier.select_one_row(dbConn, query1, [lobbyist_id])
   row2 = datatier.select_one_row(dbConn, query2, [lobbyist_id])
   rows1 = datatier.select_n_rows(dbConn, query3, [lobbyist_id])
   rows2 = datatier.select_n_rows(dbConn, query4, [lobbyist_id])
   
   # check if the lobbyist Id exists 
   if row1:
      # a list for the number of years the lobbyist has worked, list to store all the employers
      # and veriable to store the total compnesation
      years_list = [] 
      employer_list = []
      compensation = row2[0]
      
      # go through the whole years list query and add it to the lsit
      for row in rows1:
         years_list.append(row[0])
      
      # check if the compensation is zero
      if row2[0] == None or row2[0] == ():
         compensation = 0
      
      # go through the employer query results and add it to the 
      for row in rows2:
         employer_list.append(row[0])
      
      # create a LobbyistDetails object and pass all the properties to the constructor
      obj = LobbyistDetails(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row1[6], row1[7], row1[8], row1[9], 
                           row1[10], row1[11], row1[12], row1[13], row1[14], years_list, employer_list, compensation)
   
      return obj
   
   return None
         

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   
   # Query to find n top earning Lobbyist between the given year in the parameter
   query = """
            select LobbyistInfo.Lobbyist_ID, First_Name, Last_Name, Phone, sum(Compensation.Compensation_Amount) as total from LobbyistInfo
            inner join Compensation on Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
            where strftime('%Y', Compensation.Period_Start) = ? and strftime('%Y', Compensation.Period_End) = ?
            group by LobbyistInfo.Lobbyist_ID
            order by total desc limit ?;
           """
   
   # Query to find the client names for the compnesation 
   query1 = """
            select distinct ClientInfo.Client_ID, ClientInfo.Client_Name from ClientInfo
            inner join Compensation on Compensation.Client_ID = ClientInfo.Client_ID
            inner join LobbyistInfo on LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
            where strftime('%Y', Compensation.Period_Start) = ? and strftime('%Y', Compensation.Period_End) = ? and LobbyistInfo.Lobbyist_ID = ?
            order by ClientInfo.Client_Name asc;         
            """
            
   # Access the data using the datatier
   rows = datatier.select_n_rows(dbConn, query, [year, year, N])
   # List to store the top N Lobbyists
   my_list = []
   
   # check if the result of query is not empty
   if rows:
      # go through each lobbyist from the query
      for row in rows:
         
         # list to store all the clients
         clients_list = []
         clients = datatier.select_n_rows(dbConn, query1, [year, year, row[0]])
         
         # store the clients in the list above
         if clients:
            for client in clients:
               clients_list.append(client[1])
         
         # create a LobbyistClients object by passing all the parameters to the constructor and add it to the list
         obj = LobbyistClients(row[0], row[1], row[2], row[3], row[4], clients_list)
         my_list.append(obj)
   
   return my_list
   


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   
   # Check if the Lobbyist ID exists
   query = "select * from LobbyistInfo where Lobbyist_ID = ?;"
   row = datatier.select_one_row(dbConn, query, [lobbyist_id])
   
   # if the Lobbyist Exists Then
   if row != None and row != ():
      
      # query to go to the Lobbyist Years table and add the year value
      query1 = "insert into LobbyistYears(Lobbyist_ID, Year) values(?,?);"
      num_rows = datatier.perform_action(dbConn, query1, [lobbyist_id, year])
      
      # check if any rows changed after the perform action function from the datatier and return 1
      if num_rows > 0:
         return 1
   
   return 0



##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   
   # Check if the Lobbyist ID exists
   query = "select * from LobbyistInfo where Lobbyist_ID = ?;"
   row = datatier.select_one_row(dbConn, query, [lobbyist_id])
   
   # if the Lobbyist Exists Then
   if row != None and row != ():
      
      # query to update the Salutation of the Lobbyist with the given Lobbyist ID
      query1 = "update LobbyistInfo set Salutation = ? where Lobbyist_ID = ?;"
      num_rows = datatier.perform_action(dbConn, query1, [salutation, lobbyist_id])

      # check if any rows changed
      if num_rows > 0:
         return 1
      
   return 0

   