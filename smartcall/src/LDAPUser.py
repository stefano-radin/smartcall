'''
Created on 09 gen 2017

@author: radin
'''
from pyad import *

def cercaLDAP(ricerca):
    q = adquery.ADQuery()
    
    q.execute_query(
        attributes = ["Name","Manager","Department","l","streetAddress","co","Title","TelephoneNumber","mail","thumbnailPhoto","jpegPhoto"],
        where_clause = "cn = '" + ricerca + "'",
        #base_dn=""
        base_dn = "DC=corp, DC=generali, DC=net"
    )
    
    row=q.get_single_result();
    return row["Title"],row["Department"]
#     for row in q.get_results():
#         print("-------------------")
#         if row["Name"] is not None:
#             print("Nome: " + row["Name"])
#         if row["Title"] is not None:
#             print("Ruolo: " + row["Title"])
#         q1 = adquery.ADQuery()
#         if row["Manager"] is not None:
#             q1.execute_query(
#                 attributes = ["Name"],
#                 where_clause = "DistinguishedName = '" + row["Manager"] + "'",
#                 base_dn = "DC=corp, DC=generali, DC=net"
#             )
#             row1 = q1.get_single_result()
#             print("Manager: " + row1["Name"])
#         if row["Department"] is not None:
#             print("Dipartimento: " + row["Department"])
#         if row["l"] is not None:
#             print("Citta: " + row["l"])
#         if row["streetAddress"] is not None:
#             print("Indirizzo: " + row["streetAddress"])
#         if row["co"] is not None:
#             print("Stato: " + row["co"])
#         if row["TelephoneNumber"] is not None:
#             print("Telefono: " + row["TelephoneNumber"])
#         if row["mail"] is not None:
#             print("email: " + row["mail"])
#         if row["thumbnailPhoto"] is not None:     
#             with open("D:\\"+row["Name"]+".jpg", "wb") as out_file:
#                 out_file.write(row["thumbnailPhoto"])