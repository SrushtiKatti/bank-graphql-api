Bank GraphQL API 

Project Overview:
This project implements a GraphQL API for bank branches using Django and Graphene.
It allows querying banks and their branches, including branch name, IFSC code, and associated bank name.

Method Used:-

1.Django Models:
   Bank – stores bank names.
   Branch – stores branch name, IFSC code, and a foreign key linking to the bank.

2.GraphQL Schema:
  Used Graphene-Django.
  Created Relay Nodes for Bank and Branch.
  Implemented Query with DjangoConnectionField to fetch lists of banks and branches.
  Nested bank info under branch.

3.Sample Data for Testing:
  Banks: “State Bank of India”, “HDFC Bank”
  Branches:
    “Sion Branch” – SBIN0001234
    “Andheri Branch” – HDFC0005678

4.GraphQL Query Example:

query {
  branches {
    edges {
      node {
        branch
        ifsc
        bank {
          name
        }
      }
    }
  }
}


Sample Response:

{
  "data": {
    "branches": {
      "edges": [
        {
            "node": {
            "branch": "Sion Branch",
            "ifsc": "SBIN0001234",
            "bank": {
              "name": "State Bank of India"
            }
          }
        },
        {
          "node": {
            "branch": "Andheri Branch",
            "ifsc": "HDFC0005678",
            "bank": {
              "name": "HDFC Bank"
            }
          }
        }
      ]
    }
  }
}


Project Structure:
bank_api_project/
├── bank_api_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── branches/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── schema.py
│   ├── tests.py
│   └── migrations/
├── manage.py
└── README.md

Time Taken:
Approx. 4–5 hours to complete the assignment, including setting up Django, creating models, GraphQL schema, and testing queries.

