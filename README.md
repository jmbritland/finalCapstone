# finalCapstone
HyperionDev Software Engineering Bootcamp Capstone 4 - Warehouse Inventory Manager
This project is an inventory warehouse for a Nike warehouse. For each item, it stores information about product name, SKU, cost, country, and quantity in inventory. Users can view a list of the current inventory, search for and edit a specific item, add a new item, restock the lowest stock item, mark the highest stock item as on sale, and view a report on the total inventory in the warehouse.
The current inventory.txt file contains sample information. This information should be deleted and new information added to use the inventory manager. The only files necessary are inventory.txt and inventory.py.

_Summary of functions_

In the initial menu, type the option you would like to use.

![image](https://user-images.githubusercontent.com/120101780/210521479-fc8812dc-5ae7-4c91-823b-7e17cc46f403.png)

The view function prints the inventory in this format.

![image](https://user-images.githubusercontent.com/120101780/210521697-5988ca22-37af-46b3-90e4-6127b4c13063.png)

The search function allows the user to search inventory by SKU and edit the quantity and cost of the item.

![image](https://user-images.githubusercontent.com/120101780/210522295-c595ccf3-2ed0-4d73-9af6-850c9a94cce4.png)

The add function gets information about a new product and adds it to the inventory

![image](https://user-images.githubusercontent.com/120101780/210522584-1d022ecc-f7a3-4ca4-af81-da474d63c819.png)

The restock function finds the product with the least stock and allows the user to restock it. A ordering list for restocks is printed on exiting the program.

![image](https://user-images.githubusercontent.com/120101780/210522733-acc9c16f-d4c6-498a-8d84-216191689afd.png)

The sale function finds the product with the most stock and adds it to a list of sale items that is printed on exiting the program.

![image](https://user-images.githubusercontent.com/120101780/210523004-c6ce03f4-ba32-42ea-9b6f-da13c7362c14.png)

The value function provides information on inventory in this format.

![image](https://user-images.githubusercontent.com/120101780/210523202-febfc78e-19fd-4196-97a1-e788b77d4239.png)

When the user uses the exit option, the program prints the restock and sale lists and then overwrites the information in inventory.txt . No information is saved until the exit option is used; therefore, it is important that the user uses the program exit option rather than just terminating at any time.

![image](https://user-images.githubusercontent.com/120101780/210523382-0a88f6ad-650d-4358-b67c-a91267c7e651.png)
